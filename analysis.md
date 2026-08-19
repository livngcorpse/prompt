# Experiment 1: Environment and Connectivity

## Analysis Question 1

What did `repr(out)` reveal that a plain `print` would have hidden? Why does this matter when parsing model output programmatically?

### Answer

`repr(out)` shows the Python representation of the returned string, including quote marks, escaped characters, line breaks, tabs, and trailing whitespace. Plain `print(out)` renders those characters, so some differences may be invisible. This matters when parsing model output because exact whitespace, line breaks, and unexpected extra text can affect whether a parser accepts the response.

## Analysis Question 2

Compare the input token count against the number of words sent. Explain the discrepancy and its implication for budgeting a long prompt against a tokens-per-minute cap.

### Answer

The prompt contained approximately 10 space-separated words, while the API reported 14 input tokens. Tokens are not the same as words: a tokenizer can split words into sub-word pieces and count punctuation or symbols separately. Therefore, word count is only a rough estimate. Long prompts should be budgeted using token counts, with additional capacity reserved for generated output, rather than using word count alone.

## Analysis Question 3

Your key is in `.env` and `.env` is listed in `.gitignore`. Name one route by which the key could still escape your machine and one specific control that would close it.

### Answer

The key could escape through an accidental terminal paste, screenshot, notebook cell, debug log, or public Git commit. A specific control is to inspect `git diff --cached` before every commit and use a pre-commit secret scanner. The key should remain only in the local `.env`; if it is exposed, revoke it immediately and generate a replacement.
