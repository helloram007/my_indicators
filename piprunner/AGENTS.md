# Piprunner development instructions

- Read `docs/PROJECT_CONTEXT.md`, `docs/DECISIONS.md`, `docs/roadmap.md` and relevant requirements before editing.
- Target TradingView; use Pine Script v6 for new chart scripts. Keep source, tests and documentation under this directory.
- Develop one feature at a time. First deliverable: proposed 4H Bias indicator with configurable educational annotations, no orders.
- Preserve 4H bias → 1H setup → 15m execution and all confirmed End-of-P2 invariants.
- Keep CONFIRMED requirements distinct from PROPOSED algorithm choices and OPEN decisions. Platform confirmation is not approval of the proposed structural model.
- Do not silently replace signal-candle plus one-tick entries, retest-based stops, three-bar expiry, minimum 2R, 50% TP1 or runner management with Piprunner rules.
- Treat EMA36/100 and 15m Williams Fractals as independent optional experiments. Annotation switches only affect visuals.
- Use confirmed higher-timeframe evidence; distinguish pivot origin, confirmation and publication timestamps. Never backdate actionable signals.
- Every implemented feature needs rule IDs, meaningful causal/state tests, explanatory annotations and a clear status report.
- Never claim Pine compilation or TradingView replay validation from a Python/reference test alone. Record actual platform checks separately; if unavailable, mark them pending.
- Do not invent zone, SPA, candle, retest, target or runner definitions. Unresolved required predicates must remain visibly undefined.
- After meaningful work update the context, roadmap and decision log. Record changes, checks actually run, limitations and exact next action.
- Check branch, remote and working-tree state before Git operations. Preserve user changes. Current development branch at handover is `piprunner/setup`; verify rather than assuming it forever.
- Do not commit credentials, private tokens, exported sessions or account secrets.
