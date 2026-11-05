# Portable strategy contract

Snapshot: 5 November 2026. Current repository documents and later explicit user corrections supersede this snapshot.

# Shared MTA contract

Applies to both named indicators. CONFIRMED denotes user requirements; PROPOSED denotes candidate mechanics; OPEN denotes unresolved choices. Implemented means code exists, not that its trading model is approved.

## Confirmed rules

- C01: TradingView; 4H directional authority → 1H end-of-P2 qualification → 15m execution confirmation. Lower timeframes cannot override 4H. Neutral/unknown 4H blocks new directional qualification.
- C02: 1H retracement reaches support/resistance OR supply/demand, followed by ANY ONE directional SPA pattern: pin rejection, engulfing or piercing. SPA means Strong Price Action; phase is end of P2, not P3.
- C03: A zone invalidates only on a finalized candle close from that zone's own timeframe beyond its buffered far edge. Current disclosed buffer interpretation: full base range R=baseHigh-baseLow; demand threshold=baseLow−0.30R, supply=baseHigh+0.30R. Equality/wick-only breaches do not invalidate. Buffer changes invalidation, not zone-contact boundaries or retest stops.
- C04: Full 15m sequence: CHoCH → separate swing break → retest → qualifying signal candle. Entry one minimum tick beyond that signal candle; tick and pip are distinct units.
- C05: Three-bar pending expiry; stop beyond retest extreme; minimum 2R opportunity; 50% TP1 and runner. Exact counting, buffers, targets and runner policies are OPEN.
- C06: Configurable teaching annotations for each step. Display switches and dashboard orientation do not affect calculations. Preserve timeframe prefixes and SH/SL with HH/HL/LH/LL classification, horizontal levels and larger BOS/CHoCH text. 4H teal/red, 1H blue/orange, 15m fuchsia/yellow, all configurable.
- C07: Six configurable visual EMA overlays: 8 yellow, 20 blue, 36 dotted blue, 50 red, 100 amber, 200 green. Neither visibility nor their presence activates a filter. EMA36/100 logic is a separate optional experiment; baseline decisions must be reproducible with it off.

## Proposed mechanics and current source

UI1.1.0 contains independent strict confirmed swing extraction on 4H/1H/15m (default 2/2), HH+HL/LH+LL classification, protected levels, research BOS/CHoCH, latest-zone base/departure detector, buffered own-timeframe-close invalidation, 1H S/D SPA candidates and visual EMAs. These are reusable prototype components. Current 15m structural pivots are NOT an implemented Williams Fractal continuation signal.

The proposed 4H model neutralizes on protected-level close-break, invalidation takes priority over simultaneous new evidence, and fresh confirmed evidence is needed to rearm. Exact model approval, tie/dual-pivot policies and calibration remain pending. Read requirements.md Sections3–5 and existing source for full proposed rules; do not replace structure with EMA bias.

S/R, full approved 1H lifecycle, linked 15m entry sequence, order plans, expiry and management are incomplete. UI1.1.0 compiled/rendered on the user's EURCHF three-chart layout on 5 November; full replay/non-repainting acceptance remains pending. Existing local reference tests do not execute Pine.

## State and timing contract

Separate context, setup, execution and post-entry tracking. Proposed execution states: WAIT_CONTEXT → WAIT_LOCATION → WAIT_SPA → SETUP_QUALIFIED → WAIT_CHOCH → WAIT_SWING_BREAK → WAIT_RETEST → WAIT_SIGNAL → VALIDATE_PLAN → ARMED → TRIGGERED → TP1_PARTIAL → RUNNER → CLOSED. WAIT_FRACTAL is added only in product2 under its proposed timing rule. This is a design state model, not a claim the current indicator implements it.

Every transition requires finalized source evidence plus valid parents linked by IDs/versions. A failed mandatory predicate cannot be replaced by a display annotation. UNKNOWN/missing data never advances a gate. Optional disabled gates are DISABLED, not PASS. Risk failure is BLOCKED. Expiry/cancellation produces EXPIRED/CANCELLED rather than a recycled signal.

Proposed pre-trigger invalidation priority: data-quality block → published 4H permission change or linked setup/zone loss → expiry → new qualification/trigger. Exact same-bar trigger/cancel ordering, setup replacement, same-bar multi-stage permissions and post-trigger bias-loss behavior remain OPEN; do not infer a trade fill order from OHLC alone. After invalidation retain a historical event record and require new eligible setup evidence. Do not retroactively erase a trigger published before a later HTF update.

Record source timeframe, candle close, origin/confirmation/publication time, setup ID, parent snapshot version, direction, reference level and reason. Evaluate HTF direction only after its close evidence is published. Source-timeframe zone finality remains independent of viewing interval. Never backdate actionable events onto pivot origins.

## Inputs and outputs

Logic inputs: confirmed pivot configuration (proposed), zone detector/buffer, SPA/contact thresholds, future approved retest/signal/expiry/target policies and optional EMA logic flag default off. Undefined required inputs report UNDEFINED and block the affected plan. Instrument tick size and pip size must remain separate.

Visual inputs: layer and per-step visibility, Training/Guided/Minimal/Off, label size, colors, bounded history, zones, EMA overlays, panel position and Horizontal/Vertical orientation. Hiding detail never hides enabled-gate failures from an otherwise visible summary. Print symbol, chart/source TFs, finality and last update.

Outputs are educational levels, candidate/qualified/blocked states and proposed trade plans, not routed orders. Future alerts require explicit event semantics; strategy orders/backtest execution belong to separate test harnesses with declared fill/cost assumptions.

## Open decisions

Exact structural model approval; P1/P2 bounds; S/R construction/invalidation; zone pooling/freshness; numerical SPA strength/contact and bearish piercing counterpart; CHoCH versus separate swing-break references; retest tolerance/timeout/extreme interval; signal pattern; bar-count inclusivity and reset/cancellation policy; minimum 2R interpretation and target selection; stop buffer; TP1/runner/break-even/rounding; sessions/feed/symbols/costs. Previously mentioned FVG context is not a confirmed mandatory gate.

## Nonfunctional acceptance

Deterministic outputs on fixed data/configuration; prefix invariance under future bars; no duplicate MTF publication; bounded objects/history; versioned settings; traceable reason/evidence; indicator state isolated between products. Numeric performance limits remain OPEN. Verify visibility/layout toggles leave decision ledgers unchanged. Run separate Pine compilation, chart rendering, replay/reload and cross-timeframe consistency checks. Never present prototype display success as validated trading performance.


# Piprunner + MTA-End-of-P2

Product2 requirements v1, 5 November 2026. Independent combined indicator CONFIRMED. User selected **additional fractal confirmation while preserving the full End-of-P2 entry sequence**. Inherits every baseline rule in MTA_END_OF_P2_REQUIREMENTS.md (repository document) and SHARED_MTA_CONTRACT.md (repository document).

## Additional requirements

- P01: implement a 15m Williams Fractal continuation signal as an additional qualification gate. Generic swing pivots or a single fractal marker are insufficient.
- P02: supplied default2 left / 2 right; confirmation only after right-side candles close. Expose pivot origin and confirmation/publication separately. Exact equality/dual-pivot handling is OPEN.
- P03: original long pattern: preceding highs showHH and lowsHL, then a confirmedLH high fractal appears. Original short: preceding highsLH and lowsLL, then a confirmedHL low fractal appears. Selection/order/strictness of preceding references and replacement/consumption policy remain OPEN. HTF direction and valid 1H setup remain mandatory in the combined product.
- P04: preserve CHoCH → separate swing break → retest → signal candle; preserve signal candle±one tick, retest stop, three-bar expiry, minimum 2R, 50% TP1 and runner. Never switch to original Piprunner's fractal ± one pip, opposite-fractal stop or 1R target.
- P05: expose candidate state, confirmation delay, source references, direction, setup linkage and rejection reasons in labels/dashboard. New `showFractals` affects drawings only; `useFractalConfirmation` affects experiment identity and plan eligibility. Proposed default for this named combined mode is ON; default/preset is still a proposal. Disabled-gate mode must be labelled baseline comparison, never fractal-confirmed.
- P06: optional EMA36/100 filter is independent of the fractal gate and visual EMAs. Original supplied relation is36 > 100 for long / 36 < 100 for short; proposed evaluation context 15m confirmed close, timing/default off await review. The user's additional-fractal choice does not make EMA mandatory.
- P07: compare baseline and combined on identical input data. Gateoff reproduces MTA baseline; gate on adds a restriction rather than bypassing baseline requirements.

## Proposed gate placement — not confirmed

Preferred design candidate: evaluate and link fractal evidence in parallel with15m baseline stages, then require eligible fractal confirmation at VALIDATE_PLAN, before ARMED. A confirmed candidate may predate the signal only within an approved same-setup window. If unavailable when the signal closes, remain WAIT_FRACTAL and do not backdate an order. Reject stale/invalid baseline signal rather than extending its life indefinitely. No entry is eligible before the later publication of all mandatory gates.

OPEN: can confirmation arrive after the signal; allowable same-setup window; when signal validity begins/ends while waiting; whether the three-bar clock starts from the baseline signal or arming; treatment if intended entry already traded before arming; candidate consumption/replacement; whether a further price break of theLH/HLfractal is required. Until these are resolved, a missing gate may display WAIT/UNDEFINED but cannot create executable plans. No new breakout requirement is invented here.

## Implementation and acceptance

Fractal continuation detector/gate NOT implemented. Current prototype structural pivots do not satisfyP01. Separate combined entrypoint not created by this requirements split.

F01: no publication before right-bar close; future bars cannot rewrite confirmed events. F02: mirroredHH/HL→LH andLH/LL→HLfixtures, missing precursor/equal/dual-pivot cases. F03: permitted baseline with no fractal remains blocked/waiting when gate on; valid fractal cannot bypass any missing baseline stage. F04: 4Hconflict rejects fractal; expired setup cannot reuse it. F05: gate off ledger equals baseline; EMA flag independent; show/hide/orientation parity. F06: signal/confirmation clock, crossed-entry and expiry-boundary fixtures after policy approval. F07: tick entry, retest stop,2R,partial/runner identical tobaseline on matched eligible setups. F08: actual Pine compile/replay/reload/source clock tests. No success-rate claim without locked costs and out-of-sample evaluation.
