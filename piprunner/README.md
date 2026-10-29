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
- [Current UI 1.0 zones and SPA implementation](docs/ZONES_SPA_IMPLEMENTATION.md)

Architecture: **4H bias → 1H setup → 15m structure and execution**.

Preserve the End-of-P2 sequence: CHoCH, separate swing break, retest, qualifying signal candle, one-tick breakout entry, three-bar expiry, stop beyond the retest extreme, minimum 2R opportunity, 50% at TP1 and runner. Exact unresolved predicates are tracked in the requirements.

EMA 36/100 and 15m Williams Fractals are independent optional experiments. Chart annotation visibility must never change trading decisions.

## Current status

UI 1.0 provides proposed 4H/1H/15m structure, automated S/D candidate zones with 30% own-timeframe close invalidation, and 1H HTF-aligned S/D SPA research annotations. See ZONES_SPA_IMPLEMENTATION for configurable detector/pattern defaults and latest-zone limits. Thirty-two local oracle tests pass; updated Pine compilation/replay is pending. Separate S/R, complete setup lifecycle and qualified 15m entry/orders are not implemented. The Word design has not passed visual rendering verification.

The confirmed platform is **TradingView**. New chart scripts will use **Pine Script v6**. The first implementation is the proposed non-repainting 4H Bias indicator with configurable learning annotations and causal tests. Proposed structural rules remain subject to chart review and approval.

Source and tests live in `src/` and `tests/`. Each feature should include its rule references, tests, annotation behavior and remaining limitations.
