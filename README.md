# Supplementary evidence: release 0.8.55 (anonymized for review)

Everything here was produced from the published 0.8.55 release wheels, installed from the package index, with no
source build. Library and author names, paths and machine addresses are replaced for double-blind review.
Some parts use earlier versions, as the paper states: the NVIDIA two-GPU verification (release 0.8.10), the AMD two-GPU records (version 0.8.5), the GPT-3 Small-shaped scale run (releases 0.8.15 to 0.8.24), and the live three-vendor training and custom-model records. Measurement boards reference per-race raw archives (logs and outputs) by content hash; those archives are retained and released with the camera-ready version.

| Folder | What it holds |
|---|---|
| `release-identity/` | Bitwise verification on six targets: Apple M4 GPU (Metal), NVIDIA L40S (native CUDA), NVIDIA RTX A6000 (the PTX build), AMD MI300X (HIP), Apple M4 Arm CPU, AMD EPYC x86-64 CPU. Evidence documents per target and profile, and every direct comparison. See its README. |
| `two-gpu-0.8.10/` | The one-GPU versus two-GPU verification cited in the paper: release 0.8.10 from the package index on two NVIDIA RTX 4090, the self-test that shows the check can fail, and every lane over all nine fixtures, with each session's logs and the summary. |
| `two-gpu-amd-0.8.5/` | The AMD two-GPU records cited in the paper, at the 0.8.5 source: two AMD MI300X running the two-GPU configurations, compared cell for cell with single-GPU Apple, NVIDIA and AMD columns (and two NVIDIA H100 for the second set). |
| `gpt3-six-segment/` | The GPT-3 Small-shaped six-segment training run (releases 0.8.15 to 0.8.24): per-segment step records, receipts and checkpoint digests for both routes, including segments trained on two NVIDIA H100 and on two AMD MI300X, the live H100 and MI325X segment, and the evidence checker's report. See ANONYMIZED_COPY.md. |
| `live-three-vendor/` | Apple M4, NVIDIA H100 and AMD MI300X training one small decoder together, with per-step state hashes, plus the single-process runs, checkpoint resumes and gradient-capture records behind the offline replay checks. |
| `byte-lm/` | The byte-level language model's records: 128 steps on Apple, NVIDIA and AMD, resume across vendors in both directions, and CPU recomputation on seven CPUs. |
| `custom-models/` | Custom and imported models with matching trained-parameter and prediction digests on Apple, NVIDIA and AMD. |
| `MANIFEST.sha256` | SHA-256 of every file in this folder. |
| `measurements/` | Speed and quality boards on NVIDIA L40S and AMD MI300X: neural, classical, tree and gradient-boosting lanes, every opponent re-run in the same session on its fastest supported path, with matched parameters. `paper-tables/` holds the two boards the paper's tables are generated from (the AMD board includes the ROCm 7 opponent races; two lossguide races were re-scored under corrected tooling by the included script, old verdicts kept in their audit history). `FAIRNESS_AUDIT.md` lists, for every race and opponent, the parameter check, the clock compared, the ratio and the quality verdict. |
