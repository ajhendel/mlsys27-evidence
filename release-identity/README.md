# Release 0.8.55 verification (anonymized for review)

The library's installed verifier was run on the published 0.8.55 release wheels, installed from the package index
with no source build, on six targets. Each run writes one evidence document per profile. Library and author names,
local paths and machine addresses are replaced in these copies for double-blind review.

| Column | Device | Route |
|---|---|---|
| apple | Apple M4 GPU | Metal |
| nvidia | NVIDIA L40S, compute capability 8.9 | native CUDA (sm_89) |
| ptx | NVIDIA RTX A6000, compute capability 8.6 | the release's PTX build (sm_80) |
| amd | AMD Instinct MI300X (gfx942) | HIP |
| armcpu | Apple M4 CPU (Arm64), selected with the library's CPU switch | CPU |
| x86cpu | AMD EPYC x86-64 CPU, selected with the library's CPU switch | CPU |

## Profiles

- `evidence/verify_all-<column>.json.gz`: the routine profile, 449 lanes on nine fixtures (3,546 cells).
- `evidence/verify_neural_training-<column>.json.gz`: neural training, backward and optimizer fixtures (68 lanes).
- `evidence/x86cpu-*.json.gz`: the x86 CPU run, as seven routine lane groups plus the neural-training profile
  (cell results do not depend on how cells are grouped). Each group repeats the same 116 portable parts, so the
  per-group comparison reports in `comparisons/` sum to 11,999 recorded matches; the unique count is 11,303.

## Direct comparisons (`comparisons/`, `verify --compare A B`)

| Pair | Routine profile, cell parts | Neural training, cell parts |
|---|---|---|
| nvidia vs amd | 15,362 agree, 0 differ | 2,349 agree, 0 differ |
| nvidia vs apple | 15,362 agree, 0 differ | 2,349 agree, 0 differ |
| nvidia vs ptx | 15,362 agree, 0 differ | 2,349 agree, 0 differ |
| nvidia vs armcpu | 11,375 agree, 0 differ | 2,349 agree, 0 differ |
| nvidia vs x86cpu | 11,303 agree, 0 differ (unique parts) | 2,349 agree, 0 differ |
| armcpu vs x86cpu | 11,303 agree, 0 differ (unique parts) | 2,349 agree, 0 differ |

## Reference table

`reference-0.8.55.1/` holds the corrected reference table. It refreshes 36 entries in three optimizer lanes that
were outdated in the table shipped with 0.8.55; every other entry is unchanged. Against it, every reference-checked
part in these documents matches: 13,743 on each GPU target and 13,608 on the Arm CPU.

## CPU coverage

The CPU documents contain fewer parts than the GPU documents because some checks exist only on a GPU, such as
GPU-against-CPU inference, and two ranking lanes have no CPU route. Of the 11,438 GPU-verified parts that have a
CPU route, the Arm CPU verifies 11,375. The remainder are two weighted extra-trees lanes with no CPU reference
entry, and a stratified group splitter that the 0.8.55 CPU build refuses (reported as REFUSED, never as a match).
On x86, two approximate nearest-neighbor lanes (IVF-PQ and filtered ANN) stop their CPU worker in 0.8.55; they
verify on the Arm CPU and on every GPU, and the two affected x86 groups were run without them.

These runs did not use the verifier's challenge option, so the comparisons show that the documents agree.
