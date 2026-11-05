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


# MTA-End-of-P2

Product1 requirements v1, 5 November 2026. Name and independent product boundary CONFIRMED. Applies SHARED_MTA_CONTRACT.md (repository document); workflow/panels: DASHBOARD_WORKFLOW.md (repository document).

## Purpose and exclusions

Standalone End-of-P2 multi-timeframe indicator. 4H controls direction, 1H qualifies the pullback ending at S/R OR S/D with SPA, 15m supplies the full End-of-P2 sequence. No Williams Fractal signal requirement in this product. Existing structural pivots may remain as the proposed swing extractor without being presented as Piprunner signals. Visual EMAs may be shared; EMA trading filters are outside the core baseline and must be explicitly labelled experiments if later added.

## Functional requirements

- M01: publish finalized 4H structural permission, protection, evidence and reason; UNKNOWN/NEUTRAL blocks new directional setup qualification.
- M02: identify source-owned S/R and S/D locations with separate IDs/lifecycles; apply own-zone-timeframe buffered-close invalidation to S/D. S/R mechanics remain OPEN.
- M03: qualify 1H end-of-P2 only with eligible location AND any one approved directional SPA pattern AND current 4H permission. Current S/D research candidates cannot be labelled full setup qualification.
- M04: create a proposed unique setup record carrying direction, HTF version, location ID, qualification time and invalidation/expiry policy. Policy details require approval.
- M05: link distinct 15m CHoCH, swing-break, retest and signal-candle events to that setup. No entry until all mandatory stages pass in approved order.
- M06: compute one-tick signal-candle entry and retest-extreme stop; freeze the plan after approved validation; reject nonpositive risk and failed minimum 2R. Exact policies remain OPEN.
- M07: track three-bar pending expiry and explicit cancellation/rejection reasons. Indicator tracking does not submit orders.
- M08: depict50% TP1 and runner under an approved policy. Do not invent targets or a runner stop from generic fractals.
- M09: expose every workflow stage in both dashboard orientations with per-step annotation switches; calculations independent of display.
- M10: retain baseline traceability and test results separate from product2; identify itself as MTA-End-of-P2 in title, panels and exported events.

## Delivery status

Reusable research code exists for M01/M02 and partial M03/M09 in the legacy prototype. Separate indicator entrypoint not yet created. S/R, full setup/lifecycle, qualified execution, risk and management remain pending. Existing generic BOS/CHoCH are explanatory structure events, not completed M05.

## Acceptance

A01: no fractal or EMA requirement blocks an otherwise qualified core-baseline fixture. A02: bearish 4H cannot produce bullish qualification despite bullish 1H/15m; unknown/neutral 4H blocks. A03: zone wick/equality holds; own-timeframe strict close beyond buffer invalidates on the correct source clock. A04: location without SPA orSPA without location cannot qualify. A05: missing/reordered execution stage cannot arm; separate swing break has its own event reference. A06: correct long/short tick entry and retest stop; expiry boundary and RR tests only after definitions resolved. A07: 50% quantity and runner consistency in future harness. A08: horizontal/vertical/per-step toggle parity, causal publication and replay/reload stability. All must be exercised against actual Pine in addition to local reference fixtures.
