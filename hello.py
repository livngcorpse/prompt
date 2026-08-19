from pe_lab import BACKEND, DEFAULT_MODEL, ask

print("backend:", BACKEND, "| model:", DEFAULT_MODEL)
out = ask(
    "Reply with exactly this text and nothing else: Hello, world!",
    temperature=0.0,
    tag="E1-hello",
)
print("response:", repr(out))
