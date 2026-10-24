# PACT Gate 11 — DAC novelty assessment

A distinct DAC research contribution is **not established**. Gate11 demonstrates reproducible accounting of a weak/negative transfer result under one frozen open-source flow.


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
