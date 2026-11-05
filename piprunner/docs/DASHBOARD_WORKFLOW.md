# HTF-to-LTF dashboard workflow

Design for both indicators, 5 November 2026. The user requested horizontal and vertical dashboards showing every step. The local HTML is an interactive teaching/design artifact, not a market-connected TradingView panel.

## Ordered steps

### D00 · Context · Data and finality

Validate symbol, feed, supported chart, finalized bars and sufficient warm-up.

Gate: Usable finalized history; otherwise UNKNOWN.

Chart evidence: Feed, symbol, candle close, warm-up status.

Implementation: Partial.

### D01 · 4H · Confirmed structure

Identify confirmed swing pairs, direction and protected level. The exact structural model is proposed.

Gate: Enough confirmed structure under the approved model.

Chart evidence: 4SH/HH or LH; 4SL/HL or LL; protection; confirmation time.

Implementation: Research exists.

### D02 · 4H · Direction permission

4H authorizes direction. Lower timeframes cannot override it.

Gate: Bullish or bearish permission; neutral/unknown blocks new directional qualification.

Chart evidence: Published 4H state, version and reason.

Implementation: Research exists.

### D03 · Locations · S/R or S/D zone

Locate eligible support/resistance OR supply/demand. S/R is missing; S/D detection is a research proposal.

Gate: Active eligible source-owned zone. S/D requires its own timeframe close beyond the buffered edge to invalidate.

Chart evidence: Zone ID, source TF, boundaries, 30% buffer, validity.

Implementation: Partial.

### D04 · 1H · Pullback at location

Identify P2 retracement into the eligible location; exact phase/contact mechanics remain open.

Gate: Approved location contact and valid parent 4H permission.

Chart evidence: Pullback interval, zone contact, source candle.

Implementation: Partial.

### D05 · 1H · Directional SPA

Any one pin rejection, engulfing or piercing at the location in the 4H direction. S/D candidates exist; full setup qualification does not.

Gate: Location AND any one approved pattern AND HTF alignment.

Chart evidence: Pattern, contact evidence, 1H closed candle, direction.

Implementation: Partial.

### D06 · 1H → 15m · Qualified setup handoff

Create and maintain a setup ID linking 4H permission, location and 1H SPA. Lifecycle policies need definition.

Gate: Qualified setup remains current; invalid parents block downstream stages.

Chart evidence: Setup ID, HTF version, zone ID, creation and invalidation policy.

Implementation: Pending.

### D07 · 15m · CHoCH

Wait for a qualified change of character linked to the setup. Existing research labels are not a completed execution gate.

Gate: Approved directional CHoCH event after eligible setup.

Chart evidence: Broken reference, close/wick policy, confirmation, setup ID.

Implementation: Partial.

### D08 · 15m · Separate swing break

Require the distinct swing break after CHoCH; do not count one event twice.

Gate: Approved second structure event in the required order.

Chart evidence: Separate swing reference and event ID.

Implementation: Pending.

### D09 · 15m · Retest and extreme

Accept the retest under agreed tolerance, depth and timeout rules; preserve its extreme for the stop.

Gate: Retest valid and linked to the broken level.

Chart evidence: Level, interval, extreme, invalidation reason.

Implementation: Pending.

### D10 · 15m · Signal candle

Confirm the qualifying candle after the retest; exact pattern definition remains open.

Gate: Approved finalized signal candle and current setup.

Chart evidence: OHLC, candle time, direction and pattern.

Implementation: Pending.

### P11 · 15m · Williams Fractal gate

Combined only: add confirmed continuation evidence. Long: prior HH/HL then LH high fractal; short: prior LH/LL then HL low fractal. Generic pivots are insufficient.

Gate: Full baseline plus eligible confirmed fractal. Final pre-arm check is proposed; timing/age/expiry policy remains OPEN.

Chart evidence: Pivot origin, right-bar confirmation, publication, precursor references, setup ID.

Implementation: Pending.

### D12 · Plan · Entry, stop and ≥2R

Entry one tick beyond the signal candle; stop beyond retest extreme; minimum 2R opportunity. No one-pip or 1R substitution.

Gate: All gates pass, positive risk and approved target opportunity. Undefined policy blocks the plan.

Chart evidence: Frozen signal entry, retest stop, target, tick size, initial R.

Implementation: Pending.

### D13 · Pending · Arm / expire / cancel

Track a plan with three-bar expiry and explicit cancellation. Exact counting and event precedence remain open. Indicator submits no orders.

Gate: All mandatory rules defined and valid at arming; never retroactively arm.

Chart evidence: Arming time, expiry clock, parent validity, cancellation reason.

Implementation: Pending.

### D14 · Tracking · Hypothetical trigger

Track the plan trigger separately from an actual broker fill. Gaps and same-bar path need test-harness assumptions.

Gate: Trigger occurs while eligible under approved timing.

Chart evidence: Trigger time, planned price, execution assumptions.

Implementation: Pending.

### D15 · Management · 50% TP1 → runner → exit

Depict 50% at TP1 and retain the runner. Target mapping, runner stop/exit and rounding policy remain open.

Gate: Only approved management rules can transition the tracked state.

Chart evidence: TP1, partial quantity, remaining size, runner policy, exit reason.

Implementation: Pending.

## Horizontal and vertical layouts

Horizontal: connected step columns from left to right, grouped by context, 4H direction/location, 1H setup, 15m execution, plan/expiry and management. Proposed compact TradingView cells show timeframe, condition, state and reason; full cells add evidence and confirmation time. Horizontal overflow must remain navigable rather than silently omit steps.

Vertical: one row per step in the same order, with timeframe, condition, state, reason and evidence. Both orientations use the same calculation snapshot. The browser preview also offers Both; TradingView may select a single orientation to preserve chart space.

Baseline contains 15 steps; combined contains 16, including P11. Fractal detection can run alongside the baseline sequence, but the proposed final check cannot bypass CHoCH, the distinct swing break, retest or signal candle. Arrows show dependencies, not a fully approved timing policy.

## States, controls and annotations

Proposed gate states: PASS, WAIT, BLOCKED, UNKNOWN, UNDEFINED, DISABLED, EXPIRED, CANCELLED, TRIGGERED and CLOSED. Each has a plain-language reason and publication timestamp. A separate implementation field reports research code, partial or pending. The local dashboard deliberately shows readiness instead of invented live PASS values.

Panel metadata: product/version, symbol/feed, chart and source timeframes, last update, finality, setup ID, 4H permission, enabled gates and primary blocker. Inputs: show panel, Horizontal/Vertical orientation, position, text size, compact/full, per-step detail, reason/evidence visibility, retained history and Training/Guided/Minimal/Off. Every step has configurable teaching annotations; drawing switches never affect calculations. A visible summary still discloses unmet mandatory gates even when detailed drawings are hidden.

Preserve horizontal levels, timeframe colors, SH/SL slash classifications and larger BOS/CHoCH. The combined product adds distinct fractal origin and confirmation markers. Show which candle confirmed a condition, the important level and why a stage is waiting or blocked.

## Acceptance

Verify every step in both products, product switching, both orientations, selected-step explanations, mirrored trade directions, source-timeframe zone ownership and open-versus-closed candle wording. Unknown/unimplemented mandatory rules cannot display PASS. Check identical decision ledgers across orientation/visibility changes and bounded object counts in actual Pine.

The HTML preview has been opened in the local browser: both product counts, horizontal/vertical layouts and selected fractal details were checked. TradingView dashboard implementation and live state linkage remain pending. No broker orders or performance results are produced.
