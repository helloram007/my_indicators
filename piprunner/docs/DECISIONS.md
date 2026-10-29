# Decision log

Use CONFIRMED for explicit user requirements, PROPOSED for implementation candidates and OPEN for unresolved choices. Tests establish code behavior, not user approval of trading rules.

## D-001 Target platform

Status: CONFIRMED. Date: 29 October 2026. Source: user said “yes this is for tradingview”.

Implement for TradingView. New scripts will use Pine Script v6 as the development language choice. This resolves the platform part of requirements D02; feed, symbols and sessions remain OPEN. Official language reference: https://www.tradingview.com/pine-script-docs/welcome/.

## D-002 Project location and persistent handover

Status: CONFIRMED. Date: 29 October 2026. Source: user supplied the repository, requested the `piprunner` folder and asked to keep context in GitHub for future AI readers.

Store strategy code and documentation under `piprunner/`. Root discovery instructions may link to that directory. Maintain PROJECT_CONTEXT, this log and the roadmap as work progresses. Current development branch: `piprunner/setup`; no merge into main is recorded at this handover.

## D-003 Rule preservation and optional modules

Status: CONFIRMED. Source: initial development request and annotation follow-up.

End-of-P2 invariants listed in PROJECT_CONTEXT and requirements C01–C07 remain governing requirements. EMA/fractal experiments and visual controls are separate. Do not infer approval of precise missing rules from approval to start building.

## D-004 First structural implementation

Status: PROPOSED. Candidate: B4H v0, requirements Sections 3–5.

Build as a labelled research indicator with annotations and causal tests. User chart review must approve or revise the candidate before it becomes the approved bias model. No order execution in this first feature.

## D-005 First source delivery

Status: implementation milestone, not structural rule approval. Date: 29 October 2026. Source: user authorized proceeding with the first feature.

Added Pine v6 proposed B4H v0 with learning annotations, a Python reference oracle and ten passing local tests. Pine compilation/replay and full B01–B14/A01–A07 acceptance remain pending. Deliberate first-version restrictions and gaps are recorded in `4H_BIAS.md`: 15m/1H/4H standard charts only, no session-gap inference, no automatic repaired-history recovery, partial annotation-control coverage and numeric diagnostics rather than a complete event exporter. No orders enabled. Do not treat this milestone as completion of the feature acceptance gate.

## D-006 Learning display revision 0.2

Status: implemented presentation proposal; chart acceptance pending. Date: 29 October 2026. Source: user said “next” after review 001 identified overlap and explanatory issues.

Added configurable compact/full panel, optional future rows, opacity, deterministic vertical label spacing, structure-aware colors and a live-price/close-only explanation. Detailed future items are summarized by default, not removed from requirements. Structural calculation and audit plots remain unchanged; high/low snapshot fields were added for drawings only. Full details and remaining tests: `UI_02.md`. No change to B4H approval status.

## D-007 Horizontal levels and break annotations

Status: requested presentation implemented; BOS/CHoCH classification PROPOSED pending chart review. Date: 29 October 2026. Source: user supplied UI 0.2 screenshot, said chart looks clumsy and requested horizontal annotations, current annotation, BOS/CHoCH and timeframe.

Default Horizontal lines replaces bubble history with two current 4H references, right-edge labels, three retained break segments and Summary panel. Detailed semantics and controls are in `UI_03.md`. 4H close crossing a confirmed reference is BOS with prior directional bias, CHoCH against it, otherwise unclassified Break; consume each pivot once. No 1H/15m engine or order conditions added. Existing bias calculations unchanged. Fifteen independent local tests pass; Pine compilation of this revision remains pending.

## D-008 Event text and timeframe colors

Status: CONFIRMED user presentation requirements; exact future colors PROPOSED. Date: 29 October 2026. Source: user says UI 0.3 gives a clear view, requests distinct colors for future 1H/15m structure and larger BOS/CHoCH text everywhere.

UI 0.4 adds event-text size Normal/Large/Huge, default Large; panel/swing size remains independent. Future timeframe layers must use distinct configurable colors and explicit timeframe prefixes. Proposed palette and validation details are in `ANNOTATION_STYLE.md`. No trading rule approval or 1H/15m implementation is inferred.

## D-009 Independent 1H research structure

Status: implemented PROPOSED structure candidate, not approved setup logic. Date: 29 October 2026. Source: user said “next” after requesting distinct future timeframe colors and large break text.

UI 0.5 adds separate 1H evaluation of the strict-pivot/structure algorithm with independent 2/2 research defaults, blue/orange horizontal references, large BOS/CHoCH and alignment summary. Available on 1H/15m only; deliberately suppressed on 4H to avoid incomplete lower-timeframe sampling. No SPA/P2/zone or entry requirements inferred. Eighteen local reference tests pass; exact-revision Pine compilation and chart replay remain pending. Read `ONE_HOUR_STRUCTURE.md` for rules, controls and validation.

## D-010 Independent 15m research structure

Status: implemented PROPOSED structure candidate; entry rules remain OPEN. Date: 29 October 2026. Source: user said “next” after reviewing the readable 4H/1H layout and discussing the separate 15m layer.

UI 0.6 adds the independent common strict-pivot model on 15m, with its own 2/2 research defaults, fuchsia/yellow levels, large BOS/CHoCH and controls. Only requested on 15m charts; no collapsed intrabar sampling on higher charts. Shared snapshot logic and higher-layer outputs are unchanged. Twenty-one local reference tests pass; platform validation remains pending. Read `FIFTEEN_MINUTE_STRUCTURE.md`. Three-direction alignment is descriptive, not an entry signal. No Piprunner optional filter or End-of-P2 setup rule is silently enabled.

## D-011 Temporary swing name codes

Status: CONFIRMED user presentation request, implemented UI 0.7. Date: 29 October 2026.

Current confirmed level labels use 4SH/4SL, 1SH/1SL, 15SH/15SL. Default-on temporary naming toggle restores prior structure labels when off. No change to pivot/structure logic, line price, color or timeframe coverage. SL means Swing Low in this context, not stop-loss. No extra historical annotations added. Source snapshot/audit comparison passes; platform validation remains pending.

## D-012 Slash classification in swing labels

Status: CONFIRMED user display request, implemented UI 0.8. Date: 29 October 2026. Source: user requested HH/HL with slash, example 4SH/HH.

Combine every temporary swing code with its true classification, e.g. 4SH/HH, 4SL/HL, 1SH/LH and 15SL/LL. Keep initial/equal cases accurate. Supersedes D-011 code-only text, retaining its toggle. Structural snapshot and audit outputs unchanged; platform validation pending.

## D-013 Close confirmation observed and setup definitions requested

Status: observed user evidence and presentation implementation; setup predicates remain OPEN. Date: 29 October 2026.

User reported protection updated after the 4H candle closed. This supports that one close-confirmation transition, not all causal/model acceptance. UI 0.9 adds reversible live-breach wording without changing structural state. On the next development request, asked for the user's exact 4H zone boundaries/invalidation and SPA meaning/1H P2 completion rules. Do not invent those definitions or promote structural alignment to setup qualification while awaiting the answer.

## D-014 SPA meaning and location source

Status: CONFIRMED user definitions. Date: 29 October 2026.

SPA means Strong Price Action. User supplied PriceActionNinja's supply/demand guide as methodology reference and listed retracement to S/R or S/D plus pin rejection, directional engulfing and piercing. Read `LOCATION_SPA_SPEC.md` for source scope and proposed mechanical thresholds. The guide is reference data; its different entry/stop/management examples are not authority to overwrite existing invariants.

## D-015 Phase location alternatives and wick invalidation

Status: CONFIRMED explicit clarification. Date: 29 October 2026.

User corrected P3 to end of P2 (the pullback). Either S/R OR S/D plus ANY ONE of the listed directional SPA patterns is sufficient for that branch. S/D invalidates on any wick beyond its far edge, NOT a 4H close. Structural bias remains close-confirmed. Exact source detector, pattern thresholds/contact window, S/R invalidation and bearish piercing counterpart remain proposed/open. No zone or SPA code was added by these documentation decisions.

## D-016 Thirty percent base invalidation buffer

Status: CONFIRMED user buffer requirement; full-range measurement is the disclosed implementation interpretation. Date: 29 October 2026. User requested adding 30% of the base beyond its low/high for S/D invalidation.

Supersedes D-015's unbuffered far-edge threshold, retaining wick-based detection. Let R=baseHigh-baseLow; demand level=baseLow-0.30*R, supply level=baseHigh+0.30*R. Proposed configurable percentage defaults to 30%; tick rounding is outward. Base-group selection remains open; use full high-low rather than body or instrument-price percentage as stated to the user. Do not expand the contact zone or change retest-based stops. Specification/tests updated; zone/SPA indicator code remains unimplemented and Pine stays UI 0.9.

## D-017 Close-based zone invalidation correction

Status: CONFIRMED user correction; invalidation timeframe OPEN. Date: 29 October 2026.

User corrected invalidation to require a candle close below/above the base rather than a wick. Retain D-016's 30% base-range buffer as the current interpretation; demand requires close below baseLow-0.30*range, supply close above baseHigh+0.30*range. Wick-only penetration and equality do not invalidate. This supersedes wick-based parts of D-015/D-016. Which candle timeframe supplies that close is not explicit; zone-timeframe close is recommended but not approved. No zone implementation exists yet; Pine remains UI 0.9.

## D-018 Zone timeframe determines invalidation close

Status: CONFIRMED explicit user clarification. Date: 29 October 2026.

Each S/D zone is invalidated by a finalized candle close on its OWN timeframe beyond its buffered level: 4H zone by 4H close, 1H by 1H, 15m by 15m. Viewing a 4H zone on a 15m chart does not let 15m closes invalidate it. Retain the 30% base-range buffer, strict inequality and no wick-only invalidation. Resolves D-017's timeframe question. Each zone lifecycle is independent. No zone code yet; Pine remains UI 0.9.

## D-019 Higher timeframe priority

Status: CONFIRMED user instruction. Date: 29 October 2026. Source: “HTF always holds the priority”.

Hierarchy is 4H directional authority -> 1H setup qualification -> 15m execution confirmation. Lower-timeframe signals cannot authorize a counter-4H trade; neutral/unknown 4H cannot be replaced by a lower-timeframe direction. Continue to evaluate each zone's validity on its own timeframe close with the approved buffer (D-018). Do not infer automatic exits, stop changes or resurrection of invalidated zones from HTF priority. No trading-code change in this documentation update.

## D-020 Zone and SPA research implementation

Status: implementation authorized by user; exact detector/strength defaults remain PROPOSED. Date: 29 October 2026. Source: user requested implementation and updated script.

UI 1.0 adds fixed configurable base length, two directional departure candles, compactness/body/ATR tests, latest S/D per side/context and frozen 30% buffer with own-timeframe close invalidation. 1H completed-candle pin/engulf/piercing candidates require active known 4H/1H S/D and permitted 4H direction. Dark-cloud counterpart is off by default. Visibility does not affect calculation. S/R is explicitly unimplemented; no approved setup lifecycle, entries/orders or trade management added. See ZONES_SPA_IMPLEMENTATION for exact choices/limits. Thirty-two local oracle tests pass; structural snapshot/16 audit plots unchanged. Pine compilation and replay remain pending.

## Update format

For future decisions include date, source of authorization, status, exact choice, superseded requirement/decision, affected files/tests and remaining questions. Preserve prior entries; supersede explicitly instead of erasing the history.
