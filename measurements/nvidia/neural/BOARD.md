# anonlib benchmark board

Generated 2026-10-30T06:56:54Z from `board.json` (schema `anonlib-bench-board/1`).

## Box

| field | value |
|---|---|
| vendor / API | nvidia / cuda |
| GPU | NVIDIA L40S |
| GPU driver | 595.91.07 |
| CPU | AMD EPYC 9374F 32-Core Processor (128 logical cores) |
| memory bytes | 1623028502528 |
| OS | Ubuntu 22.04.5 LTS |
| Python | 3.11.10 CPython |
| anonlib | 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl, sha256 ca912ce50c59efaeffd64d7b195215d4ea48c67e00c9dabd619475a6be4c1170) |
| script commit | 79fd411391c5b48137c48217b27b06ecef72f45d |
| patch sync | - |
| modes | identical |
| rounds | 1 timed after 1 warm-up, arms interleaved round by round |
| seed | 7 |
| opponent versions | catboost 1.2.10, xgboost 3.2.0, lightgbm 4.7.0, scikit-learn 1.7.2, cuml-cu12 26.8.0, cuvs-cu12 26.8.1, torch 2.13.0+cu129, numba 0.64.0, statsmodels 0.15.0, numpy 2.4.6 |

## How to read this board

- Times are wall milliseconds of the public fit call (trees) or the lane's timed call (classical), median of the timed rounds; min..max beside it.
- `ours IDENTICAL / arm` is our IDENTICAL median divided by that opponent's median; `ours FAST / arm` likewise. Below 1.0 our median time is the lower one, above 1.0 the higher one. A ratio is shown only when both arms completed every round in this run, and only against an opponent: our two modes are never divided by each other here.
- Two clocks (AGENTS.md measurement item 6): `whole ms` is the operation including the host-to-device copy of its inputs, `kernel ms` the same with the inputs already on the device; `copy ms` comes only from a stored field, named beside it (`upload_ms_separate`: our separate upload probe, kernel = median - copy; `upload_ms_untimed`: an opponent's pre-clock upload, whole = median + copy; `cpu-arm`: no device copy exists). A clock the stored fields cannot give is `-`, never estimated. `ours IDENTICAL / arm (clock)` reads a torch GPU arm on kernel/kernel and every other arm on whole/whole; when that clock is missing on a side it falls back to the other common clock (labelled), and with no common clock it is the two stored medians labelled MIXED with each side's clock.
- Quality comes from the drivers: FSPEED-ACC for trees (held-out rows), one float64 NumPy function per lane for classical.
- Comparability: trees carry FSPEED-FIT-VERDICT (total leaves within 10% across arms is COMPARABLE); classical carry the clock span (SPAN-ASYMMETRIC names an arm whose clock excludes an upload or a fit that ours includes).
- Classical, wave 2 (`classical2`, tools/bench_board_more.py): the same worker protocol as classical; every lane's parameters, rows, timed span and each unavoidable mismatch with its reason are in the cells' `settings.lane_config`. Quality is one float64 NumPy function per lane over each arm's saved outputs.
- Neural: our IDENTICAL arm only (the neural surface builds no other tier, on any vendor) against torch at every fast setting it supports on this box, one arm each, the setting in the arm name: `torch-eager-fp32` (TF32 off), `torch-compile-fp32` (torch.compile, inductor), `torch-eager-tf32` / `torch-compile-tf32` (NVIDIA CUDA only), `torch-eager-bf16` / `torch-compile-bf16` (bf16 autocast mixed precision). TF32 and bf16 arms are ANOTHER PRECISION than ours; their quality columns show how far. An arm torch cannot run on this box is REFUSED by name in its cell. Every clock is host in, host out, synchronized. Every arm starts from the same parameters and reads the same inputs, so losses and outputs are comparable; `max_abs_diff_vs_ours` / `max_rel_diff_vs_ours` are the arm's output against ours. The torch models are library classes: transformers' LlamaForCausalLM / LlamaDecoderLayer for the LM and transformer lanes, mamba_ssm's Mamba3 blocks with transformers' attention layers for Samba; the Mamba lanes' opponent is mamba_ssm's own fused kernels (`mamba-ssm-fp32`, and `mamba-ssm-tf32` on NVIDIA), and their pure-PyTorch reference torch arms are REFUSED by name. A compile arm compiles in its untimed warm-up (`compile_warmup_ms`).
- `installed_wheel` confirms our binding loaded from site-packages, not the repo tree.
- Our CPU is never raced or reported: the board races only our GPU, against GPU opponents; a race keeps CPU opponents only when it has no GPU opponent (the author, Oct 2 2026). A cell of ours on the CPU in an old record is dropped before rendering.
- Memory: `peak host MB` and `peak GPU MB` are the highest per-round peaks over the timed rounds, read outside the clock; each arm's method is listed under its table (host: the resettable peak RSS on Linux, the peak physical footprint on macOS, which holds Metal buffers too; GPU: torch's own counter for torch arms, the driver's per-process figure for the rest, none on Apple).
- Inference: after a race's fit rounds each arm predicts with its own fitted model (no fit retimed), same rows, same output kind, one warm-up then the timed rounds interleaved. Trees: batch `test` (the held-out split) and `large` (1,000,000 training rows, capped at the training rows), host rows in and host predictions out on every arm; each arm's call is printed under its table. Classical: kmeans predict, pca transform, ols predict and svc predict on the eval rows, with the fit's clock span. Ratios are per batch, ours over each opponent.

## Coverage

Races: 19 planned, 19 done, 0 failed, 0 unsupported, 0 pending. Cells: 121 (REFUSED 21, ok 100).

## Quality at a glance

Per lane and dataset: our FAST value, our IDENTICAL value, and each opponent's.

| family | lane | dataset | metric | ours FAST | ours IDENTICAL | opponents |
|---|---|---|---|---|---|---|
| neural | gemm-bf16 | gaussian | max_rel_err_vs_fp64 (lower is better) | - | 1.155e-07 | torch-eager-bf16 0.002764; torch-compile-bf16 0.002764 |
| neural | gemm-bf16 | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-bf16 1.000977; torch-compile-bf16 1.000977 |
| neural | gemm-bf16 | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-bf16 0.002764; torch-compile-bf16 0.002764 |
| neural | gemm-int8 | gaussian | max_rel_err_vs_fp64 (lower is better) | - | 0.000000 | torch-eager-int8 0.000000; torch-compile-int8 0.000000 |
| neural | gemm-int8 | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-int8 0.000000; torch-compile-int8 0.000000 |
| neural | gemm-int8 | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-int8 0.000000; torch-compile-int8 0.000000 |
| neural | gemm | gaussian | max_rel_err_vs_fp64 (lower is better) | - | 2.399e-07 | torch-eager-fp32 1.401e-06; torch-eager-tf32 0.0002784; torch-compile-fp32 1.401e-06; torch-compile-tf32 0.0002784; torch-eager-bf16 0.003752; torch-compile-bf16 0.003752 |
| neural | gemm | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 0.0005341; torch-eager-tf32 0.100822; torch-compile-fp32 0.0005341; torch-compile-tf32 0.100822; torch-eager-bf16 1.358337; torch-compile-bf16 1.358337 |
| neural | gemm | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.475e-06; torch-eager-tf32 0.0002785; torch-compile-fp32 1.475e-06; torch-compile-tf32 0.0002785; torch-eager-bf16 0.003751; torch-compile-bf16 0.003751 |
| neural | lm-forward | bytes | mean_nll (lower is better) | - | 9.015586 | torch-eager-fp32 9.015586; torch-eager-tf32 9.015582; torch-compile-fp32 9.015586; torch-compile-tf32 9.015581; torch-eager-bf16 9.015491; torch-compile-bf16 9.015490; torch-graph-fp32 9.015586; torch-graph-tf32 9.015582 |
| neural | lm-forward | bytes | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.371e-06; torch-eager-tf32 0.000755; torch-compile-fp32 1.326e-06; torch-compile-tf32 0.0007218; torch-eager-bf16 0.006870; torch-compile-bf16 0.006485; torch-graph-fp32 1.371e-06; torch-graph-tf32 0.000755 |
| neural | lm-forward | bytes | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.882e-06; torch-eager-tf32 0.001037; torch-compile-fp32 1.821e-06; torch-compile-tf32 0.0009909; torch-eager-bf16 0.009431; torch-compile-bf16 0.008903; torch-graph-fp32 1.882e-06; torch-graph-tf32 0.001037 |
| neural | lm-train-step | bytes | loss_first_step (same init and batches on every arm) | - | 9.015587 | torch-eager-fp32 9.015587; torch-eager-tf32 9.015582; torch-compile-fp32 9.015587; torch-compile-tf32 9.015580; torch-eager-bf16 9.015491; torch-compile-bf16 9.015490 |
| neural | lm-train-step | bytes | loss_last_step (same init and batches on every arm) | - | 8.405828 | torch-eager-fp32 8.405829; torch-eager-tf32 8.406206; torch-compile-fp32 8.405828; torch-compile-tf32 8.406154; torch-eager-bf16 8.405970; torch-compile-bf16 8.404997 |
| neural | lm-train-step | bytes | steps | - | 2 | torch-eager-fp32 2; torch-eager-tf32 2; torch-compile-fp32 2; torch-compile-tf32 2; torch-eager-bf16 2; torch-compile-bf16 2 |
| neural | lm-train-step | bytes | loss_first_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 0.000000; torch-eager-tf32 4.768e-06; torch-compile-fp32 0.000000; torch-compile-tf32 6.676e-06; torch-eager-bf16 9.537e-05; torch-compile-bf16 9.727e-05 |
| neural | lm-train-step | bytes | loss_last_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 1.907e-06; torch-eager-tf32 0.0003786; torch-compile-fp32 9.537e-07; torch-compile-tf32 0.0003262; torch-eager-bf16 0.0001421; torch-compile-bf16 0.0008307 |
| neural | mamba1-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba1-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba1-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba1-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba1-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba1-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.0001944 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 0.0001588; mamba-ssm-tf32 0.175704 |
| neural | mamba1-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 6.377e-09 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 5.039e-09; mamba-ssm-tf32 6.398e-07 |
| neural | mamba1-forward | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 1.192e-07; mamba-ssm-tf32 3.815e-06 |
| neural | mamba1-forward | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; mamba-ssm-fp32 5.945e-08; mamba-ssm-tf32 1.902e-06 |
| neural | mamba2-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba2-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba2-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba2-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba2-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba2-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.236111 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 0.020408; mamba-ssm-tf32 24.892473 |
| neural | mamba2-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 1.497e-07 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 8.531e-08; mamba-ssm-tf32 9.072e-05 |
| neural | mamba2-forward | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 1.669e-06; mamba-ssm-tf32 0.0005126 |
| neural | mamba2-forward | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 5.674e-07; mamba-ssm-tf32 0.0001743 |
| neural | mamba3-decode | gaussian | host_reference_atol | - | 1e-06 | - |
| neural | mamba3-decode | gaussian | host_reference_rtol | - | 1e-05 | - |
| neural | mamba3-decode | gaussian | host_reference_tolerance_ratio | - | 0.000000 | - |
| neural | mamba3-decode | gaussian | max_abs_diff_vs_host | - | 0.000000 | - |
| neural | mamba3-decode | gaussian | max_rel_diff_vs_host | - | 0.000000 | - |
| neural | mamba3-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba3-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba3-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba3-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba3-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 -; mamba-ssm-tf32 - |
| neural | mamba3-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.009235 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 129.116095; mamba-ssm-tf32 119.090758 |
| neural | mamba3-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 5.551e-08 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 0.0001981; mamba-ssm-tf32 0.0001993 |
| neural | mamba3-forward | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 0.001235; mamba-ssm-tf32 0.001290 |
| neural | mamba3-forward | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 0.0005401; mamba-ssm-tf32 0.0005645 |
| neural | mlp-train-step | gaussian | loss_first_step (same init and batches on every arm) | - | 1.160401 | torch-eager-fp32 1.160401; torch-eager-tf32 1.160392; torch-compile-fp32 1.160401; torch-compile-tf32 1.160392; torch-eager-bf16 1.160498; torch-compile-bf16 1.160498 |
| neural | mlp-train-step | gaussian | loss_last_step (same init and batches on every arm) | - | 1.123361 | torch-eager-fp32 1.123361; torch-eager-tf32 1.123355; torch-compile-fp32 1.123361; torch-compile-tf32 1.123355; torch-eager-bf16 1.123461; torch-compile-bf16 1.123462 |
| neural | mlp-train-step | gaussian | steps | - | 2 | torch-eager-fp32 2; torch-eager-tf32 2; torch-compile-fp32 2; torch-compile-tf32 2; torch-eager-bf16 2; torch-compile-bf16 2 |
| neural | mlp-train-step | gaussian | loss_first_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 2.384e-07; torch-eager-tf32 8.941e-06; torch-compile-fp32 2.384e-07; torch-compile-tf32 8.941e-06; torch-eager-bf16 9.656e-05; torch-compile-bf16 9.656e-05 |
| neural | mlp-train-step | gaussian | loss_last_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 2.384e-07; torch-eager-tf32 5.484e-06; torch-compile-fp32 2.384e-07; torch-compile-tf32 5.603e-06; torch-eager-bf16 0.0001006; torch-compile-bf16 0.0001007 |
| neural | ops-session-step | gaussian | loss | - | 2.798163 | torch-eager-fp32 2.798162; torch-eager-tf32 2.798163; torch-compile-fp32 2.798162; torch-compile-tf32 2.798162; torch-eager-bf16 2.798156; torch-compile-bf16 2.798156 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_b1 | - | - | torch-eager-fp32 5.821e-10; torch-eager-tf32 1.619e-05; torch-compile-fp32 5.821e-10; torch-compile-tf32 1.619e-05; torch-eager-bf16 5.06e-05; torch-compile-bf16 5.06e-05 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_b2 | - | - | torch-eager-fp32 2.794e-09; torch-eager-tf32 4.443e-06; torch-compile-fp32 3.725e-09; torch-compile-tf32 4.441e-06; torch-eager-bf16 3.965e-05; torch-compile-bf16 3.965e-05 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_w1 | - | - | torch-eager-fp32 2.794e-09; torch-eager-tf32 4.365e-05; torch-compile-fp32 2.736e-09; torch-compile-tf32 4.365e-05; torch-eager-bf16 7.59e-05; torch-compile-bf16 7.59e-05 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_w2 | - | - | torch-eager-fp32 4.191e-09; torch-eager-tf32 2.888e-06; torch-compile-fp32 4.191e-09; torch-compile-tf32 2.888e-06; torch-eager-bf16 3.952e-05; torch-compile-bf16 3.952e-05 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_b1 | - | - | torch-eager-fp32 3.833e-07; torch-eager-tf32 0.010665; torch-compile-fp32 3.833e-07; torch-compile-tf32 0.010665; torch-eager-bf16 0.033320; torch-compile-bf16 0.033320 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_b2 | - | - | torch-eager-fp32 1.329e-07; torch-eager-tf32 0.0002114; torch-compile-fp32 1.773e-07; torch-compile-tf32 0.0002113; torch-eager-bf16 0.001887; torch-compile-bf16 0.001887 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_w1 | - | - | torch-eager-fp32 2.102e-06; torch-eager-tf32 0.032848; torch-compile-fp32 2.059e-06; torch-compile-tf32 0.032848; torch-eager-bf16 0.057112; torch-compile-bf16 0.057112 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_w2 | - | - | torch-eager-fp32 4.676e-07; torch-eager-tf32 0.0003222; torch-compile-fp32 4.676e-07; torch-compile-tf32 0.0003222; torch-eager-bf16 0.004410; torch-compile-bf16 0.004410 |
| neural | ops-session-step | gaussian | loss_abs_diff_vs_ours | - | - | torch-eager-fp32 7.153e-07; torch-eager-tf32 0.000000; torch-compile-fp32 7.153e-07; torch-compile-tf32 2.384e-07; torch-eager-bf16 6.676e-06; torch-compile-bf16 6.676e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_b1 | - | - | torch-eager-fp32 1.863e-09; torch-eager-tf32 8.103e-07; torch-compile-fp32 3.638e-12; torch-compile-tf32 8.103e-07; torch-eager-bf16 2.53e-06; torch-compile-bf16 2.53e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_b2 | - | - | torch-eager-fp32 0.000000; torch-eager-tf32 2.217e-07; torch-compile-fp32 0.000000; torch-compile-tf32 2.217e-07; torch-eager-bf16 1.982e-06; torch-compile-bf16 1.982e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_w1 | - | - | torch-eager-fp32 3.725e-09; torch-eager-tf32 2.183e-06; torch-compile-fp32 3.725e-09; torch-compile-tf32 2.183e-06; torch-eager-bf16 3.795e-06; torch-compile-bf16 3.795e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_w2 | - | - | torch-eager-fp32 3.725e-09; torch-eager-tf32 1.453e-07; torch-compile-fp32 3.725e-09; torch-compile-tf32 1.453e-07; torch-eager-bf16 1.978e-06; torch-compile-bf16 1.978e-06 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_b1 | - | - | torch-eager-fp32 2.982e-08; torch-eager-tf32 1.297e-05; torch-compile-fp32 5.824e-11; torch-compile-tf32 1.297e-05; torch-eager-bf16 4.05e-05; torch-compile-bf16 4.05e-05 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_b2 | - | - | torch-eager-fp32 0.000000; torch-eager-tf32 5.8e-06; torch-compile-fp32 0.000000; torch-compile-tf32 5.8e-06; torch-eager-bf16 5.185e-05; torch-compile-bf16 5.185e-05 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_w1 | - | - | torch-eager-fp32 5.958e-08; torch-eager-tf32 3.491e-05; torch-compile-fp32 5.958e-08; torch-compile-tf32 3.491e-05; torch-eager-bf16 6.069e-05; torch-compile-bf16 6.069e-05 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_w2 | - | - | torch-eager-fp32 8.398e-08; torch-eager-tf32 3.275e-06; torch-compile-fp32 8.398e-08; torch-compile-tf32 3.275e-06; torch-eager-bf16 4.459e-05; torch-compile-bf16 4.459e-05 |
| neural | program-run | gaussian | max_abs_err_vs_fp64 | - | 7.398e-08 | torch-eager-fp32 3.219e-08; torch-eager-tf32 3.73e-05; torch-compile-fp32 3.333e-08; torch-compile-tf32 3.73e-05; torch-eager-bf16 0.0004913; torch-compile-bf16 0.0004913 |
| neural | program-run | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 8.941e-08; torch-eager-tf32 3.727e-05; torch-compile-fp32 7.451e-08; torch-compile-tf32 3.727e-05; torch-eager-bf16 0.0004913; torch-compile-bf16 0.0004913 |
| neural | program-run | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 5.226e-07; torch-eager-tf32 0.0002178; torch-compile-fp32 4.355e-07; torch-compile-tf32 0.0002178; torch-eager-bf16 0.002871; torch-compile-bf16 0.002871 |
| neural | samba-decode | bytes | mean_nll (lower is better) | - | 5.640151 | - |
| neural | samba-forward | bytes | mean_nll (lower is better) | - | 5.640151 | torch-eager-fp32 5.640315; torch-eager-tf32 5.640322; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 5.640346; torch-compile-bf16 -; torch-graph-fp32 5.640305; torch-graph-tf32 5.640320 |
| neural | samba-forward | bytes | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 0.011567; torch-eager-tf32 0.010282; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 0.015470; torch-compile-bf16 -; torch-graph-fp32 0.010900; torch-graph-tf32 0.009999 |
| neural | samba-forward | bytes | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 0.007038; torch-eager-tf32 0.006256; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 0.009412; torch-compile-bf16 -; torch-graph-fp32 0.006632; torch-graph-tf32 0.006084 |
| neural | samba-train-step | bytes | loss_first_step (same init and batches on every arm) | - | 5.640152 | torch-eager-fp32 5.640307; torch-eager-tf32 5.640319; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 5.640351; torch-compile-bf16 - |
| neural | samba-train-step | bytes | loss_last_step (same init and batches on every arm) | - | 4.822321 | torch-eager-fp32 4.822999; torch-eager-tf32 4.822763; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 4.822189; torch-compile-bf16 - |
| neural | samba-train-step | bytes | steps | - | 2 | torch-eager-fp32 2; torch-eager-tf32 2; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 2; torch-compile-bf16 - |
| neural | samba-train-step | bytes | loss_first_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 0.000155; torch-eager-tf32 0.0001669; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 0.0001993; torch-compile-bf16 - |
| neural | samba-train-step | bytes | loss_last_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 0.0006776; torch-eager-tf32 0.0004425; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 0.0001316; torch-compile-bf16 - |
| neural | sequential-fit | synthetic | accuracy (higher is better) | - | 0.899070 | torch-eager-fp32 0.898660; torch-eager-tf32 0.898470; torch-compile-fp32 0.898790; torch-compile-tf32 0.898420; torch-eager-bf16 0.898620; torch-compile-bf16 0.898400 |
| neural | sequential-fit | synthetic | auc (higher is better) | - | 0.968973 | torch-eager-fp32 0.968843; torch-eager-tf32 0.968846; torch-compile-fp32 0.968810; torch-compile-tf32 0.968805; torch-eager-bf16 0.968818; torch-compile-bf16 0.968846 |
| neural | sequential-fit | synthetic | held_out_rows | - | 100000 | torch-eager-fp32 100000; torch-eager-tf32 100000; torch-compile-fp32 100000; torch-compile-tf32 100000; torch-eager-bf16 100000; torch-compile-bf16 100000 |
| neural | sequential-fit | synthetic | log_loss | - | 0.225010 | torch-eager-fp32 0.225338; torch-eager-tf32 0.225332; torch-compile-fp32 0.225476; torch-compile-tf32 0.225478; torch-eager-bf16 0.225426; torch-compile-bf16 0.225339 |
| neural | sequential-fit | synthetic | loss_curve_length | - | 1 | torch-eager-fp32 1954; torch-eager-tf32 1954; torch-compile-fp32 1954; torch-compile-tf32 1954; torch-eager-bf16 1954; torch-compile-bf16 1954 |
| neural | sequential-fit | synthetic | train_loss_last_step | - | 0.240776 | torch-eager-fp32 0.143858; torch-eager-tf32 0.143500; torch-compile-fp32 0.145113; torch-compile-tf32 0.144524; torch-eager-bf16 0.144841; torch-compile-bf16 0.144898 |
| neural | sequential-fit | synthetic | accuracy_diff_vs_ours | - | - | torch-eager-fp32 -0.00041; torch-eager-tf32 -0.0006; torch-compile-fp32 -0.00028; torch-compile-tf32 -0.00065; torch-eager-bf16 -0.00045; torch-compile-bf16 -0.00067 |
| neural | sequential-fit | synthetic | auc_diff_vs_ours | - | - | torch-eager-fp32 -0.0001299; torch-eager-tf32 -0.0001274; torch-compile-fp32 -0.0001632; torch-compile-tf32 -0.0001686; torch-eager-bf16 -0.0001549; torch-compile-bf16 -0.0001273 |
| neural | sequential-fit | synthetic | log_loss_diff_vs_ours | - | - | torch-eager-fp32 0.0003281; torch-eager-tf32 0.0003221; torch-compile-fp32 0.0004662; torch-compile-tf32 0.0004687; torch-eager-bf16 0.0004158; torch-compile-bf16 0.0003289 |
| neural | sequential-predict | synthetic | accuracy (higher is better) | - | 0.899070 | torch-eager-fp32 0.898660; torch-eager-tf32 0.898470; torch-compile-fp32 0.898710; torch-compile-tf32 0.898570; torch-eager-bf16 0.898620; torch-compile-bf16 0.898460 |
| neural | sequential-predict | synthetic | auc (higher is better) | - | 0.968973 | torch-eager-fp32 0.968843; torch-eager-tf32 0.968846; torch-compile-fp32 0.968813; torch-compile-tf32 0.968837; torch-eager-bf16 0.968818; torch-compile-bf16 0.968821 |
| neural | sequential-predict | synthetic | held_out_rows | - | 100000 | torch-eager-fp32 100000; torch-eager-tf32 100000; torch-compile-fp32 100000; torch-compile-tf32 100000; torch-eager-bf16 100000; torch-compile-bf16 100000 |
| neural | sequential-predict | synthetic | log_loss | - | 0.225010 | torch-eager-fp32 0.225338; torch-eager-tf32 0.225332; torch-compile-fp32 0.225454; torch-compile-tf32 0.225378; torch-eager-bf16 0.225426; torch-compile-bf16 0.225425 |
| neural | sequential-predict | synthetic | loss_curve_length | - | 1 | torch-eager-fp32 1954; torch-eager-tf32 1954; torch-compile-fp32 1954; torch-compile-tf32 1954; torch-eager-bf16 1954; torch-compile-bf16 1954 |
| neural | sequential-predict | synthetic | train_loss_last_step | - | 0.240776 | torch-eager-fp32 0.143858; torch-eager-tf32 0.143500; torch-compile-fp32 0.143983; torch-compile-tf32 0.144187; torch-eager-bf16 0.144841; torch-compile-bf16 0.143898 |
| neural | sequential-predict | synthetic | accuracy_diff_vs_ours | - | - | torch-eager-fp32 -0.00041; torch-eager-tf32 -0.0006; torch-compile-fp32 -0.00036; torch-compile-tf32 -0.0005; torch-eager-bf16 -0.00045; torch-compile-bf16 -0.00061 |
| neural | sequential-predict | synthetic | auc_diff_vs_ours | - | - | torch-eager-fp32 -0.0001299; torch-eager-tf32 -0.0001274; torch-compile-fp32 -0.00016; torch-compile-tf32 -0.0001365; torch-eager-bf16 -0.0001549; torch-compile-bf16 -0.0001523 |
| neural | sequential-predict | synthetic | log_loss_diff_vs_ours | - | - | torch-eager-fp32 0.0003281; torch-eager-tf32 0.0003221; torch-compile-fp32 0.0004447; torch-compile-tf32 0.0003681; torch-eager-bf16 0.0004158; torch-compile-bf16 0.0004157 |
| neural | transformer-decode | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-decode | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-decode | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-decode | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-decode | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-eager-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-decode | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 4.768e-07; torch-eager-tf32 4.768e-07; torch-eager-bf16 0.001819; torch-graph-fp32 4.768e-07; torch-graph-tf32 4.768e-07 |
| neural | transformer-decode | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.02e-07; torch-eager-tf32 1.02e-07; torch-eager-bf16 0.0003893; torch-graph-fp32 1.02e-07; torch-graph-tf32 1.02e-07 |
| neural | transformer-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-tf32 -; torch-compile-fp32 -; torch-compile-tf32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 -; torch-graph-tf32 - |
| neural | transformer-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.018605 | torch-eager-fp32 -; torch-eager-tf32 11.138132; torch-compile-fp32 0.003106; torch-compile-tf32 11.118677; torch-eager-bf16 118.748732; torch-compile-bf16 42.038627; torch-graph-fp32 0.000000; torch-graph-tf32 11.138132 |
| neural | transformer-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 6.056e-08 | torch-eager-fp32 -; torch-eager-tf32 2.66e-05; torch-compile-fp32 3.114e-08; torch-compile-tf32 2.659e-05; torch-eager-bf16 0.0002766; torch-compile-bf16 0.0002631; torch-graph-fp32 0.000000; torch-graph-tf32 2.66e-05 |
| neural | transformer-forward | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 4.768e-07; torch-eager-tf32 0.0002124; torch-compile-fp32 4.768e-07; torch-compile-tf32 0.0002124; torch-eager-bf16 0.001819; torch-compile-bf16 0.001819; torch-graph-fp32 4.768e-07; torch-graph-tf32 0.0002124 |
| neural | transformer-forward | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.02e-07; torch-eager-tf32 4.545e-05; torch-compile-fp32 1.02e-07; torch-compile-tf32 4.545e-05; torch-eager-bf16 0.0003893; torch-compile-bf16 0.0003893; torch-graph-fp32 1.02e-07; torch-graph-tf32 4.545e-05 |


## Neural headline: ours IDENTICAL against torch bf16

What customers run is torch in bf16. The headline divides our IDENTICAL median by torch's fastest bf16 arm (eager or compile, the lower stored median); the fp32 twin (torch's fastest fp32 arm) is the second column. Per-arm ratios stay in each race's table below.

| lane | dataset | ours IDENTICAL ms | torch bf16 ms (fastest arm) | ours / torch bf16 | torch fp32 twin ms (fastest arm) | ours / torch fp32 | note |
|---|---|---|---|---|---|---|---|
| gemm-bf16 | gaussian | 65.9 | 39.7 (torch-eager-bf16) | 1.661 | - | - | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| gemm-int8 | gaussian | 43.8 | - | - | - | - | no torch bf16 arm on this lane |
| gemm | gaussian | 46.0 | 34.0 (torch-compile-bf16) | 1.351 | 36.4 (torch-eager-fp32) | 1.263 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| lm-forward | bytes | 44.9 | 31.1 (torch-compile-bf16) | 1.445 | 35.6 (torch-compile-fp32) | 1.261 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| lm-train-step | bytes | 35.5 | 10.8 (torch-compile-bf16) | 3.278 | 22.3 (torch-eager-fp32) | 1.589 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| mamba1-forward | gaussian | 3.4 | - | - | - | - | no torch bf16 arm on this lane |
| mamba2-forward | gaussian | 5.6 | - | - | - | - | no torch bf16 arm on this lane |
| mamba3-decode | gaussian | 1815.2 | - | - | - | - | no torch bf16 arm on this lane |
| mamba3-forward | gaussian | 4.0 | - | - | - | - | no torch bf16 arm on this lane |
| mlp-train-step | gaussian | 1.9 | 1.8 (torch-eager-bf16) | 1.052 | 1.8 (torch-eager-fp32) | 1.037 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| ops-session-step | gaussian | 2.3 | 2.4 (torch-eager-bf16) | 0.944 | 2.6 (torch-eager-fp32) | 0.881 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| program-run | gaussian | 1.0 | 0.7 (torch-eager-bf16) | 1.500 | 0.7 (torch-eager-fp32) | 1.589 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| samba-decode | bytes | 2517.3 | - | - | - | - | no torch bf16 arm on this lane |
| samba-forward | bytes | 4.6 | 4.3 (torch-eager-bf16) | 1.063 | 4.0 (torch-eager-fp32) | 1.157 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| samba-train-step | bytes | 45.7 | 19.3 (torch-eager-bf16) | 2.368 | 14.1 (torch-eager-fp32) | 3.248 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| sequential-fit | synthetic | 271.4 | 2250.2 (torch-compile-bf16) | 0.121 | 1986.4 (torch-compile-fp32) | 0.137 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| sequential-predict | synthetic | 4.3 | 1.5 (torch-eager-bf16) | 2.866 | 1.6 (torch-compile-fp32) | 2.646 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| transformer-decode | gaussian | 1104.9 | 861.8 (torch-eager-bf16) | 1.282 | 749.8 (torch-eager-fp32) | 1.474 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| transformer-forward | gaussian | 5.6 | 2.4 (torch-compile-bf16) | 2.352 | 2.7 (torch-eager-fp32) | 2.086 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |

## Neural

### gemm-bf16 / gaussian (neural shape full: 4096x4096x4096)

race: done, driver rc 0, log `logs/neural.gemm-bf16.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 39.7 ms) = 1.661; fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 65.9 | 65.9..65.9 | 1 | - | - | 65.9 | - | - (stored whole) | - | - | 1694.1 | 1164.0 | max_rel_err_vs_fp64=1.155e-07 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 39.7 | 39.7..39.7 | 1 | 1.661 | - | 39.7 | - | - (stored whole) | 1.661 (whole/whole) | - | 1384.6 | 176.2 | max_abs_diff_vs_ours=1.000977, max_rel_diff_vs_ours=0.002764, max_rel_err_vs_fp64=0.002764 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 40.4 | 40.4..40.4 | 1 | 1.632 | - | 40.4 | - | - (stored whole) | 1.632 (whole/whole) | - | 1454.9 | 176.2 | max_abs_diff_vs_ours=1.000977, max_rel_diff_vs_ours=0.002764, max_rel_err_vs_fp64=0.002764 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.matmul_bf16(operand_value_type='bfloat16', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-eager-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='bfloat16', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-compile-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='bfloat16', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-eager-bf16 |
|---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) |
| input_arrays | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} |
| operand_value_type | "bfloat16" | "bfloat16" | "bfloat16" |
| operation | "matmul" | "matmul" | "matmul" |
| seed | 7 | 7 | 7 |
| transpose_b | false | false | false |

### gemm-int8 / gaussian (neural shape full: 4096x4096x4096)

race: done, driver rc 0, log `logs/neural.gemm-int8.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 43.8 | 43.8..43.8 | 1 | - | - | 43.8 | - | - (stored whole) | - | - | 354.2 | 682.0 | max_rel_err_vs_fp64=0.000000 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-int8 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 37.7 | 37.7..37.7 | 1 | 1.159 | - | 37.7 | - | - (stored whole) | 1.159 (whole/whole) | - | 968.3 | 160.0 | max_abs_diff_vs_ours=0.000000, max_rel_diff_vs_ours=0.000000, max_rel_err_vs_fp64=0.000000 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-int8 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 38.7 | 38.7..38.7 | 1 | 1.131 | - | 38.7 | - | - (stored whole) | 1.131 (whole/whole) | - | 1033.9 | 160.0 | max_abs_diff_vs_ours=0.000000, max_rel_diff_vs_ours=0.000000, max_rel_err_vs_fp64=0.000000 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.matmul_int8(operand_value_type='int8', operation='matmul', seed=7, transpose_b=True, a=int8[4096x4096], b=int8[4096x4096])`
- `torch-eager-int8`: `torch._VariableFunctionsClass._int_mm(operand_value_type='int8', operation='matmul', seed=7, transpose_b=True, a=int8[4096x4096], b=int8[4096x4096])`
- `torch-compile-int8`: `torch._VariableFunctionsClass._int_mm(operand_value_type='int8', operation='matmul', seed=7, transpose_b=True, a=int8[4096x4096], b=int8[4096x4096])`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-int8, torch-compile-int8: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-int8 | torch-eager-int8 |
|---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) |
| input_arrays | {"a": {"dtype": "int8", "sha256": "4157ef2ec27e9864de38ff7e412e678d3fa3de8978b6dd6630b961545d5ac553", "shape": [4096, 4096]}, "b": {"dtype": "int8", "sha256": "43e1e9a5539cbe4b30b30b49e55820f96c3688e9245c43972f6fd0e7dea508fd", "shape": [4096, 4096]}} | {"a": {"dtype": "int8", "sha256": "4157ef2ec27e9864de38ff7e412e678d3fa3de8978b6dd6630b961545d5ac553", "shape": [4096, 4096]}, "b": {"dtype": "int8", "sha256": "43e1e9a5539cbe4b30b30b49e55820f96c3688e9245c43972f6fd0e7dea508fd", "shape": [4096, 4096]}} | {"a": {"dtype": "int8", "sha256": "4157ef2ec27e9864de38ff7e412e678d3fa3de8978b6dd6630b961545d5ac553", "shape": [4096, 4096]}, "b": {"dtype": "int8", "sha256": "43e1e9a5539cbe4b30b30b49e55820f96c3688e9245c43972f6fd0e7dea508fd", "shape": [4096, 4096]}} |
| operand_value_type | "int8" | "int8" | "int8" |
| operation | "matmul" | "matmul" | "matmul" |
| seed | 7 | 7 | 7 |
| transpose_b | true | true | true |

### gemm / gaussian (neural shape full: 4096x4096x4096)

race: done, driver rc 0, log `logs/neural.gemm.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 34.0 ms) = 1.351; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 36.4 ms) = 1.263. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 46.0 | 46.0..46.0 | 1 | - | - | 46.0 | - | - (stored whole) | - | - | 1755.3 | 908.0 | max_rel_err_vs_fp64=2.399e-07 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 36.4 | 36.4..36.4 | 1 | 1.263 | - | 36.4 | - | - (stored whole) | 1.263 (whole/whole) | - | 1089.4 | 200.1 | max_abs_diff_vs_ours=0.0005341, max_rel_diff_vs_ours=1.475e-06, max_rel_err_vs_fp64=1.401e-06 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 35.0 | 35.0..35.0 | 1 | 1.314 | - | 35.0 | - | - (stored whole) | 1.314 (whole/whole) | - | 1090.4 | 200.1 | max_abs_diff_vs_ours=0.100822, max_rel_diff_vs_ours=0.0002785, max_rel_err_vs_fp64=0.0002784 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 39.0 | 39.0..39.0 | 1 | 1.178 | - | 39.0 | - | - (stored whole) | 1.178 (whole/whole) | - | 1159.8 | 200.1 | max_abs_diff_vs_ours=0.0005341, max_rel_diff_vs_ours=1.475e-06, max_rel_err_vs_fp64=1.401e-06 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 35.6 | 35.6..35.6 | 1 | 1.291 | - | 35.6 | - | - (stored whole) | 1.291 (whole/whole) | - | 1161.5 | 200.1 | max_abs_diff_vs_ours=0.100822, max_rel_diff_vs_ours=0.0002785, max_rel_err_vs_fp64=0.0002784 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 34.4 | 34.4..34.4 | 1 | 1.338 | - | 34.4 | - | - (stored whole) | 1.338 (whole/whole) | - | 1329.0 | 240.2 | max_abs_diff_vs_ours=1.358337, max_rel_diff_vs_ours=0.003751, max_rel_err_vs_fp64=0.003752 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 34.0 | 34.0..34.0 | 1 | 1.351 | - | 34.0 | - | - (stored whole) | 1.351 (whole/whole) | - | 1432.6 | 240.2 | max_abs_diff_vs_ours=1.358337, max_rel_diff_vs_ours=0.003751, max_rel_err_vs_fp64=0.003752 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-eager-fp32`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-eager-tf32`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-compile-fp32`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-compile-tf32`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-eager-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-compile-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| input_arrays | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} |
| operand_value_type | "float32" | "float32" | "float32" | "float32" | "float32" | "float32" | "float32" |
| operation | "matmul" | "matmul" | "matmul" | "matmul" | "matmul" | "matmul" | "matmul" |
| seed | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| transpose_b | false | false | false | false | false | false | false |

### lm-forward / bytes (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024 layers8 V8192)

race: done, driver rc 0, log `logs/neural.lm-forward.bytes.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 31.1 ms) = 1.445; fp32 twin: ours IDENTICAL / torch fp32 (torch-compile-fp32, 35.6 ms) = 1.261. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 44.9 | 44.9..44.9 | 1 | - | - | 44.9 | - | - (stored whole) | - | - | 1656.0 | 4492.0 | mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 36.7 | 36.7..36.7 | 1 | 1.223 | - | 36.7 | - | - (stored whole) | 1.223 (whole/whole) | - | 1494.4 | 153.7 | max_abs_diff_vs_ours=1.371e-06, max_rel_diff_vs_ours=1.882e-06, mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 34.0 | 34.0..34.0 | 1 | 1.320 | - | 34.0 | - | - (stored whole) | 1.320 (whole/whole) | - | 1509.4 | 153.7 | max_abs_diff_vs_ours=0.000755, max_rel_diff_vs_ours=0.001037, mean_nll=9.015582 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 35.6 | 35.6..35.6 | 1 | 1.261 | - | 35.6 | - | - (stored whole) | 1.261 (whole/whole) | - | 1465.7 | 168.7 | max_abs_diff_vs_ours=1.326e-06, max_rel_diff_vs_ours=1.821e-06, mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 34.0 | 34.0..34.0 | 1 | 1.319 | - | 34.0 | - | - (stored whole) | 1.319 (whole/whole) | - | 1445.8 | 168.7 | max_abs_diff_vs_ours=0.0007218, max_rel_diff_vs_ours=0.0009909, mean_nll=9.015581 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 34.2 | 34.2..34.2 | 1 | 1.311 | - | 34.2 | - | - (stored whole) | 1.311 (whole/whole) | - | 1616.3 | 191.5 | max_abs_diff_vs_ours=0.006870, max_rel_diff_vs_ours=0.009431, mean_nll=9.015491 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 31.1 | 31.1..31.1 | 1 | 1.445 | - | 31.1 | - | - (stored whole) | 1.445 (whole/whole) | - | 1638.1 | 191.5 | max_abs_diff_vs_ours=0.006485, max_rel_diff_vs_ours=0.008903, mean_nll=9.015490 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 32.6 | 32.6..32.6 | 1 | 1.377 | - | 32.6 | - | - (stored whole) | 1.377 (whole/whole) | - | 1589.1 | 158.8 | max_abs_diff_vs_ours=1.371e-06, max_rel_diff_vs_ours=1.882e-06, mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 31.6 | 31.6..31.6 | 1 | 1.422 | - | 31.6 | - | - (stored whole) | 1.422 (whole/whole) | - | 1609.9 | 158.8 | max_abs_diff_vs_ours=0.000755, max_rel_diff_vs_ours=0.001037, mean_nll=9.015582 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-eager-tf32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-compile-fp32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-compile-tf32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-eager-bf16`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-compile-bf16`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-graph-fp32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-graph-tf32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16, torch-graph-fp32, torch-graph-tf32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 | torch-graph-fp32 | torch-graph-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |

### lm-train-step / bytes (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024 layers8 V8192)

race: done, driver rc 0, log `logs/neural.lm-train-step.bytes.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 10.8 ms) = 3.278; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 22.3 ms) = 1.589. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 35.5 | 35.5..35.5 | 1 | - | - | 35.5 | - | - (stored whole) | - | - | 1530.1 | 4236.0 | loss_first_step=9.015587, loss_last_step=8.405828, steps=2 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 22.3 | 22.3..22.3 | 1 | 1.589 | - | 22.3 | - | - (stored whole) | 1.589 (whole/whole) | - | 1547.9 | 959.2 | loss_first_abs_diff_vs_ours=0.000000, loss_first_step=9.015587, loss_last_abs_diff_vs_ours=1.907e-06, loss_last_step=8.405829, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 19.4 | 19.4..19.4 | 1 | 1.830 | - | 19.4 | - | - (stored whole) | 1.830 (whole/whole) | - | 1532.3 | 959.2 | loss_first_abs_diff_vs_ours=4.768e-06, loss_first_step=9.015582, loss_last_abs_diff_vs_ours=0.0003786, loss_last_step=8.406206, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 24.2 | 24.2..24.2 | 1 | 1.469 | - | 24.2 | - | - (stored whole) | 1.469 (whole/whole) | - | 1454.1 | 736.8 | loss_first_abs_diff_vs_ours=0.000000, loss_first_step=9.015587, loss_last_abs_diff_vs_ours=9.537e-07, loss_last_step=8.405828, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 18.4 | 18.4..18.4 | 1 | 1.931 | - | 18.4 | - | - (stored whole) | 1.931 (whole/whole) | - | 1449.4 | 743.2 | loss_first_abs_diff_vs_ours=6.676e-06, loss_first_step=9.015580, loss_last_abs_diff_vs_ours=0.0003262, loss_last_step=8.406154, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 22.5 | 22.5..22.5 | 1 | 1.577 | - | 22.5 | - | - (stored whole) | 1.577 (whole/whole) | - | 1640.0 | 827.1 | loss_first_abs_diff_vs_ours=9.537e-05, loss_first_step=9.015491, loss_last_abs_diff_vs_ours=0.0001421, loss_last_step=8.405970, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 10.8 | 10.8..10.8 | 1 | 3.278 | - | 10.8 | - | - (stored whole) | 3.278 (whole/whole) | - | 1599.7 | 554.1 | loss_first_abs_diff_vs_ours=9.727e-05, loss_first_step=9.015490, loss_last_abs_diff_vs_ours=0.0008307, loss_last_step=8.404997, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-eager-tf32`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-compile-fp32`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-compile-tf32`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-eager-bf16`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-compile-bf16`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false | false | false |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| capturable | - | false | false | false | false | false | false |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" |
| decoupled_weight_decay | true | true | true | true | true | true | true |
| differentiable | - | false | false | false | false | false | false |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| foreach | - | null | null | null | null | null | null |
| fused | - | null | null | null | null | null | null |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| maximize | false | false | false | false | false | false | false |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 | 7 |
| weight_decay | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |

accepted difference: torch-eager-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-tf32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-tf32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-tf32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-tf32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-tf32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-tf32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-tf32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-tf32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

### mamba1-forward / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba1-forward.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 3.4 | 3.4..3.4 | 1 | - | - | 3.4 | - | - (stored whole) | - | - | 1516.6 | 908.0 | host_reference=Mamba1BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.0001944, rel_fro_vs_torch_eager_fp32=6.377e-09 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba1-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba1-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba1-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| mamba-ssm-fp32 | mamba-ssm | gpu | NVIDIA L40S (host nv-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 3.3 | 3.3..3.3 | 1 | 1.036 | - | 3.3 | - | - (stored whole) | 1.036 (whole/whole) | - | 1257.3 | 54.6 | max_abs_diff_vs_ours=1.192e-07, max_rel_diff_vs_ours=5.945e-08, max_rel_diff_vs_torch_eager_fp32=0.0001588, rel_fro_vs_torch_eager_fp32=5.039e-09 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| mamba-ssm-tf32 | mamba-ssm | gpu | NVIDIA L40S (host nv-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 3.2 | 3.2..3.2 | 1 | 1.074 | - | 3.2 | - | - (stored whole) | 1.074 (whole/whole) | - | 1236.4 | 54.6 | max_abs_diff_vs_ours=3.815e-06, max_rel_diff_vs_ours=1.902e-06, max_rel_diff_vs_torch_eager_fp32=0.175704, rel_fro_vs_torch_eager_fp32=6.398e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `mamba-ssm-fp32`: `mamba_ssm.Block(seed=7, ssm_d_conv=4, ssm_d_state=16, ssm_dt_rank=24, ssm_expand=2)`
- `mamba-ssm-tf32`: `mamba_ssm.Block(seed=7, ssm_d_conv=4, ssm_d_state=16, ssm_dt_rank=24, ssm_expand=2)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-eager-bf16: host not sampled; GPU not sampled

memory, mamba-ssm-fp32, mamba-ssm-tf32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | mamba-ssm-fp32 | mamba-ssm-tf32 | ours |
|---|---||---|---||---|---|
| library (source) | mamba-ssm (declared) | mamba-ssm (declared) | anonlib (declared) |
| seed | 7 | 7 | "none (deterministic)" |
| ssm_d_conv | 4 | 4 | 4 |
| ssm_d_state | 16 | 16 | 16 |
| ssm_dt_rank | 24 | 24 | 24 |
| ssm_expand | 2 | 2 | 2 |

### mamba2-forward / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba2-forward.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 5.6 | 5.6..5.6 | 1 | - | - | 5.6 | - | - (stored whole) | - | - | 1518.9 | 682.0 | host_reference=Mamba2BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.236111, rel_fro_vs_torch_eager_fp32=1.497e-07 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| mamba-ssm-fp32 | mamba-ssm | gpu | NVIDIA L40S (host nv-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 3.3 | 3.3..3.3 | 1 | 1.697 | - | 3.3 | - | - (stored whole) | 1.697 (whole/whole) | - | 1492.9 | 58.6 | max_abs_diff_vs_ours=1.669e-06, max_rel_diff_vs_ours=5.674e-07, max_rel_diff_vs_torch_eager_fp32=0.020408, rel_fro_vs_torch_eager_fp32=8.531e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| mamba-ssm-tf32 | mamba-ssm | gpu | NVIDIA L40S (host nv-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 2.8 | 2.8..2.8 | 1 | 1.985 | - | 2.8 | - | - (stored whole) | 1.985 (whole/whole) | - | 1301.4 | 58.6 | max_abs_diff_vs_ours=0.0005126, max_rel_diff_vs_ours=0.0001743, max_rel_diff_vs_torch_eager_fp32=24.892473, rel_fro_vs_torch_eager_fp32=9.072e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `mamba-ssm-fp32`: `mamba_ssm.Block(seed=7, ssm_chunk_size=256, ssm_d_conv=4, ssm_d_state=128, ssm_dt_limit=[0, inf], ssm_expand=2, ssm_headdim=64, ssm_ngroups=1)`
- `mamba-ssm-tf32`: `mamba_ssm.Block(seed=7, ssm_chunk_size=256, ssm_d_conv=4, ssm_d_state=128, ssm_dt_limit=[0, inf], ssm_expand=2, ssm_headdim=64, ssm_ngroups=1)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host not sampled; GPU not sampled

memory, mamba-ssm-fp32, mamba-ssm-tf32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | mamba-ssm-fp32 | mamba-ssm-tf32 | ours |
|---|---||---|---||---|---|
| library (source) | mamba-ssm (declared) | mamba-ssm (declared) | anonlib (declared) |
| seed | 7 | 7 | "none (deterministic)" |
| ssm_chunk_size | 256 | 256 | 256 |
| ssm_d_conv | 4 | 4 | 4 |
| ssm_d_state | 128 | 128 | 128 |
| ssm_dt_limit | [0.0, Infinity] | [0.0, Infinity] | [0.0, Infinity] |
| ssm_expand | 2 | 2 | 2 |
| ssm_headdim | 64 | 64 | 64 |
| ssm_ngroups | 1 | 1 | 1 |

### mamba3-decode / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba3-decode.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 1815.2 | 1815.2..1815.2 | 1 | - | - | 1815.2 | - | - (stored whole) | - | - | 1529.9 | 682.0 | host_reference=Mamba3BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (declared) |
| seed | "none (deterministic)" |

### mamba3-forward / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba3-forward.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 4.0 | 4.0..4.0 | 1 | - | - | 4.0 | - | - (stored whole) | - | - | 1521.8 | 682.0 | host_reference=Mamba3BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.009235, rel_fro_vs_torch_eager_fp32=5.551e-08 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| mamba-ssm-fp32 | mamba-ssm | gpu | NVIDIA L40S (host nv-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 3.2 | 3.2..3.2 | 1 | 1.225 | - | 3.2 | - | - (stored whole) | 1.225 (whole/whole) | - | 1430.4 | 70.0 | max_abs_diff_vs_ours=0.001235, max_rel_diff_vs_ours=0.0005401, max_rel_diff_vs_torch_eager_fp32=129.116095, rel_fro_vs_torch_eager_fp32=0.0001981 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| mamba-ssm-tf32 | mamba-ssm | gpu | NVIDIA L40S (host nv-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 3.1 | 3.1..3.1 | 1 | 1.290 | - | 3.1 | - | - (stored whole) | 1.290 (whole/whole) | - | 1429.1 | 70.0 | max_abs_diff_vs_ours=0.001290, max_rel_diff_vs_ours=0.0005645, max_rel_diff_vs_torch_eager_fp32=119.090758, rel_fro_vs_torch_eager_fp32=0.0001993 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `mamba-ssm-fp32`: `mamba_ssm.Block(seed=7, ssm_chunk_size=64, ssm_d_state=128, ssm_expand=2, ssm_headdim=64, ssm_ngroups=1, ssm_rope_angles=32)`
- `mamba-ssm-tf32`: `mamba_ssm.Block(seed=7, ssm_chunk_size=64, ssm_d_state=128, ssm_expand=2, ssm_headdim=64, ssm_ngroups=1, ssm_rope_angles=32)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host not sampled; GPU not sampled

memory, mamba-ssm-fp32, mamba-ssm-tf32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | mamba-ssm-fp32 | mamba-ssm-tf32 | ours |
|---|---||---|---||---|---|
| library (source) | mamba-ssm (declared) | mamba-ssm (declared) | anonlib (declared) |
| seed | 7 | 7 | "none (deterministic)" |
| ssm_chunk_size | 64 | 64 | 64 |
| ssm_d_state | 128 | 128 | 128 |
| ssm_expand | 2 | 2 | 2 |
| ssm_headdim | 64 | 64 | 64 |
| ssm_ngroups | 1 | 1 | 1 |
| ssm_rope_angles | 32 | 32 | 32 |

### mlp-train-step / gaussian (neural shape full: rows256 8-16-3)

race: done, driver rc 0, log `logs/neural.mlp-train-step.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 1.8 ms) = 1.052; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 1.8 ms) = 1.037. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 1.9 | 1.9..1.9 | 1 | - | - | 1.9 | - | - (stored whole) | - | - | 1507.6 | 682.0 | loss_first_step=1.160401, loss_last_step=1.123361, steps=2 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.8 | 1.8..1.8 | 1 | 1.037 | - | 1.8 | - | - (stored whole) | 1.037 (whole/whole) | - | 1028.3 | 16.3 | loss_first_abs_diff_vs_ours=2.384e-07, loss_first_step=1.160401, loss_last_abs_diff_vs_ours=2.384e-07, loss_last_step=1.123361, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.7 | 1.7..1.7 | 1 | 1.131 | - | 1.7 | - | - (stored whole) | 1.131 (whole/whole) | - | 1028.6 | 16.3 | loss_first_abs_diff_vs_ours=8.941e-06, loss_first_step=1.160392, loss_last_abs_diff_vs_ours=5.484e-06, loss_last_step=1.123355, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.1 | 2.1..2.1 | 1 | 0.906 | - | 2.1 | - | - (stored whole) | 0.906 (whole/whole) | - | 1114.2 | 16.3 | loss_first_abs_diff_vs_ours=2.384e-07, loss_first_step=1.160401, loss_last_abs_diff_vs_ours=2.384e-07, loss_last_step=1.123361, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.1 | 2.1..2.1 | 1 | 0.901 | - | 2.1 | - | - (stored whole) | 0.901 (whole/whole) | - | 1060.2 | 16.3 | loss_first_abs_diff_vs_ours=8.941e-06, loss_first_step=1.160392, loss_last_abs_diff_vs_ours=5.603e-06, loss_last_step=1.123355, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.8 | 1.8..1.8 | 1 | 1.052 | - | 1.8 | - | - (stored whole) | 1.052 (whole/whole) | - | 1240.5 | 16.3 | loss_first_abs_diff_vs_ours=9.656e-05, loss_first_step=1.160498, loss_last_abs_diff_vs_ours=0.0001006, loss_last_step=1.123461, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.9 | 1.9..1.9 | 1 | 1.006 | - | 1.9 | - | - (stored whole) | 1.006 (whole/whole) | - | 1309.2 | 16.3 | loss_first_abs_diff_vs_ours=9.656e-05, loss_first_step=1.160498, loss_last_abs_diff_vs_ours=0.0001007, loss_last_step=1.123462, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-eager-tf32`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-compile-fp32`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-compile-tf32`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-eager-bf16`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-compile-bf16`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false | false | false |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| capturable | - | false | false | false | false | false | false |
| config_readback | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" |
| decoupled_weight_decay | true | true | true | true | true | true | true |
| differentiable | - | false | false | false | false | false | false |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| foreach | - | null | null | null | null | null | null |
| fused | - | null | null | null | null | null | null |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| maximize | false | false | false | false | false | false | false |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 | 7 |
| weight_decay | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |

accepted difference: torch-eager-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-tf32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-tf32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-tf32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-tf32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-tf32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-tf32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-tf32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-tf32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

### ops-session-step / gaussian (neural shape full: B4096 256-512-16 linear relu linear CE sgd)

race: done, driver rc 0, log `logs/neural.ops-session-step.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 2.4 ms) = 0.944; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 2.6 ms) = 0.881. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 2.3 | 2.3..2.3 | 1 | - | - | 2.3 | - | - (stored whole) | - | - | 1514.5 | 682.0 | grad_digests={'b1': 'af8a97d53a3ad547', 'b2': '00290c152a66267b', 'w1': '4ff384d9d46fb712', 'w2': 'd836f93eb9369f50'}, grads_finite=True, loss=2.798163, loss_finite=True | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.6 | 2.6..2.6 | 1 | 0.881 | - | 2.6 | - | - (stored whole) | 0.881 (whole/whole) | - | 1004.3 | 44.9 | grad_digests={'b1': '545b00f23e9400cc', 'b2': 'fa46f0e813a1cd2a', 'w1': '3adb09a2a6301952', 'w2': '7cb528dd0872f847'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=5.821e-10, grad_max_abs_diff_vs_ours_b2=2.794e-09, grad_max_abs_diff_vs_ours_w1=2.794e-09, grad_max_abs_diff_vs_ours_w2=4.191e-09, grad_max_rel_diff_vs_ours_b1=3.833e-07, grad_max_rel_diff_vs_ours_b2=1.329e-07, grad_max_rel_diff_vs_ours_w1=2.102e-06, grad_max_rel_diff_vs_ours_w2=4.676e-07, grads_finite=True, loss=2.798162, loss_abs_diff_vs_ours=7.153e-07, loss_finite=True, param_max_abs_diff_vs_ours_b1=1.863e-09, param_max_abs_diff_vs_ours_b2=0.000000, param_max_abs_diff_vs_ours_w1=3.725e-09, param_max_abs_diff_vs_ours_w2=3.725e-09, param_max_rel_diff_vs_ours_b1=2.982e-08, param_max_rel_diff_vs_ours_b2=0.000000, param_max_rel_diff_vs_ours_w1=5.958e-08, param_max_rel_diff_vs_ours_w2=8.398e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.1 | 2.1..2.1 | 1 | 1.095 | - | 2.1 | - | - (stored whole) | 1.095 (whole/whole) | - | 999.2 | 44.9 | grad_digests={'b1': '66a0167ce6700071', 'b2': '273b124ff4eeeedd', 'w1': '00037a00072692fc', 'w2': 'b6ce886fcaf763ca'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=1.619e-05, grad_max_abs_diff_vs_ours_b2=4.443e-06, grad_max_abs_diff_vs_ours_w1=4.365e-05, grad_max_abs_diff_vs_ours_w2=2.888e-06, grad_max_rel_diff_vs_ours_b1=0.010665, grad_max_rel_diff_vs_ours_b2=0.0002114, grad_max_rel_diff_vs_ours_w1=0.032848, grad_max_rel_diff_vs_ours_w2=0.0003222, grads_finite=True, loss=2.798163, loss_abs_diff_vs_ours=0.000000, loss_finite=True, param_max_abs_diff_vs_ours_b1=8.103e-07, param_max_abs_diff_vs_ours_b2=2.217e-07, param_max_abs_diff_vs_ours_w1=2.183e-06, param_max_abs_diff_vs_ours_w2=1.453e-07, param_max_rel_diff_vs_ours_b1=1.297e-05, param_max_rel_diff_vs_ours_b2=5.8e-06, param_max_rel_diff_vs_ours_w1=3.491e-05, param_max_rel_diff_vs_ours_w2=3.275e-06 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.6 | 2.6..2.6 | 1 | 0.874 | - | 2.6 | - | - (stored whole) | 0.874 (whole/whole) | - | 1037.0 | 37.1 | grad_digests={'b1': '67b50b90a41f7a17', 'b2': '42829beb2350d146', 'w1': '4d446ceae9876b79', 'w2': '2b480dd79eb97929'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=5.821e-10, grad_max_abs_diff_vs_ours_b2=3.725e-09, grad_max_abs_diff_vs_ours_w1=2.736e-09, grad_max_abs_diff_vs_ours_w2=4.191e-09, grad_max_rel_diff_vs_ours_b1=3.833e-07, grad_max_rel_diff_vs_ours_b2=1.773e-07, grad_max_rel_diff_vs_ours_w1=2.059e-06, grad_max_rel_diff_vs_ours_w2=4.676e-07, grads_finite=True, loss=2.798162, loss_abs_diff_vs_ours=7.153e-07, loss_finite=True, param_max_abs_diff_vs_ours_b1=3.638e-12, param_max_abs_diff_vs_ours_b2=0.000000, param_max_abs_diff_vs_ours_w1=3.725e-09, param_max_abs_diff_vs_ours_w2=3.725e-09, param_max_rel_diff_vs_ours_b1=5.824e-11, param_max_rel_diff_vs_ours_b2=0.000000, param_max_rel_diff_vs_ours_w1=5.958e-08, param_max_rel_diff_vs_ours_w2=8.398e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.7 | 2.7..2.7 | 1 | 0.839 | - | 2.7 | - | - (stored whole) | 0.839 (whole/whole) | - | 983.1 | 37.1 | grad_digests={'b1': 'a8604de82d26c030', 'b2': '52e6ee173ea6c3d7', 'w1': '121fb6ad333c5e4f', 'w2': 'b8403585841a58b6'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=1.619e-05, grad_max_abs_diff_vs_ours_b2=4.441e-06, grad_max_abs_diff_vs_ours_w1=4.365e-05, grad_max_abs_diff_vs_ours_w2=2.888e-06, grad_max_rel_diff_vs_ours_b1=0.010665, grad_max_rel_diff_vs_ours_b2=0.0002113, grad_max_rel_diff_vs_ours_w1=0.032848, grad_max_rel_diff_vs_ours_w2=0.0003222, grads_finite=True, loss=2.798162, loss_abs_diff_vs_ours=2.384e-07, loss_finite=True, param_max_abs_diff_vs_ours_b1=8.103e-07, param_max_abs_diff_vs_ours_b2=2.217e-07, param_max_abs_diff_vs_ours_w1=2.183e-06, param_max_abs_diff_vs_ours_w2=1.453e-07, param_max_rel_diff_vs_ours_b1=1.297e-05, param_max_rel_diff_vs_ours_b2=5.8e-06, param_max_rel_diff_vs_ours_w1=3.491e-05, param_max_rel_diff_vs_ours_w2=3.275e-06 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.4 | 2.4..2.4 | 1 | 0.944 | - | 2.4 | - | - (stored whole) | 0.944 (whole/whole) | - | 1236.9 | 50.9 | grad_digests={'b1': '2e792524b5b24c65', 'b2': '60726365514709eb', 'w1': 'ed0f0384c273ed54', 'w2': '9026da9d0e57cdf5'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=5.06e-05, grad_max_abs_diff_vs_ours_b2=3.965e-05, grad_max_abs_diff_vs_ours_w1=7.59e-05, grad_max_abs_diff_vs_ours_w2=3.952e-05, grad_max_rel_diff_vs_ours_b1=0.033320, grad_max_rel_diff_vs_ours_b2=0.001887, grad_max_rel_diff_vs_ours_w1=0.057112, grad_max_rel_diff_vs_ours_w2=0.004410, grads_finite=True, loss=2.798156, loss_abs_diff_vs_ours=6.676e-06, loss_finite=True, param_max_abs_diff_vs_ours_b1=2.53e-06, param_max_abs_diff_vs_ours_b2=1.982e-06, param_max_abs_diff_vs_ours_w1=3.795e-06, param_max_abs_diff_vs_ours_w2=1.978e-06, param_max_rel_diff_vs_ours_b1=4.05e-05, param_max_rel_diff_vs_ours_b2=5.185e-05, param_max_rel_diff_vs_ours_w1=6.069e-05, param_max_rel_diff_vs_ours_w2=4.459e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.7 | 2.7..2.7 | 1 | 0.837 | - | 2.7 | - | - (stored whole) | 0.837 (whole/whole) | - | 1269.9 | 32.8 | grad_digests={'b1': 'c57b7657cfa678d1', 'b2': '0967efa359c77ca9', 'w1': 'ed0f0384c273ed54', 'w2': '9026da9d0e57cdf5'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=5.06e-05, grad_max_abs_diff_vs_ours_b2=3.965e-05, grad_max_abs_diff_vs_ours_w1=7.59e-05, grad_max_abs_diff_vs_ours_w2=3.952e-05, grad_max_rel_diff_vs_ours_b1=0.033320, grad_max_rel_diff_vs_ours_b2=0.001887, grad_max_rel_diff_vs_ours_w1=0.057112, grad_max_rel_diff_vs_ours_w2=0.004410, grads_finite=True, loss=2.798156, loss_abs_diff_vs_ours=6.676e-06, loss_finite=True, param_max_abs_diff_vs_ours_b1=2.53e-06, param_max_abs_diff_vs_ours_b2=1.982e-06, param_max_abs_diff_vs_ours_w1=3.795e-06, param_max_abs_diff_vs_ours_w2=1.978e-06, param_max_rel_diff_vs_ours_b1=4.05e-05, param_max_rel_diff_vs_ours_b2=5.185e-05, param_max_rel_diff_vs_ours_w1=6.069e-05, param_max_rel_diff_vs_ours_w2=4.459e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Session(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-eager-fp32`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-eager-tf32`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-compile-fp32`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-compile-tf32`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-eager-bf16`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-compile-bf16`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| batch_size | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 |
| layers | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] |
| learning_rate | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |
| loss | "cross_entropy" | "cross_entropy" | "cross_entropy" | "cross_entropy" | "cross_entropy" | "cross_entropy" | "cross_entropy" |
| momentum | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| nesterov | false | false | false | false | false | false | false |
| optimizer | "sgd" | "sgd" | "sgd" | "sgd" | "sgd" | "sgd" | "sgd" |
| reduction | "mean" | "mean" | "mean" | "mean" | "mean" | "mean" | "mean" |
| seed | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| steps | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| weight_decay | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### program-run / gaussian (neural shape full: B4096 256-512-16 linear relu linear softmax, one Program.run)

race: done, driver rc 0, log `logs/neural.program-run.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 0.7 ms) = 1.500; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 0.7 ms) = 1.589. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 1.0 | 1.0..1.0 | 1 | - | - | 1.0 | - | - (stored whole) | - | - | 1512.0 | 682.0 | finite=True, max_abs_err_vs_fp64=7.398e-08, output_digest=da6c27db289f0438 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 0.7 | 0.7..0.7 | 1 | 1.589 | - | 0.7 | - | - (stored whole) | 1.589 (whole/whole) | - | 908.3 | 28.7 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=8.941e-08, max_abs_err_vs_fp64=3.219e-08, max_rel_diff_vs_ours=5.226e-07, output_digest=64a2315d407a0850 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 0.6 | 0.6..0.6 | 1 | 1.795 | - | 0.6 | - | - (stored whole) | 1.795 (whole/whole) | - | 903.8 | 28.7 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=3.727e-05, max_abs_err_vs_fp64=3.73e-05, max_rel_diff_vs_ours=0.0002178, output_digest=3738c9f2fbbc49ad | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.4 | 1.4..1.4 | 1 | 0.739 | - | 1.4 | - | - (stored whole) | 0.739 (whole/whole) | - | 995.4 | 20.9 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=7.451e-08, max_abs_err_vs_fp64=3.333e-08, max_rel_diff_vs_ours=4.355e-07, output_digest=724850f771480afc | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.3 | 1.3..1.3 | 1 | 0.787 | - | 1.3 | - | - (stored whole) | 0.787 (whole/whole) | - | 937.5 | 20.9 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=3.727e-05, max_abs_err_vs_fp64=3.73e-05, max_rel_diff_vs_ours=0.0002178, output_digest=77ab240062f9c6cd | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 0.7 | 0.7..0.7 | 1 | 1.500 | - | 0.7 | - | - (stored whole) | 1.500 (whole/whole) | - | 1140.8 | 36.8 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=0.0004913, max_abs_err_vs_fp64=0.0004913, max_rel_diff_vs_ours=0.002871, output_digest=62714ae1b3d04652 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.2 | 1.2..1.2 | 1 | 0.854 | - | 1.2 | - | - (stored whole) | 0.854 (whole/whole) | - | 1207.0 | 27.0 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=0.0004913, max_abs_err_vs_fp64=0.0004913, max_rel_diff_vs_ours=0.002871, output_digest=29bbd7817c0126d3 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Program(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-eager-fp32`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-eager-tf32`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-compile-fp32`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-compile-tf32`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-eager-bf16`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-compile-bf16`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| batch_size | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 |
| layers | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] |
| mode | "inference" | "inference" | "inference" | "inference" | "inference" | "inference" | "inference" |
| seed | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| steps | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### samba-decode / bytes (neural shape full: B2 L512 DM384 V256 H6 FF1024 layers mamba3+attention+mamba3+attention)

race: done, driver rc 0, log `logs/neural.samba-decode.bytes.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 2517.3 | 2517.3..2517.3 | 1 | - | - | 2517.3 | - | - (stored whole) | - | - | 1565.8 | 682.0 | mean_nll=5.640151 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (declared) |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" |
| dropout | 0.0 |
| eps | 1e-05 |
| max_grad_norm | "n/a" |
| rope_theta | 10000.0 |
| seed | "none (deterministic)" |

### samba-forward / bytes (neural shape full: B2 L512 DM384 V256 H6 FF1024 layers mamba3+attention+mamba3+attention)

race: done, driver rc 0, log `logs/neural.samba-forward.bytes.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 4.3 ms) = 1.063; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 4.0 ms) = 1.157. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 4.6 | 4.6..4.6 | 1 | - | - | 4.6 | - | - (stored whole) | - | - | 1533.5 | 1164.0 | mean_nll=5.640151 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 4.0 | 4.0..4.0 | 1 | 1.157 | - | 4.0 | - | - (stored whole) | 1.157 (whole/whole) | - | 1569.5 | 62.0 | max_abs_diff_vs_ours=0.011567, max_rel_diff_vs_ours=0.007038, mean_nll=5.640315 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 4.9 | 4.9..4.9 | 1 | 0.942 | - | 4.9 | - | - (stored whole) | 0.942 (whole/whole) | - | 1563.2 | 62.0 | max_abs_diff_vs_ours=0.010282, max_rel_diff_vs_ours=0.006256, mean_nll=5.640322 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-fp32 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-tf32 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 4.3 | 4.3..4.3 | 1 | 1.063 | - | 4.3 | - | - (stored whole) | 1.063 (whole/whole) | - | 1562.4 | 72.9 | max_abs_diff_vs_ours=0.015470, max_rel_diff_vs_ours=0.009412, mean_nll=5.640346 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-bf16 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-graph-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.7 | 1.7..1.7 | 1 | 2.681 | - | 1.7 | - | - (stored whole) | 2.681 (whole/whole) | - | 1396.9 | 39.1 | max_abs_diff_vs_ours=0.010900, max_rel_diff_vs_ours=0.006632, mean_nll=5.640305 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.4 | 1.4..1.4 | 1 | 3.342 | - | 1.4 | - | - (stored whole) | 3.342 (whole/whole) | - | 1377.9 | 39.1 | max_abs_diff_vs_ours=0.009999, max_rel_diff_vs_ours=0.006084, mean_nll=5.640320 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-eager-tf32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-compile-fp32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-compile-tf32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-eager-bf16`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-compile-bf16`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-graph-fp32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-graph-tf32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-eager-bf16, torch-graph-fp32, torch-graph-tf32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

memory, torch-compile-fp32, torch-compile-tf32, torch-compile-bf16: host not sampled; GPU not sampled

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 | torch-graph-fp32 | torch-graph-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" |
| dropout | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| eps | 1e-05 | 1e-05 | 1e-05 | 1e-05 | 1e-05 | 1e-05 | 1e-05 | 1e-05 | 1e-05 |
| max_grad_norm | "n/a" | "n/a" | "n/a" | "n/a" | "n/a" | "n/a" | "n/a" | "n/a" | "n/a" |
| rope_theta | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |

### samba-train-step / bytes (neural shape full: B2 L512 DM384 V256 H6 FF1024 layers mamba3+attention+mamba3+attention)

race: done, driver rc 0, log `logs/neural.samba-train-step.bytes.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 19.3 ms) = 2.368; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 14.1 ms) = 3.248. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 45.7 | 45.7..45.7 | 1 | - | - | 45.7 | - | - (stored whole) | - | - | 1538.1 | 1420.0 | loss_first_step=5.640152, loss_last_step=4.822321, steps=2 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 14.1 | 14.1..14.1 | 1 | 3.248 | - | 14.1 | - | - (stored whole) | 3.248 (whole/whole) | - | 1922.7 | 218.7 | loss_first_abs_diff_vs_ours=0.000155, loss_first_step=5.640307, loss_last_abs_diff_vs_ours=0.0006776, loss_last_step=4.822999, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 11.8 | 11.8..11.8 | 1 | 3.881 | - | 11.8 | - | - (stored whole) | 3.881 (whole/whole) | - | 1915.2 | 218.7 | loss_first_abs_diff_vs_ours=0.0001669, loss_first_step=5.640319, loss_last_abs_diff_vs_ours=0.0004425, loss_last_step=4.822763, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-fp32 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-tf32 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 19.3 | 19.3..19.3 | 1 | 2.368 | - | 19.3 | - | - (stored whole) | 2.368 (whole/whole) | - | 1869.3 | 183.4 | loss_first_abs_diff_vs_ours=0.0001993, loss_first_step=5.640351, loss_last_abs_diff_vs_ours=0.0001316, loss_last_step=4.822189, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-bf16 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |

calls:
- `torch-eager-fp32`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-eager-tf32`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-compile-fp32`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-compile-tf32`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-eager-bf16`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-compile-bf16`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-eager-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

memory, torch-compile-fp32, torch-compile-tf32, torch-compile-bf16: host not sampled; GPU not sampled

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| accumulation_steps | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| amsgrad | false | false | false | false | false | false | false |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| capturable | - | false | false | false | false | false | false |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" |
| decoupled_weight_decay | true | true | true | true | true | true | true |
| differentiable | - | false | false | false | false | false | false |
| dropout | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| foreach | - | null | null | null | null | null | null |
| fused | - | null | null | null | null | null | null |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| max_grad_norm | "off" | "off" | "off" | "off" | "off" | "off" | "off" |
| maximize | false | false | false | false | false | false | false |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 | 7 |
| weight_decay | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |

accepted difference: torch-eager-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-tf32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-tf32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-tf32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-tf32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-tf32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-tf32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-tf32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-tf32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

### sequential-fit / synthetic (neural shape full: synthetic train 1000000 test 100000 32-128-64-1 b512 1 epoch adam + predict_proba)

race: done, driver rc 0, log `logs/neural.sequential-fit.synthetic.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 2250.2 ms) = 0.121; fp32 twin: ours IDENTICAL / torch fp32 (torch-compile-fp32, 1986.4 ms) = 0.137. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 271.4 | 271.4..271.4 | 1 | - | - | 271.4 | - | - (stored whole) | - | - | 1654.2 | 938.0 | accuracy=0.899070, auc=0.968973, held_out_rows=100000, log_loss=0.225010, loss_curve_length=1, train_loss_finite=True, train_loss_last_step=0.240776 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2131.4 | 2131.4..2131.4 | 1 | 0.127 | - | 2131.4 | - | - (stored whole) | 0.127 (whole/whole) | - | 1291.8 | 227.6 | accuracy=0.898660, accuracy_diff_vs_ours=-0.00041, auc=0.968843, auc_diff_vs_ours=-0.0001299, held_out_rows=100000, log_loss=0.225338, log_loss_diff_vs_ours=0.0003281, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.143858 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2326.2 | 2326.2..2326.2 | 1 | 0.117 | - | 2326.2 | - | - (stored whole) | 0.117 (whole/whole) | - | 1303.2 | 227.6 | accuracy=0.898470, accuracy_diff_vs_ours=-0.0006, auc=0.968846, auc_diff_vs_ours=-0.0001274, held_out_rows=100000, log_loss=0.225332, log_loss_diff_vs_ours=0.0003221, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.143500 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1986.4 | 1986.4..1986.4 | 1 | 0.137 | - | 1986.4 | - | - (stored whole) | 0.137 (whole/whole) | - | 1332.9 | 227.6 | accuracy=0.898790, accuracy_diff_vs_ours=-0.00028, auc=0.968810, auc_diff_vs_ours=-0.0001632, held_out_rows=100000, log_loss=0.225476, log_loss_diff_vs_ours=0.0004662, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.145113 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2287.0 | 2287.0..2287.0 | 1 | 0.119 | - | 2287.0 | - | - (stored whole) | 0.119 (whole/whole) | - | 1285.7 | 227.6 | accuracy=0.898420, accuracy_diff_vs_ours=-0.00065, auc=0.968805, auc_diff_vs_ours=-0.0001686, held_out_rows=100000, log_loss=0.225478, log_loss_diff_vs_ours=0.0004687, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.144524 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 3077.3 | 3077.3..3077.3 | 1 | 0.088 | - | 3077.3 | - | - (stored whole) | 0.088 (whole/whole) | - | 1468.0 | 195.1 | accuracy=0.898620, accuracy_diff_vs_ours=-0.00045, auc=0.968818, auc_diff_vs_ours=-0.0001549, held_out_rows=100000, log_loss=0.225426, log_loss_diff_vs_ours=0.0004158, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.144841 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2250.2 | 2250.2..2250.2 | 1 | 0.121 | - | 2250.2 | - | - (stored whole) | 0.121 (whole/whole) | - | 1535.4 | 195.1 | accuracy=0.898400, accuracy_diff_vs_ours=-0.00067, auc=0.968846, auc_diff_vs_ours=-0.0001273, held_out_rows=100000, log_loss=0.225339, log_loss_diff_vs_ours=0.0003289, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.144898 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-tf32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-tf32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false | false | false |
| batch_size | 512 | 512 | 512 | 512 | 512 | 512 | 512 |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| epochs | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| layers | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| loss | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" |
| maximize | false | false | false | false | false | false | false |
| optimizer | "adam" | "adam" | "adam" | "adam" | "adam" | "adam" | "adam" |
| seed | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| shuffle | true | true | true | true | true | true | true |
| weight_decay | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### sequential-predict / synthetic (neural shape full: synthetic train 1000000 test 100000 32-128-64-1 b512 1 epoch adam, predict_proba 100000 rows timed)

race: done, driver rc 0, log `logs/neural.sequential-predict.synthetic.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 1.5 ms) = 2.866; fp32 twin: ours IDENTICAL / torch fp32 (torch-compile-fp32, 1.6 ms) = 2.646. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 4.3 | 4.3..4.3 | 1 | - | - | 4.3 | - | - (stored whole) | - | - | 1650.9 | 938.0 | accuracy=0.899070, auc=0.968973, held_out_rows=100000, log_loss=0.225010, loss_curve_length=1, train_loss_finite=True, train_loss_last_step=0.240776 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.8 | 1.8..1.8 | 1 | 2.423 | - | 1.8 | - | - (stored whole) | 2.423 (whole/whole) | - | 1322.5 | 93.0 | accuracy=0.898660, accuracy_diff_vs_ours=-0.00041, auc=0.968843, auc_diff_vs_ours=-0.0001299, held_out_rows=100000, log_loss=0.225338, log_loss_diff_vs_ours=0.0003281, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.143858 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.4 | 1.4..1.4 | 1 | 3.094 | - | 1.4 | - | - (stored whole) | 3.094 (whole/whole) | - | 1298.2 | 93.0 | accuracy=0.898470, accuracy_diff_vs_ours=-0.0006, auc=0.968846, auc_diff_vs_ours=-0.0001274, held_out_rows=100000, log_loss=0.225332, log_loss_diff_vs_ours=0.0003221, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.143500 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.6 | 1.6..1.6 | 1 | 2.646 | - | 1.6 | - | - (stored whole) | 2.646 (whole/whole) | - | 1276.2 | 77.0 | accuracy=0.898710, accuracy_diff_vs_ours=-0.00036, auc=0.968813, auc_diff_vs_ours=-0.00016, held_out_rows=100000, log_loss=0.225454, log_loss_diff_vs_ours=0.0004447, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.143983 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.6 | 2.6..2.6 | 1 | 1.613 | - | 2.6 | - | - (stored whole) | 1.613 (whole/whole) | - | 1270.3 | 77.0 | accuracy=0.898570, accuracy_diff_vs_ours=-0.0005, auc=0.968837, auc_diff_vs_ours=-0.0001365, held_out_rows=100000, log_loss=0.225378, log_loss_diff_vs_ours=0.0003681, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.144187 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.5 | 1.5..1.5 | 1 | 2.866 | - | 1.5 | - | - (stored whole) | 2.866 (whole/whole) | - | 1470.8 | 60.6 | accuracy=0.898620, accuracy_diff_vs_ours=-0.00045, auc=0.968818, auc_diff_vs_ours=-0.0001549, held_out_rows=100000, log_loss=0.225426, log_loss_diff_vs_ours=0.0004158, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.144841 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 1.9 | 1.9..1.9 | 1 | 2.199 | - | 1.9 | - | - (stored whole) | 2.199 (whole/whole) | - | 1485.6 | 52.6 | accuracy=0.898460, accuracy_diff_vs_ours=-0.00061, auc=0.968821, auc_diff_vs_ours=-0.0001523, held_out_rows=100000, log_loss=0.225425, log_loss_diff_vs_ours=0.0004157, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.143898 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-tf32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-tf32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false | false | false |
| batch_size | 512 | 512 | 512 | 512 | 512 | 512 | 512 |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| epochs | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| layers | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| loss | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" |
| maximize | false | false | false | false | false | false | false |
| optimizer | "adam" | "adam" | "adam" | "adam" | "adam" | "adam" | "adam" |
| seed | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| shuffle | true | true | true | true | true | true | true |
| weight_decay | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### transformer-decode / gaussian (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024)

race: done, driver rc 0, log `logs/neural.transformer-decode.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 861.8 ms) = 1.282; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 749.8 ms) = 1.474. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 1104.9 | 1104.9..1104.9 | 1 | - | - | 1104.9 | - | - (stored whole) | - | - | 1536.1 | 682.0 | host_reference=TransformerBlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 749.8 | 749.8..749.8 | 1 | 1.474 | - | 749.8 | - | - (stored whole) | 1.474 (whole/whole) | - | 1255.2 | 30.9 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 725.3 | 725.3..725.3 | 1 | 1.523 | - | 725.3 | - | - (stored whole) | 1.523 (whole/whole) | - | 1255.5 | 30.9 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 861.8 | 861.8..861.8 | 1 | 1.282 | - | 861.8 | - | - (stored whole) | 1.282 (whole/whole) | - | 1402.5 | 43.8 | max_abs_diff_vs_ours=0.001819, max_rel_diff_vs_ours=0.0003893 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 326.5 | 326.5..326.5 | 1 | 3.384 | - | 326.5 | - | - (stored whole) | 3.384 (whole/whole) | - | 2079.9 | 30.0 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 329.1 | 329.1..329.1 | 1 | 3.358 | - | 329.1 | - | - (stored whole) | 3.358 (whole/whole) | - | 2080.9 | 30.0 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-eager-tf32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-eager-bf16`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-graph-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-graph-tf32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-eager-bf16, torch-graph-fp32, torch-graph-tf32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 | torch-graph-fp32 | torch-graph-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| eps | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 |
| rope_theta | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 |

### transformer-forward / gaussian (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024)

race: done, driver rc 0, log `logs/neural.transformer-forward.gaussian.shape-full.log`, ran on nv-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 2.4 ms) = 2.352; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 2.7 ms) = 2.086. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 5.6 | 5.6..5.6 | 1 | - | - | 5.6 | - | - (stored whole) | - | - | 1526.2 | 908.0 | host_reference=TransformerBlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.018605, rel_fro_vs_torch_eager_fp32=6.056e-08 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.7 | 2.7..2.7 | 1 | 2.086 | - | 2.7 | - | - (stored whole) | 2.086 (whole/whole) | - | 1235.4 | 48.9 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 3.3 | 3.3..3.3 | 1 | 1.681 | - | 3.3 | - | - (stored whole) | 1.681 (whole/whole) | - | 1231.5 | 48.9 | max_abs_diff_vs_ours=0.0002124, max_rel_diff_vs_ours=4.545e-05, max_rel_diff_vs_torch_eager_fp32=11.138132, rel_fro_vs_torch_eager_fp32=2.66e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.7 | 2.7..2.7 | 1 | 2.074 | - | 2.7 | - | - (stored whole) | 2.074 (whole/whole) | - | 1229.9 | 41.8 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07, max_rel_diff_vs_torch_eager_fp32=0.003106, rel_fro_vs_torch_eager_fp32=3.114e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.6 | 2.6..2.6 | 1 | 2.151 | - | 2.6 | - | - (stored whole) | 2.151 (whole/whole) | - | 1188.0 | 41.8 | max_abs_diff_vs_ours=0.0002124, max_rel_diff_vs_ours=4.545e-05, max_rel_diff_vs_torch_eager_fp32=11.118677, rel_fro_vs_torch_eager_fp32=2.659e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 3.7 | 3.7..3.7 | 1 | 1.523 | - | 3.7 | - | - (stored whole) | 1.523 (whole/whole) | - | 1376.7 | 55.8 | max_abs_diff_vs_ours=0.001819, max_rel_diff_vs_ours=0.0003893, max_rel_diff_vs_torch_eager_fp32=118.748732, rel_fro_vs_torch_eager_fp32=0.0002766 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.4 | 2.4..2.4 | 1 | 2.352 | - | 2.4 | - | - (stored whole) | 2.352 (whole/whole) | - | 1434.3 | 46.3 | max_abs_diff_vs_ours=0.001819, max_rel_diff_vs_ours=0.0003893, max_rel_diff_vs_torch_eager_fp32=42.038627, rel_fro_vs_torch_eager_fp32=0.0002631 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-fp32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 2.4 | 2.4..2.4 | 1 | 2.356 | - | 2.4 | - | - (stored whole) | 2.356 (whole/whole) | - | 1238.0 | 30.0 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07, max_rel_diff_vs_torch_eager_fp32=0.000000, rel_fro_vs_torch_eager_fp32=0.000000 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-tf32 | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 3.3 | 3.3..3.3 | 1 | 1.684 | - | 3.3 | - | - (stored whole) | 1.684 (whole/whole) | - | 1234.2 | 30.0 | max_abs_diff_vs_ours=0.0002124, max_rel_diff_vs_ours=4.545e-05, max_rel_diff_vs_torch_eager_fp32=11.138132, rel_fro_vs_torch_eager_fp32=2.66e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-eager-tf32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-compile-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-compile-tf32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-eager-bf16`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-compile-bf16`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-graph-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-graph-tf32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-eager-fp32, torch-eager-tf32, torch-compile-fp32, torch-compile-tf32, torch-eager-bf16, torch-compile-bf16, torch-graph-fp32, torch-graph-tf32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-compile-tf32 | torch-eager-bf16 | torch-eager-fp32 | torch-eager-tf32 | torch-graph-fp32 | torch-graph-tf32 |
|---|---||---|---||---|---||---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| eps | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 |
| rope_theta | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |

## Not covered by this board

- Classical, wave 2: RadiusNeighbors, the preprocessing scalers, HDBSCAN's prediction data, Cholesky and the parallel_* and Distributed* wrappers are public and not raced here; taxi-derived time series are not used (the ARIMA and ExponentialSmoothing lanes fit seeded synthetic series, as the repo's own ARIMA quality work does).
- Classical, wave 2, not planned on this vendor: cuML GaussianMixture, GaussianProcessRegressor/Classifier, Nystroem, RBFSampler: cuML 26.8.0 has none; scikit-learn on the CPU is the arm.
- Classical, wave 2, not planned on this vendor: faiss-gpu: no pinned PyPI wheel for this image; cuVS ivf_flat from the pinned rapids set (cuvs-cu12==26.8.1) is the IVF-Flat GPU arm.
- Classical, wave 2, not planned on this vendor: umap-learn and faiss-cpu: not installed on NVIDIA; cuML UMAP and cuVS are the arms.
- Classical, wave 2, not planned on this vendor: cuML SpectralClustering/SpectralEmbedding: present only in newer cuML; if the pinned 26.8.0 lacks them the arm refuses by name and scikit-learn stands beside it.
- Classical, wave 2, not planned on this vendor: cuML on elasticnet: refused, different algorithm: ours' coordinate descent forms X^T X once and sweeps the Gram; cuML's cd sweeps every row per coordinate and refuses precompute (UnsupportedOnGPU) (2026-10-13 audit); scikit-learn on the CPU is the arm.
- Classical, wave 2, not planned on this vendor: cuML on lasso: refused, different algorithm: ours' coordinate descent forms X^T X once and sweeps the Gram; cuML's cd sweeps every row per coordinate and refuses precompute (UnsupportedOnGPU) (2026-10-13 audit); scikit-learn on the CPU is the arm.
- Classical, wave 2, not planned on this vendor: cuML on linearsvc: refused, different algorithm and model: liblinear (dual='auto' takes its primal trust-region Newton here) with a penalized intercept; ours and cuML L-BFGS on the primal with an unpenalized intercept (2026-10-13 audit); scikit-learn on the CPU is the arm.
- Classical, wave 2, not planned on this vendor: cuML on linearsvr: refused, different algorithm and model: liblinear dual coordinate descent with a penalized intercept; ours and cuML L-BFGS on the primal with an unpenalized intercept (2026-10-13 audit); scikit-learn on the CPU is the arm.
- Classical, wave 2, not planned on this vendor: cuML on ridge: refused, different algorithm: ours solves the centered normal equations by Cholesky (eigendecomposition only when its trust gate rejects the factor); cuML Ridge has no Cholesky solver ('eig' also forms U = A V) (2026-10-13 audit); scikit-learn on the CPU is the arm.
- Classical, wave 2, not planned on this vendor: cuML on tsvd: refused, different algorithm: ours 'covariance_eigh' (the eigendecomposition of X^T X); scikit-learn TruncatedSVD has only 'arpack' (Lanczos on X) and 'randomized', and no CPU library has ours' algorithm (2026-10-13 audit); scikit-learn on the CPU is the arm.
- Inference, trees: a single-row latency batch is not timed (the batches are the held-out split and 1,000,000 training rows); ONNX, Treelite and other export paths are not raced.
- Inference, classical: the classical2 family's predict calls (the linear models, GaussianMixture, SVR, KernelRidge and others in tools/bench_board_more.py) are timed as those lanes define their clocks, not as a separate inference cell; svc times predict, not decision_function.
- Our CPU: never raced or reported; the board races only our GPU (the author, Oct 2 2026). The host column gives same-bits digests only (lq ID).
- Neural, not planned: lm-host-train-step, lm-infer, mamba1-infer, mamba2-infer, mamba3-infer, mlp-infer, samba-infer, transformer-infer: ours runs the CPU binding, and our CPU is never raced, in no numeric mode (the Apple FAST neural tier is the GPU lanes only).
- Memory: GPU memory on Apple has no per-process counter (Metal buffers are inside the host footprint); the trees driver runs every arm in one process, so its GPU figure is the process total; a figure taken at the round's end misses a buffer freed inside the round; inference cells carry memory only on the classical lanes.
- Neural: The Mamba lanes' torch-* arms would be the repo's pure-PyTorch references (mamba/corpus/gen_corpus.py: mamba_ssm's selective_scan_ref for Mamba-1, the chunked SSD reference for Mamba-2, the SISO reference for Mamba-3), not mamba-ssm's fused CUDA/Triton kernels; a reference implementation is not an opponent, so they are refused by name. The Mamba opponent is mamba_ssm's own fused kernels (mamba-ssm-fp32 on NVIDIA and AMD, mamba-ssm-tf32 on NVIDIA), and the Samba torch arms run mamba_ssm's Mamba3 layers with transformers' LlamaDecoderLayer attention; where mamba_ssm is not built (Apple) those lanes have no opponent.
- Neural: The blocks' backward (the Mamba and TransformerBlock VJPs), ragged `lengths` and a prefill followed by decode are public and not raced; the zero-state forward (*-forward) and the zero-state token-by-token decode (*-decode) are.
- Neural: The byte LM has no incremental decode on any route: LanguageModelTrainer (GPU) and LanguageModelInference (CPU) expose full-sequence logits only (lm-forward on the GPU), no KV-cache state or step, so there is no lm-decode row.
- Neural: The *-infer and lm-host-train-step rows are the CPU host binding and are never raced; their GPU twins are the *-forward, *-decode and mlp-predict rows.
- Neural: The GPT-3-small target shape is not on the board (the LM lanes use the smaller control shape so one shape runs on every box, a 16 GB Mac included).
- Neural: The fit lanes time one whole fit (one epoch at the recipe's batch size); the held-out prediction after it is not timed, and multi-epoch fits, early stopping and the classifier variants of the recurrent models are not raced.
- Neural: causal-lm-generate* time greedy generate at one prompt shape (batch 1); batched or sampled decoding, a stop token, a tokenizer in the clock and the low-bit weight formats are not raced; the memory figures come from an untimed pass after each round.
- Neural: sequential-fit times the fit and the held-out predict_proba together; ops-session-step times one recorded step (no multi-step loop, no optimizer state); the session's other operations are timed per operation by tools/ag_opbench.py, not on the board.
- Neural: program-run times one Program.run of a two-layer forward (inference only); the eager session's time for the same forward is the A/B operation program_eager, not a board arm.
- Neural, not planned on this vendor: torch-compile-* on mamba1-forward and mamba1-infer: the only torch Mamba-1 twin is the pure-PyTorch reference scan, a per-token Python loop that torch.compile would unroll L times; mamba1 races the eager arms only
- Neural, not planned on this vendor: gemm-bf16 races torch's bf16 settings only (bf16 operands, fp32 accumulate)
- Neural, not planned on this vendor: mamba1-decode, mamba2-decode, mamba3-decode and samba-decode race ours alone: the repo's torch Mamba references are full-sequence scans with no carried-state decode step (a torch decode twin is not written yet)
- Neural, not planned on this vendor: torch-compile-* on transformer-decode: the twin is a per-token loop over a growing KV cache; transformer-decode races the eager arms only
- Neural, not planned on this vendor: mamba-ssm bf16: our Mamba blocks are float32, so mamba_ssm races in float32 (and its TF32 setting on NVIDIA)
- Neural, not planned on this vendor: mlx-fp32 on the fit lanes: MLX runs on Apple silicon only
- Neural, not planned on this vendor: torch-compile-* on causal-lm-generate*: transformers' generate is a per-token loop over a growing KV cache; the generate lanes race the eager arms only
- Neural, not planned on this vendor: mlx-fp32 on sequential-predict: no MLX prediction twin is written; it races the torch arms

