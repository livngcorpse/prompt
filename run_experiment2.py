import time

from prompts import BASELINE_RUNS, ABLATIONS, VARIANCE_CASES
from pe_lab import safe_ask


def run_cases(cases):
    for idx, (tag, prompt, system, temperature) in enumerate(cases, start=1):
        safe_ask(
            prompt,
            system=system,
            temperature=temperature,
            max_tokens=512,
            tag=tag,
        )

        if idx % 5 == 0:
            print(f"Completed batch of 5 calls. Waiting 12 seconds for quota reset...")
            time.sleep(12)


if __name__ == "__main__":
    # Preserve existing run history and append new Experiment 2 entries.
    # Run baseline + ablations
    run_cases(BASELINE_RUNS)
    run_cases(ABLATIONS)

    # Run variance probe
    run_cases(VARIANCE_CASES)

    print("Experiment 2 completed.")
