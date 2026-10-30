# Two-GPU records at version 0.8.5 (AMD 2x MI300X, NVIDIA 2x H100)

These records run the library's two-GPU configurations on two GPUs in one process and compare every cell with
the same configuration's one-GPU values recorded on Apple M4, NVIDIA and AMD single GPUs.

- `2026-09-14_136-lanes/`: two AMD Instinct MI300X (gfx942) and two NVIDIA H100 (sm_90a), each column as one
  JSON document, with the one-GPU columns and the per-cell comparison tables (`diff.*.txt`).
- `2026-09-15_par-lanes-new/`: eight further two-GPU configurations on two MI300X and on two H100; every
  training, inference, model and batch part is IDENTICAL to the one-GPU values (72 training parts per column).
