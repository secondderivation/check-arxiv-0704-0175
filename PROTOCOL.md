# Protocol and provenance

This is a retrospective public packaging note, prepared 5 November 2026. It does not preregister or independently repeat the original discovery.

The original scientific protocol is preserved byte-for-byte in [SCIENTIFIC-PROTOCOL-2026-11-04.md](SCIENTIFIC-PROTOCOL-2026-11-04.md). It was committed before its execution at `88f7b2ad9fb181638255a8633d3c14ac720d2026`; its SHA-256 and fixed source hashes are in [SOURCE.json](SOURCE.json). Its `waiting_for_commit` header records the historical preparation state, not the present release state. The original receipt and coordinator acknowledgement remain in the private audit trail. No private correspondence or third-party paper files are distributed.

## Scope and provenance

The supported result is a discrepancy within arXiv:0704.0175v2: the printed potentials and round-trip integral imply a GB coefficient smaller by 35 than the printed delay/Doppler result. The square-root change to the coupling bound is conditional on the paper's proxy construction. It is not a newly fitted Cassini confidence limit, a verification of the journal equations, or a refutation of the cosmological model. See [DERIVATION.md](DERIVATION.md) and [SCOPE.md](SCOPE.md).

Claude supplied the historical first pass. Historical OpenAI review of this particular coefficient was exposed to earlier reasoning. The 4 November Codex critique implemented the derivation anew from the fixed source but knew the hypothesis. It was an informed critique, not a fresh blind B or external human confirmation. The present package reuses that implementation. A fresh package replay is not an independent discovery or another provider. Any specialist confirmation remains absent.

## Frozen numerical suite

Python standard library, Fraction arithmetic and Decimal precision 60. The original suite uses Simpson quadrature with 16384 panels, relative tolerance 1e-10, at b/b_min = 1, 2, 5 for fixed Cartesian and fixed radial endpoints. Finite-difference steps are 1e-4 and 1e-5 times b; the finer step must agree to 1e-7. GR, zero-coupling, mass normalization and one/two-way checks remain as recorded. Literal paper-input constants, including both proxy thresholds, are in the frozen reference JSON. No Cassini recordings, inference chains or external services are required.

## Public replay contract

Run `python3 reproduce.py --output run-results` from this directory. Use Python 3.11 or later; no installation or network access is needed. The output directory must not exist. The wrapper checks the frozen reference hash, runs the unchanged mathematical suite once with a 30-second wall timeout (and a 30-second CPU limit on POSIX), and writes only into that new directory. No retry. The distributed reference remains untouched. Failures are preserved in the output directory.

Acceptance requires all 21 named checks, identical structured keys and exact rational/string values; finite floating-point summaries use relative tolerance 1e-12 and absolute tolerance 1e-12. Runtime metadata is excluded. This tolerance concerns replay portability, not scientific confidence or the original paper. It does not relax the suite's own quadrature/derivative criteria. A separate checker test exercises corrupted scientific values, verdicts, missing fields, nonfinite values and harmless display roundoff without rerunning the science.

The packaging changes only output handling and runtime guarding. Candidate integrity, a fresh P2 audit and owner publication approval are separate gates. No online CI run is claimed. Publication history: the predecessor review 0.1.0-rc2 was approved and published on 10 November 2026. The preceding preparation statements describe that historical stage. The owner approved publication of this editorial revision, 0.1.0-rc3, on 11 November 2026.
