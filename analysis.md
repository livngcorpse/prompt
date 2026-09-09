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

# Experiment 2: Baseline versus Enhanced Prompts

## Analysis Question 1

Which single removal cost the most points? Is that element doing semantic work or formatting work? Support your classification with a specific difference between two outputs.

### Answer

The strongest single loss is most likely the removal of the required-content list (A3), because that element changes what the model is actually asked to say rather than only how it says it. In the logged outputs, P1 explicitly asks for three specific facts — work with Charles Babbage, what Note G describes, and the year of publication — while A3 drops that list and becomes a generic Ada Lovelace bio. The result is a weaker, less specific response, so the removed element is semantic work.

## Analysis Question 2

P1 bans a specific phrase. Did the model comply? Did compliance cost anything in fluency or accuracy? Generalise when a negative constraint is the wrong instrument.

### Answer

The model did comply with the banned-phrase constraint in P1, because the logged output does not contain the disallowed phrase. The cost was mostly stylistic rather than factual: the model had to avoid a familiar phrasing and choose a more cautious formulation. A negative constraint is the wrong instrument when you can express the desired wording more directly, for example by requiring the positive content and preferred style. In that case, a positive instruction or a concrete exemplar is usually clearer and more reliable.

## Analysis Question 3

Suppose your ablation shows role framing changed the score by one point out of twenty on one run. Why is that not enough evidence that role framing is useless? Describe the smallest experiment that would settle the question.

### Answer

A one-point difference on a single run is not enough evidence because one run is noisy: a model may occasionally produce a slightly different answer for reasons unrelated to the role instruction. That result could be random variation, a different token path, or a different completion state. The smallest useful experiment is to repeat the comparison many times at the same temperature, score each run, and compare the average score and variance between the prompt with role framing and the prompt without it. If the mean improves consistently across repeated runs, the role framing is likely doing real work even if the single-run difference was small.

## Analysis Question 4

Your rubric scores Completeness by counting three required facts. Name one failure mode this rubric cannot detect at all, and propose one additional measurable criterion that would catch it.

### Answer

A major failure mode the rubric cannot detect is factual inaccuracy hidden inside otherwise complete-looking responses. For example, the model might include all three required facts but get one of them wrong, such as the wrong year or a mistaken description of Note G. An additional measurable criterion would be a factual-accuracy score that checks each required fact against a trusted source and gives points only for correct claims.
