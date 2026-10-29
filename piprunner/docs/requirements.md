# Piprunner and End of P2
Strategy Requirements and Design Document
Version 0.2 | 29 October 2026 | Requirements baseline and proposed implementation design

This document defines a hybrid strategy in which 4H structure supplies directional bias, 1H analysis qualifies a P2 setup, and 15m structure and price action control entry. The immediate development deliverable is a non-repainting 4H Bias indicator with an auditable event log. Trading execution follows only after the remaining strategy definitions are resolved and tested.
End-of-P2 remains the governing strategy. Piprunner EMA alignment and Williams Fractals are optional experimental modules. Their inclusion must never silently change entry offsets, stop placement, minimum reward, expiry or partial exits.
### Status conventions
CONFIRMED means explicitly required in the current request. SOURCE means described in the earlier conversation but not independently approved as a precise mechanical rule. PROPOSED means a concrete design candidate for review and testing. OPEN means a decision is still needed before the affected feature can be considered production ready.
All algorithmic choices below are PROPOSED unless identified as CONFIRMED. A precise proposed rule is not an approved change to the trading methodology. No profitability or backtest results are claimed.
### Confirmed invariants
- C01 Architecture: 4H bias, 1H setup, 15m structure and execution.
- C02 Entry sequence: 15m CHoCH, required swing break, retest, qualifying signal candle, breakout entry one minimum tick beyond the signal candle.
- C03 Pending order expiry: three bars. Exact counting and event precedence are proposed in Section 6.
- C04 Stop beyond the retest extreme; minimum 2R opportunity; close 50% at TP1 and retain a runner.
- C05 EMA 36/100 and Williams Fractals are optional A/B features, not mandatory replacements.
- C06 Develop 4H Bias first, with clear non-repainting rules and tests.
- C07 Provide configurable educational annotations for every required checklist item across all timeframes, allowing the user to reduce or disable them over time. Exact presentation defaults below are proposed.
### Document map
Sections 1 and 2 specify requirements, architecture and interfaces. Sections 3 to 5 define the proposed 4H Bias feature and its acceptance tests. Sections 6 and 7 specify execution and experiment controls. Sections 8 and 9 define validation, development gates and open decisions.
## 1 Scope and rule ownership
### Strategy boundary
The hybrid seeks continuation after a countertrend P2 pullback. P1 and P2 are working labels for expansion and pullback, not yet sufficient machine definitions. The system must distinguish directional bias, eligible location, setup validity and execution trigger. A bullish bias alone is never an entry signal.
SOURCE context includes 4H supply and demand zones, possible FVG context, HTF CHoCH and SPA confirmation, and 1H SPA setup/location analysis. The earlier assistant described these; it did not provide the user's complete End-of-P2 manual. Definitions and mandatory status remain OPEN. The zone and SPA modules must not be bypassed in a strategy labelled a fully validated End-of-P2 implementation.
### Functional requirements
- FR01 Emit 4H bias as UNKNOWN, NEUTRAL, BULLISH or BEARISH using only information available at the event timestamp. Supply reason and evidence references.
- FR02 Expose 4H location separately from bias. Unspecified location rules report UNDEFINED and block fully automated setup qualification.
- FR03 Create a 1H setup only when approved setup and location predicates pass in the permitted direction. Assign a unique setup ID and explicit invalidation condition.
- FR04 Track CHoCH, subsequent swing break, retest and signal candle as distinct 15m events linked to that setup. A fractal marker alone satisfies none of these predicates.
- FR05 Freeze signal-candle entry, retest stop and target references when arming the order. Reject nonpositive risk, invalid price rounding, insufficient reward or unresolved required predicates.
- FR06 Enforce three-bar expiry, one active order per setup and idempotent cancellation. Record every rejection and cancellation reason.
- FR07 Manage 50% TP1 and runner as separate position components sharing the initial risk reference. Runner stop and exit rules require an explicit policy.
- FR08 Keep EMA and fractal modules independently switchable. With both off, the baseline must reproduce the approved End-of-P2 rules.
- FR09 Export event, setup, order and trade ledgers including configuration, data version, costs and experiment variant.
### Explicit exclusions from the hybrid baseline
Original Piprunner uses fractal entry plus or minus one pip, an opposite-fractal stop and a fixed 1R target. These are SOURCE rules for a separate comparator only. Its one-unit sizing, million-dollar capital and zero-cost assumptions are not inherited by the hybrid. No live execution is included in the first feature.
### Acceptance of the overall specification
Every confirmed rule has a testable implementation reference; every unresolved predicate is visibly blocked or explicitly marked as a research proxy. An experiment cannot be presented as the confirmed baseline when it changes an invariant.
## 2 Architecture and data contracts
### Module flow
Market data and calendar -> confirmed bars -> 4H structural engine -> bias and location gates -> 1H setup engine -> 15m execution state machine -> order and risk engine -> position management -> audit and experiment reporting.
Bias is a context service. Location and 1H setup are independent services. Optional 15m EMA filtering and fractal-assisted pivots feed the execution engine through named interfaces. They do not write directly to orders or exits.
### Required records
Bar: symbol, feed ID, timeframe, open time, close time, OHLC, volume if available, finality, session and data-quality status. Price calculations use integer ticks where possible. Tick size and pip size are separate instrument metadata.
Pivot: ID, side, price, pivot bar time, confirmation time, strength, source module and configuration version. Historical drawing time may be the pivot time; actionable time is always confirmation time.
BiasSnapshot: symbol, version, as-of 4H close, publication time, state, last two confirmed highs and lows, protected high/low, consumed reference IDs, reason code and quality status.
Setup: ID, direction, 4H snapshot version, 1H creation time, zone IDs and bounds, P2 evidence, invalidation level, validity deadline and status. Undefined fields cannot be replaced by guessed values.
ExecutionContext: setup ID, CHoCH event, swing-break reference, retest interval and extreme, signal-candle time and OHLC, frozen entry/stop/TP1, expiry bar, optional module flags and rejection reasons.
Order and Trade: client ID, submission and acknowledgement times, fill prices and quantities, slippage, initial risk, partial exits, runner state, fees and final net R.
### Clock and synchronization contract
PROPOSED: use feed-native 4H and 1H bar boundaries; store times in UTC and display in a chosen timezone. Do not infer 4H boundaries from the user's timezone. Lock feed, session and calendar in each run.
Process final bars in timestamp order, updating available 4H context before 1H and 15m decisions at the same decision timestamp. A context change can affect a new decision only after it is published. It cannot retroactively cancel a fill that occurred earlier in the closing interval.
Missing or nonfinal bars trigger a data-quality block, not synthetic confirmations. Market-closed intervals do not count as new candles. Feed revisions create a new data version; they are not silently merged into prior test results.
### Nonfunctional requirements
- NFR01 Determinism: identical ordered data and configuration produce identical event IDs, state transitions and trade decisions across reruns.
- NFR02 Causality: appended future bars cannot alter already published outputs on unchanged data. State must survive replay/restart from the same warm-up boundary.
- NFR03 Traceability: each bias and order decision includes timestamped source bars, pivot IDs, prior state, new state and reason.
- NFR04 Safety: missing inputs, invalid instrument metadata and undefined mandatory rules block new orders and expose an error; active positions retain their protective orders.
- NFR05 Performance: process each finalized bar once; use bounded pivot buffers and retained event logs. A numeric runtime budget will be set after platform and symbol count are chosen.
- NFR06 Configuration: version every rule change, validate ranges and prohibit silent defaults for risk or account settings. Platform-specific limitations must be documented before execution release.
## 3 First feature 4H Bias rules
### Proposed candidate B4H v0
Purpose: supply a mechanically reproducible structural direction. This candidate is a research definition to compare with the user's annotated 4H charts. It does not assume approval of a particular swing strength or substitute an EMA trend for structure.
Inputs: timeframe fixed to 4H; pivot left strength L4=2 and right strength R4=2 as proposed research defaults, integer minimum 1; strict comparisons; wick-based pivot prices; close-based breaks; fixed feed/session; tick size from instrument metadata. EMA and 15m Williams switches have no effect on this feature.
Although a 2/2 pivot resembles a Williams Fractal, this is an explicitly proposed 4H structural extractor, independently configured from the optional 15m Piprunner module. If this extractor is not accepted, replace it with an approved causal swing detector through the same interface.
### Pivot confirmation
At finalized 4H bar t, candidate p=t-R4 becomes a high pivot only if High[p] is strictly greater than every high in the L4 bars before p and R4 bars after p. A low pivot requires the symmetric strictly lower comparison. All bars in the window must exist and be final.
Equal prices disqualify the tied candidate; no hidden tolerance is applied. If one outside bar qualifies as both a high and a low, discard both for B4H v0 and log AMBIGUOUS_DUAL_PIVOT. These are proposed tie policies to test, not general claims about discretionary swing analysis.
Never replace a published pivot with a later more extreme pivot. Keep the high and low lists independently ordered by pivot time; consecutive same-side pivots are allowed. Use the last two confirmed highs and last two confirmed lows, without pretending they form an alternating sequence. An alternating swing model is a separate future candidate.
### Structural classification
Let Hprev and Hlast be the two latest confirmed high prices, and Lprev and Llast the two latest confirmed low prices. Bull candidate = Hlast > Hprev AND Llast > Lprev. Bear candidate = Hlast < Hprev AND Llast < Lprev. Equal or mixed pairs are structurally neutral candidates.
At a new pivot event, B4H v0 reclassifies from the latest pairs. Bull candidate sets BULLISH and protects Llast; bear candidate sets BEARISH and protects Hlast; mixed/equal pairs set NEUTRAL and clear active protection. With no new pivot and no protected-level break, hold the previous state. This can neutralize bias during a pullback before the opposite trend forms; that behavior is intentional in this candidate and must be reviewed against examples.
### Protected level invalidation
If previously BULLISH and a later finalized 4H close is strictly below the stored protected low, invalidate to NEUTRAL. If previously BEARISH and close is strictly above the stored protected high, invalidate to NEUTRAL. A wick breach or equality does not invalidate. Store the broken protection ID and mark the current pivot evidence tuple consumed.
Do not flip directly on a protected-level break. Opposite bias requires a new qualifying pivot event and the opposite structural classification. Do not rearm from the unchanged consumed tuple even if price rebounds. Same-direction rearming also requires new pivot evidence.
## 4 First feature state transitions and timing
### Update algorithm in exact priority order
1. Deduplicate by symbol and 4H close time. Validate the new bar and required history. Invalid data publishes UNKNOWN with a quality reason and blocks direction use; retain diagnostic history but do not infer missing bars.
2. On a valid bar after recovery, rebuild state from the unchanged valid warm-up boundary. UNKNOWN persists until replay is complete and two confirmed highs plus two confirmed lows exist. Then initialize through the classification rules below.
3. Evaluate a break of the PREVIOUS snapshot's protected level against the new close before processing any newly confirmed pivot. If broken, publish NEUTRAL, record invalidation, add any new pivots for later use, consume that evidence tuple and end this update. Invalidation wins over same-close confirmation.
4. Confirm and append eligible new pivots. If fewer than two highs or lows exist, publish UNKNOWN with INSUFFICIENT_STRUCTURE. No direction may be inferred from an EMA or a single swing pair.
5. On first sufficient history or a new unconsumed pivot tuple, classify the latest pairs. Publish BULLISH, BEARISH or NEUTRAL. A bullish candidate must also have current close >= its proposed protected low; a bearish candidate must have current close <= its proposed protected high. Otherwise publish NEUTRAL with ALREADY_INVALIDATED and consume the tuple.
6. Without a new tuple, hold the previous state and protection; update as-of time. Neutral holds until fresh evidence. Increment snapshot version only for a changed decision/evidence payload; record a heartbeat separately if needed.
### Transition contract
- UNKNOWN -> UNKNOWN: missing/invalid data or insufficient confirmed structure.
- UNKNOWN -> BULLISH or BEARISH or NEUTRAL: replay complete and sufficient evidence, using classification and protection checks.
- BULLISH -> NEUTRAL: protected low close-break has first priority, or a fresh tuple is mixed, equal or already invalidated.
- BEARISH -> NEUTRAL: symmetric protected high rule or fresh nonqualifying evidence.
- NEUTRAL -> BULLISH or BEARISH: new unconsumed tuple meets the directional and protection checks.
- BULLISH <-> BEARISH: permitted only on fresh opposite structural evidence when the prior protection is not broken on that same update. If it is broken, neutralization wins and opposite classification waits for a later fresh tuple.
- Any -> UNKNOWN: data-quality failure. Previously emitted history is preserved; new directional use is blocked until replay recovery.
### Publication and non repainting
A pivot at bar p becomes known only at the close of p+R4. With R4=2 this is two additional 4H bars after p closes, not at the plotted pivot. The bias becomes actionable no earlier than its publication timestamp. In a 15m close-only implementation, act at the first scheduled 15m decision that can observe that publication; log any additional platform delay.
For a Pine implementation, compute the state in the 4H context and request confirmed historical state fields with an appropriate historical offset and lookahead policy. TradingView documents the offset expression plus lookahead_on pattern for stable HTF requests. Never apply lookahead_on to an unoffset developing state, and never assume barstate checks alone solve cross-timeframe repainting. Validate the actual timestamp mapping with replay fixtures before using it for entries.
Reference: TradingView Concepts Other timeframes and data, Avoiding repainting, https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/ (reviewed 29 October 2026).
## 5 First feature tests and acceptance
### Deterministic unit fixtures
B01 Confirmation delay: with L4=R4=2 and highs [9,10,13,11,12], no high pivot is published through bar 3; pivot at index 2, price 13 is published only at bar 4 close. Using zero-based indices, lows [7,6,3,5,4] produce the symmetric low. Keep the opposite OHLC values valid in each fixture.
B02 Failed candidate: highs [9,10,13,11,14] produce no pivot at index 2. A live tentative marker must not enter the confirmed log.
B03 Equality: highs [9,10,13,13,12] reject index 2. A close exactly equal to protection holds bias; one tick beyond protection invalidates.
B04 Bull classification: inject already confirmed pivot records Hprev=100, Hlast=110, Lprev=90, Llast=95 with increasing timestamps and current close=105. Expect BULLISH, protected low=95 and evidence IDs preserved. Pair this engine fixture with a raw-OHLC integration fixture to prove confirmation timing.
B05 Bear classification: highs 110 then 100 and lows 95 then 90, close=94, produce BEARISH with protected high=100. Mixed pairs (100,110; 95,90) produce NEUTRAL.
B06 Wick versus close: start from B04. A later low=94 and close=96 holds BULLISH when no new pivot confirms. A later close=94 produces NEUTRAL. Rebound to 105 without new pivots remains NEUTRAL.
B07 Fresh recovery: after B06, confirm fresh evidence with highs 110 then 112, lows 95 then 97, close=108. Expect BULLISH protecting 97. Old evidence cannot rearm it.
B08 Invalidation priority: prior protection=95; new close=94 and new pivots on the same update otherwise imply a direction. Expect NEUTRAL and a consumed tuple, with no same-update reversal or rearm.
B09 Edge handling: dual high/low candidate is discarded; same-side pivot confirmations remain independent; missing window bar produces UNKNOWN; repeated event ID produces no duplicate pivot or transition.
B10 Warm-up and recovery: one high or one low is insufficient. After a data gap, direction remains unavailable until deterministic rebuild passes. Rebuilding from the same boundary reproduces the original valid prefix.
### Integration and property tests
B11 Prefix invariance: for every prefix of a fixed OHLC dataset, run from the same initial boundary. Compare outputs up to that prefix with the full run. Prices, states, evidence IDs and actionable times must match exactly.
B12 Replay parity: feed historical bars incrementally, then reload. Confirm no state or signal changes on unchanged finalized data. Mutate only the open 4H candle repeatedly and confirm no published 4H bias changes.
B13 Timeframe boundaries: test 4H closes aligned to 1H and 15m, DST transitions, market reopening and missing 15m bars. No child decision can use a snapshot before its publication. Each 4H close processes once.
B14 Independence: toggle 15m EMA and fractals across all four combinations. The 4H bias event ledger remains identical. Test a non-2/2 approved 4H extractor setting to show configurations are independent.
B15 Chart review: jointly label a proposed set of 20 bullish, 20 bearish and 20 mixed/invalidation examples. Log disagreements as definition issues; do not tune against unseen outcomes. Numeric sample size is proposed and reviewable.
### Feature acceptance gate
All B01 to B14 must pass with zero causal or timestamp mismatches; B15 must produce a reviewed discrepancy log. Display state, protected level, pivot time, confirmation time and publication time. No order submission is enabled. Deliver configuration schema, reference engine, event export and test results. User agreement on the structural candidate is required to call it the approved bias model; code correctness alone does not establish trading validity.
## 6 Setup and execution state machine
### Proposed predicates needing rule approval
1H SetupReady(direction) requires aligned available 4H bias, approved 4H location and 1H P2/SPA rules, an explicit invalidation level, and an active validity window. Until those definitions are resolved, use labelled manual annotations for research, not a guessed automatic proxy.
For 15m, propose closed-candle CHoCH through a frozen countertrend swing; a later closed-candle break through a separately identified continuation swing; a retest of that broken level/zone; then an approved signal candle. The precise swing selection, close-versus-wick rule, retest tolerance and candle predicate are OPEN. CHoCH and required swing break remain distinct events; this candidate does not allow one candle to satisfy both. Same-bar retest plus signal is also OPEN.
### Transitions with guards and actions
- BLOCKED -> WAIT_SETUP when data/configuration are valid and a directional 4H snapshot is available. Otherwise log the blocking reason.
- WAIT_SETUP -> WAIT_CHOCH on a valid 1H setup; freeze setup identity, direction and invalidation references.
- WAIT_CHOCH -> WAIT_SWING_BREAK on an approved, timestamped 15m CHoCH after setup availability; freeze the next swing reference.
- WAIT_SWING_BREAK -> WAIT_RETEST on the approved subsequent swing break; freeze broken level and retest zone.
- WAIT_RETEST -> WAIT_SIGNAL on an approved retest; retain retest start/end and extreme. If invalidated before confirmation, abandon the setup.
- WAIT_SIGNAL -> PENDING after the qualifying candle closes, valid stop and target exist, minimum reward passes and risk sizing is feasible. Freeze prices and submit one order.
- PENDING -> OPEN on a confirmed fill within validity; cancel remaining entry quantity under the partial-fill policy. PENDING -> CANCELLED on expiry or an approved invalidation before fill.
- OPEN -> RUNNER on a 50% TP1 fill; OPEN -> CLOSED on stop or other approved full exit. RUNNER -> CLOSED on its approved stop/exit. Actual quantities and fills govern state, not just price touches.
- CANCELLED or CLOSED -> WAIT_SETUP on a new eligible setup ID. No automatic rearm of an old signal. Any pre-entry state -> CANCELLED if setup invalidates; cancellation acknowledgement completes removal of a live order.
### Proposed three bar expiry convention
Signal candle S closes and arms the order. The order first becomes eligible on S+1; S+1, S+2 and S+3 are the three eligible completed 15m bars. Cancel unfilled order at S+3 close; it cannot fill on S+4. A touch during S does not count. This interpretation needs confirmation, because three-bar expiry alone does not define inclusivity.
### Event precedence
Use real event time when available: existing protective fills first, then entry fills that already occurred, then newly published context and setup decisions, then cancellations/submissions. On S+3, an established intrabar fill precedes close-time expiry. A new order at a candle close cannot use that candle's earlier high/low for a fill.
If bar data cannot resolve an entry/stop/expiry conflict, flag AMBIGUOUS_PATH and apply the declared conservative fill model, with sensitivity results. Proposed bias loss/reversal policy cancels pending setups but leaves filled trades to their exit rules. Any different policy is an experiment requiring explicit configuration.
## 7 Entry risk and trade management
### Frozen baseline prices
CONFIRMED: long stop-entry = signal-candle high + one minimum tick; short stop-entry = signal-candle low - one minimum tick. Tick is not a forex pip. Round prices outward to valid instrument ticks and retain original calculated prices for audit.
CONFIRMED: stop beyond retest extreme. PROPOSED research buffer is one tick below the lowest price of the accepted long retest interval, or one tick above the highest price of the short interval. Buffer amount and the interval's end must be approved. A later unrelated fractal cannot move this stop reference.
Let E be planned entry and S be initial stop. Long risk distance d=E-S; short d=S-E. Reject d<=0. Let T be the chosen first structural profit objective. Proposed minimum-2R interpretation requires (T-E)/d >=2 for longs or (E-T)/d >=2 for shorts before costs. The user must confirm whether the minimum applies to TP1, the ultimate objective or the whole position and whether costs are included. Until then record each interpretation and do not label automated target qualification approved.
TP1 closes 50% of original filled quantity, not 50% of the remaining balance. The other 50% becomes the runner. If TP1 is 2R, that partial contributes +1R of original position risk before costs; total trade R also includes the runner outcome. A minimum-2R opportunity does not guarantee a realized 2R result.
Runner target/trailing logic, break-even timing and post-TP1 stop are OPEN. Do not assume automatic break-even. TP1 and runner must never close more than the actual position; sibling protective order quantities must be adjusted after fills.
### Account and execution inputs
OPEN: symbol universe, risk per trade, account currency, initial capital, leverage/margin, lot step, minimum lot, maximum concurrent exposure and session limits. Proposed sizing: risk cash divided by stop distance times point value, currency adjusted and rounded down to lot step; reject quantities below minimum or exceeding exposure/margin limits.
Gap fills can change actual risk and available reward. Keep planned and actual R separately. Declare whether the order supports a maximum deviation or stop-limit constraint before assuming a gap can be rejected. A filled trade must receive protection even if post-fill reward is below the planned gate. Partial fills and indivisible position sizes require a declared rounding policy for the 50% exit.
### Optional Piprunner modules
EMA experiment: 15m close-based EMA36 > EMA100 permits longs; EMA36 < EMA100 permits shorts; equality blocks an EMA-filtered candidate. PROPOSED evaluation is at signal-candle close, with no retroactive changes. Whether a later crossover cancels a pending order is a separate switch, initially off for the comparison.
Fractal structure experiment: confirm 15m pivots only after R right bars close; proposed L=R=2. They supply candidate swing references, while all baseline CHoCH, swing-break, retest and candle predicates remain mandatory. Log lost opportunities caused by confirmation delay. Fractal plotting must show actionable confirmation time.
Fractal breakout experiment: a separate variant may require an additional confirmed fractal breakout after the same baseline setup. Replacing signal-candle entry with fractal plus one pip, opposite-fractal stop or 1R exit creates a separate comparator, never the baseline hybrid.
## 8 Validation and backtesting plan
### Engineering tests before performance claims
Unit-test every predicate and state guard with mirrored long/short fixtures. Test wrong-order events, duplicate events, equality, missing data, late confirmation and configuration changes. Assert that entry cannot precede setup/CHoCH/break/retest/signal, expiry cannot be extended silently, and optional modules cannot rewrite risk rules.
Execution fixtures: S+1 and S+3 fills, S+4 rejection, no fill on signal candle, stop before entry, gap through entry, simultaneous TP/SL touch, partial fill, cancellation race, fractional lot rounding, TP1 quantity update and runner closure. No single OHLC bar may be assigned a favorable path without evidence.
### Dataset and chronology
Select symbols, feed, sessions and history before inspecting performance. Include trending, ranging, high-volatility and low-volatility periods. Use fixed calendar training, validation and untouched out-of-sample segments; exact dates are OPEN. Purge setups crossing split boundaries and use prior history only for warm-up. Warm-up trades are excluded from reported results.
Use ordinary time-based OHLC, not synthetic candle prices, for fills. Prefer lower-timeframe or tick data to resolve order sequence; otherwise report a conservative model plus alternate-path sensitivity. Record spread, commissions, slippage, financing where applicable, contract value and currency conversions. Costs must never default silently to zero in reported strategy tests.
### Experiment matrix
A: approved End-of-P2 baseline, EMA off and 15m fractals off. B: A plus EMA only. C: A with fractal-assisted structure only. D: A with both. Keep dates, feed, risk, exits and all other parameters identical. Compare executable strategy outcomes and matched setup cohorts, so filtering and entry timing effects remain visible.
E: optional additional-fractal-breakout confirmation after the baseline sequence. F: original Piprunner comparator with its own one-pip entry, opposite-fractal stop and 1R exit. F answers a different strategy question and cannot isolate the EMA or fractal contribution to the hybrid.
Freeze each version before out-of-sample evaluation. Record every tested parameter set and failed variant, not just the best result. Repeat across adjacent pivot strengths, cost levels and market regimes; avoid choosing a narrow optimum from the test set.
### Reported measures
Report setup count, armed count, fills, expiry/cancellation reasons, trade count, net expectancy in original-risk R, median R, win rate, profit factor, maximum equity drawdown, time in market and exposure. Include TP1 hit rate, runner contribution, maximum favorable/adverse excursion, fill delay and reward lost during fractal confirmation.
Report cost sensitivity, per-symbol and regime results, and a distribution or confidence interval for expectancy. Proposed resampling should preserve clustering by day/week rather than assume every trade is independent. Mark small samples inconclusive; a numerical minimum sample and acceptable drawdown remain OPEN.
### Acceptance and limits
Engineering acceptance requires zero lookahead violations, zero expiry/invariant violations and reproducible ledgers. Performance acceptance requires pre-agreed economic thresholds evaluated after costs on untouched data. Positive in-sample results alone do not pass. Paper forward testing follows backtesting and compares signals, fills and costs against the simulator before any live-release decision.
## 9 Development stages and decisions
### Staged development roadmap
Stage 0 Requirements baseline: resolve glossary and platform/feed, collect annotated charts and assign rule IDs. Deliver a signed decision log. Gate: distinguish approved manual rules from research proxies.
Stage 1 4H Bias: implement only B4H v0 as a proposed indicator, fixtures B01 to B14 and reviewed examples B15. Deliver evidence labels, publication timestamps and event export. Gate: causal tests pass and user accepts or revises the structural definition. This is the first feature to build.
Stage 2 4H location and 1H setup: define supply/demand, FVG relevance, SPA and P2 eligibility; implement validity and invalidation. Gate: labelled examples reproduce accepted decisions, including negative cases.
Stage 3 15m baseline: implement approved CHoCH, separate swing break, retest, signal candle, tick entry, expiry, stop and target qualification. Gate: all sequence, timing and mirrored-direction fixtures pass with optional modules off.
Stage 4 Position management: implement risk sizing, execution assumptions, TP1 50% and approved runner rules. Gate: quantity conservation, actual/planned risk accounting and cancellation/fill tests pass.
Stage 5 Optional modules: introduce EMA and fractals independently; version the four-way experiment. Gate: invariant regression suite passes and setup attribution is complete.
Stage 6 Research and forward validation: run locked chronological tests and paper monitoring. Gate: agreed economic thresholds and operational parity pass. Live routing is a separate release decision, not part of this document's authorization.
### Open decision register
D01 Before Stage 1 approval: accept or revise 4H pivot strength, strict tie/dual-pivot policy, independent swing lists, HH/HL versus break-led bias model and neutral/rearm rules. Proposed B4H v0 is fully specified on Sections 3 to 5; protected-swing continuation is an alternative, not silently combined.
D02 Before Stage 1 implementation: choose target platform, data feed, supported symbols and feed-native bar sessions. Confirm publication delay acceptable on 15m. Pine is a candidate, not a confirmed requirement.
D03 Before Stage 2: define P1/P2 boundaries, 4H zone creation/mitigation/invalidation, FVG necessity, SPA meaning and candle/structure rules. Confirm whether 4H CHoCH and SPA are mandatory in addition to structural bias.
D04 Before Stage 3: define CHoCH and swing selection, close/wick breaks, retest tolerance/depth/timeout, signal-candle pattern, same-bar permissions, setup replacement and one-trade-per-setup policy.
D05 Before Stage 3: confirm S+1 to S+3 expiry counting; pending cancellation on bias loss, zone invalidation and setup timeout; define stop buffer and retest interval.
D06 Before Stage 4: clarify minimum 2R interpretation and costs, TP1 structural target selection, runner exit and stop policy, break-even rule, partial rounding and gap behavior.
D07 Before backtesting: choose risk/account settings, exposure limits, sessions, costs, history splits, sample adequacy, acceptable expectancy/drawdown thresholds and forward-test duration.
D08 Before optional-module testing: approve EMA gate timing and fractal mapping to baseline swing roles. Any entry/stop/target replacement must be named as a distinct variant.
### Change control and source record
For each decision record ID, status, selected rule, rationale, example charts, effective version and affected tests. User confirmation changes PROPOSED to CONFIRMED; test evidence changes implementation status, not rule ownership.
Sources: current user request dated 29 October 2026 supplies the confirmed invariants. The referenced ChatGPT conversation Analyse Strategy Integration, ID 6ae359fc-2d4c-83eb-a580-3d277ef48ff1, supplies Piprunner descriptions and prior integration proposals; those proposals are not treated as user approval. TradingView's official HTF documentation supports the platform timing note in Section 4, not the strategy's effectiveness. Existing strategy source code and empirical backtest data were not supplied; code audit and performance validation remain development deliverables.
## 10 Configurable learning annotations
### Purpose and governing behavior
CONFIRMED: annotate every required checklist item so the user can learn to recognize multi-timeframe behavior, then selectively disable the annotations. This extends the requirements; it does not change trading logic. The controls, wording and defaults below are PROPOSED implementation details.
Each decision must answer: what am I looking at, which timeframe owns it, when did it become knowable, what rule did it satisfy, and what must happen next? Display short chart labels alongside a persistent checklist panel and a selectable event explanation. Do not rely on color alone.
### Common checklist contract
Every item exposes one of WAITING, PASS, FAIL, INVALIDATED, UNDEFINED or DISABLED OPTIONAL. WAITING means eligible but not yet observed; FAIL means a tested candidate failed; INVALIDATED means previously valid evidence is no longer usable. UNDEFINED means a required rule has not been specified and blocks automated qualification. Only optional trading modules can be DISABLED OPTIONAL; hiding a required annotation never disables its trading rule.
Each row records item ID, owning timeframe, status, observed value, required condition, evidence IDs, confirmation/publication time and a plain-language reason. A panel header shows current 4H bias, active 1H setup ID, current 15m state and the first blocking condition in sequence. Rows with later prerequisites remain WAITING with a dependency reason, rather than claiming their price conditions failed.
### Full annotation checklist
- AN01 Data and timing: show feed, session, tick size, latest final bar time per timeframe, stale/missing-data blocks and active configuration version. Explain that a developing candle is not confirmed evidence.
- AN02 4H pivots: mark confirmed swing highs/lows, their prices, HH/HL/LH/LL or equal relationships, left/right strength and the two pairs used by bias. The first same-side pivot reads unclassified until a prior reference exists. Show confirmation delay explicitly.
- AN03 4H bias: label BULLISH, BEARISH, NEUTRAL or UNKNOWN and the exact supporting pair comparisons. For example, “4H bullish: high 110 > 100 and low 95 > 90; longs permitted by bias only.” These are illustrative values, not market observations.
- AN04 Protection and changes: draw the active protected level; mark close-break invalidation, neutralization, fresh rearming evidence and ambiguous/equal pivots. Explain why a wick or equal close did not invalidate. Display the next requirement, such as “Wait for fresh confirmed structure.”
- AN05 4H location: draw approved supply/demand bounds and optional FVG context with creation, availability and invalidation times. Show whether the location is mandatory or informational. Until rules are approved, display UNDEFINED rather than a guessed zone.
- AN06 4H additional confirmations: expose required HTF CHoCH/SPA as distinct rows once their mandatory status and definitions are approved. Unresolved requirements remain visibly UNDEFINED. Bias alone must not make these rows pass.
- AN07 1H setup: mark P2 start and qualifying pullback evidence, SPA/location bounds, direction, setup ID, invalidation level and validity window when defined. Show “4H aligned, 1H setup waiting” when appropriate. Highlight the selected active setup and any replacement/cancellation reason.
- AN08 15m CHoCH: identify the exact frozen countertrend swing, reference price and confirming candle. Label the break rule and confirmation time; explain that CHoCH is the first required step, not an entry.
- AN09 15m subsequent swing break: mark its distinct reference swing, break level and confirmation candle. Link to the preceding CHoCH; show WAITING if the CHoCH prerequisite is absent.
- AN10 Retest: draw the accepted broken level/zone, tolerance, retest interval and extreme. Explain valid, failed, timed-out or waiting retests under the approved predicate. Distinguish the retest extreme from an unrelated fractal.
- AN11 Signal candle: identify the actual qualifying candle and list the approved candle predicate, high/low, close time and prerequisites. If no candle predicate is approved, show UNDEFINED instead of treating any directional candle as a signal.
- AN12 Entry and expiry: draw the frozen signal-candle high plus one tick for longs or low minus one tick for shorts. Show tick size, pending status and “eligible bar 1/3, 2/3, 3/3” under the chosen expiry convention; label fill or expiry at its actual event time.
- AN13 Stop and risk: draw the frozen retest extreme and stop buffer, planned entry, initial stop distance, monetary risk and position size when defined. Annotate invalid rounding, nonpositive risk, margin/quantity blocks and gap-driven actual risk separately.
- AN14 Reward gate and targets: draw TP1 and any approved runner target, show planned R to the relevant objective and PASS/FAIL against the minimum-2R interpretation. Until that interpretation is approved, display it as UNDEFINED. Show the nearest blocking structural objective if part of the approved target rule.
- AN15 Partial and runner: annotate actual 50% TP1 fill quantity, remaining runner quantity, runner stop/exit policy, subsequent stop changes and final exit with reason and net R. Do not show an automatic break-even move unless that rule is approved.
- AN16 Optional EMA: show 15m EMA36/EMA100 values, relative alignment, gate evaluation time and whether filtering is enabled. With filtering off, an optional educational overlay may still show the values but must read “Informational, not gating.”
- AN17 Optional fractals: mark confirmed 15m fractals, pivot and confirmation times, role in CHoCH/swing references or additional-breakout experiment, and the delay introduced. Distinguish informational drawings from active experimental gates.
- AN18 Rejections and lifecycle: mark setup invalidation, bias loss, insufficient reward, expiry, duplicate prevention, ambiguous fill path and order cancellation/fill events. State the actual reason and next state, not a generic “No trade.”
## 11 Annotation controls and acceptance
### Proposed configuration schema
annotationMode = Training | Guided | Minimal | Off. Training is the proposed initial default and shows all applicable checklist rows, causal explanations and current-setup drawings. Guided shows current state, blocking reasons and active evidence. Minimal shows bias/setup summary and active order/risk lines. Off hides all educational chart objects and the checklist panel. This switch never changes strategy decisions or protective order behavior.
Independent controls: show4H, show1H, show15m, showChecklist, showReasonText, showHistoricalEvents, showPivotOrigins, showConfirmationMarkers, showZones, showStructureLevels, showOrderLevels, showRiskAndTargets, showManagementEvents and showRejectedCandidates. Add one visibility toggle per AN01 to AN18 and separate optional EMA/fractal overlay switches. A preset establishes values; later individual overrides are retained as a custom preset until reset.
Keep trading configuration separate: useEMAFilter, useFractalStructure and useAdditionalFractalBreakout affect logic and experiment identity. showEMA and showFractals affect drawings only. Changing a logic switch starts a new version/run; a visibility switch does not. The checklist always identifies enabled gates when visible, even if their chart drawings are hidden.
Learning depth = Short | Detailed. Short displays “4H HL confirmed”; Detailed expands the observed prices, exact predicate, confirmation delay and next condition. If the target platform lacks tooltips or click selection, use a details panel for the latest selected event or a configurable event index. Do not promise unsupported interactions.
History scope = Current setup | Last N setups | All retained. Proposed defaults: current setup, N=5 if selected, maximum 150 chart objects, label size medium, panel top-right, modest zone opacity. Object and history limits must be validated against the chosen platform. On reaching a limit, prune oldest historical drawings before active evidence, show a history-truncated notice, and keep the event export complete.
Expose label size, panel position, direction/status colors, zone opacity and a reset-to-training action. Use explicit timeframe prefixes and text/shape distinctions so overlapping 4H, 1H and 15m evidence remains understandable. Where possible combine nearby labels or offset them without changing their evidence anchor.
### Causal drawing and review behavior
Mark origin time separately from actionable confirmation time. A confirmed pivot can have an origin anchor at its historical candle, but its confirmation marker and label must disclose when it became known. Historical origin drawings must not appear before confirmation in replay. Tentative pivots, if offered, use a separate off-by-default “Developing preview” switch, dashed styling and “UNCONFIRMED, not used for decisions.”
Do not repaint a failed candidate into a historical success. Record the original event; later show invalidation or supersession as a new timestamped event. The current checklist updates with the selected setup, while retained history preserves each event's state at publication. Any hindsight-only review overlays must be separately labelled and excluded from trading evidence.
An explanatory trail might read: “4H bullish confirmed -> 1H P2 setup qualified -> 15m CHoCH confirmed -> waiting for separate swing break -> retest accepted -> signal candle closed -> order armed, 1/3 -> filled -> 50% TP1 -> runner.” This is an illustrative sequence; real labels must use actual events and approved predicates.
### Acceptance tests and staged delivery
- A01 Checklist coverage: each AN item has a status and evidence/reason in Training mode when applicable. Undefined mandatory rules remain visible and block approval. No row silently disappears because its predicate is unresolved.
- A02 Visibility isolation: replay identical data/configuration in every preset and toggle combination. Bias, setup, order and trade ledgers must be identical; only drawings differ.
- A03 Causality: a 2/2 pivot origin and its evidence cannot appear before the second right bar closes. Repeat prefix/reload tests for labels, confirmation markers and panels as well as engine outputs.
- A04 Explanation accuracy: verify displayed comparisons, reference prices, tick offsets, stop distance, R calculations, expiry counter and partial quantities against their engine records for both directions.
- A05 Sequence clarity: absent prerequisites read WAITING with the blocking step. Expired/invalidated setups show the specific reason; disabled optional gates never appear as required passes.
- A06 Usability and limits: inspect dense charts, all timeframe overlays, color-independent status recognition, object pruning, saved custom presets, master Off and reset. Current protective levels remain available in the order engine even when educational drawings are hidden.
- A07 Training review: step through accepted and rejected annotated chart examples without seeing future candles. Confirm the user can identify the active timeframe, supporting evidence, actionable time and next required step. Track confusing labels and revise wording without modifying trading predicates.
Stage 1 now includes AN01 to AN04, the full checklist shell, causal markers and configurable visibility. Show later unimplemented rows as UNDEFINED or not yet implemented, never PASS. Stage 2 adds AN05 to AN07; Stage 3 adds AN08 to AN14 and lifecycle explanations; Stage 4 adds AN15; Stage 5 adds AN16 to AN17. AN18 grows with each implemented lifecycle. All stages include A02 to A06 regression tests.
### Additional open decisions
D09 Choose preferred label wording and initial preset after reviewing annotated examples; no need to resolve styling before building the first 4H demonstration. D10 Validate platform object limits, available panel interactions and configuration persistence. D11 Confirm which contextual overlays are mandatory gates after SPA, zone and FVG definitions are resolved. Annotation implementation cannot decide their trading status.
