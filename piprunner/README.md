# Piprunner and End-of-P2

Development home for the multi-timeframe strategy. All strategy-specific code, tests and documentation belong inside `piprunner/`.

## Design

- [Requirements and design](docs/requirements.md)
- [Editable Word document](docs/requirements.docx)
- [Feature checklist](docs/roadmap.md)

Architecture: **4H bias → 1H setup → 15m structure and execution**.

Preserve the End-of-P2 sequence: CHoCH, separate swing break, retest, qualifying signal candle, one-tick breakout entry, three-bar expiry, stop beyond the retest extreme, minimum 2R opportunity, 50% at TP1 and runner. Exact unresolved predicates are tracked in the requirements.

EMA 36/100 and 15m Williams Fractals are independent optional experiments. Chart annotation visibility must never change trading decisions.

## Current status

Documentation foundation only. No executable indicator or trading strategy has been implemented or validated. The Word document has not passed visual rendering verification; Markdown is the reviewable text version.

The first implementation is the proposed non-repainting 4H Bias indicator with configurable learning annotations and causal tests. Confirm the target platform before adding platform-specific source code. Proposed structural rules remain subject to chart review and approval.

Future source and tests will live in `src/` and `tests/` when implemented. Each feature should include its rule references, tests, annotation behavior and remaining limitations.
