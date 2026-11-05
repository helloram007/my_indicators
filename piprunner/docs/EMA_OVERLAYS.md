# Configurable EMA overlays UI 1.1.0

User request confirmed on 5 November 2026: six configurable EMAs, defaults 8 yellow, 20 blue, 36 dotted blue, 50 red, 100 amber and 200 green.

## Controls

Inputs contains a master **Show EMA overlays** switch and a shared price source (default close). Each EMA slot has independent visibility, length (1–5000), color, line width (1–4) and Solid/Dotted/Dashed style controls. All six are visible by default. Amber defaults to #FFBF00; other colors use Pine's named colors. Default widths are one pixel. Numeric slot names reflect the original requested defaults; changing a length does not rename TradingView's fixed plot title.

EMAs calculate on the current chart's timeframe: 8 on a 15m chart means eight 15m candles; on 1H, eight hourly candles. Existing standard-chart restrictions (15m, 1H, 4H) remain. Values update with the open candle's selected price source. These are visual overlays only, not additional bias, SPA, setup or entry gates. In particular, displaying EMA36/100 does not enable the optional Piprunner EMA filter.

EMA visibility is controlled by its own switches, independently of annotation mode. Annotation mode Off can hide educational drawings while leaving EMAs visible; turn off Show EMA overlays to hide them all. Input values remain hidden from the title/status line by source display settings. EMA plots appear on the price pane and in the Data Window, avoiding extra status-line/price-scale value labels.

## Installation

Replace the complete existing source with UI 1.1.0 and save/update the chart. Settings → Inputs → EMA overlays and the six EMA groups contain the controls. Verify the title and end marker both read UI 1.1.0. Do not paste only the new block; use the complete delivered .pine or .txt file.

## Validation and limits

Source checks verified six ta.ema calls, correct default lengths/colors/styles, 27 total plot outputs and the final completeness marker. Removing the new overlay block and normalizing the version reproduces the previous source exactly. Existing calculations and annotation logic are unchanged. No new numerical EMA oracle was added for this display-only feature. TradingView compilation and visual checking of UI 1.1.0 remain pending, as do the earlier unresolved chart/replay checks described in COMPILE_CHECKS.

Native dotted lines use plot.linestyle_dotted, supported by current Pine v6. Official reference: https://www.tradingview.com/pine-script-docs/visuals/plots/#plot-parameters.
