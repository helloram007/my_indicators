# Two-indicator requirements split

5 November 2026. CONFIRMED product separation requested by the user. These documents supersede the single-product interpretation of requirements.md; retain that file for detailed historical mechanics/test cases, subject to subsequent decisions.

1. **MTA-End-of-P2**: standalone multi-timeframe End-of-P2 analysis, setup and entry-plan indicator. Requirements: [MTA_END_OF_P2_REQUIREMENTS.md](MTA_END_OF_P2_REQUIREMENTS.md). Skill: `mta-end-of-p2`.
2. **Piprunner + MTA-End-of-P2**: the same baseline plus an additional confirmed 15m Williams Fractal continuation gate. Requirements: [PIPRUNNER_MTA_END_OF_P2_REQUIREMENTS.md](PIPRUNNER_MTA_END_OF_P2_REQUIREMENTS.md). Skill: `piprunner-mta-end-of-p2`.

The user explicitly chose **add fractal confirmation; preserve the full End-of-P2 entry sequence**. Original Piprunner's one-pip entry, opposite-fractal stop and 1R target are excluded from both indicators. The historical combined skill is retained only as a compatibility router.

Current `src/piprunner_4h_bias.pine` UI1.1.0 remains an unchanged shared research prototype. Two separate runnable indicators have NOT been produced by this documentation/skill split. Proposed future entrypoints are `src/mta_end_of_p2.pine` and `src/piprunner_mta_end_of_p2.pine`; do not claim they exist. Shared algorithms must remain version-aligned with independent instance state, settings and names. Pine library versus generated shared-source blocks remains an implementation choice.

Read [SHARED_MTA_CONTRACT.md](SHARED_MTA_CONTRACT.md) for common rules and [DASHBOARD_WORKFLOW.md](DASHBOARD_WORKFLOW.md) for the horizontal/vertical panel contract. Open `../workflows/mta-workflow-dashboard.html` locally for the interactive design dashboard. That browser dashboard contains no market feed and is not connected to TradingView.

## Staged implementation

1. Review unresolved baseline definitions; extract two separately named indicator entrypoints without changing shared calculation outputs.
2. Validate the proposed 4H/zone model; implement S/R and full 1H setup lifecycle.
3. Complete baseline 15m execution-plan states, expiry and risk/management annotations.
4. Implement confirmation-aware Williams Fractals and continuation candidates independently; integrate the selected additional gate with agreed timing.
5. Build TradingView horizontal/vertical dashboards over the same snapshot; regression-test product parity and gate isolation.
6. Run replay/reload, locked backtests in separate strategy harnesses and paper-forward checks. Indicators themselves do not place orders.

Open decisions block the corresponding release, not unrelated documentation or display work. No performance claims or live execution authorization follow from this split.
