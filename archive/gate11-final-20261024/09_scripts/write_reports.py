import pathlib,json,csv,math,datetime,collections
R=pathlib.Path(r'F:\Research\PACT\Gate11'); P=R/'01_inputs/S008/PACT'; G=P/'reports/gate10a'; O=R/'08_reports'
rows=json.load(open(R/'06_causality/enriched_results.json')); base=json.load(open(R/'06_causality/base_analysis.json')); diag=json.load(open(R/'06_causality/diagnostic_summary.json')); factors=json.load(open(R/'06_causality/followup_01_results.json')); run=json.load(open(R/'10_logs/followup_01.manifest.json'))
def table(headers,data): return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+'\n'.join('| '+' | '.join(map(str,r))+' |' for r in data)+'\n'
def num(x,d=4): return f'{x:.{d}f}' if x is not None else 'MISSING'
def write(name,s): (O/name).write_text(s.strip()+'\n',encoding='utf-8')
primary=[r for r in rows if r['configuration']=='CS_C1']
primarytable=table(['Comparison','E %','H8 %','FF Q transitions %','Combinational transitions %','Dynamic estimate %','Dynamic delta µW'],[[f"{r['design']} C1 / {r['baseline']}",num(r['E_delta_percent']),num(r['H8_delta_percent']),num(r['scan_FF_Q_transitions_delta_percent']),num(r['combinational_transitions_delta_percent']),num(r['dynamic_w_delta_percent']),num(r['dynamic_w_absolute_delta']*1e6)] for r in primary])
alltable=table(['Design','Architecture','Scan-path µm','Total route µm','E (fF·transitions)','H8','Data transitions','Dynamic mW'],[[r['design'],r['configuration'],num(r['routed_scan_path_um'],3),r['total_route_wire_um'],num(r['E_ff_transitions'],3),num(r['H8_ff_transitions'],3),r['total_data_transitions'],num(r['dynamic_w']*1e3,6) if 'dynamic_w' in r else 'MISSING'] for r in rows])
transfertable=table(['Design','Variant','Search ΔE %','Implemented ΔE %','Search ΔH8 %','Implemented ΔH8 %'],[[r['design'],r['configuration'],num(r['search_E_delta_percent']),num(r['E_delta_percent']),num(r['search_H8_delta_percent']),num(r['H8_delta_percent'])] for r in rows if r['configuration'].startswith('CS_')])
factortable=table(['Design','Variant','Activity / reference E %','Capacitance / reference E %','Offset of activity saving %','Matched reference E %'],[[r['design'],r['candidate'],num(r['activity_component_percent_baseline_E']),num(r['capacitance_component_percent_baseline_E']),num(100*r['cap_offset_fraction_of_activity_saving']),num(100*r['baseline_common_E_share'],5)] for r in factors])
pp=base['native_power_components']; ptable=[]
for d,b in [('b14_opt','B3T'),('b15_opt','B2')]:
 for c in ['Sequential','Combinational','Clock']:
  x=next(r for r in pp if r['design']==d and r['configuration']==b and r['native_category']==c); y=next(r for r in pp if r['design']==d and r['configuration']=='CS_C1' and r['native_category']==c); total=next(r for r in rows if r['design']==d and r['configuration']==b)['dynamic_w']
  ptable.append([d,c,num(x['internal_w']*1e6,3),num(x['switching_w']*1e6,3),num(100*x['dynamic_w']/total,2),num((y['dynamic_w']-x['dynamic_w'])*1e6,4)])
powertable=table(['Design','Native category','Ref internal µW','Ref switching µW','Ref dynamic share %','C1 dynamic delta µW'],ptable)
spatialtable=table(['Design','H8 bin','Ref mean dynamic share %','Same-bin mean dynamic Δ%','H8 maximum Δ%'],[[r['design'],r['reference_H8_bin'],num(100*r['reference_bin_average_dynamic_fraction']),num(r['same_bin_average_dynamic_delta_percent']),num(r['H8_peak_delta_percent'])] for r in diag['peak_bin_budgets']])
provenance='''
- Recovered source snapshot: archived main worktree HEAD `e84f4afbf04a918060b4ad845f5166d8e6c7b92c`, from preserved Git audit G005. Selective regular-file restoration, not a full Git clone; original member hashes identify the actual bytes.
- Gate09 PACT SHA `71b059d9d1a00735d79b6a428693eaba549a5f33`; b14 comparison implementation SHA `e43da79d76d363fe67ae120d5e53a3c2d04a9a2f44549601d8df2daabc05cf3e`. Row-specific provenance is retained separately.
- Gate10A parent `53ebab37fd76970d7c5e676b0caec13c7c16296e`; preregistration `b9869834a3479a57f256c83fa74a4617faab4af2`.
- Common OpenROAD `08f67ee5ecd14db5a42be8c610bbfd1ccf079299`, version `26Q2-1164-g08f67ee5ec`, binary SHA-256 `fcd7dcfc37d329bd43a7ede75805319a2e70e6879da11d42b4fd1c2e50e645c3`.
- ORFS `5e8b1450d19263f797a27c4f371b9dd19f32a3aa`; declared embedded OpenSTA `76c4d6df3537ccce331b5caa812196c3330ba7c4`. Supporting OpenROAD source `dc5eee77c45dba8e5ace2fc89c38c6d9a4ed6e0f` differs from the binary. Standalone STA 3.1.0 was not the power engine.
- FAN_ATPG base `26b2b36c0e9db11a4b6d9e759df6e44357121f39`; qualified repair `4c253bfa613e5827f17c42a5fce8be7bea779e1e`.
- I99T sources `8a2c3b500ee7ff20e7031de92592b737bedc6d8c`.
- Nangate45 typical Liberty SHA-256 `8d540a4d4cf6d09d27c87ad067857a9c0c2eeb023ab7a56e058cd3113db4e9b1`; exact library/RC bytes recovered and verified.
'''
refs='''
Primary sources checked 23 October 2026. Search indexing dates are not publication dates.

| Work | Verified scope and relevance | Access boundary |
| --- | --- | --- |
| Gupta, Kahng, Mantik, Routing-Aware Scan Chain Ordering, ASP-DAC 2003 | Routing-driven ordering and route-aware costs predate PACT. [Author paper](https://nanocad.ee.ucla.edu/wp-content/papercite-data/pdf/c2.pdf) | Full paper retrieved. |
| Ghosh, Basu, Touba, Joint Minimization of Power and Area in Scan Testing by Scan Cell Reordering, ISVLSI 2003; UT-CERC-TR-NAT02-1 | Test-vector-driven ordering, dynamic minimum-transition filling and power/area tradeoffs are established. [Author report](https://users.ece.utexas.edu/~touba/research/scan-tr.pdf), [author publication list](https://users.ece.utexas.edu/~touba/research/pub.html) | Indexed primary report text and publication list verified; direct PDF open failed. |
| X.-L. Huang, J.-L. Huang, A Routability Constrained Scan Chain Ordering Technique for Test Power Reduction, ASP-DAC 2006, pp. 648–652 | Test-power ordering under explicit routing constraints is established. [Official abstract](https://www.aspdac.com/aspdac2006/archives/7a/index.html), [conference paper](https://www.cecs.uci.edu/~papers/aspdac06/pdf/p648_7A-1.pdf) | Official abstract and indexed primary paper text verified. |
| Wu, Chao, Scan-Cell Reordering for Minimizing Scan-Shift Power Based on Nonspecified Test Cubes, TODAES 16(1), Article 10, 2010, DOI 10.1145/1870109.1870119 | Pattern/response correlations, scan-in/out transitions, inverse connections and routing overhead tradeoffs appear together. [Institutional paper](https://ir.lib.nycu.edu.tw/bitstream/11536/32040/1/000284931600010.pdf) | Indexed institutional paper text; journal version distinct from VTS 2008. |
| Lee, Chang, Lee, Yang, Physical-Aware Approaches for Speeding Up Scan Shift Operations in SoCs, ETRI Journal 38(3), 2016 | Physical constraints and induced logic toggling during shift are recognized; functional-output gating is discussed. [Publisher full text](https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.16.0115.0779) | Full text retrieved; primary contribution is shift timing. |
| S. Lee et al., Low-Power Scan Correlation-Aware Scan Cluster Reordering for Wireless Sensor Networks, Sensors 21(18):6111, 2021 | Correlation-based clustering for scan activity is established. [Publisher](https://www.mdpi.com/1424-8220/21/18/6111), [archived article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8472869/) | Indexed primary text; direct opens returned 429/challenge. Not all detailed methods independently inspected. |
| Physical-Design Aware Scan Cell Reordering for Low Power Testing, EWDTS 2024, DOI 10.1109/EWDTS63723.2024.10873686 | Directly overlapping physical-aware peak-power/routing claims exist. [IEEE abstract](https://ieeexplore.ieee.org/abstract/document/10873686) | Indexed publisher abstract; direct open 418. Detailed methods/signoff assumptions not verified. |

Targeted overlap check, not an exhaustive systematic review. Abstract access cannot establish method equivalence or absence of novelty. No third-party summaries are used as technical proof.
'''
hypotheses='''## H1 — Surrogate objective mismatch: Inconclusive for omitted-combinational causality

Prediction: search E/H4/H8 gains may not predict implemented logic activity or power. Measurement: b14 C2 predicts H8 −9.6995% but implemented H8 rises 4.8490%; b15 C1 predicts H4 −4.2107% but implemented H4 rises 2.6185%. The depth-3 settled search model approximates candidate capacitance and fixes the buffer skeleton; final E includes all mapped settled data-net transitions.

Observed surrogate mismatch is supported, but its specific attribution to omitted combinational switching is not isolated. Supporting evidence: predictor/implemented reversals and attenuation; E omits internal and clock power. Contradiction to a simplistic omission claim: final E already includes combinational nets, and all five power-covered PACT cases reduce both FF-Q and combinational transitions. Implemented E and dynamic estimates move in the same direction. Descriptive r=0.9844 for their five dependent deltas is partly model-coupled, not independent prediction validation.

Confounders: depth coverage, geometry/capacitance approximation, baseline-fixed buffers and routing differ together. Saved H8 diagnostics predate Gate11 and report omitted-region/capacitance errors, but ordered nonlinear substitutions do not uniquely allocate causes. Confidence: high in observed mismatch; limited in assigning it specifically to omitted logic. No new algorithmic correction is validated.

## H2 — Physical capacitance cancels activity: Not Supported as the dominant common explanation

Prediction: positive capacitance contributions counteract activity savings. The registered fixed-factor analysis matches 100% of PACT reference E support. Capacitance helps b14 C1/C3 and b15 C2; it offsets only 7.57%/6.82% of activity-only savings in b15 C1/C3. Unweighted total capacitance is not a reliable attribution.

Supporting evidence: small positive offsets in two b15 cases. Contradiction: negative offsets in three of five PACT comparisons, including both b14 cases. B5 saves about 20% E and 12.6–13.6% dynamic power despite greater scan-path wire cost; its different wire budget prevents treating it as a feasible replacement.

Confounders: exact arithmetic within the saved ground-plus-pin C×N model is not a timing-aware circuit intervention. Coupling, slew, glitches and internal power lie outside the identity; raw SPEF/mapping was not recovered. Confidence: high for saved-model accounting; physical/signoff extension untested.

## H3 — Gains are localized: Supported for peak-versus-average mismatch

Prediction: an improved local maximum need not appreciably change total mean energy. b14 C1 H8 improves 5.6876%, but full-chip maximum per-cycle C×N improves only 0.1967%, E 0.3574%, and average dynamic power 0.2321%. The winning H8 bin contributes 3.59% of reference average dynamic power; its mean dynamic power rises 1.0453%, with the same winning bin 34. b15's winning bin contributes 2.85% and its mean falls 0.9324%.

Supporting evidence: spatial accounting, retained maximum/percentile summaries, persistent clock budgets and the same-bin b14 counterexample. Limit: average bin share does not establish share at the exact peak cycle; a rare local reduction can still matter to a local transient constraint. Cycle-synchronous Liberty power, occupancy and timing-aware activity were not recovered. Confidence: high for local/peak versus whole/mean distinction; physical peak-power and dynamic-IR benefits inconclusive. Activity maps do not prove dynamic IR improvement.
'''
write('PACT_GATE11_DAC_NOVELTY.md','''# PACT Gate 11 — DAC novelty assessment

A distinct DAC research contribution is **not established**. Gate11 demonstrates reproducible accounting of a weak/negative transfer result under one frozen open-source flow.

'''+refs+'''
## Claims versus actual evidence

| Proposed claim | Assessment |
| --- | --- |
| Combine placement/routing and test-pattern correlation | Broad concept established by earlier routing, correlation and constrained-ordering work. |
| Weight transitions by physical capacitance | Standard switching model; PACT E already uses ground-plus-pin weighting. Adding it again is not new. |
| Include induced combinational switching | Established concern and already included in final PACT activity. Better search-cone coverage is an engineering direction; no new algorithm or novel solution is validated. |
| Improve PI through source-localized hotspots | No guaranteed transfer and no recovered transient/signoff validation. Peak/local versus average/whole distinction does not itself establish novelty. |
| Calibrate routed internal/clock/load contributions | Possible direction; no distinct predictor, held-out validation or robust physical advantage demonstrated. |
| Release the negative-result/audit artifact | Useful reproducibility contribution; usefulness alone does not establish a DAC technical advance. |

A workload-aware mapping from legal scan permutations to time-resolved, spatially distributed power including clock, internal, parasitic and hazard effects could be investigated. Gate11 establishes neither its novelty nor the matched timing-aware evidence needed to validate it. It must remain a research question, not an achieved claim.

Keep optimization frozen. Reconsideration needs a separately registered mechanism, comparisons to overlapping literature and independent physical validation. No broader optimizer, weight sweep, machine learning or new architecture was built.
''')
write('PACT_GATE11_CAUSAL_FINDINGS.md','''# PACT Gate 11 — causal findings

The recovered estimates show small, real average-power reductions. The strongest discrepancy is a local peak metric compared with whole-workload mean power. It does not mean that no switching changed.

'''+primarytable+'''
**Why did E/H8 improve?** Frozen permutations changed correlated scan loads/responses and induced data activity under wire constraints. H8 changes a source-localized cycle maximum. Search and final routed metrics differ substantially; neither is a direct watt/voltage measure. No new optimizer ran.

**Did modeled activity decrease?** b14 C1 FF-Q transitions: 6,389,951 → 6,323,571; combinational: 66,979,151 → 66,845,222. b15 C1 FF-Q: 22,286,672 → 21,795,076; combinational: 118,675,166 → 117,072,400. These are new reaggregations of frozen zero-delay netlist exports, not new simulations. All 18 architectures' aggregate outcomes remain reported.

**Why is total power change small?** Implemented E falls only 0.27–1.37% in the five power-covered PACT cases. Substantial internal and clock energy lies outside E. Retained b14 density controls leave 208.404 µW at zero nonclock data activity, 31.37% of nominal 664.406 µW. This fixed-model floor includes clock-network and sequential clock-driven internal power; the historical intervention is not a new Gate11 experiment or a universal silicon floor.

**Which contributions dominate?** b14 reference dynamic shares: combinational 54.51%, sequential 26.29%, Clock 19.20%. b15: 35.06%, 39.36%, 25.58%. Internal power is about 51.65%/55.88% of dynamic power. Cell-class percentages and internal/switching percentages are orthogonal and must not be added.

'''+powertable+'''
**Does extra capacitance explain it?** Only a small design-dependent part. The sole registered factor experiment contradicts a common dominant-offset mechanism. With N counting both transition directions, the analytical ground-plus-pin switching estimate is 0.5×V²×E/T (after fF→F conversion), excluding clock/internal power.

'''+factortable+'''
**Is a correctable algorithmic weakness demonstrated?** Depth-limited geometry/activity/source-localization prediction has a demonstrated weakness. A broader calibrated model could address engineering mismatch, but Gate11 does not show that a correction changes the qualified feasible frontier or yields a useful new physical benefit.

**Is that weakness distinct from prior work?** Not established. Physical-aware ordering, routing constraints, pattern/response correlations and induced logic switching are established topics. Literature access limits and direct links are in the novelty report.

'''+hypotheses+'''
The causal explanation is bounded to the recovered activity-derived model. It does not uniquely establish silicon causality, physical glitches, transient peak power or dynamic IR. Missing raw inputs and the broken qualified runtime prevent a fresh physical reproduction.
''')
audit=r'''# PACT Gate 11 input audit

## Discovery and read-only boundary

The current C: workspace is no longer a Git checkout and contains only forensic-quarantine directories. Original projects/results were inspected read-only. Canonical evidence was found in `F:\Research_Archives\PACT\`, selected through `F:\Research_Archives\AUDIT_REPORTS\archive_manifest.csv`. The archived active worktree was `C:\Users\Abhinav\OneDrive\Desktop\PACT\PACT`.

No original repository, archive, WSL registration, historical output, junction or symlink was modified. No environment/worktree was created outside F:. The user authorizes this separate Gate11 study; the original project's freeze remains intact.

## Recovered evidence

| Evidence | Path below `01_inputs/S008/PACT/` | Integrity/scope |
| --- | --- | --- |
| Stage A | `results/stage_a/`, `results/pact_oss_benchmark/topology_recovery_20261004/` | 19/19 selected and 27/30 indexed qualified; checksums/projections verified. |
| Gate09 | `results/pact_gate09_open_source_20261005/final/`, `repair_attempts/` | 18 b14/b15 rows, B0/B1/B2/B3T/B4/B5, C1/C2/C3, seed 11, fairness/hashes, selections and failures. |
| Gate10A | `reports/gate10a/` | Nine selected records, 17 attempted/control runs, net activity and per-instance power, spatial vectors, protocol/decision/tool provenance. |
| Implementations/evaluator | `src/pact/optimizer/`, `src/pact/activity/`, `scripts/pact_cpu_activity.py` | Depth3/stateful and exact compact Icarus sources; qualified crosscheck receipts. |
| End-to-end | `results/pact_end_to_end_20261004/` | Original verifier passes 12 records/fault-identity comparisons. |
| H8 diagnosis | `results/pact_h8_rootcause/` | Historical omitted-region/capacitance findings and nonlinear attribution limits. |
| Liberty/RC | `external/OpenROAD-flow-scripts/flow/platforms/nangate45/` | Exact hash-matched Liberty, setRC and grid strategy recovered; no tool build. |
| s5378 | Stage A/B tables | Total-route non-improvement corroborated; exact earlier phase1 HPWL raw pair not recovered. |

4,578 initial regular files plus seven additional required files were selectively extracted and individually checked against archived member hashes. No links were created. Both source containers matched the archived checksum ledger. `selected_inputs_manifest.json`, `extraction_receipts.json`, and `additional_extraction_receipts.json` identify each member. Environments, tool builds, .git objects and large caches were not wholesale restored.

`retained_hash_verification.json` passes 674 retained bindings, audited original/public normalization rules, Stage-A table projections and selected Gate10A outputs. This successful hash-only audit is separate from blocked numerical optimizer replay.

## Missing evidence and reproduction blockers

Selected raw count traces, routed Verilog/ODB/SPEF, logical/physical maps, qualified b14/b15 patterns, large stimuli and placement inputs are hash-addressed historically but absent from the recoverable PACT regular-file inventory. Alternate identical-file hashes were checked. Of 245 unique selected/input/tool/output bindings, 165 had recoverable matches and 80 did not. All recoverable required matches are now staged; a recorded binary hash does not recover the binary.

The prior `E:\PACT_ARCHIVES\20261008\gate_results\pact_gate09_open_source_20261005.tar.zst` path is absent. Its indexed expected SHA-256 is `2ed5ab00d1e4b9190d58ecd3c22fc03add0b2ea2f9bce8a8be662c06febe7a9f`. No substitute private package or download URL was invented.

Ubuntu-24.04 is registered but fails on missing `F:\green-ecc-iscas-sustainability-temp\wsl-relocated\Ubuntu-24.04\ext4.vhdx`; configured F: swap path is also missing. Linux did not start. No repair/reinstall/config change occurred. Native Icarus is present but cannot reconstruct the qualified workload without exact inputs/cell models and matching runtime/VPI evidence.

Original `verify_reproducibility.py` fails immediately because Numba is absent. Archived .optimizer-deps Numba/llvmlite are Linux binaries and were not used as a fake Windows replacement. The 18 numerical Stage-B State/reference replays are not newly verified. The separate end-to-end verifier passes.

No new VCD/SAIF, occupancy, timing-aware glitches, extracted route, ideal/routed comparison, transient IR, thermal, EM or signoff result exists. Prior complete-count validation is recovered record evidence plus export integrity, not a new read of missing raw traces. Frozen path-normalized exports were checked, not resealed.

## Provenance
'''+provenance+r'''

## Storage/resources

Fresh root: `F:\Research\PACT\Gate11\`. All required numbered directories and scratch/cache/tmp exist. Initial free F: bytes: 168,161,681,408. Controlled TEMP/TMP/TMPDIR, pip/XDG/Python/Matplotlib/Numba caches, HOME, working/output directories resolve inside Gate11. No install/build/GPU/full physical flow ran. Analysis was serial; two inexpensive retention checks briefly overlapped.

Machine audit: `storage_audit_initial.json`, `storage_audit_final.json`, `current_tool_audit.json`, `10_logs/*.manifest.json`. Initial discovery is recorded retrospectively without invented timestamps. Initial inventory/recovery has source/log/member receipts rather than a fabricated prospective manifest; every launched scientific analysis has a prospective command/resource manifest.

Controllable experimental storage complies with F-only. Codex transcripts/tool transport, OS/WSL service bookkeeping, pagefile/antivirus/system logs cannot be certified as system-wide F-only. WSL tried its preconfigured missing F: swap/disk paths outside Gate11 and failed before Linux. No deliberate experimental output was written there or to C:/D:/E:.
'''
(R/'00_audit/PACT_GATE11_INPUT_AUDIT.md').write_text(audit.strip()+'\n',encoding='utf-8')
report='''# PACT Gate 11 — Physical Power Causality

23 October 2026 (Asia/Calcutta). Decision: **NO-GO** for another optimizer stage or a DAC claim under the current evidence; keep PACT frozen. This bounded decision does not imply that scan-power optimization is generally ineffective.

## 1. Executive summary

Recorded gains partially transfer: primary candidates reduce modeled FF/combinational transitions and estimated average power. Effects are small because implemented aggregate E reductions are small, clock/internal power persists, and H8 targets a local cycle maximum rather than workload energy. Search predictions also fail in some coordinates. A dominant capacitance-cancellation mechanism is contradicted in three of five power-covered PACT cases. These results do not establish a distinct new DAC contribution.

'''+primarytable+'''
Recovered: 18 Gate09 architecture results, nine net/power export pairs, all 17 Gate10A attempts including three failures, Stage-A tables, evaluator source, selected orders/provenance and 12 end-to-end records. New: hash audits, component aggregation, predictor-transfer comparison, spatial budgets and exactly one registered fixed-factor experiment. Blocked: new matched netlist/VCD/SAIF replay, raw SPEF/routed reproduction, fresh OpenROAD power and timing-aware peak/dynamic-IR analysis.

## 2. Research question

Why do scan activity objectives fail to consistently produce meaningful physical shift-power gains, and is there a nontrivial, potentially novel, solvable DAC mechanism? No objective, order, weight, selection or historical threshold was changed to answer this question.

## 3. Recovered historical evidence

Stage A completion: 19/19 selected and 27/30 indexed architectures qualified; original/portable table checksums and projections pass. Gate09 mixed generalization is recovered at seed 11. b14 C1/C3 scan-path wire changes: +0.043699%/+0.066987%; E −0.357366%/−0.273978%; H8 −5.687626%/−5.732276%. b15 C1/C2/C3 scan-path wire: +1.336176%/+0.896204%/+1.249134%; E −1.266742%/−1.365970%/−1.011480%; H8 −1.682756%/+4.151258%/−1.340455%.

These wire percentages concern the connected scan-path net-length upper bound, including functional branches. Detailed-route total wire is separate: b14 C1 65,969 → 65,933 µm (−0.054571%); b15 C1 110,472 → 110,678 µm (+0.186473%).

For s5378, Stage-A B0 total route is 26,639 µm; qualified P0 totals are 26,655–26,717 µm, corroborating non-improvement for those P0 results. The exact earlier phase1 HPWL raw comparison was not recovered; its reported HPWL gain is not a newly verified measurement.

Gate10A's registered static-PI outcome is unchanged: worst-drop improvements 3/8 µV; no architecture meets ≥1% relative AND ≥100 µV absolute improvement in BOTH worst and p99 drop, plus guardrails. This is a static-PI criterion. No new dynamic-power materiality cutoff is invented.

'''+alltable+'''
## 4. Experimental methodology

Recover selected regular files only from existing F: archives, checking container and member SHA-256. Use a fresh output namespace. Freeze the historical Gate10A power selection before new comparisons. Recompute per-net totals and classify sources from the recovered Liberty sequential definitions and exported instance/pin identities. Independently sum per-instance power and compare to frozen totals; native cell-category aggregates are separate because they use binary32 reduction.

Existing Windows Python 3.12.5 and installed analysis packages were reused. No install, build, search, ATPG, placement, route, extraction or simulation was run. The sole optional experiment was registered before factor swaps in `07_hypothesis/followup_01_preregistration.md`. Actual resources: '''+f"{run['wall_seconds']:.3f} s wall, {run['cpu_seconds']:.3f} s CPU, {run['peak_working_set_bytes']/2**20:.2f} MiB peak working set, {run['disk_after_bytes']-run['disk_before_bytes']:,} bytes workspace growth including logs/manifest."+'''

## 5. Baseline fairness and provenance

Include all nine historical power records unchanged: b14 B3T/C1/C3/B5; b15 B2/C1/C2/C3/B5. b14 C2's adverse H8 result and every B0/B1/B2/B3T/B4/B5 result remain in the 18-row table. Missing power is blank. The subset is inherited from the prior user-frozen Gate10A population, not Gate11 outcome selection.

Fairness receipts match source netlist/FF identities/placement/coordinates, patterns, K=2, seed 11, endpoint policy, constraints, simulation models and common backend/extraction settings within design. b14: 245 FFs, chains 123/122, 453 patterns, 111,438 shift cycles. b15: 449 FFs, chains 225/224, 464 patterns, 208,800 shift cycles. The earlier invalid b14 446-pattern attempt is not reused. Coverage concerns the frozen mapped-source collapsed-fault universe, not new post-route buffer faults.

Use Nangate45 typical, 1.1 V, period 10 ns (100 MHz), clock duty50%, nonclock assumed duty0.5, scan enable asserted. Windows cover identical load/unload shifting, excluding setup/capture. No gain is attributed to fewer equivalent shift cycles.

'''+provenance+'''
B0 uses source order; B1 native placed greedy; B2 endpoint-inclusive Manhattan 2-opt (`6fff875551fe13a2aae3a22f871a6ca7f8d5c1cf`); B3T patched partitioned directed scan-pin ordering (`5c3751171685d507939ee7064a67feec786e5219`); B4 activity-disagreement greedy; B5 fixed 0.5/0.5 geometry/activity greedy. Generation commits differ from the common qualification backend.

## 6. Netlist-level activity

Exact CPU backend `icarus_vpi_settled_counts_v1` records compact uint8 net/cycle settled timestamp counts with completeness/overflow/unknown checks. Source fails unknown active nets/transitions; setup uses an unmeasured marker. Historical FF-Q crosschecks cover every physical FF/cycle against independent simultaneous chain replay. Timestamp settling is zero-delay, not glitch-accurate physical activity.

All nine exported FF-Q populations equal selected counts (245/449). Every net source maps to an instance/pin or explicit PORT source. The scan-data scope includes buffers/ports and differs from strict FF-Q counts. Raw logical/physical maps/patterns are missing, so logical-workload equivalence is receipt-supported rather than freshly replayed. Complete-count validation is a recovered historical record, not a new read of absent payloads. No new initialization, X-state or high-occupancy qualification is claimed.

'''+transfertable+'''
Implemented E sums mapped ground-plus-pin activity. Search E is a depth 3 candidate-capacitance surrogate; their absolute magnitudes are different models, not two energies. Deltas use each model's own reference. b14 C2 H8 and b15 C1/C3 H4 reversals prove transfer weakness without uniquely attributing it to depth or routing.

For the five power-covered PACT variants, implemented ΔE correlates descriptively with ΔFF-Q transitions (r0.9967), Δcombinational transitions (r0.9898) and Δdynamic estimate (r0.9844). ΔH8 does not order average-power effects consistently (r−0.7985). These five rows share two designs/references, one seed and common activity inputs; no independent-sample inference or confidence interval is justified.

## 7. Routed parasitic/power analysis

Historical receipts bind detailed-route OpenRCX SPEF/ODB, and saved logs/scripts read them. Recovered CSVs carry extracted ground, incident coupling and Liberty pin capacitance. Ground-plus-pin values reproduce all frozen E totals. Raw SPEF/ODB is absent, so this verifies export provenance/arithmetic, not a fresh extraction.

Power is embedded OpenSTA internal plus switching; leakage is separate. Instance total power feeds static PDNSim. Native Sequential/Combinational/Clock categories are observable below. The Clock category is not all clock-driven energy: sequential internal power also contains clock-driven components.

'''+powertable+'''
b14 C1's Clock category grows0.1382 µW and offsets part of sequential/combinational savings; b15 Clock falls0.3605 µW. Internal power is not αCV²f. Incident coupling sums may count each physical coupling from both incident nets; no qualified coupling-switching energy is inferred from their sum.

Analytical ground-plus-pin data switching: P=0.5×V²×E×10⁻¹⁵/T because N counts both transition directions, equivalent to α₀₁CV²f for charge events/cycle. This excludes clock/internal/coupling/hazard energy and is not a new power-tool result. Workload dynamic energy estimates P×T: b14 reference/C1 0.740401/0.738683 µJ; b15 1.881859/1.866379 µJ. Workload durations match exactly.

No matched ideal-versus-routed power comparison was recovered. No transient peak-window power/current, dynamic IR, ground bounce, thermal or signoff result is invented. Averaged counts at fixed duty cannot supply those quantities.
'''
report+='''
## 8. H1/H2/H3 results

'''+hypotheses+'''
### Registered factor accounting

'''+factortable+'''
PACT support matches 100%; B5 retains >99.89% reference E with explicit unmatched residuals. The symmetric product decomposition reproduces ΔE up to roundoff without choosing an attribution order. It does not solve nonlinear H8 maximum attribution.

### Spatial budget

'''+spatialtable+'''
Per-net/cell distributions, top 1%/10% contributions and all 4×4/8×8 bins are retained. Rank fractions are descriptive, not success thresholds. Historical maxima/p95/p99 cycle summaries are recovered; without raw cycle rows, overlap/duration of exact high-power events cannot be reconstructed.

## 9. Contradictions and failure cases

- b14 C2 search H8 improves while implemented H8 worsens; its missing power export remains blank.
- b15 C2 has the largest implemented E gain but worsens H8; C1 has the larger average-power estimate gain.
- b14 C1's same winning H8 bin has higher mean power despite lower H8.
- B5 reduces estimated dynamic power13.6192%/12.5759%, showing that the flow can register larger modeled effects, but increases scan-path wire16.7434%/14.3983%. It is not an equal-wire-budget replacement.
- All17 Gate10A attempts include three implementation/qualification failures. Invalid earlier nominal implementations are not independent scientific samples.
- New blockers/failures: WSL cannot mount its missing configured disk; optimizer verifier fails on absent Numba. Two new accounting attempts stopped on PORT naming and method/candidate schema assertions. Failed sources/logs remain; corrected analysis passes without model/selection changes. Report packaging also hit a Windows command-length limit before process creation and was split into bounded writes.

## 10. Statistical/modeling limitations

Only seed 11 has matched b14/b15 power data. No independent seed variation, significance or confidence interval is reported. Related families and one technology cannot establish industrial generalization. Identical historical nominal repeats show numerical repeatability, not calibrated physical accuracy. Native float reduction errors are checked separately from scientific materiality. Fixed duty, unavailable occupancy, state/slew approximations, missing glitches and coupling validation remain uncalibrated; observed deltas exceed arithmetic roundoff but are not shown to exceed physical-model uncertainty.

The historical static-IR threshold is preserved. No new sub1% power cutoff is imposed. NO-GO reflects absent distinct mechanism/correction/benefit under this evidence, not a theorem that every fractional-percent saving is valueless.

## 11. Scientific interpretation

Two transfer boundaries matter: the search surrogate sometimes mispredicts implemented weighted switching; then modest data-activity gains are diluted by persistent clock/internal budgets. A local maximum can improve while the same bin's mean energy rises. Capacitance creates a small inconsistent offset. This explains the recovered model without uniquely establishing real-silicon causality.

## 12. Potential novel claims

A validated permutation-to-time-resolved physical-power predictor controlling clock/internal/load/hazard effects could be a research question. No new predictor, optimizer, independent circuit intervention or held-out physical validation was demonstrated. Adding capacitance weighting (already in E) or recognizing logic switching (already in final counts) is not an achieved new contribution.

## 13. DAC relevance

`PACT_GATE11_DAC_NOVELTY.md` provides primary-source checks/access limits. Routing-aware ordering, explicit routability constraints, pattern/response correlation and induced switching have substantial prior art. This is useful negative-result/reproducibility evidence; a distinct DAC-level advance is not established. The literature review is targeted, not exhaustive.

## 14. Final decision

**NO-GO. Preserve artifacts and keep PACT optimizer development frozen.** Recovered failures are known approximation/budget/localization limitations without a demonstrated novel correction. Missing raw/runtime evidence is not positive evidence and blocks stronger causal/signoff conclusions. No new sweep, optimizer or architecture is justified.

If independent verification is later authorized, first recover exact b14 B3T/C1 routed netlists, ODB/SPEF/SDC, identity maps, qualified 453-pattern workload, stimulus, full traces and the qualified binary; verify hashes, then replay that one pair with measured duty and cycle-synchronous activity/power. Timing-aware extension is required before physical peak/glitch/dynamic-IR claims. This is a prerequisite, not an authorized optimization campaign or evidence that one pair establishes novelty.

See `PACT_GATE11_REPRODUCIBILITY.md` for artifact locations and the final storage audit for disk totals/system-level caveats.
'''
write('PACT_GATE11_PHYSICAL_POWER_CAUSALITY.md',report)
write('PACT_GATE11_DECISION.md','''# PACT Gate 11 decision

Classification: **NO-GO**

Preserve research artifacts and keep PACT optimizer development frozen. A credible distinct DAC contribution is not established.

'''+primarytable+'''
## Exact supporting evidence

1. `03_activity/predictor_implemented_transfer.csv`: b14 C2 predicted H8−9.6995% becomes implemented+4.8490%. Approximation/coverage/physical-transfer weakness is demonstrated, but no new solution.
2. `03_activity/source_class_activity.csv` and `04_power/native_power_components.csv`: real modeled scan/logic reductions remain small; clock/internal budgets persist. Retained b14 density-zero control leaves31.37% of nominal dynamic power.
3. `06_causality/followup_01_factor_accounting.csv`: capacitance helps both b14 PACT cases; b15 C1's positive capacitance term offsets7.57% of activity-only savings. Dominant common capacitance cancellation is not supported.
4. `06_causality/spatial_budget.csv`: b14 H8 improves5.6876% while the same bin's mean dynamic power rises1.0453%; local maxima are not mean total power.
5. Frozen Gate10A static-PI criteria fail. Primary dynamic differences remain fixed-duty estimates, without new timing-aware/transient/signoff measurements or a newly imposed materiality cutoff.
6. `PACT_GATE11_DAC_NOVELTY.md`: overlapping physical/routing/correlation methods exist; a distinct validated correction is absent.

## Confidence and work status

Confidence is strong for recovered-output accounting and the bounded freeze recommendation; limited for unique silicon causes/generalization. H1: Inconclusive for the specific omitted-combinational cause; prediction mismatch is observed. H2: Not Supported as dominant common cause. H3: Supported for local/peak versus mean/total mismatch. Timing-aware physical causality remains unresolved.

Completed: archive/member/retained hash checks; 12-record end-to-end verifier; all 18 activity/route rows; nine net/power reaggregations and seven available comparisons; one preregistered factor experiment; literature overlap check; reports and versioned reproduction helper.

Blocked: exact raw b14/b15 patterns/netlists/counts/SPEF, new simulation/duty occupancy, qualified OpenROAD runtime, ideal/routed rerun, physical peak and dynamic IR. WSL disk paths are missing; Numba is absent for the separate optimizer verifier. Missing evidence is never scored as positive.

Smallest prerequisite for reopening: recover/hash the exact b14 B3T/C1 workload/maps/routed inputs/traces and qualified runtime, then validate occupancy/time-resolved power for that pair under a new registration. No optimizer change is warranted beforehand. Missing bindings: `00_audit/required_binding_recovery.json`.
''')
metadata={'schema':'PACT_GATE11_RESULTS_v1','rows':18,'power_export_rows':9,'activity':'historical zero-delay settled netlist counts, newly aggregated','search':'historical depth 3 candidate-capacitance surrogate; separate from implemented E/H8','power':'historical routed Liberty fixed-duty ESTIMATE; not measured silicon','empty_numeric_fields':'missing/not applicable, never zero-imputed','class_activity':'strict source instance/pin and Liberty ff/latch classes; scan scope also contains buffers/ports','wire_fields':{'routed_scan_path_um':'connected scan path upper bound including functional branches','total_route_wire_um':'detailed-route total wirelength'},'shift_energy':'analytical P*T, identical duration; not independent measurement','missing_raw_bindings':'../00_audit/required_binding_recovery.json','independent_samples':False,'provenance':'comparison/receipt/export paths and SHA256 columns; full member hashes in 00_audit'}
(O/'PACT_GATE11_RESULTS_METADATA.json').write_text(json.dumps(metadata,indent=2))
(R/'05_parasitics/README.md').write_text('''# Parasitic evidence boundary

Original receipts bind detailed-route OpenRCX SPEF/ODB for nine architectures. Raw files are missing. Frozen net_activity_capacitance.csv exports contain ground_ff, incident_coupling_ff, pin_ff, ground_pin_ff with EXTRACTED status. Gate11 recomputes C*N and factor identities, without inferred replacement parasitics. Exact Nangate45 typical Liberty/RC files were hash-verified. Coupling is excluded from primary E; incident sums are not a physical coupling total. No extraction or ideal-versus-routed power comparison was run.
''')
write('PACT_GATE11_REPRODUCIBILITY.md',r'''# PACT Gate 11 reproducibility package

Root: `F:\Research\PACT\Gate11\`.

## Reports and audit

- `08_reports/PACT_GATE11_PHYSICAL_POWER_CAUSALITY.md`
- `08_reports/PACT_GATE11_RESULTS.csv` and `PACT_GATE11_RESULTS_METADATA.json`
- `08_reports/PACT_GATE11_CAUSAL_FINDINGS.md`
- `08_reports/PACT_GATE11_DAC_NOVELTY.md`
- `08_reports/PACT_GATE11_DECISION.md`
- `08_reports/PACT_GATE11_CAUSAL_SUMMARY.png` and `.pdf`
- `00_audit/PACT_GATE11_INPUT_AUDIT.md`, storage audits and `PACKAGE_SHA256SUMS.json`

## Source/input identities and dependencies

`00_audit/selected_inputs_manifest.json` binds original path, archive/member, size and SHA256. Additional recoveries: `additional_extraction_receipts.json`; container hashes: `extraction_receipts.json`; missing/alternate matching: `required_binding_recovery.json`. `archived_source_git_audit_G005.json` and the scientific report distinguish source snapshot/Gate09/Gate10/tool commits. Historical scientific receipts remain byte-identical under `01_inputs/S008/PACT/reports/gate10a/`.

Current runtime: existing `D:\Python\python.exe` 3.12.5, NumPy2.1.3 and Matplotlib3.9.2. Exact executable hashes/package metadata: `00_audit/current_tool_audit.json`. Existing zstd1.5.5 streamed archives. No environment/dependency installation. Qualified EDA identities/Liberty hash are in the scientific report and recovered tool provenance. WSL EDA is blocked; native Icarus availability does not prove qualified experiment reproduction.

## Executed commands/environment

All scientific analysis uses this environment wrapper and prospective manifest:

```powershell
& 'F:\Research\PACT\Gate11\09_scripts\environment.ps1' `
  -Script 'F:\Research\PACT\Gate11\09_scripts\run_manifest.py' `
  -ScriptArgs @('UNIQUE_RUN_NAME','D:\Python\python.exe','-B','F:\Research\PACT\Gate11\09_scripts\SCRIPT.py')
```

`10_logs/*.manifest.json` records exact argv, cwd, source hashes, environment, UTC start/completion, wall/CPU time, peak working set and disk increment. stdout/stderr is beside each manifest. Original failed attempts/sources and WSL failure logs remain. `historical_Gate10A_all_attempts.csv` is the entire17-attempt historical table, not new execution. Discovery/inventory/initial recovery have retrospective command/source/receipt records without fabricated prospective timestamps.

Ordered stages: `inventory.py`, `recover_inputs.py`, `freeze_and_bindings.py`, `recover_extra.py`; original end-to-end verifier; `analyze_frozen_outputs.py`; sole registered `followup_01_factor_accounting.py`; `derive_diagnostics.py`; `enrich_predicted_transfer.py`; `tool_audit.py`; `write_reports.py`; final package validation. First two parser sources/logs are preserved. Original numerical optimizer verifier fails on Numba; no replacement is called equivalent.

## Safe rerun

Run `09_scripts/reproduce_analysis.py` through `environment.ps1` with the existing Python. It creates a fresh timestamped child under `02_reproduction/`, reuses staged inputs read-only, copies analysis scripts/protocol only, redirects every controllable cache/temp path into the child, records original/transformed source hashes and runs the frozen accounting pipeline. It refuses overlays and compares scientific numeric columns to the delivered table. Root/input path substitutions are explicit in its manifest; original executed sources remain preserved. It does not install, search, ATPG, route, extract or simulate. This is a delivered future rerun helper, not an additional optional experiment already executed.

Complete physical reproduction is blocked by80 missing raw/tool bindings and the missing qualified runtime. First restore the exact b14 B3T/C1 pair as described in the decision. Timing-aware modeling is a new registered extension, not a substitute for zero-delay history.

## Machine artifact locations

- `02_reproduction/frozen_comparisons.json`: frozen population/fairness.
- `03_activity/`: classified nets, source-class activity, predictor/implemented transfer.
- `04_power/native_power_components.csv`: Sequential/Combinational/Clock internal/switching/leakage.
- `05_parasitics/README.md`: availability boundary; C exports also in `03_activity/per_net_classified.csv` and frozen input CSVs.
- `06_causality/`: seven factor comparisons, complete spatial/concentration/source budgets, base/enriched/diagnostic JSON.
- `07_hypothesis/followup_01_preregistration.md`: single optional experiment's falsifiable protocol.
- `10_logs/`: all launched command/resource manifests, failures and verifier outputs.

## Storage compliance

All intentionally generated experiments/reports/scripts/logs/caches/temp data are on F: inside Gate11. Originals were read-only; unrelated files were not deleted/moved. Exact logical/allocated file bytes and scope: `00_audit/storage_audit_final.json`. Codex/OS service logs, paging and host bookkeeping cannot be forced entirely onto F:, so no absolute system-wide claim is made. WSL failed before Linux on missing preconfigured F: disk/swap paths. No working Linux /tmp/home experimental writes occurred.
''')
for r in primary: print('DIMENSIONS',r['design'],r['patterns'],r['shift_cycles'],r['chain_lengths'])
print('Wrote report package',len(list(O.iterdir())))

