# 1H structure layer UI 0.5

This feature adds independent 1H structure annotations to the existing indicator. It is a **PROPOSED research structure model**, not a completed End-of-P2 1H setup engine. P2, SPA, zones and setup invalidation remain undefined and cannot be passed by directional alignment alone.

## Rules and presentation

Use the same documented strict confirmed-pivot algorithm as B4H v0, evaluated on 1H bars with independent left/right strengths (proposed 2/2 defaults). Two rising high/low pairs give bullish structure; two falling pairs give bearish; mixed pairs are neutral and insufficient history unknown. Protected-level close-break neutralizes structure, and fresh evidence is needed to rearm. The 1H result never changes the 4H state.

The educational break overlay uses prior 1H structure: a strict closed-candle crossing of an existing confirmed high/low is BOS with the prior directional state, CHoCH against it and otherwise an unclassified Break. Equality and wick-only breaches do not count. Each pivot can break only once. Same-close invalidation has the same precedence as 4H. These are proposed 1H display rules, not an approved 15m entry sequence.

1H uses configurable **blue/orange**, versus the existing 4H **teal/red**. Every level and event has a 1H prefix. The shared BOS/CHoCH size defaults Large. Current 1H labels default farther right (14 chart bars) than 4H (6), with separate offset and history settings. Equal-level text may still overlap; adjust offsets or hide a layer when needed. No automatic collision detection is claimed.

One-hour structure is drawn on **1H and 15m charts only**, using confirmed prior 1H snapshots and lookahead_on. It is deliberately not requested on a 4H chart: a single lower-timeframe sample per chart bar could skip hourly events. A future intrabar-array implementation would be needed to display the complete 1H event sequence there. The 4H panel explains this restriction. The conditional request is based on chart interval, not annotation visibility; turning off drawings does not stop calculation on supported charts.

Native feed bar boundaries apply. Pivot origin is historical; evidence is available only after right-side bars close. With 2 right bars, 1H confirmation is two additional hourly closes after pivot close. The next available chart bar receives that confirmed snapshot. Hover event labels for confirmation/publication times. Live levels are current-endpoint views, not an exported history of all references.

## Panel and controls

The summary displays 4H bias and 1H structure as aligned, opposed or without directional alignment. Agreement means only the structural directions match. It does not qualify a P2 trade. The row explicitly says P2 is not qualified; future checklist rows remain waiting or undefined.

Controls: Show 1H, current levels, break events, history count (default 2), label offset and bullish/bearish/neutral colors. One-hour strengths affect its proposed structure; drawing switches do not. Minimal shows current levels without break history; Off hides both layers. `Show 4H annotations` hides 4H drawings but leaves the combined context panel available if its own switch is on. The 1H layer uses lines regardless of the 4H legacy-label setting.

Data Window includes five new 1H plots: structure state, structural protection, confirmed timestamp, latest high and latest low. They remain active with drawings hidden on 1H/15m; they are unavailable on 4H. This is not a complete event export. Current 1H protection is diagnostic only, not a trade stop.

## Apply and check

Replace the existing indicator source; the filename remains `piprunner_4h_bias.pine` for continuity, while the indicator title becomes **Piprunner MTF Structure · UI 0.5**. Do not add a second copy over the old one. On 1H or 15m, enable both layers and review the colors, label offsets and independent event clocks. On 4H, only the 4H layer is available.

Local verification: 18 reference tests pass, including independent strengths, synthetic 15m publication scheduling and separate prefix/reload clocks. The Pine snapshot function was parameterized without changing its calculation body; source comparison with prior 4H parameter names normalized confirms equivalence. Existing six 4H audit plots are unchanged. These are reference/source checks, not Pine execution.

Outstanding: compile UI 0.5 in TradingView, verify independent request state, contrast and label overlap, confirm each 1H event appears once, compare 1H snapshots on 1H and 15m at matching publication times, check annotation-toggle parity, replay both directions and malformed-history behavior. Full prior 4H acceptance gates remain open. Neither structure model has been approved by chart review yet.

## Next development boundary

Before calling this a 1H setup engine, define P2, SPA, valid zones, confirmation and invalidation with accepted positive/negative chart examples. A future 15m structure annotation layer can be developed separately as a labelled research model, but must not imply the required End-of-P2 CHoCH, swing break, retest and signal-candle sequence is approved or implemented.

Official reference: https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/.
