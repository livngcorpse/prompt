# Sheet 0: Environment, Security, and Logging Record

## Table 0.1: Environment Record

| Item | Entry ||
|---|---|---|
| Name and roll number | **Mohammad Arif / 23VV1A1233** |
| Backend chosen | `gemini` |
| Exact model ID used | `models/gemini-3.6-flash` |
| SDK version | `google-genai 2.17.0` |
| Python version | `Python 3.11.9` |
| Operating system | Windows NT 10.0.26200.0 |
| Free-tier limits found in provider docs today | **TODO: fill in RPM / TPM / RPD** |
| Date of first successful call | `2026-09-09` |

## Table 1.1 - Connectivity Runs

| Run | Tag | Model ID | In tokens | Out tokens | Latency (s) | Response exact? |
|---:|---|---|---:|---:|---:|---|
| 1 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 2.467 | Y |
| 2 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 3.818 | Y |
| 3 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 3.693 | Y |
| 4 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 59.667 | Y |

## Table 1.2 - Error Catalogue

| Fault injected | Exception / HTTP code | First line of message | Correct fix |
|---|---|---|---|
| Invalid API key | `google.genai.errors.ClientError`, HTTP `401 UNAUTHENTICATED` | `401 UNAUTHENTICATED` | Restore the correct local key; revoke and replace it if exposed. |
| `max_tokens=5` | No API exception; truncated response | Response was `'The'` with 1 output token | Increase `max_tokens` when a complete response is required. |
| Wrong model ID | `google.genai.errors.ClientError`, HTTP `404 NOT_FOUND` | `404 NOT_FOUND` | Select a currently reachable model from the provider listing. |

## Table 2.1 - Scoring Rubric and Baseline Comparison

| Criterion (0-5 each) | What earns full marks | P0 | P1 |
|---|---|---:|---:|
| Relevance | Every sentence is about Ada Lovelace and answers the prompt | 5 | 5 |
| Completeness | All three required facts present and correct (1.67 each) | 4 | 5 |
| Format compliance | Word count in range, one paragraph, no Markdown, banned phrase absent, closing sentence present | 3 | 5 |
| Verifiability | Claims are specific enough to check against a source; no vague filler | 4 | 5 |
| Total (out of 20) | Sum of the four criteria | 16 | 20 |

## Table 2.2 - Ablation

| Variant | Element removed | Total score /20 | Change vs P1 | What visibly broke |
|---|---|---:|---:|---|
| A1 | Role framing | 19 | -1 | Slight reduction in polished framing; response is still strong and complete |
| A2 | Length target | 18 | -2 | The output is still one paragraph, but the explicit 90–110 word target is no longer enforced |
| A3 | Required-content list | 15 | -5 | The model drops one or more required facts and becomes a generic Ada Lovelace bio |
| A4 | Negative constraints | 19 | -1 | The banned phrase is no longer explicitly controlled, so some runs drift toward a familiar trope |
| A5 | Closing-sentence instruction | 18 | -2 | The final sentence explaining why the work matters is missing |

## Table 2.3 - Variance Probe

| Prompt | Temperature | Run 1 = Run 2? | Run 2 = Run 3? | Observation |
|---|---:|---|---|---|
| P0 | 0.0 | No | No | Three newly logged runs are not byte-identical; wording and emphasis vary across repeats, though the core bio stays similar |
| P1 | 0.0 | No | No | Three newly logged runs are not byte-identical; the answer keeps the required facts and format, but sentence structure differs across repeats |
| P0 | 1.0 | No | No | Three newly logged runs are not byte-identical; higher temperature increases variation in wording and detail selection |
| P1 | 1.0 | No | No | Three newly logged runs are not byte-identical; the answer remains on-topic, but wording, phrasing, and some factual emphasis shift across repeats |

## Table 3.1 - Round-by-round compliance (3 runs per round)

| Round | What changed | Exactly 2 sentences | ≤ 45 words | Verona present | Feud named | Deficiency remaining |
|---|---|---:|---:|---:|---:|---|
| R1 | Minimal instruction | 0/3 | 0/3 | 3/3 | 3/3 | All three runs violated the 2-sentence and 45-word constraints |
| R2 | + length and style | 3/3 | 3/3 | 2/3 | 3/3 | One run omitted the literal word Verona |
| R3 | + content elements | 3/3 | 3/3 | 3/3 | 3/3 | None; all three runs complied fully |

## Table 3.2 - Single good prompt versus weak prompt plus repair loop

| Route | API calls | Total input tokens | Total output tokens | Compliant at end? |
|---|---:|---:|---:|---|
| Round 3 prompt, one call | 1 | 612 | 537 | Yes |
| Round 1 prompt + repair loop | 2 | 1726 | 2042 | Yes |


