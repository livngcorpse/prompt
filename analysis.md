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

# Experiment 3: Iterative Refinement on a Simple Task

## Analysis Question 1

Which constraint was violated most often across your nine runs? Explain why an exact sentence count is harder for the model to satisfy than an approximate word ceiling, in terms of how text is generated token by token.

### Answer

The most frequently violated constraint was the exact two-sentence requirement in Round 1, where all three runs produced far more than two sentences. The word-limit constraint also failed in Round 1, but the sentence-count issue is the stronger signal because the model generates text token by token and does not naturally stop at a precise boundary unless that boundary is strongly specified. An approximate word cap is easier to satisfy because the model can simply produce a shorter response, whereas an exact sentence count requires the model to know when a sentence should terminate and then stop cleanly at that point.

## Analysis Question 2

Round 3 added content requirements while keeping the 45-word cap. Did adding content requirements degrade compliance with the length constraint? Describe the trade-off in your own data.

### Answer

Adding the content requirements did not degrade length compliance in this run. In Round 2, all three runs were within 45 words and exactly two sentences, but one run missed the literal word Verona. In Round 3, all three runs satisfied the sentence count, word limit, Verona check, and feud check. The trade-off is that the added content made the prompt more demanding, but the model still stayed within the 45-word cap by compressing the summary more tightly; the main remaining risk shifted from length to missing a required literal token such as Verona.

## Analysis Question 3

From Table 3.2: which route is cheaper in tokens? Name one realistic situation in which you would still prefer the repair loop despite the cost.

### Answer

The Round 3 prompt in a single call is cheaper in tokens: it used 1 API call, 612 input tokens, and 537 output tokens in the first compliant run, whereas the repair route used 2 calls, 1726 input tokens, and 2042 output tokens. I would still prefer the repair loop when the prompt is expensive to design carefully in advance, or when a user is working interactively and needs a quick fallback that fixes a known formatting issue without re-engineering the entire prompt from scratch.

## Analysis Question 4

Your checker tests for the literal string "Verona". Write one summary that is semantically correct but fails your checker, and one that is semantically wrong but passes it. What does this pair demonstrate about string matching as an evaluation method, and what would you replace it with?

### Answer

A semantically correct summary that fails the checker is: "Two young lovers from rival families in northern Italy die after a feud tears their city apart, and the tragedy shows how love is destroyed by inherited hatred." This is correct in meaning, but it does not contain the literal string Verona, so the checker rejects it.

A semantically wrong summary that passes the checker is: "In Verona, the Montague and Capulet families feud, and Romeo and Juliet marry and live happily ever after." This contains Verona, Montague, and Capulet, so the checker passes it, even though the outcome is factually wrong.

This pair shows that literal string matching is brittle: it can miss correct paraphrases and accept incorrect statements that happen to contain the right words. A better replacement would be a semantic checker that verifies the required entities and events with an entailment or rubric-based judge, or by extracting structured facts and checking them against the story rather than only searching for strings.
