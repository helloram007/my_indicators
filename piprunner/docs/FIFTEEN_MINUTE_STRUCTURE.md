# Independent 15m research structure UI 0.6

Adds the third structural display layer without creating an entry strategy. The proposed research extractor is the same strict confirmed-pivot model used for 4H/1H, evaluated independently with its own 15m left/right strengths. This does not make the optional Piprunner Williams Fractal confirmation module mandatory; its mapping to approved End-of-P2 entry swings remains unresolved.

## Display and controls

- 4H: teal/red, available on 4H, 1H and 15m charts.
- 1H: blue/orange, available on 1H and 15m charts.
- 15m: fuchsia in the violet family/yellow, available on the 15m chart only.

All colors are configurable; explicit timeframe prefixes and direction arrows remain. The 15m layer has independent visibility, current-level and break-event switches, history count (default 2), label offset (default 22 chart bars) and pivot strengths (proposed 2/2). It uses the shared event text size, default Large, while normal swing labels remain separately sized. Adjust chart right margin/label offsets or hide individual layers if levels coincide. No collision detection is claimed.

Current references are horizontal with updating labels; solid means unbroken and dotted means consumed by a confirmed close. Historical break segments are bounded separately for each timeframe. Minimal shows current levels only; Off hides educational drawings while supported diagnostic series continue calculating. The 15m layer uses lines even if 4H legacy-label mode is selected.

## Proposed rules and timing

HH plus HL yields bullish research structure; LH plus LL bearish; mixed pairs neutral; insufficient history unknown. Protected-level invalidation and fresh-evidence rearming use the documented common algorithm. BOS is a strict close crossing with the prior directional state; CHoCH is against it; neutral/unknown yields unclassified Break. Equality and wick-only breaches do not qualify. Each pivot identity is consumed once, and levels already broken at discovery do not invent earlier events.

The 15m request is gated by the chart interval, not the drawing switches. It uses prior confirmed snapshot fields on the 15m chart. A candidate with two right bars is confirmed two subsequent completed 15m bars after the pivot closes (30 minutes). The confirmed snapshot becomes available at the next chart bar opening, not at the historical pivot origin. Current live-price changes do not change a published structural snapshot.

No 15m lower-timeframe request is made on a 1H or 4H chart. A future intrabar-array design would be needed to show complete 15m history on those charts. Existing restrictions to standard candles and supported intervals remain.

## Checklist semantics

The summary now shows all three structural states. “3TF aligned, no entry” means only that all three are bullish or all three bearish. It does not pass the setup gate. 1H P2/SPA and the required 15m CHoCH → separate swing break → retest → signal candle remain unqualified. Research CHoCH labels do not silently substitute for those approved predicates.

Five new Data Window plots expose 15m structure, diagnostic protection, confirmation time, latest high and latest low. They are unavailable on higher chart intervals. Existing higher-timeframe calculations and eleven audit plots are unchanged.

## Verification and review

Twenty-one local reference tests pass, including three independent synthetic clocks, 30-minute pivot confirmation delay, open 15m bar mutations, and 15m prefix parity at multiple strengths. Source comparison confirms the snapshot function, 4H/1H request/render blocks and eleven existing audit plots are unchanged. These tests do not compile or execute Pine and cannot establish TradingView replay behavior.

Load the complete updated source and confirm UI 0.6. Use the 15m chart to see all three layers, then toggle each layer and compare audit outputs on identical history. Check both break directions, equality, one event per pivot, replacement of current lines, Large/Huge labels, history limits and fixed publication timestamps. On 1H/4H the panel should explain the missing lower-timeframe layer rather than fabricate it. TradingView compilation, visual review and full causal/reload acceptance remain pending.

The user screenshot of UI 0.5 showed readable 4H and 1H lines with a 1H upward CHoCH while 4H was bearish and 1H neutral. Record that as partial user-provided runtime/presentation evidence, not proof of complete replay acceptance.

## Next boundary

After chart review, define and validate actual 4H location and 1H P2/SPA requirements before adding executable entry qualification. Required decisions include zone creation/mitigation, SPA definition, which 15m swing constitutes the required CHoCH and later swing break, retest tolerance/expiry and the signal-candle predicate. Preserve one-tick entry, three-bar order expiry, retest-based stop, minimum-2R opportunity, 50% TP1 and runner; do not turn research alignment into a trade trigger.
