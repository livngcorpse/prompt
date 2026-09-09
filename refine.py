import re

from pe_lab import ask, safe_ask


ROUND_1 = "Summarize the plot of Romeo and Juliet."

ROUND_2 = """Summarize the plot of Romeo and Juliet in exactly two sentences,
no more than 45 words in total. Use the present tense and a
neutral encyclopaedic register."""

ROUND_3 = """Summarize the plot of Romeo and Juliet in exactly two sentences,
no more than 45 words in total. Use the present tense and a
neutral encyclopaedic register.
Sentence 1 must establish the setting: Verona, and the feud
between the Montague and Capulet households.
Sentence 2 must state the outcome and name the central theme of
love set against inherited hatred.
Do not name more than two characters."""

ROUNDS = [
    ("E3-R1", ROUND_1),
    ("E3-R2", ROUND_2),
    ("E3-R3", ROUND_3),
]


def check(text, max_words=45, n_sent=2):
    t = " ".join(text.split())
    sents = [s for s in re.split(r'(?<=[.!?])\s+', t) if s]
    words = len(t.split())
    low = t.lower()
    return {
        "sentences": len(sents),
        "words": words,
        "sentence_ok": len(sents) == n_sent,
        "word_ok": words <= max_words,
        "has_verona": "verona" in low,
        "has_feud": "montague" in low and "capulet" in low,
    }


def run_rounds():
    results = []
    for round_tag, prompt in ROUNDS:
        for run_index in range(3):
            tag = f"{round_tag}-{run_index + 1}"
            out = safe_ask(prompt, temperature=0.0, tag=tag)
            results.append({
                "tag": tag,
                "prompt": prompt,
                "out": out,
                "check": check(out),
            })
    return results


def run_repair_loop():
    out = safe_ask(ROUND_1, temperature=0.0, tag="E3-repair-0")
    history = [{"tag": "E3-repair-0", "out": out, "check": check(out)}]

    for attempt in range(1, 5):
        c = history[-1]["check"]
        if c["sentence_ok"] and c["word_ok"]:
            break

        fix = (
            f"The following summary must be exactly 2 sentences and "
            f"at most 45 words. It is currently {c['sentences']} "
            f"sentences and {c['words']} words. Rewrite it to "
            f"satisfy both constraints, changing nothing else.\n\n"
            f"{out}"
        )
        out = safe_ask(fix, temperature=0.0, tag=f"E3-repair-{attempt}")
        history.append({"tag": f"E3-repair-{attempt}", "out": out, "check": check(out)})

    return history


if __name__ == "__main__":
    rounds_results = run_rounds()
    repair_history = run_repair_loop()

    print("Experiment 3 round results:")
    for item in rounds_results:
        print(item["tag"], item["check"])

    print("\nExperiment 3 repair loop:")
    for item in repair_history:
        print(item["tag"], item["check"])
