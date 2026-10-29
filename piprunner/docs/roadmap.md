# Feature checklist

Checked items represent delivered work, not approval of proposed trading rules.

- [x] Create the `piprunner` project directory.
- [x] Record requirements, confirmed invariants and open decisions.
- [x] Specify configurable learning annotations AN01–AN18.
- [x] Confirm platform: TradingView; use Pine Script v6 for new scripts.
- [x] Add durable AI instructions, project handover and decision log.
- [ ] Obtain any existing strategy scripts, if available; none supplied yet.
- [x] Implement proposed 4H Bias source with confirmed pivots, structural classification and protected levels; platform compilation pending.
- [x] Add initial 4H learning annotations, checklist shell and Training/Guided/Minimal/Off controls; visual acceptance pending.
- [x] Pass 10 independent local reference tests; see `4H_BIAS.md` for coverage and limitations.
- [ ] Compile the Pine source and validate replay/visual behavior in TradingView.
- [x] Review user snapshot on 4H/1H/15m: matching current state and partial visual evidence; see `CHART_REVIEW_001.md`.
- [x] Implement UI 0.2 compact/opaque panel, optional future rows, label spacing, structure colors and developing-price explanation.
- [x] UI 0.2 output visible in user screenshot; presentation superseded by UI 0.3 before full acceptance.
- [x] Review user UI 0.2 screenshot: indicator runs but bubble clutter remains unacceptable; superseded by UI 0.3.
- [x] Implement UI 0.3 horizontal levels, updating current labels, bounded proposed 4H BOS/CHoCH history and Summary panel.
- [x] Pass 15 local reference tests (bias and educational break overlay); platform checks remain separate.
- [ ] Validate UI 0.3 compilation, line readability, publication timing and numeric audit parity in TradingView.
- [x] User reports UI 0.3 gives a clear view; this is partial presentation acceptance, not model/replay approval.
- [x] UI 0.4: independent larger BOS/CHoCH text control and durable future timeframe-color requirements.
- [ ] Check UI 0.4 larger-text readability in TradingView.
- [ ] Apply distinct configurable 1H/15m color families and larger BOS/CHoCH text when those layers are implemented.
- [x] UI 0.5: independent proposed 1H structure, blue/orange levels, large BOS/CHoCH, alignment summary and controls.
- [x] Pass 18 local reference tests including synthetic multi-timeframe clocks and strength isolation.
- [ ] Compile/replay UI 0.5 and compare 1H snapshots on 1H/15m; see `ONE_HOUR_STRUCTURE.md`.
- [x] UI 0.6: independent 15m research structure on 15m charts, fuchsia/yellow levels, large BOS/CHoCH and layer controls.
- [x] Pass 21 local reference tests; snapshot, higher-layer request/render blocks and 11 audit plots unchanged.
- [ ] Compile/replay UI 0.6, check three-layer readability and fixed-history annotation-toggle parity.
- [x] UI 0.7 temporary current swing names 4SH/4SL, 1SH/1SL and 15SH/15SL with reversible display toggle.
- [x] UI 0.8 combines swing names and classification with slash, e.g. 4SH/HH and 4SL/HL.
- [ ] Visually check all six names and toggle in TradingView; earlier replay acceptance gates remain open.
- [x] User confirms protection updated after the 4H close in their example; single-transition evidence only.
- [x] UI 0.9: optional live-breach wording explains why confirmed 4H protection is retained before close.
- [ ] Define actual location/P2/SPA and 15m entry predicates before promoting research labels into setup/entry qualification.
- [x] Confirm SPA = Strong Price Action; end of P2; either S/R or S/D plus any one directional SPA pattern.
- [x] Confirm S/D zone invalidation on any far-edge wick breach; keep 4H structural bias close-confirmed.
- [x] Review user course and draft `LOCATION_SPA_SPEC.md` with confirmed intent, proposed mechanics and implementation tests.
- [ ] Finalize zone detector, pattern strength/contact and remaining S/R/short-pattern decisions before setup qualification.
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
