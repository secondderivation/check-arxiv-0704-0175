# Solar System Constraints on Gauss-Bonnet Mediated Dark Energy

[0704.0175v2](https://arxiv.org/abs/0704.0175v2) · Review 0.1.0-rc1

**Technical finding — not externally confirmed.** The printed potentials imply a Doppler coefficient 35 times smaller, weakening the paper’s proxy coupling bound by sqrt(35).

**Limit:** arXiv v2 only. No new Cassini-data confidence limit, journal-equation verification, or external confirmation.

## Checked scope

- Internal consistency of the weak-field potentials, round-trip delay and differentiated Doppler term.
- Conditional rescaling of the paper-input proxy bound; finite-endpoint, GR and convention controls.

Not checked: Field-equation solution beyond the assumed potentials; A new Cassini-data fit or calibrated confidence interval; Journal equations and all cosmological conclusions

## Review record

| Claim | Method | Outcome / adequacy | Evidence |
|---|---|---|---|
| F2: arXiv v2 equations (17), (18), (29), (30), (33), (34) — The GB coefficients from the printed potentials are smaller by 35; the same proxy bound weakens by sqrt(35). | independent\_derivation | held:discrepancy / pass | [DERIVATION.md](DERIVATION.md), [reference/check-results.json](reference/check-results.json), [SCOPE.md](SCOPE.md) |

[Protocol and provenance](PROTOCOL.md). This review record is retrospective.

## Review provenance

Historical Claude first pass; OpenAI coefficient review was exposed. The 4 November Codex critique derived and implemented the calculation anew from the fixed source while knowing the hypothesis. This is informed derivational independence, not blind discovery or external human confirmation. This package replays that saved implementation; it does not independently reanalyse Cassini recordings. See PROTOCOL.md and SOURCE.json.

Tools: Claude (historical first pass); Codex, gpt-6-astra/high (informed critique and packaging); Python standard library. Human involvement: Owner selected scope and the unconfirmed technical-finding route; no external scientific confirmation..

## Replay

~~~sh
python3 reproduce.py --output run-results
~~~

One local CPU; 30-second wall/CPU cap per replay; no dependencies beyond Python 3.11+. Replays 21 deterministic checks of the conditional derivation and controls; no Cassini-data fit.
