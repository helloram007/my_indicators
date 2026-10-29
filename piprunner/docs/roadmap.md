# Feature checklist

Checked items represent delivered work, not approval of proposed trading rules.

- [x] Create the `piprunner` project directory.
- [x] Record requirements, confirmed invariants and open decisions.
- [x] Specify configurable learning annotations AN01–AN18.
- [x] Confirm platform: TradingView; use Pine Script v6 for new scripts.
- [x] Add durable AI instructions, project handover and decision log.
- [ ] Obtain any existing strategy scripts, if available; none supplied yet.
- [ ] Implement proposed 4H Bias with confirmed pivots, structural classification and protected levels.
- [ ] Add 4H learning annotations, checklist shell and Training/Guided/Minimal/Off controls.
- [ ] Pass B01–B14 causal and state tests; review B15 chart examples.
- [ ] Approve or revise the 4H structural model.
- [ ] Define and implement 4H location and 1H P2/SPA qualification.
- [ ] Define and implement 15m CHoCH, separate swing break and retest.
- [ ] Implement approved signal candle, one-tick entry, expiry and stop rules.
- [ ] Resolve minimum-2R interpretation, TP1 and runner policies; implement position management.
- [ ] Add optional EMA and fractal modules independently.
- [ ] Complete A01–A07 annotation acceptance tests as features become available.
- [ ] Run chronological backtests with declared costs and untouched evaluation data.
- [ ] Complete paper forward validation before considering live execution.

## First feature delivery

Scope: 4H Bias only, no orders. Include state and reason, confirmed swing labels, protected levels, origin/confirmation/publication timestamps, invalidation and rearming explanations, and configurable visibility. Later unimplemented checklist rows must not display PASS.

Acceptance: deterministic results, no future-data use, stable replay/reload outputs and identical decision ledgers with annotations enabled or disabled. See requirements Sections 3–5 and 10–11.
