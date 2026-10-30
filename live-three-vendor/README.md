# Three vendors training one model (Appendix: cross-vendor live training)

- `live/`: the live run. An Apple M4, an NVIDIA H100 and an AMD MI300X, each in its own machine, trained one decoder
  (2 blocks, width 32, 512-token vocabulary, 51,328 parameters) for 6 steps with four microbatches per step.
  `rows.json` holds each worker's full training-state SHA-256 after every step; `coordinator.log` and
  `apple-worker.log` are the coordinator's and the Apple worker's logs; the gate files record the NVIDIA and AMD
  workers' environment checks.
- `single-process-and-replay/`: the same model in one process on one M4, one H100, two H100 and one MI300X; the
  step-3 checkpoints written on two H100 GPUs and on the MI300X, resumed on the M4; and the four gradient-capture
  records used for the 1,512 offline mixed-source gradient-fold checks.
