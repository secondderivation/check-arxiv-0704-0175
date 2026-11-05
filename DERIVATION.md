# Derivation from the frozen potentials

This is a new informed C derivation, not a blind reconstruction. Exact arithmetic and numeric values are in `code/check.py`, `reference/check-results.json` (the frozen historical output). Inputs are the original v2 TeX and the visually checked original PDF, not historical code.

## Null ray and finite integral

With the paper's signature and isotropic metric,

`ds² = -(1+2 Phi)c²dt² + (1-2 Psi) dl²`,

so the null condition gives `c dt = [1 - Phi - Psi] dl` at the retained weak-field order. For the static round trip along the same unperturbed ray, `c Delta t = -2 integral(Phi+Psi) dx`. Insert the pure GB pieces of (17)-(18):

`Phi+Psi = -(96/7) A² m³/(x²+b²)^(7/2)`.

The substitution `x=b tan(theta)` followed by `u=sin(theta)` gives

`I(b) = integral dx/(x²+b²)^(7/2) = b^-6 [F(u_E)+F(u_S)]`,

`F(u)=u-(2/3)u³+(1/5)u⁵`, `u_i=x_i/sqrt(x_i²+b²)`.

Differentiating F recovers `(1-u²)²`, providing an exact primitive check independent of numeric quadrature. At infinite endpoints, `F(1)+F(1)=16/15`. Therefore

`c Delta t_GB = (1024/35) A² m³/b⁶`,

and in the paper's y convention,

`y_GB = -(6144/35) A² m³/(c b⁷) db/dt`

`     = -(4m/cb)(db/dt) [(1536/35) A² m²/b⁶]`.

This discrepancy is between the paper's own potentials, integration definition and printed result; no new field-equation solution is needed to establish that particular conditional inconsistency. Whether a different solution or physical model invalidates those potentials is a different question, not resolved by this stage.

## Finite endpoints and differentiation

Set `S=F(u_E)+F(u_S)`. For fixed Cartesian endpoints,

`dI/db = b^-7 [-6S - sum_i u_i (1-u_i²)³]`.

For fixed radial distances R_i, `x_i=sqrt(R_i²-b²)` and

`dI/db = b^-7 [-6S - sum_i (1-u_i²)³/u_i]`.

The latter includes the chain-rule boundary terms. These two geometric limits are explicitly distinct from a spacecraft ephemeris; neither includes general independent radial endpoint velocities. Decimal arithmetic retains the small tail; a floating-point quadrature that rounds the tail to zero is not evidence that it is exactly zero. Simpson quadrature of cos(theta)^5 and the finite-difference derivatives pass the frozen criteria for the declared grid. See `reference/check-results.json`, `finite_endpoints`, for the complete numerical results.

## GR calibration, c and measured mass

For Phi=-m/r and Psi=-gamma m/r, the one-way delay is `(1+gamma)m/c` times the endpoint asinh sum, approaching `(1+gamma)m/c ln(4R_E R_S/b²)`. Round-trip delay doubles it. Their derivatives are, respectively,

`y_one = -(2m/cb)(1+gamma) db/dt`,

`y_two = -(4m/cb)(1+gamma) db/dt`.

Thus the paper's round-trip definition and (33) agree in the GR limit. Its (32) uses a rounded coefficient near `2m/c` instead of `4m/c`. Comparing its (32) and (33) literally fails already in GR; treating that mismatch as an additional coupling correction is invalid. If signal, reference and uncertainty are all expressed in the same convention, the inferred A is unchanged. A frequency-sign convention similarly reverses both signal and reference. Units require c Delta t to have length; A²m³/b⁶ has precisely that dimension.

For the remaining pieces, Phi+Psi contains `-Vr²/12`, yielding `(V/6) integral r² dx` for the round trip and the paper's V term. Before redefining G the inverse-radius coefficient is `(2+4AV')m0`; after `m=m0(1+8AV'/3)` it becomes `(2-4AV'/3)m` at first order. This gives the logarithmic factor in (30) and the AV' term in (33). The wrong constant under the printed logarithm does not affect d/db at this order. Neither this constant, nor using measured instead of bare mass consistently, supplies the missing GB factor.

## Coordinate and local-gamma alternatives

The formula using Phi+Psi applies in the specified isotropic coordinates. Under a linearized gauge change, the null-ray metric contraction changes by a total derivative along the unperturbed ray; the transformed endpoint coordinate-time/flat-path terms must be included. Transforming the potentials while retaining the old isotropic formula or old endpoints is not an alternative convention for the same observable. An impact-parameter correction of the neglected weak-field order changes the leading GB term only at higher perturbative order. These facts do not prove a fully gauge-invariant fitted Cassini observable here; they show why a coordinate relabeling cannot consistently multiply this fixed leading calculation by the alleged factor.

For `q=A²m²/r⁶`, the local ratio `Psi/Phi` is `(1+32q/7)/(1+64q/7)` and hence differs from unity by `-32q/7` at first order. The integrated Doppler bracket has `+1536q/35` evaluated at b. Even the sign differs. A local potential ratio is not the same quantity as the effective amplitude of this non-PPN signal.

## Bound interpretation

With the other terms suppressed, the paper's proxy sets `K A²m²/b⁶ <= delta`, where `K` is the Doppler bracket coefficient. Thus `A_max=sqrt(delta/K)b³/m`; changing K from its printed value to the derived value produces the square-root rescaling exactly. It is conditional on keeping the same proxy threshold, geometry and exclusions.

The GB signal is proportional to `bdot/b⁷`; the constant-gamma template is proportional to `bdot/b`. Their ratio varies as `b^-6`. Therefore a fitted uncertainty on constant gamma does not by itself furnish a statistically calibrated threshold for the GB template after noise weighting and orbital/plasma nuisance estimation. The published central value plus quoted uncertainty reproduces the paper's rounded number; this does not establish a confidence construction. At the smooth minimum of b, bdot vanishes, so maximal delay is not maximal instantaneous Doppler. Choosing b_min is strongest for a pointwise fixed proxy threshold, and is not proved statistically conservative.

At a single b the same-order bracket contains the sum of GB, AV' and V terms. Cancellations are possible without a jointly constrained model; their different time dependence could in principle help distinguish them, but no such fit is performed here. The unconditional observational bound remains unresolved. The cosmological mapping additionally assumes local and cosmological coupling equality and the scalar time evolution used in the paper.
