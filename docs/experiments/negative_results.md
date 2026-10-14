# Negative findings and limits

**Final state: frozen research.** `PACT_GATE10A_NO_MATERIAL_PHYSICAL_IMPACT`, recommendation `FREEZE`. PACT distinguishes proxy gains, routed tradeoffs, correctness/timing/DRC qualification and practical physical impact. Failed hypotheses retain their compact data and exact input/architecture bindings. The [canonical index](../reproduction/canonical_results.md) provides direct evidence links.

## Proxy gains can fail to transfer

Nine Stage-B selections qualified under routed wire budgets, but not every winner improved every activity coordinate. Some s15850 selections regress measured H4; s9234 selections are dominated on the combined original three-objective front. Adding H4 changes interpretation without erasing the original comparison. [The complete report](../../results/pact_stage_b/REPORT.md) retains every outcome.

Bounded coverage and candidate ground-C error can move the decisive spatial maximum. Counterfactual substitutions are nonlinear/order-dependent and do not uniquely assign causal shares. A fixed-background probe recovered some H4 directions while failing H8 and was not promoted as the executed method.

## Generalization is mixed and admission-limited

Gate 09 b14 improves activity versus B3T with a small wire increase. b15 improves E/H8 while increasing H4 and wire versus B2. Neither primary dominates every baseline across four coordinates. b17 timed out in ATPG before placement/search; b18 was policy-deferred. These are neither successful industrial scaling nor fabricated optimizer losses. [Cohort report](../../results/pact_gate09_open_source_20261005/final/campaign/report.md) preserves the entire comparison.

## No material static power-integrity benefit

Gate 10A qualified nine frozen b14/b15 architectures. No PACT comparison met the joint worst/p99-drop requirement of at least 1% **and 100 µV**, subject to power/current guardrails. Primary worst-drop gains were only 3 µV and 8 µV. `PACT_GATE10A_NO_MATERIAL_PHYSICAL_IMPACT` recommends **FREEZE** under the tested basis.

Regional activity/static-IR correlation is strong on b14 but fails the registered cross-design criterion on b15. B5 yields larger estimated power/IR improvement at roughly 14–17% scan-wire cost and remains a control. H4/H8 are not established cross-design predictors of material static PI benefit. [Preregistration, report and decision](../../reports/gate10a/report.md) preserve smaller effects and controls.

The [protocol](../../reports/gate10a/protocol.json) requires at least 1% relative and 100 µV absolute reduction in **both worst and p99 drop**, with at most 1% dynamic-power and peak-segment-current regression. Modest scan-wire cost is separately limited to 2%. The [full-precision comparison](../../reports/gate10a/final_comparison.csv) keeps every primary, secondary and control result. Native voltage exports have approximately 1 µV resolution; interpolated percentile arithmetic does not establish finer solver precision.

The analysis uses Liberty mean power at 1.1 V and a 10 ns scan period, assumed nonclock duty 0.5 and ideal stripe-end supplies without package resistance. A common in-memory PG-connectivity normalization is audited against unchanged physical geometry; original routed ODB identities remain preserved. These assumptions delimit the static study. It establishes no transient droop, ground-bounce, current-density or thermal benefit. **THERMAL_IMPACT_NOT_EVALUATED**.

## Why the layers did not imply one another

The candidate evaluator predicts activity under a bounded logic/geometry model. Route/extraction measures a different electrical realization with shared-net loads, buffers and detours. Source-localized H4/H8 maximize capacitance-weighted activity over a bin and cycle, whereas Gate 10A uses averaged activity-derived power and a static resistive PDN solve. They are different observables, not interchangeable measurements.

The Stage-B saved s15850 diagnostic supports a coverage contribution: omitted activity changes the decisive spatial maximum even when represented trajectories agree. Ground-capacitance errors are also documented. Counterfactual substitutions are nonlinear and order-dependent; neither they nor the static study uniquely identify one causal share for routing, capacitance or coverage. Gate 10A additionally shows small absolute drop changes and inconsistent cross-design spatial correspondence. The tested proxy/activity gains were only partially preserved or insufficiently predictive of the final impact metric under this flow.

## Decision and non-claims

The registered materiality and spatial-correspondence criteria were not met, so the original algorithm-development basis was frozen. Tuning objectives or thresholds against these downstream outcomes would require a new hypothesis and registration. Smaller effects remain reported rather than discarded.

This does not prove that scan optimization or activity-aware DFT cannot improve physical design, that H4/H8 have no value elsewhere, or that another workload cannot yield material PI benefit. Thermal and transient benefit were not disproven; they were not established. Results do not generalize to arbitrary industrial SoCs or constitute a universal theorem about proxy optimization.

Collapsed fault-class identities/weights agree in the frozen gate; individual uncollapsed members are not enumerated. Zero-delay trajectories omit glitches; global-route timing is not detailed-route signoff. Earlier synthetic solver scaling does not qualify the full stateful model on industrial designs. New hypotheses require separate registration; cleanup does not rerun, tune or redefine these findings.
