# Reusable HTF market structure

The same pivot and directional-bias engine can be shared by every indicator. It is independent of supply/demand zones. All files remain in this workstream folder under repository conventions.

## Run now

Paste `src/htf_structure.pine` into TradingView Pine Editor. This standalone version needs no library publication. Select **Structure HTF** in settings: `1M` monthly, `1W` weekly, `1D` daily, `240` 4H, or `60` 1H. Other valid time-based selections are allowed. The source timeframe must be equal to or higher than the chart timeframe; standard candle charts only.

Example: on a 15m chart select `240` for 4H structure. On a daily chart select `1W` for weekly structure. To view monthly structure directly, use a monthly chart and select `1M`.

## Reuse in every indicator

1. Compile `src/HTFStructure.pine` as a library in TradingView and publish it under your TradingView account (privately or publicly as appropriate).
2. Open `src/htf_structure_import.pine.example`. Replace `YOUR_TRADINGVIEW_USERNAME` and version `1` with the actual published import path. This example deliberately cannot compile until that path exists.
3. Reuse its import and `request.security()` call in another indicator. Keep the timeframe validation and completed-snapshot timing. The library has no drawings, inputs, orders, or supply/demand dependencies.
4. Use returned bias to filter your indicator: `1` bullish, `-1` bearish, `2` transitional, `0` neutral. Bias alone is not an entry permission.
5. Pin an explicit published library version in each consumer. Updating the GitHub file does not update TradingView imports; publish a new library version and update consumers deliberately.

Pine does not import local GitHub files. Publishing the library is required only for the import workflow; nothing has been published to TradingView by this change.

`evaluate(leftBars, rightBars)` returns provisional current-source-bar calculations. Use it only with a suitable closed-bar policy. `confirmed(leftBars, rightBars)` returns the previous completed source-bar snapshot and is the recommended request expression with `barmerge.lookahead_on`. Call consistently on every source bar, not only when your indicator has a signal. Do not apply an extra chart-timeframe history offset to its results.

Return tuple order: latest high, latest low, bias, bullish BOS, bearish BOS, bullish CHoCH, bearish CHoCH, high label text, low label text, source open time, source close time, high-pivot open time, low-pivot open time, source high, source low. Empty label text means no newly confirmed pivot on that source bar.

## Common rules and timeframe settings

No separate monthly, weekly, daily, 4H, or 1H rule sets are required by this implementation. HH/HL, LH/LL, close-based BOS/CHoCH, level consumption, and transitional bias use the same definitions. See `phase-1-htf-structure.md` for exact rules.

The starting pivot setting is 2 left / 2 right candles for every timeframe; this is a research default, not an optimized recommendation. Two confirmation candles mean two monthly candles on monthly, two weekly candles on weekly, two daily candles on daily, eight trading hours on 4H, and two trading hours on 1H (session gaps can lengthen elapsed time). Monthly data needs sufficient history to establish multiple pivots.

You can configure pivot lengths separately in each consuming indicator without forking the algorithm. If testing supports different lengths, session filters, or instrument settings, record those as explicit per-timeframe profiles here. There are currently no validated timeframe-specific profiles. An indicator can request several independent timeframes by using separate consistent requests and inputs.

## Why an apparent swing may have no HH or LL label

A higher traded price is not automatically a confirmed HH pivot. With 2 right confirmation bars, a candidate high must satisfy the pivot-high test over both following source candles. If price pulls back for one candle and then exceeds the candidate high on the second candle, the earlier high is not confirmed and has no HH label. The next confirmed pivot high is compared with the previous confirmed pivot high to choose HH/LH/EH.

Highs and lows are detected independently. A low can qualify as HL even when the preceding small high does not qualify. The engine does not force alternating high/low labels or insert a synthetic HH to complete a visual sequence.

To capture smaller one-candle pullbacks, set **Swing confirmation bars (HTF candles)** to **1**. This is a configurable sensitivity choice, not a missing-label repair. Keep left bars at 2 initially if only reducing the right-side requirement. Such changes also affect bias, levels and structural breaks. Defaults remain 2/2. Do not label an unconfirmed high as a confirmed HH.

Completed HTF level values and pivot annotations now become visible on the same receiving update. This corrects the previous realtime mismatch where a guide showed a newly confirmed high but its annotation waited until the receiving chart candle closed. Labels may be redrawn during that candle under Pine rollback; no unclosed source candles are consumed. Alerts retain their chart-close timing.

Replay checks: find a candidate high followed by a lower high and then a higher high. It must not qualify with right=2; it can qualify with right=1 if the left-side pivot conditions also hold. Test the mirrored low case. On a live receiving candle, verify a newly delivered source pivot label appears with its level, without duplicate labels after the receiving candle closes or the script reloads.

## Swing lines: meaning and display

Red identifies the latest confirmed HTF swing high; green identifies the latest confirmed HTF swing low. The engine compares completed closes with unbroken pivot levels to detect BOS or CHoCH. These references are not supply/demand zones, trade entries, or necessarily still-unbroken levels.

**Swing level display** defaults to **Compact**: two short, thin dashed guides near the last chart candle, with price labels. This removes the historical staircase. Set line length, right offset, and price-label visibility under Swing levels. Increase the chart's right margin if labels are clipped.

Choose **Hidden** for annotations and bias background without level lines, or **Full history** to restore the historical staircase for investigation. Display choices do not affect the library, bias, swing events, or alerts. High/low values remain available in the Data Window in every mode. Compact guides track the latest bar rather than a historical candle when scrolling backward; use Full history or Bar Replay for historical inspection.

Visual acceptance: compare all three modes on the same chart and inputs. Events/bias must remain identical. Compact must retain no historical line trail; Hidden must show no swing-level guides or price labels. Confirm the right-edge labels follow the latest confirmed values and remain formatted to the symbol tick size. TradingView visual verification of this display change remains pending.

## Annotation placement and availability

- HH/HL/LH/LL/EH/EL labels are anchored to the actual source pivot candle's timestamp and extreme, not the later confirmation candle. They are created only after the right-side source candles complete. Hover for the confirmation time.
- BOS/CHoCH labels are anchored to the source candle whose close broke the level, not the later receiving chart candle.
- Both use source timestamps with `xloc.bar_time`. For an HTF pivot on a lower chart, the label identifies the HTF candle's opening time, not necessarily the exact lower-timeframe candle within it that made the extreme.
- These historical annotations must not be interpreted as signals available on the pivot candle. Bias and step lines are not shifted backward.
- Completed snapshots arrive at the start of the next source period. This policy also applies when chart and HTF match, so the display uses the prior completed candle. Labels are drawn as soon as a completed source snapshot arrives, including on the opening update of the receiving chart candle. Alerts wait until that receiving candle closes. On equal timeframes, labels therefore appear at the next source candle opening, while alerts arrive at its close; both identify the correct historical source candle.
- A changing source-open timestamp deduplicates events across lower-timeframe bars. The first loaded snapshot is not treated as a new event. Missing market bars may delay delivery.
- Only the most recent 500 labels are retained. Standard exchange/session time boundaries determine source candles.

## Maintenance and checks

The library is the canonical calculation source. Edit it and `src/htf_structure_view.pine.inc`, then run `python supply_and_demand/tools/build_indicator.py` from the repository root. This regenerates the standalone indicator and import example without maintaining separate copies of the algorithm. Use `--check` to detect drift.

Run `python -m unittest discover -s supply_and_demand/tests`. These source-contract tests check generation and timestamp/offset wiring; they are not a Pine compiler or market simulation.

TradingView compilation and Bar Replay verification remain pending. Validate the standalone version and published import version on 1M, 1W, 1D, 240, and 60; compare identical source candles across chart timeframes with matching history/session settings. Confirm labels land on pivot/break candles while alerts occur only at the receiving candle close, with no duplicates across lower-timeframe bars. Reload to compare closed-bar results. The engine is a local-pivot interpretation, not a protected-swing/external structure model or a proven trading edge.

References: [TradingView libraries](https://www.tradingview.com/pine-script-docs/concepts/libraries/) and [confirmed HTF requests](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/).
