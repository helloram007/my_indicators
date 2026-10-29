# Chart review 001

Date: 29 October 2026. User supplied a TradingView snapshot after applying the indicator on 4H, 1H and 15m.

Source: https://www.tradingview.com/x/JPaT4zMi/

Snapshot identifies PEPPERSTONE GBPUSD, captured at 15:32 UTC. Review is visual evidence from a static image, not an interactive compiler or replay test. Exact source revision and all input values are not independently established.

## Observed behavior

All three visible panels display BEARISH, reason LH_AND_LL, the high pair 1.33590 → 1.33386, low pair 1.33278 → 1.32727, protected high 1.33386, and last confirmed 4H close 2026-10-29 13:00 UTC. The visible shared state agrees across the three chart intervals at this moment.

The snapshot shows price around 1.33636 above protection while the current 4H candle remains open. This is consistent with retaining bearish bias until a finalized 4H close breaks protection. A confirmed close above 1.33386 would neutralize the bearish state under this model; it would not itself establish bullish bias. A screenshot cannot verify the next transition occurred correctly.

The latest 4H pivot origin labels identify LH at 1.33386 and LL at 1.32727. The 1H and 15m panels display these same 4H origins; they are not independent 1H/15m swing classifications. The latter modules are not built.

Later checklist rows visibly remain undefined/waiting and optional modules are disabled. The presence of rendered indicator output is evidence that a version has loaded and run on the user's charts. It does not independently establish the exact Git revision, full input coverage or all Pine compiler/runtime checks.

## Usability findings

- The tall Training panel overlaps recent price action, particularly on 15m. The existing panel-position setting can relocate it; Guided or Minimal reduces its size. A compact/opaque panel and clearer management of future-row placeholders are improvement candidates.
- Several confirmation labels overlap one another and candles, particularly on 4H. A deterministic label-spacing/stacking control would improve learning clarity.
- LH origin labels use the teal high-pivot color while LL origins use red. These colors currently identify pivot side, not trend direction; wording or configurable structure-aware coloring should make that distinction clearer.
- Retained-label pruning counts differ substantially between chart intervals. Different loaded history can cause this. Do not infer historical equivalence from matching current state alone; compare fixed-range exports before attributing count differences to duplication.
- A visible “4H candle developing; close required for invalidation” status would help explain why live price can be beyond protection while bias remains unchanged.

## Acceptance status and next actions

Partial visual acceptance only: current bias/evidence/protection agree across panels and placeholders are honest. Full B13/B14 and annotation acceptance remain open.

Next: improve annotation readability without changing model logic; then compare the same closed snapshot before/after a 4H close and replay an invalidation/rearm sequence. Verify label timing and annotation-toggle numeric parity. User review/approval of B4H v0 remains outstanding.
