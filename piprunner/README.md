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
- [Current UI 0.5 independent 1H structure](docs/ONE_HOUR_STRUCTURE.md)
- [Current UI 0.6 independent 15m structure](docs/FIFTEEN_MINUTE_STRUCTURE.md)
- [Location and Strong Price Action specification](docs/LOCATION_SPA_SPEC.md)

Architecture: **4H bias → 1H setup → 15m structure and execution**.

Preserve the End-of-P2 sequence: CHoCH, separate swing break, retest, qualifying signal candle, one-tick breakout entry, three-bar expiry, stop beyond the retest extreme, minimum 2R opportunity, 50% at TP1 and runner. Exact unresolved predicates are tracked in the requirements.

EMA 36/100 and 15m Williams Fractals are independent optional experiments. Chart annotation visibility must never change trading decisions.

## Current status

UI 0.6 provides proposed 4H/1H/15m research structure in `src/piprunner_4h_bias.pine`. All three layers appear on 15m; 1H displays 4H/1H and 4H displays its own layer. Configurable colors distinguish timeframe and direction; BOS/CHoCH defaults Large. Twenty-one local reference tests pass; revised Pine compilation/replay remains pending. No P2/SPA setup qualification, retest, signal-candle entry or orders are implemented. The Word design has not passed visual rendering verification.

The confirmed platform is **TradingView**. New chart scripts will use **Pine Script v6**. The first implementation is the proposed non-repainting 4H Bias indicator with configurable learning annotations and causal tests. Proposed structural rules remain subject to chart review and approval.

Source and tests live in `src/` and `tests/`. Each feature should include its rule references, tests, annotation behavior and remaining limitations.
