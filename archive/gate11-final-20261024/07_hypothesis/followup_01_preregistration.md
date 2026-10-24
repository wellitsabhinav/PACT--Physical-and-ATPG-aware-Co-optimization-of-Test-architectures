# Gate 11 optional experiment 1: fixed-factor switched-capacitance accounting

Registered after base component analysis, before computing any factor swaps.

Hypothesis: increased physical ground-plus-pin capacitance on matched data nets offsets reduced transition counts, explaining weak total-power transfer (H2).

Population: all seven nonreference comparisons with frozen Gate 10A per-net exports, including both B5 controls and every available PACT variant. b14 CS_C2 remains in the 18-row historical table but lacks a power/per-net export; do not impute it.

Hold orders, workloads, physical results and transition records fixed. Match only identical net name, source pin, source Liberty master and source coordinates. Any unmatched net contributes a separately reported topology/mapping residual, with no forced correspondence.

Compute E_bb=sum(C_b*N_b), E_cb=sum(C_b*N_c), E_bc=sum(C_c*N_b), E_cc=sum(C_c*N_c) on the common support. Also compute the order-independent symmetric product decomposition:

- activity contribution = sum((C_b+C_c)/2 * (N_c-N_b))
- capacitance contribution = sum((N_b+N_c)/2 * (C_c-C_b))
- unmatched contribution = candidate-only E - reference-only E

Their sum must reproduce the exported E difference within floating-point roundoff. H2 predicts a positive capacitance contribution that counteracts a negative activity contribution. Report the actual fraction offset; do not infer a dominant cause from total route length or unweighted capacitance alone. If the capacitance term is nonpositive, it contradicts H2 for that comparison. If matching is poor or raw inputs cannot support identities, classify the physical causal extension as limited/inconclusive.

Convert weighted data activity to an analytical ground-plus-pin switching estimate using 0.5*V^2*E*1e-15/T, with V=1.1 V, T=shift_cycles*10 ns and E counting both transition directions. This excludes clock and internal power and is not a fresh OpenSTA run. Do not optimize, retune, change scan order or rank-select candidates.

Budget: one serial Python invocation, at most 120 seconds wall time, 512 MiB peak working set target, 20 MiB new outputs. No downloads, builds, GPU, simulator, route, extraction, or additional optional experiments. Record actual CPU, peak memory and disk increment through run_manifest.py.

Interpretation: an exact identity for the saved C*N model is controlled arithmetic evidence, not a circuit intervention or proof about transient/signoff power. Raw SPEF and mapping recovery gaps remain explicit. This protocol has no new empirical power-materiality threshold.
