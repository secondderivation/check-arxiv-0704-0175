# What this finding does and does not establish

**Technical finding — not externally confirmed.** The result concerns the internal consistency of the fixed arXiv v2 equations, conditional on their weak-field potentials. It is not an accusation of misconduct and does not establish that the authors' underlying computation used the printed coefficient.

| Public statement | Source | Saved output |
|---|---|---|
| Round-trip GB coefficient 1024/35 rather than 1024 | Potentials (17)–(18), integral (29), result (30) | `reference/check-results.json`: `exact.roundtrip_delay`, `exact.printed_delay_ratio` |
| Doppler bracket coefficient 1536/35 rather than 1536 | Derivative of the delay, equation (33) | `exact.doppler_bracket`, `exact.printed_doppler_ratio` |
| Conditional coupling limit weakens by sqrt(35), about 5.916 | Same proxy threshold, geometry and suppressed other terms | `sqrt35`, `bounds[0].rescale` |
| Paper-input proxy changes from about 1.58248e20 to 9.36207e20 square metres | Equation (34), paper constants, central value plus quoted uncertainty used as a proxy | `bounds[0].original_formula_A_m2`, `bounds[0].corrected_formula_A_m2` |

The constant-gamma template scales as bdot/b; the GB template scales as bdot/b^7. Their fitted uncertainties cannot simply be identified. A statistically calibrated observational bound would require an appropriate signal, orbit, plasma and noise analysis. No such fitted bound is delivered here. The broader Cassini archive pilot ended without a validated combined observable or gravity fit; saved-result reconciliation did not rerun it independently. That unfinished branch is outside this local coefficient result.

The journal citation is JCAP 10 (2007) 004, DOI 10.1088/1475-7516/2007/10/004. Journal metadata is known; journal equations were not compared. We do not claim the same discrepancy is present in the version of record, universal novelty, or a complete literature search. The 4 November search did not resolve those limits.

Authors were contacted on 4 October 2026 according to the case record. No substantive response or external scientific confirmation is recorded as of this package preparation. Silence is not agreement. A substantive response or a source correction would trigger review of this scoped result.

The ancillary GR, endpoint, potential-term and cosmological proxy outputs are controls or conditional diagnostics. They are not additional externally confirmed findings or a new cosmological exclusion. Algebraic transcription, approximation and physical interpretation remain possible shared failure modes despite internal agreement.

License: LICENSE applies to this package's original code and review text. The paper and other third-party sources are linked, not redistributed or relicensed.
