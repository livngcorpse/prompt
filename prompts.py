P0 = "Write a one-paragraph bio of Ada Lovelace."

P1_SYSTEM = "You are a technical historian writing short reference entries for first-year engineering students."

P1_PROMPT = """Write ONE paragraph of 90-110 words on Ada Lovelace.
Include all three of the following:
(a) her work with Charles Babbage on the Analytical Engine;
(b) what Note G describes;
(c) the year her notes were published.
Style: plain declarative sentences, third person, no rhetorical questions. Do not use bullet points, headings, or Markdown.
Do not use the phrase \"the world's first computer programmer\".
End with exactly one sentence stating why her work matters to computing today."""

A1_PROMPT = """Write ONE paragraph of 90-110 words on Ada Lovelace.
Include all three of the following:
(a) her work with Charles Babbage on the Analytical Engine;
(b) what Note G describes;
(c) the year her notes were published.
Style: plain declarative sentences, third person, no rhetorical questions. Do not use bullet points, headings, or Markdown.
Do not use the phrase \"the world's first computer programmer\".
End with exactly one sentence stating why her work matters to computing today."""

A2_PROMPT = """Write ONE paragraph on Ada Lovelace.
Include all three of the following:
(a) her work with Charles Babbage on the Analytical Engine;
(b) what Note G describes;
(c) the year her notes were published.
Style: plain declarative sentences, third person, no rhetorical questions. Do not use bullet points, headings, or Markdown.
Do not use the phrase \"the world's first computer programmer\".
End with exactly one sentence stating why her work matters to computing today."""

A3_PROMPT = """Write ONE paragraph of 90-110 words on Ada Lovelace.
Style: plain declarative sentences, third person, no rhetorical questions. Do not use bullet points, headings, or Markdown.
Do not use the phrase \"the world's first computer programmer\".
End with exactly one sentence stating why her work matters to computing today."""

A4_PROMPT = """Write ONE paragraph of 90-110 words on Ada Lovelace.
Include all three of the following:
(a) her work with Charles Babbage on the Analytical Engine;
(b) what Note G describes;
(c) the year her notes were published.
Style: plain declarative sentences, third person, no rhetorical questions. Do not use bullet points, headings, or Markdown.
End with exactly one sentence stating why her work matters to computing today."""

A5_PROMPT = """Write ONE paragraph of 90-110 words on Ada Lovelace.
Include all three of the following:
(a) her work with Charles Babbage on the Analytical Engine;
(b) what Note G describes;
(c) the year her notes were published.
Style: plain declarative sentences, third person, no rhetorical questions. Do not use bullet points, headings, or Markdown.
Do not use the phrase \"the world's first computer programmer\"."""

BASELINE_RUNS = [
    ("E2-P0", P0, None, 0.0),
    ("E2-P1", P1_PROMPT, P1_SYSTEM, 0.0),
]

ABLATIONS = [
    ("E2-A1", A1_PROMPT, None, 0.0),
    ("E2-A2", A2_PROMPT, P1_SYSTEM, 0.0),
    ("E2-A3", A3_PROMPT, P1_SYSTEM, 0.0),
    ("E2-A4", A4_PROMPT, P1_SYSTEM, 0.0),
    ("E2-A5", A5_PROMPT, P1_SYSTEM, 0.0),
]

VARIANCE_CASES = [
    ("E2-VAR-P0-0", P0, None, 0.0),
    ("E2-VAR-P0-1", P0, None, 0.0),
    ("E2-VAR-P0-2", P0, None, 0.0),
    ("E2-VAR-P1-0", P1_PROMPT, P1_SYSTEM, 0.0),
    ("E2-VAR-P1-1", P1_PROMPT, P1_SYSTEM, 0.0),
    ("E2-VAR-P1-2", P1_PROMPT, P1_SYSTEM, 0.0),
    ("E2-VAR-P0-3", P0, None, 1.0),
    ("E2-VAR-P0-4", P0, None, 1.0),
    ("E2-VAR-P0-5", P0, None, 1.0),
    ("E2-VAR-P1-3", P1_PROMPT, P1_SYSTEM, 1.0),
    ("E2-VAR-P1-4", P1_PROMPT, P1_SYSTEM, 1.0),
    ("E2-VAR-P1-5", P1_PROMPT, P1_SYSTEM, 1.0),
]
