# Byte-level language model, step by step (Appendix A.5)

A two-block decoder with 34,944 parameters trained on pinned real text. Each file is the retained summary record of
one experiment, with its provenance block:

- `byte-lm-three-vendor-continuous-2026-09-07.json`: 128 training steps on Apple, NVIDIA and AMD GPUs; every recorded
  array of every step (parameters, gradients, AdamW moments, losses, held-out outputs, checkpoint bytes) matches.
- `byte-lm-expanded-continuous-2026-09-07.json`: the expanded continuous comparison.
- `byte-lm-two-vendor-resume-2026-09-06.json`: the step-64 checkpoint resumed on the other vendor in both directions,
  rejoining the uninterrupted run.
- `byte-lm-cpu-training-2026-09-12.json`: seven CPUs with no GPU present, each given one step's recorded state,
  recompute gradients, losses, parameters and moments equal to the GPU record.
- `byte-lm-cpu-inference-2026-09-11.json`: CPU inference on the trained model compared with the GPU record.
