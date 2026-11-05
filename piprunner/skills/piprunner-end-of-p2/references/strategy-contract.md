# Strategy contract

Baseline recorded 5 November 2026. Repository decisions and later explicit user corrections take precedence. This is a portable rule reference, not a claim that all rules are implemented.

## Confirmed End-of-P2 requirements

- TradingView; current development language Pine v6.
- 4H bias has priority; 1H qualifies the end of P2 (the pullback); 15m confirms execution. Neutral/unknown 4H blocks directional qualification. Lower timeframes cannot authorize counter-4H entries.
- 1H location is support/resistance OR supply/demand; require ANY ONE of pin-bar rejection, directional engulfing or piercing in the HTF direction. SPA means Strong Price Action. Numeric strength/contact rules and bearish piercing interpretation require explicit definition; current research thresholds are proposals.
- S/D invalidation requires the zone's OWN timeframe candle CLOSE strictly beyond its buffered extreme. The buffer is 30% of full base high-low range under the current disclosed implementation interpretation: demand below baseLow − 0.30×range; supply above baseHigh + 0.30×range. Wick-only breach/equality does not invalidate. Viewing chart timeframe does not change ownership. Buffer does not widen the contact zone or redefine trade stops.
- Entry sequence: 15m CHoCH → distinct swing break → retest → signal candle → entry one minimum tick beyond the signal candle in the trade direction.
- Pending entry expires after three bars. Exact counting/inclusivity and competing-event precedence remain open.
- Stop beyond retest extreme; minimum 2R opportunity; 50% at TP1 and a runner. Exact stop buffer, target mapping, runner exits and post-fill bias-change handling remain open.
- Optional EMA and fractal experiments must not silently override those invariants. Drawing toggles do not change trading decisions.

## Original Piprunner signal — supplied strategy description

This belongs to the original comparator. It is not yet implemented as a 15m signal in the hybrid.

- 36 EMA above 100 EMA permits original long setups; below permits original shorts.
- Williams Fractals: supplied default two bars left/two right; confirmation only after right-side bars CLOSE.
- Long: prior fractal highs establish higher highs and prior lows higher lows; a confirmed lower-high fractal then appears. Original buy-stop is that lower-high high + 1 pip; original stop is latest fractal low − 1 pip; original target is 1R.
- Short: prior highs establish lower highs and prior lows lower lows; a confirmed higher-low fractal appears. Original sell-stop is that higher-low low − 1 pip; original stop is latest fractal high + 1 pip; original target is 1R.
- Supplied original assumptions included 15m default, automatic forex pip size with manual override, pending cancellation on close through intended stop, one-unit size, million initial capital and zero costs. These are source assumptions, not adopted hybrid requirements.

The hybrid's optional EMA filter, fractal structure references, additional continuation signal and original comparator must have separate identities. Do not call visual EMA overlays or generic structural pivots implementation of the original signal.

## Decisions before implementing the fractal signal

Determine only those needed for the requested feature:

1. Role: informational candidates, structure assistance, additional gate after the baseline sequence, or original comparator. Replacing an End-of-P2 trigger requires a separately named/approved variant.
2. Exact fractal equality/tie handling, left/right configuration and whether classical asymmetrical equal-high/low cases are included. Do not assume generic pivot functions match the intended Williams definition.
3. Which prior confirmed highs/lows form the continuation structure; ordering, strict inequalities, interleaving and reset rules; what happens when both sides confirm together.
4. How the new LH/HL candidate links to a qualified 1H setup and baseline 15m sequence; one candidate per setup, replacement, cancellation and stale candidate policy.
5. If used as a hybrid gate, its expiry and timing relation to the baseline three-bar order expiry. Preserve tick versus pip units.

Useful tests: no event before right-bar close; future-bar extension cannot change previously published events; correct confirmation on reload/replay; ties and equal extremes; HH/HL then LH and mirrored short fixtures; missing precursor structure; delayed confirmation when price already crossed a level; duplicate MTF delivery; HTF conflict; setup cancellation; simultaneous events; configurable lengths; visual-toggle ledger parity; optional gate off reproduces baseline. Separately verify the original comparator's pip entry/stop/1R behavior if requested. Reference tests alone do not prove Pine correctness or trading performance.

## Implementation snapshot

UI 1.1.0: proposed 4H/1H/15m structural extractor, horizontal levels, research BOS/CHoCH, proposed S/D detection/lifecycle, 1H S/D SPA candidates and six display-only EMAs exist. S/R branch, approved full setup lifecycle, qualified 15m execution, Williams Fractal continuation signal and trade management are incomplete. Complete script compiled and rendered on EURCHF 4H/1H/15m on 5 November; full replay/non-repainting and numerical acceptance remain pending. Consult live repository for later changes.
