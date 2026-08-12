# pe_lab.py — shared helper for the Prompt Engineering Lab
import os, json, time, hashlib, datetime
from dotenv import load_dotenv

load_dotenv()
BACKEND  = os.getenv("PE_BACKEND", "gemini").lower()
LOG_PATH = "runs.jsonl"

if BACKEND == "gemini":
    from google import genai
    from google.genai import types
    _client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    DEFAULT_MODEL = os.getenv("PE_MODEL") or "<paste your verified Gemini model id>"
elif BACKEND == "groq":
    from groq import Groq
    _client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    DEFAULT_MODEL = os.getenv("PE_MODEL") or "<paste your verified Groq model id>"
else:
    raise ValueError("PE_BACKEND must be 'gemini' or 'groq'")


def ask(prompt, system=None, temperature=0.0, max_tokens=512,
        model=None, tag="", log=True):
    """Send one prompt, return the text, append one record to runs.jsonl."""
    model = model or DEFAULT_MODEL
    t0 = time.time()

    if BACKEND == "gemini":
        cfg = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
            system_instruction=system)
        r = _client.models.generate_content(
            model=model, contents=prompt, config=cfg)
        text  = r.text
        usage = {"in":  r.usage_metadata.prompt_token_count,
                 "out": r.usage_metadata.candidates_token_count}
    else:
        msgs = ([{"role": "system", "content": system}] if system else [])
        msgs.append({"role": "user", "content": prompt})
        r = _client.chat.completions.create(
            model=model, messages=msgs,
            temperature=temperature, max_tokens=max_tokens)
        text  = r.choices[0].message.content
        usage = {"in":  r.usage.prompt_tokens,
                 "out": r.usage.completion_tokens}

    dt = round(time.time() - t0, 3)
    if log:
        rec = {"ts": datetime.datetime.now().isoformat(timespec="seconds"),
               "tag": tag, "backend": BACKEND, "model": model,
               "temperature": temperature, "system": system,
               "prompt": prompt,
               "prompt_sha8": hashlib.sha256(
                   prompt.encode()).hexdigest()[:8],
               "response": text, "usage": usage, "latency_s": dt}
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return text


def safe_ask(*args, **kwargs):
    """ask() with exponential backoff on rate-limit errors."""
    for attempt in range(5):
        try:
            return ask(*args, **kwargs)
        except Exception as e:
            msg = str(e).upper()
            if "429" not in msg and "RESOURCE_EXHAUSTED" not in msg \
                    and "RATE" not in msg:
                raise
            wait = 2 ** attempt
            print(f"rate limited, sleeping {wait}s")
            time.sleep(wait)
    raise RuntimeError("gave up after 5 rate-limited attempts")
