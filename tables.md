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
| Date of first successful call | `2026-08-19` |

## Table 1.1 - Connectivity Runs

| Run | Tag | Model ID | In tokens | Out tokens | Latency (s) | Response exact? |
|---:|---|---|---:|---:|---:|---|
| 1 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 4.179 | Y |
| 2 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 1.811 | Y |
| 3 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 2.551 | Y |
| 4 | `E1-hello` | `models/gemini-3.6-flash` | 14 | 4 | 9.537 | Y |

## Table 1.2 - Error Catalogue

| Fault injected | Exception / HTTP code | First line of message | Correct fix |
|---|---|---|---|
| Invalid API key | `google.genai.errors.ClientError`, HTTP `401 UNAUTHENTICATED` | `401 UNAUTHENTICATED` | Restore the correct local key; revoke and replace it if exposed. |
| `max_tokens=5` | No API exception; truncated response | Response was `'The'` with 1 output token | Increase `max_tokens` when a complete response is required. |
| Wrong model ID | `google.genai.errors.ClientError`, HTTP `404 NOT_FOUND` | `404 NOT_FOUND` | Select a currently reachable model from the provider listing. |


