# Piprunner and End-of-P2

Development home for the multi-timeframe strategy. All strategy-specific code, tests and documentation belong inside `piprunner/`.

## Design

- [Start here for project context](docs/PROJECT_CONTEXT.md)
- [Confirmed decisions and proposals](docs/DECISIONS.md)
- [Requirements and design](docs/requirements.md)
- [Editable Word document](docs/requirements.docx)
- [Feature checklist](docs/roadmap.md)
- [4H Bias source and TradingView instructions](docs/4H_BIAS.md)
- [UI 0.2 display update and review settings](docs/UI_02.md)
- [Current UI 0.3 horizontal structure display](docs/UI_03.md)
- [UI 0.4 event text and future timeframe color conventions](docs/ANNOTATION_STYLE.md)

Architecture: **4H bias → 1H setup → 15m structure and execution**.

Preserve the End-of-P2 sequence: CHoCH, separate swing break, retest, qualifying signal candle, one-tick breakout entry, three-bar expiry, stop beyond the retest extreme, minimum 2R opportunity, 50% at TP1 and runner. Exact unresolved predicates are tracked in the requirements.

EMA 36/100 and 15m Williams Fractals are independent optional experiments. Chart annotation visibility must never change trading decisions.

## Current status

The first Pine v6 4H Bias indicator is implemented in `src/piprunner_4h_bias.pine`. UI 0.3 defaults to horizontal levels with updating 4H labels and proposed educational BOS/CHoCH annotations. Fifteen independent Python reference tests pass. Earlier revisions visibly ran on user charts, but this revision's TradingView compilation and replay are pending; this is not an order-generating strategy. The Word document has not passed visual rendering verification; Markdown is the reviewable text version.

The confirmed platform is **TradingView**. New chart scripts will use **Pine Script v6**. The first implementation is the proposed non-repainting 4H Bias indicator with configurable learning annotations and causal tests. Proposed structural rules remain subject to chart review and approval.

Source and tests live in `src/` and `tests/`. Each feature should include its rule references, tests, annotation behavior and remaining limitations.
