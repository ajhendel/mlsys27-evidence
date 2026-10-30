# Two GPUs against one, release 0.8.10 (NVIDIA, 2x GeForce RTX 4090)

The verifier was run from the published 0.8.10 wheel, installed from the package index into a fresh environment
outside any source checkout: `python -m anonlib verify --par`. Each two-GPU configuration runs once on one GPU
and once across two GPUs in the same process, and the two results are compared cell for cell. Every cell must
show two distinct physical GPUs by UUID, or it is refused rather than counted.

| Command | Result |
|---|---|
| `verify --par --par-self-test` | passed: a one-ULP change in the two-GPU input reads as DIVERGENT |
| `verify --par quick` | VERIFIED: 14 configurations, base fixture, 51 compared parts IDENTICAL, 0 DIVERGENT |
| `verify --par all`, all nine fixtures | 531 cells, 1,935 matching numerical parts (1,908 witnessed on two GPUs), 0 DIVERGENT |

The full sweep recorded 1,935 matching numerical parts and no divergence. Of these, 1,908 parts in 56
configurations have accepted two-device witnesses. The other 27 parts, in three byte-level language-model
configurations, matched numerically but their two-GPU column did not show a second device, so the verifier
refused those cells as unwitnessed and the affected commands are incomplete rather than verified.

`nvidia-2x-rtx4090/SUMMARY.txt` has the per-configuration table with every command's exit code and time. Each
`lease*/` folder is one machine session: the exact command script (`body.sh`), the installed packages, the GPU
inventory, and every command's log and report.
