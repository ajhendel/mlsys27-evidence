# anonlib benchmark board

Generated 2026-10-30T07:36:40Z from `board.json` (schema `anonlib-bench-board/1`).

## Box

| field | value |
|---|---|
| vendor / API | amd / hip |
| GPU | AMD Instinct MI300X VF |
| GPU driver | 6.12.12 |
| CPU | INTEL(R) XEON(R) PLATINUM 8568Y+ (20 logical cores) |
| memory bytes | 253347160064 |
| OS | Ubuntu 24.04.2 LTS |
| Python | 3.12.3 CPython |
| anonlib | 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl, sha256 ca912ce50c59efaeffd64d7b195215d4ea48c67e00c9dabd619475a6be4c1170) |
| script commit | 79fd411391c5b48137c48217b27b06ecef72f45d |
| patch sync | - |
| modes | identical |
| rounds | 1 timed after 1 warm-up, arms interleaved round by round |
| seed | 7 |
| opponent versions | catboost 1.2.10, xgboost 3.2.0, lightgbm 4.7.0, scikit-learn 1.7.2, torch 2.13.0+rocm7.1, umap-learn 0.5.12, pynndescent 0.6.0, numba 0.67.0, statsmodels 0.15.0, faiss-cpu 1.15.1, numpy 2.5.4 |

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

Races: 19 planned, 19 done, 0 failed, 0 unsupported, 0 pending. Cells: 84 (REFUSED 21, ok 63).

## Quality at a glance

Per lane and dataset: our FAST value, our IDENTICAL value, and each opponent's.

| family | lane | dataset | metric | ours FAST | ours IDENTICAL | opponents |
|---|---|---|---|---|---|---|
| neural | gemm-bf16 | gaussian | max_rel_err_vs_fp64 (lower is better) | - | 1.155e-07 | torch-eager-bf16 0.002759; torch-compile-bf16 0.002759 |
| neural | gemm-bf16 | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-bf16 0.999023; torch-compile-bf16 0.999023 |
| neural | gemm-bf16 | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-bf16 0.002759; torch-compile-bf16 0.002759 |
| neural | gemm-int8 | gaussian | max_rel_err_vs_fp64 (lower is better) | - | 0.000000 | - |
| neural | gemm | gaussian | max_rel_err_vs_fp64 (lower is better) | - | 2.399e-07 | torch-eager-fp32 2.802e-06; torch-compile-fp32 2.802e-06; torch-eager-bf16 0.003752; torch-compile-bf16 0.003752 |
| neural | gemm | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 0.001038; torch-compile-fp32 0.001038; torch-eager-bf16 1.358337; torch-compile-bf16 1.358337 |
| neural | gemm | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 2.866e-06; torch-compile-fp32 2.866e-06; torch-eager-bf16 0.003751; torch-compile-bf16 0.003751 |
| neural | lm-forward | bytes | mean_nll (lower is better) | - | 9.015586 | torch-eager-fp32 9.015586; torch-compile-fp32 9.015586; torch-eager-bf16 9.015493; torch-compile-bf16 9.015495; torch-graph-fp32 9.015586 |
| neural | lm-forward | bytes | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.401e-06; torch-compile-fp32 1.371e-06; torch-eager-bf16 0.006313; torch-compile-bf16 0.006870; torch-graph-fp32 1.386e-06 |
| neural | lm-forward | bytes | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.923e-06; torch-compile-fp32 1.882e-06; torch-eager-bf16 0.008666; torch-compile-bf16 0.009432; torch-graph-fp32 1.902e-06 |
| neural | lm-train-step | bytes | loss_first_step (same init and batches on every arm) | - | 9.015587 | torch-eager-fp32 9.015587; torch-compile-fp32 9.015586; torch-eager-bf16 9.015492; torch-compile-bf16 9.015494 |
| neural | lm-train-step | bytes | loss_last_step (same init and batches on every arm) | - | 8.405828 | torch-eager-fp32 8.405828; torch-compile-fp32 8.405828; torch-eager-bf16 8.404669; torch-compile-bf16 8.404747 |
| neural | lm-train-step | bytes | steps | - | 2 | torch-eager-fp32 2; torch-compile-fp32 2; torch-eager-bf16 2; torch-compile-bf16 2 |
| neural | lm-train-step | bytes | loss_first_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 0.000000; torch-compile-fp32 9.537e-07; torch-eager-bf16 9.441e-05; torch-compile-bf16 9.251e-05 |
| neural | lm-train-step | bytes | loss_last_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 9.537e-07; torch-compile-fp32 0.000000; torch-eager-bf16 0.001159; torch-compile-bf16 0.001081 |
| neural | mamba1-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 - |
| neural | mamba1-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 - |
| neural | mamba1-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 - |
| neural | mamba1-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 - |
| neural | mamba1-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 - |
| neural | mamba1-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.0003555 | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 0.0005092 |
| neural | mamba1-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 7.442e-09 | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 7.345e-09 |
| neural | mamba1-forward | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 2.384e-07 |
| neural | mamba1-forward | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-eager-bf16 -; mamba-ssm-fp32 1.189e-07 |
| neural | mamba2-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba2-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba2-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba2-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba2-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba2-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.195652 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 0.051988 |
| neural | mamba2-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 1.372e-07 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 7.515e-08 |
| neural | mamba2-forward | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 1.013e-06 |
| neural | mamba2-forward | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 3.445e-07 |
| neural | mamba3-decode | gaussian | host_reference_atol | - | 1e-06 | - |
| neural | mamba3-decode | gaussian | host_reference_rtol | - | 1e-05 | - |
| neural | mamba3-decode | gaussian | host_reference_tolerance_ratio | - | 0.000000 | - |
| neural | mamba3-decode | gaussian | max_abs_diff_vs_host | - | 0.000000 | - |
| neural | mamba3-decode | gaussian | max_rel_diff_vs_host | - | 0.000000 | - |
| neural | mamba3-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba3-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba3-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba3-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba3-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba3-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.013978 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mamba3-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 5.247e-08 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; mamba-ssm-fp32 - |
| neural | mlp-train-step | gaussian | loss_first_step (same init and batches on every arm) | - | 1.160401 | torch-eager-fp32 1.160401; torch-compile-fp32 1.160401; torch-eager-bf16 1.160498; torch-compile-bf16 1.160498 |
| neural | mlp-train-step | gaussian | loss_last_step (same init and batches on every arm) | - | 1.123361 | torch-eager-fp32 1.123361; torch-compile-fp32 1.123361; torch-eager-bf16 1.123461; torch-compile-bf16 1.123461 |
| neural | mlp-train-step | gaussian | steps | - | 2 | torch-eager-fp32 2; torch-compile-fp32 2; torch-eager-bf16 2; torch-compile-bf16 2 |
| neural | mlp-train-step | gaussian | loss_first_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 2.384e-07; torch-compile-fp32 2.384e-07; torch-eager-bf16 9.656e-05; torch-compile-bf16 9.656e-05 |
| neural | mlp-train-step | gaussian | loss_last_abs_diff_vs_ours (0 is our value exactly) | - | - | torch-eager-fp32 2.384e-07; torch-compile-fp32 2.384e-07; torch-eager-bf16 0.0001005; torch-compile-bf16 0.0001006 |
| neural | ops-session-step | gaussian | loss | - | 2.798163 | torch-eager-fp32 2.798162; torch-compile-fp32 2.798162; torch-eager-bf16 2.798156; torch-compile-bf16 2.798155 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_b1 | - | - | torch-eager-fp32 7.567e-10; torch-compile-fp32 8.149e-10; torch-eager-bf16 5.06e-05; torch-compile-bf16 5.06e-05 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_b2 | - | - | torch-eager-fp32 7.451e-09; torch-compile-fp32 6.519e-09; torch-eager-bf16 3.965e-05; torch-compile-bf16 3.966e-05 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_w1 | - | - | torch-eager-fp32 2.794e-09; torch-compile-fp32 2.736e-09; torch-eager-bf16 7.59e-05; torch-compile-bf16 7.59e-05 |
| neural | ops-session-step | gaussian | grad_max_abs_diff_vs_ours_w2 | - | - | torch-eager-fp32 4.191e-09; torch-compile-fp32 4.191e-09; torch-eager-bf16 3.952e-05; torch-compile-bf16 3.952e-05 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_b1 | - | - | torch-eager-fp32 4.983e-07; torch-compile-fp32 5.367e-07; torch-eager-bf16 0.033320; torch-compile-bf16 0.033320 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_b2 | - | - | torch-eager-fp32 3.545e-07; torch-compile-fp32 3.102e-07; torch-eager-bf16 0.001887; torch-compile-bf16 0.001887 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_w1 | - | - | torch-eager-fp32 2.102e-06; torch-compile-fp32 2.059e-06; torch-eager-bf16 0.057112; torch-compile-bf16 0.057112 |
| neural | ops-session-step | gaussian | grad_max_rel_diff_vs_ours_w2 | - | - | torch-eager-fp32 4.676e-07; torch-compile-fp32 4.676e-07; torch-eager-bf16 0.004410; torch-compile-bf16 0.004410 |
| neural | ops-session-step | gaussian | loss_abs_diff_vs_ours | - | - | torch-eager-fp32 7.153e-07; torch-compile-fp32 7.153e-07; torch-eager-bf16 7.153e-06; torch-compile-bf16 7.391e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_b1 | - | - | torch-eager-fp32 9.313e-10; torch-compile-fp32 9.313e-10; torch-eager-bf16 2.53e-06; torch-compile-bf16 2.53e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_b2 | - | - | torch-eager-fp32 1.863e-09; torch-compile-fp32 1.863e-09; torch-eager-bf16 1.983e-06; torch-compile-bf16 1.983e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_w1 | - | - | torch-eager-fp32 3.725e-09; torch-compile-fp32 3.725e-09; torch-eager-bf16 3.795e-06; torch-compile-bf16 3.795e-06 |
| neural | ops-session-step | gaussian | param_max_abs_diff_vs_ours_w2 | - | - | torch-eager-fp32 3.725e-09; torch-compile-fp32 3.725e-09; torch-eager-bf16 1.978e-06; torch-compile-bf16 1.978e-06 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_b1 | - | - | torch-eager-fp32 1.491e-08; torch-compile-fp32 1.491e-08; torch-eager-bf16 4.05e-05; torch-compile-bf16 4.05e-05 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_b2 | - | - | torch-eager-fp32 4.874e-08; torch-compile-fp32 4.874e-08; torch-eager-bf16 5.188e-05; torch-compile-bf16 5.188e-05 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_w1 | - | - | torch-eager-fp32 5.958e-08; torch-compile-fp32 5.958e-08; torch-eager-bf16 6.069e-05; torch-compile-bf16 6.069e-05 |
| neural | ops-session-step | gaussian | param_max_rel_diff_vs_ours_w2 | - | - | torch-eager-fp32 8.398e-08; torch-compile-fp32 8.398e-08; torch-eager-bf16 4.459e-05; torch-compile-bf16 4.459e-05 |
| neural | program-run | gaussian | max_abs_err_vs_fp64 | - | 7.398e-08 | torch-eager-fp32 3.382e-08; torch-compile-fp32 3.382e-08; torch-eager-bf16 0.0004913; torch-compile-bf16 0.0004913 |
| neural | program-run | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 8.941e-08; torch-compile-fp32 8.941e-08; torch-eager-bf16 0.0004913; torch-compile-bf16 0.0004913 |
| neural | program-run | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 5.226e-07; torch-compile-fp32 5.226e-07; torch-eager-bf16 0.002871; torch-compile-bf16 0.002871 |
| neural | samba-decode | bytes | mean_nll (lower is better) | - | 5.640151 | - |
| neural | samba-forward | bytes | mean_nll (lower is better) | - | 5.640151 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 - |
| neural | samba-train-step | bytes | loss_first_step (same init and batches on every arm) | - | 5.640152 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 - |
| neural | samba-train-step | bytes | loss_last_step (same init and batches on every arm) | - | 4.822321 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 - |
| neural | samba-train-step | bytes | steps | - | 2 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 - |
| neural | sequential-fit | synthetic | accuracy (higher is better) | - | 0.899070 | torch-eager-fp32 0.898840; torch-compile-fp32 0.898600; torch-eager-bf16 0.898680; torch-compile-bf16 0.898850 |
| neural | sequential-fit | synthetic | auc (higher is better) | - | 0.968973 | torch-eager-fp32 0.968881; torch-compile-fp32 0.968864; torch-eager-bf16 0.968887; torch-compile-bf16 0.968878 |
| neural | sequential-fit | synthetic | held_out_rows | - | 100000 | torch-eager-fp32 100000; torch-compile-fp32 100000; torch-eager-bf16 100000; torch-compile-bf16 100000 |
| neural | sequential-fit | synthetic | log_loss | - | 0.225010 | torch-eager-fp32 0.225140; torch-compile-fp32 0.225195; torch-eager-bf16 0.225122; torch-compile-bf16 0.225149 |
| neural | sequential-fit | synthetic | loss_curve_length | - | 1 | torch-eager-fp32 1954; torch-compile-fp32 1954; torch-eager-bf16 1954; torch-compile-bf16 1954 |
| neural | sequential-fit | synthetic | train_loss_last_step | - | 0.240776 | torch-eager-fp32 0.196202; torch-compile-fp32 0.198931; torch-eager-bf16 0.197198; torch-compile-bf16 0.199082 |
| neural | sequential-fit | synthetic | accuracy_diff_vs_ours | - | - | torch-eager-fp32 -0.00023; torch-compile-fp32 -0.00047; torch-eager-bf16 -0.00039; torch-compile-bf16 -0.00022 |
| neural | sequential-fit | synthetic | auc_diff_vs_ours | - | - | torch-eager-fp32 -9.22e-05; torch-compile-fp32 -0.0001094; torch-eager-bf16 -8.646e-05; torch-compile-bf16 -9.545e-05 |
| neural | sequential-fit | synthetic | log_loss_diff_vs_ours | - | - | torch-eager-fp32 0.0001306; torch-compile-fp32 0.0001857; torch-eager-bf16 0.0001118; torch-compile-bf16 0.0001394 |
| neural | sequential-predict | synthetic | accuracy (higher is better) | - | 0.899070 | torch-eager-fp32 0.898840; torch-compile-fp32 0.898890; torch-eager-bf16 0.898680; torch-compile-bf16 0.898750 |
| neural | sequential-predict | synthetic | auc (higher is better) | - | 0.968973 | torch-eager-fp32 0.968881; torch-compile-fp32 0.968882; torch-eager-bf16 0.968887; torch-compile-bf16 0.968875 |
| neural | sequential-predict | synthetic | held_out_rows | - | 100000 | torch-eager-fp32 100000; torch-compile-fp32 100000; torch-eager-bf16 100000; torch-compile-bf16 100000 |
| neural | sequential-predict | synthetic | log_loss | - | 0.225010 | torch-eager-fp32 0.225140; torch-compile-fp32 0.225134; torch-eager-bf16 0.225122; torch-compile-bf16 0.225178 |
| neural | sequential-predict | synthetic | loss_curve_length | - | 1 | torch-eager-fp32 1954; torch-compile-fp32 1954; torch-eager-bf16 1954; torch-compile-bf16 1954 |
| neural | sequential-predict | synthetic | train_loss_last_step | - | 0.240776 | torch-eager-fp32 0.196202; torch-compile-fp32 0.197984; torch-eager-bf16 0.197198; torch-compile-bf16 0.198718 |
| neural | sequential-predict | synthetic | accuracy_diff_vs_ours | - | - | torch-eager-fp32 -0.00023; torch-compile-fp32 -0.00018; torch-eager-bf16 -0.00039; torch-compile-bf16 -0.00032 |
| neural | sequential-predict | synthetic | auc_diff_vs_ours | - | - | torch-eager-fp32 -9.22e-05; torch-compile-fp32 -9.159e-05; torch-eager-bf16 -8.646e-05; torch-compile-bf16 -9.826e-05 |
| neural | sequential-predict | synthetic | log_loss_diff_vs_ours | - | - | torch-eager-fp32 0.0001306; torch-compile-fp32 0.0001245; torch-eager-bf16 0.0001118; torch-compile-bf16 0.0001686 |
| neural | transformer-decode | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-eager-bf16 -; torch-graph-fp32 - |
| neural | transformer-decode | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-eager-bf16 -; torch-graph-fp32 - |
| neural | transformer-decode | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-eager-bf16 -; torch-graph-fp32 - |
| neural | transformer-decode | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-bf16 -; torch-graph-fp32 - |
| neural | transformer-decode | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-eager-bf16 -; torch-graph-fp32 - |
| neural | transformer-decode | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 4.768e-07; torch-eager-bf16 0.001819; torch-graph-fp32 - |
| neural | transformer-decode | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.02e-07; torch-eager-bf16 0.0003893; torch-graph-fp32 - |
| neural | transformer-forward | gaussian | host_reference_atol | - | 1e-06 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 - |
| neural | transformer-forward | gaussian | host_reference_rtol | - | 1e-05 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 - |
| neural | transformer-forward | gaussian | host_reference_tolerance_ratio | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 - |
| neural | transformer-forward | gaussian | max_abs_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 - |
| neural | transformer-forward | gaussian | max_rel_diff_vs_host | - | 0.000000 | torch-eager-fp32 -; torch-compile-fp32 -; torch-eager-bf16 -; torch-compile-bf16 -; torch-graph-fp32 - |
| neural | transformer-forward | gaussian | max_rel_diff_vs_torch_eager_fp32 | - | 0.015169 | torch-eager-fp32 -; torch-compile-fp32 0.005081; torch-eager-bf16 76.084014; torch-compile-bf16 41.369141; torch-graph-fp32 0.000000 |
| neural | transformer-forward | gaussian | rel_fro_vs_torch_eager_fp32 (0 is the eager FP32 torch output exactly) | - | 5.717e-08 | torch-eager-fp32 -; torch-compile-fp32 3.096e-08; torch-eager-bf16 0.0002764; torch-compile-bf16 0.0002629; torch-graph-fp32 0.000000 |
| neural | transformer-forward | gaussian | max_abs_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 4.768e-07; torch-compile-fp32 4.768e-07; torch-eager-bf16 0.001819; torch-compile-bf16 0.001819; torch-graph-fp32 4.768e-07 |
| neural | transformer-forward | gaussian | max_rel_diff_vs_ours (0 is our output exactly) | - | - | torch-eager-fp32 1.02e-07; torch-compile-fp32 1.02e-07; torch-eager-bf16 0.0003893; torch-compile-bf16 0.0003893; torch-graph-fp32 1.02e-07 |


## Neural headline: ours IDENTICAL against torch bf16

What customers run is torch in bf16. The headline divides our IDENTICAL median by torch's fastest bf16 arm (eager or compile, the lower stored median); the fp32 twin (torch's fastest fp32 arm) is the second column. Per-arm ratios stay in each race's table below.

| lane | dataset | ours IDENTICAL ms | torch bf16 ms (fastest arm) | ours / torch bf16 | torch fp32 twin ms (fastest arm) | ours / torch fp32 | note |
|---|---|---|---|---|---|---|---|
| gemm-bf16 | gaussian | 48.5 | 17.1 (torch-eager-bf16) | 2.832 | - | - | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| gemm-int8 | gaussian | 38.7 | - | - | - | - | no torch bf16 arm on this lane |
| gemm | gaussian | 65.8 | 19.3 (torch-eager-bf16) | 3.410 | 20.4 (torch-eager-fp32) | 3.233 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| lm-forward | bytes | 58.5 | 20.4 (torch-compile-bf16) | 2.861 | 18.4 (torch-eager-fp32) | 3.182 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| lm-train-step | bytes | 43.9 | 9.7 (torch-compile-bf16) | 4.526 | 14.7 (torch-compile-fp32) | 2.992 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| mamba1-forward | gaussian | 3.0 | - | - | - | - | no torch bf16 arm on this lane |
| mamba2-forward | gaussian | 5.3 | - | - | - | - | no torch bf16 arm on this lane |
| mamba3-decode | gaussian | 2872.7 | - | - | - | - | no torch bf16 arm on this lane |
| mamba3-forward | gaussian | 3.5 | - | - | - | - | no torch bf16 arm on this lane |
| mlp-train-step | gaussian | 3.3 | 1.8 (torch-compile-bf16) | 1.840 | 1.8 (torch-eager-fp32) | 1.797 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| ops-session-step | gaussian | 2.4 | 2.2 (torch-compile-bf16) | 1.076 | 2.5 (torch-eager-fp32) | 0.944 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| program-run | gaussian | 1.2 | 0.7 (torch-compile-bf16) | 1.884 | 0.6 (torch-eager-fp32) | 2.103 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| samba-decode | bytes | 3708.3 | - | - | - | - | no torch bf16 arm on this lane |
| samba-forward | bytes | 6.1 | - | - | - | - | no torch bf16 arm on this lane |
| samba-train-step | bytes | 53.6 | - | - | - | - | no torch bf16 arm on this lane |
| sequential-fit | synthetic | 440.0 | 2092.2 (torch-compile-bf16) | 0.210 | 1661.0 (torch-eager-fp32) | 0.265 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| sequential-predict | synthetic | 4.2 | 1.2 (torch-eager-bf16) | 3.406 | 1.1 (torch-eager-fp32) | 3.732 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| transformer-decode | gaussian | 2444.7 | 1094.0 (torch-eager-bf16) | 2.235 | 929.1 (torch-eager-fp32) | 2.631 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |
| transformer-forward | gaussian | 8.0 | 1.7 (torch-eager-bf16) | 4.708 | 1.4 (torch-compile-fp32) | 5.705 | torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax |

## Neural

### gemm-bf16 / gaussian (neural shape full: 4096x4096x4096)

race: done, driver rc 0, log `logs/neural.gemm-bf16.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 17.1 ms) = 2.832; fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 48.5 | 48.5..48.5 | 1 | - | - | 48.5 | - | - (stored whole) | - | - | 2230.7 | 4268.4 | max_rel_err_vs_fp64=1.155e-07 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 17.1 | 17.1..17.1 | 1 | 2.832 | - | 17.1 | - | - (stored whole) | 2.832 (whole/whole) | - | 2880.3 | 312.0 | max_abs_diff_vs_ours=0.999023, max_rel_diff_vs_ours=0.002759, max_rel_err_vs_fp64=0.002759 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 18.3 | 18.3..18.3 | 1 | 2.650 | - | 18.3 | - | - (stored whole) | 2.650 (whole/whole) | - | 2956.1 | 312.0 | max_abs_diff_vs_ours=0.999023, max_rel_diff_vs_ours=0.002759, max_rel_err_vs_fp64=0.002759 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.matmul_bf16(operand_value_type='bfloat16', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-eager-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='bfloat16', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-compile-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='bfloat16', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/192319/vram_* bytes for this pid at the round's end (not a peak)

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

race: done, driver rc 0, log `logs/neural.gemm-int8.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 38.7 | 38.7..38.7 | 1 | - | - | 38.7 | - | - (stored whole) | - | - | 891.1 | 1698.3 | max_rel_err_vs_fp64=0.000000 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.matmul_int8(operand_value_type='int8', operation='matmul', seed=7, transpose_b=True, a=int8[4096x4096], b=int8[4096x4096])`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/192958/vram_* bytes for this pid at the round's end (not a peak)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (declared) |
| input_arrays | {"a": {"dtype": "int8", "sha256": "4157ef2ec27e9864de38ff7e412e678d3fa3de8978b6dd6630b961545d5ac553", "shape": [4096, 4096]}, "b": {"dtype": "int8", "sha256": "43e1e9a5539cbe4b30b30b49e55820f96c3688e9245c43972f6fd0e7dea508fd", "shape": [4096, 4096]}} |
| operand_value_type | "int8" |
| operation | "matmul" |
| seed | 7 |
| transpose_b | true |

### gemm / gaussian (neural shape full: 4096x4096x4096)

race: done, driver rc 0, log `logs/neural.gemm.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 19.3 ms) = 3.410; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 20.4 ms) = 3.233. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 65.8 | 65.8..65.8 | 1 | - | - | 65.8 | - | - (stored whole) | - | - | 2295.3 | 4268.3 | max_rel_err_vs_fp64=2.399e-07 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 20.4 | 20.4..20.4 | 1 | 3.233 | - | 20.4 | - | - (stored whole) | 3.233 (whole/whole) | - | 2022.9 | 268.0 | max_abs_diff_vs_ours=0.001038, max_rel_diff_vs_ours=2.866e-06, max_rel_err_vs_fp64=2.802e-06 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 22.3 | 22.3..22.3 | 1 | 2.948 | - | 22.3 | - | - (stored whole) | 2.948 (whole/whole) | - | 2093.0 | 268.0 | max_abs_diff_vs_ours=0.001038, max_rel_diff_vs_ours=2.866e-06, max_rel_err_vs_fp64=2.802e-06 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 19.3 | 19.3..19.3 | 1 | 3.410 | - | 19.3 | - | - (stored whole) | 3.410 (whole/whole) | - | 2819.6 | 376.0 | max_abs_diff_vs_ours=1.358337, max_rel_diff_vs_ours=0.003751, max_rel_err_vs_fp64=0.003752 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 20.2 | 20.2..20.2 | 1 | 3.260 | - | 20.2 | - | - (stored whole) | 3.260 (whole/whole) | - | 3145.2 | 376.0 | max_abs_diff_vs_ours=1.358337, max_rel_diff_vs_ours=0.003751, max_rel_err_vs_fp64=0.003752 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-eager-fp32`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-compile-fp32`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-eager-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`
- `torch-compile-bf16`: `torch._VariableFunctionsClass.matmul(operand_value_type='float32', operation='matmul', seed=7, transpose_b=False, a=float32[4096x4096], b=float32[4096x4096])`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/193288/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| input_arrays | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} | {"a": {"dtype": "float32", "sha256": "485a7287793a9d7d33d710ea2820ea9c7519d31100db4bafeee813baa532dd7d", "shape": [4096, 4096]}, "b": {"dtype": "float32", "sha256": "3f38db408e287e78e700728b77d904ea5344de168156ad74431c2148fc961104", "shape": [4096, 4096]}} |
| operand_value_type | "float32" | "float32" | "float32" | "float32" | "float32" |
| operation | "matmul" | "matmul" | "matmul" | "matmul" | "matmul" |
| seed | 7 | 7 | 7 | 7 | 7 |
| transpose_b | false | false | false | false | false |

### lm-forward / bytes (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024 layers8 V8192)

race: done, driver rc 0, log `logs/neural.lm-forward.bytes.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 20.4 ms) = 2.861; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 18.4 ms) = 3.182. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 58.5 | 58.5..58.5 | 1 | - | - | 58.5 | - | - (stored whole) | - | - | 2586.2 | 8554.2 | mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 18.4 | 18.4..18.4 | 1 | 3.182 | - | 18.4 | - | - (stored whole) | 3.182 (whole/whole) | - | 4223.4 | 221.5 | max_abs_diff_vs_ours=1.401e-06, max_rel_diff_vs_ours=1.923e-06, mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 21.1 | 21.1..21.1 | 1 | 2.770 | - | 21.1 | - | - (stored whole) | 2.770 (whole/whole) | - | 3487.5 | 242.0 | max_abs_diff_vs_ours=1.371e-06, max_rel_diff_vs_ours=1.882e-06, mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 25.3 | 25.3..25.3 | 1 | 2.314 | - | 25.3 | - | - (stored whole) | 2.314 (whole/whole) | - | 3976.4 | 326.5 | max_abs_diff_vs_ours=0.006313, max_rel_diff_vs_ours=0.008666, mean_nll=9.015493 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 20.4 | 20.4..20.4 | 1 | 2.861 | - | 20.4 | - | - (stored whole) | 2.861 (whole/whole) | - | 3270.1 | 326.5 | max_abs_diff_vs_ours=0.006870, max_rel_diff_vs_ours=0.009432, mean_nll=9.015495 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 21.3 | 21.3..21.3 | 1 | 2.748 | - | 21.3 | - | - (stored whole) | 2.748 (whole/whole) | - | 4674.2 | 294.5 | max_abs_diff_vs_ours=1.386e-06, max_rel_diff_vs_ours=1.902e-06, mean_nll=9.015586 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-compile-fp32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-eager-bf16`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-compile-bf16`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`
- `torch-graph-fp32`: `transformers.LlamaForCausalLM(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/194439/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16, torch-graph-fp32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 | torch-graph-fp32 |
|---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 |

### lm-train-step / bytes (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024 layers8 V8192)

race: done, driver rc 0, log `logs/neural.lm-train-step.bytes.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 9.7 ms) = 4.526; fp32 twin: ours IDENTICAL / torch fp32 (torch-compile-fp32, 14.7 ms) = 2.992. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 43.9 | 43.9..43.9 | 1 | - | - | 43.9 | - | - (stored whole) | - | - | 2459.8 | 8158.6 | loss_first_step=9.015587, loss_last_step=8.405828, steps=2 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 17.0 | 17.0..17.0 | 1 | 2.576 | - | 17.0 | - | - (stored whole) | 2.576 (whole/whole) | - | 5073.6 | 1089.6 | loss_first_abs_diff_vs_ours=0.000000, loss_first_step=9.015587, loss_last_abs_diff_vs_ours=9.537e-07, loss_last_step=8.405828, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 14.7 | 14.7..14.7 | 1 | 2.992 | - | 14.7 | - | - (stored whole) | 2.992 (whole/whole) | - | 5076.3 | 880.1 | loss_first_abs_diff_vs_ours=9.537e-07, loss_first_step=9.015586, loss_last_abs_diff_vs_ours=0.000000, loss_last_step=8.405828, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 19.4 | 19.4..19.4 | 1 | 2.263 | - | 19.4 | - | - (stored whole) | 2.263 (whole/whole) | - | 4095.6 | 961.6 | loss_first_abs_diff_vs_ours=9.441e-05, loss_first_step=9.015492, loss_last_abs_diff_vs_ours=0.001159, loss_last_step=8.404669, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 9.7 | 9.7..9.7 | 1 | 4.526 | - | 9.7 | - | - (stored whole) | 4.526 (whole/whole) | - | 3363.2 | 693.6 | loss_first_abs_diff_vs_ours=9.251e-05, loss_first_step=9.015494, loss_last_abs_diff_vs_ours=0.001081, loss_last_step=8.404747, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-compile-fp32`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-eager-bf16`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`
- `torch-compile-bf16`: `transformers.LlamaForCausalLM(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/195969/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| capturable | - | false | false | false | false |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": 8, \"n_heads\": 6, \"n_kv_heads\": 6, \"param_dtype\": \"float32\", \"tied_head\": false, \"vocab\": 8192}" |
| decoupled_weight_decay | true | true | true | true | true |
| differentiable | - | false | false | false | false |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| foreach | - | null | null | null | null |
| fused | - | null | null | null | null |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| maximize | false | false | false | false | false |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 |
| weight_decay | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |

accepted difference: torch-eager-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

### mamba1-forward / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba1-forward.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 3.0 | 3.0..3.0 | 1 | - | - | 3.0 | - | - (stored whole) | - | - | 2050.1 | 2348.6 | host_reference=Mamba1BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.0003555, rel_fro_vs_torch_eager_fp32=7.442e-09 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba1-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba1-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| mamba-ssm-fp32 | mamba-ssm | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 1.4 | 1.4..1.4 | 1 | 2.151 | - | 1.4 | - | - (stored whole) | 2.151 (whole/whole) | - | 3671.6 | 122.5 | max_abs_diff_vs_ours=2.384e-07, max_rel_diff_vs_ours=1.189e-07, max_rel_diff_vs_torch_eager_fp32=0.0005092, rel_fro_vs_torch_eager_fp32=7.345e-09 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `mamba-ssm-fp32`: `mamba_ssm.Block(seed=7, ssm_d_conv=4, ssm_d_state=16, ssm_dt_rank=24, ssm_expand=2)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/197221/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-eager-bf16: host not sampled; GPU not sampled

memory, mamba-ssm-fp32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | mamba-ssm-fp32 | ours |
|---|---||---|---|
| library (source) | mamba-ssm (declared) | anonlib (declared) |
| seed | 7 | "none (deterministic)" |
| ssm_d_conv | 4 | 4 |
| ssm_d_state | 16 | 16 |
| ssm_dt_rank | 24 | 24 |
| ssm_expand | 2 | 2 |

### mamba2-forward / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba2-forward.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 5.3 | 5.3..5.3 | 1 | - | - | 5.3 | - | - (stored whole) | - | - | 2054.1 | 2348.7 | host_reference=Mamba2BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.195652, rel_fro_vs_torch_eager_fp32=1.372e-07 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba2-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| mamba-ssm-fp32 | mamba-ssm | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | 2.7 | 2.7..2.7 | 1 | 1.949 | - | 2.7 | - | - (stored whole) | 1.949 (whole/whole) | - | 3400.3 | 126.5 | max_abs_diff_vs_ours=1.013e-06, max_rel_diff_vs_ours=3.445e-07, max_rel_diff_vs_torch_eager_fp32=0.051988, rel_fro_vs_torch_eager_fp32=7.515e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `mamba-ssm-fp32`: `mamba_ssm.Block(seed=7, ssm_chunk_size=256, ssm_d_conv=4, ssm_d_state=128, ssm_dt_limit=[0, inf], ssm_expand=2, ssm_headdim=64, ssm_ngroups=1)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/197843/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host not sampled; GPU not sampled

memory, mamba-ssm-fp32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | mamba-ssm-fp32 | ours |
|---|---||---|---|
| library (source) | mamba-ssm (declared) | anonlib (declared) |
| seed | 7 | "none (deterministic)" |
| ssm_chunk_size | 256 | 256 |
| ssm_d_conv | 4 | 4 |
| ssm_d_state | 128 | 128 |
| ssm_dt_limit | [0.0, Infinity] | [0.0, Infinity] |
| ssm_expand | 2 | 2 |
| ssm_headdim | 64 | 64 |
| ssm_ngroups | 1 | 1 |

### mamba3-decode / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba3-decode.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 2872.7 | 2872.7..2872.7 | 1 | - | - | 2872.7 | - | - (stored whole) | - | - | 2238.4 | 1876.1 | host_reference=Mamba3BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/198420/vram_* bytes for this pid at the round's end (not a peak)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (declared) |
| seed | "none (deterministic)" |

### mamba3-forward / gaussian (neural shape full: B1 L2048 DM384)

race: done, driver rc 0, log `logs/neural.mamba3-forward.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 3.5 | 3.5..3.5 | 1 | - | - | 3.5 | - | - (stored whole) | - | - | 2054.6 | 2348.7 | host_reference=Mamba3BlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.013978, rel_fro_vs_torch_eager_fp32=5.247e-08 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(refused: "not an opponent: the torch twin of mamba3-forward is a pure-PyTorch reference implementation (mamba/corpus/gen_corpus.py), not a library kernel; mamba_ssm's fused kernels are the opponent only where ) (measured this run) |
| mamba-ssm-fp32 | mamba-ssm | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | mamba-ssm 2.3.2.post1+ge9594ce1c732 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "worker returned no protocol message: worker_exited", "event": "error", "read_failure": {"deadline_s": 1800, "elapsed_s": 4.365965950999453, "reason": "eof"}, "reason": "worker_exited", "ret) (measured this run) |

calls:
- `mamba-ssm-fp32`: `mamba_ssm.Block(seed=7, ssm_chunk_size=64, ssm_d_state=128, ssm_expand=2, ssm_headdim=64, ssm_ngroups=1, ssm_rope_angles=32)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/198899/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16, mamba-ssm-fp32: host not sampled; GPU not sampled

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | mamba-ssm-fp32 | ours |
|---|---||---|---|
| library (source) | mamba-ssm (declared) | anonlib (declared) |
| seed | 7 | "none (deterministic)" |
| ssm_chunk_size | 64 | 64 |
| ssm_d_state | 128 | 128 |
| ssm_expand | 2 | 2 |
| ssm_headdim | 64 | 64 |
| ssm_ngroups | 1 | 1 |
| ssm_rope_angles | 32 | 32 |

### mlp-train-step / gaussian (neural shape full: rows256 8-16-3)

race: done, driver rc 0, log `logs/neural.mlp-train-step.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 1.8 ms) = 1.840; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 1.8 ms) = 1.797. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 3.3 | 3.3..3.3 | 1 | - | - | 3.3 | - | - (stored whole) | - | - | 2044.5 | 1698.5 | loss_first_step=1.160401, loss_last_step=1.123361, steps=2 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.8 | 1.8..1.8 | 1 | 1.797 | - | 1.8 | - | - (stored whole) | 1.797 (whole/whole) | - | 4421.6 | 152.1 | loss_first_abs_diff_vs_ours=2.384e-07, loss_first_step=1.160401, loss_last_abs_diff_vs_ours=2.384e-07, loss_last_step=1.123361, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2.1 | 2.1..2.1 | 1 | 1.604 | - | 2.1 | - | - (stored whole) | 1.604 (whole/whole) | - | 4336.9 | 152.1 | loss_first_abs_diff_vs_ours=2.384e-07, loss_first_step=1.160401, loss_last_abs_diff_vs_ours=2.384e-07, loss_last_step=1.123361, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.9 | 1.9..1.9 | 1 | 1.743 | - | 1.9 | - | - (stored whole) | 1.743 (whole/whole) | - | 2775.1 | 152.0 | loss_first_abs_diff_vs_ours=9.656e-05, loss_first_step=1.160498, loss_last_abs_diff_vs_ours=0.0001005, loss_last_step=1.123461, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.8 | 1.8..1.8 | 1 | 1.840 | - | 1.8 | - | - (stored whole) | 1.840 (whole/whole) | - | 2899.3 | 152.0 | loss_first_abs_diff_vs_ours=9.656e-05, loss_first_step=1.160498, loss_last_abs_diff_vs_ours=0.0001006, loss_last_step=1.123461, steps=2 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-compile-fp32`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-eager-bf16`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`
- `torch-compile-bf16`: `torch.Sequential(amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"activation": "relu", "bias": true, "d_in":..., decoupled_weight_decay=True, differentiable=False, eps=1e-08, lr=0.001, maximize=False, seed=7, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/199548/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| capturable | - | false | false | false | false |
| config_readback | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" | "{\"activation\": \"relu\", \"bias\": true, \"d_in\": 8, \"d_out\": 3, \"hidden\": 16}" |
| decoupled_weight_decay | true | true | true | true | true |
| differentiable | - | false | false | false | false |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| foreach | - | null | null | null | null |
| fused | - | null | null | null | null |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| maximize | false | false | false | false | false |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 |
| weight_decay | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |

accepted difference: torch-eager-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

### ops-session-step / gaussian (neural shape full: B4096 256-512-16 linear relu linear CE sgd)

race: done, driver rc 0, log `logs/neural.ops-session-step.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 2.2 ms) = 1.076; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 2.5 ms) = 0.944. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 2.4 | 2.4..2.4 | 1 | - | - | 2.4 | - | - (stored whole) | - | - | 2045.7 | 1698.5 | grad_digests={'b1': 'af8a97d53a3ad547', 'b2': '00290c152a66267b', 'w1': '4ff384d9d46fb712', 'w2': 'd836f93eb9369f50'}, grads_finite=True, loss=2.798163, loss_finite=True | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2.5 | 2.5..2.5 | 1 | 0.944 | - | 2.5 | - | - (stored whole) | 0.944 (whole/whole) | - | 4600.4 | 196.6 | grad_digests={'b1': '272078f6f0582af9', 'b2': 'c2e314e1f706b0f8', 'w1': '40d6cc2c30f07dd8', 'w2': 'e3ce6493b163048d'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=7.567e-10, grad_max_abs_diff_vs_ours_b2=7.451e-09, grad_max_abs_diff_vs_ours_w1=2.794e-09, grad_max_abs_diff_vs_ours_w2=4.191e-09, grad_max_rel_diff_vs_ours_b1=4.983e-07, grad_max_rel_diff_vs_ours_b2=3.545e-07, grad_max_rel_diff_vs_ours_w1=2.102e-06, grad_max_rel_diff_vs_ours_w2=4.676e-07, grads_finite=True, loss=2.798162, loss_abs_diff_vs_ours=7.153e-07, loss_finite=True, param_max_abs_diff_vs_ours_b1=9.313e-10, param_max_abs_diff_vs_ours_b2=1.863e-09, param_max_abs_diff_vs_ours_w1=3.725e-09, param_max_abs_diff_vs_ours_w2=3.725e-09, param_max_rel_diff_vs_ours_b1=1.491e-08, param_max_rel_diff_vs_ours_b2=4.874e-08, param_max_rel_diff_vs_ours_w1=5.958e-08, param_max_rel_diff_vs_ours_w2=8.398e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2.8 | 2.8..2.8 | 1 | 0.854 | - | 2.8 | - | - (stored whole) | 0.854 (whole/whole) | - | 4770.8 | 172.8 | grad_digests={'b1': '0227978f5af6d396', 'b2': '6c827b491c5d0a30', 'w1': '932e8d9245cc043e', 'w2': 'bc4b71b70f319961'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=8.149e-10, grad_max_abs_diff_vs_ours_b2=6.519e-09, grad_max_abs_diff_vs_ours_w1=2.736e-09, grad_max_abs_diff_vs_ours_w2=4.191e-09, grad_max_rel_diff_vs_ours_b1=5.367e-07, grad_max_rel_diff_vs_ours_b2=3.102e-07, grad_max_rel_diff_vs_ours_w1=2.059e-06, grad_max_rel_diff_vs_ours_w2=4.676e-07, grads_finite=True, loss=2.798162, loss_abs_diff_vs_ours=7.153e-07, loss_finite=True, param_max_abs_diff_vs_ours_b1=9.313e-10, param_max_abs_diff_vs_ours_b2=1.863e-09, param_max_abs_diff_vs_ours_w1=3.725e-09, param_max_abs_diff_vs_ours_w2=3.725e-09, param_max_rel_diff_vs_ours_b1=1.491e-08, param_max_rel_diff_vs_ours_b2=4.874e-08, param_max_rel_diff_vs_ours_w1=5.958e-08, param_max_rel_diff_vs_ours_w2=8.398e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2.4 | 2.4..2.4 | 1 | 0.986 | - | 2.4 | - | - (stored whole) | 0.986 (whole/whole) | - | 2984.6 | 202.6 | grad_digests={'b1': 'd4bced898a836854', 'b2': 'eaa485df0efd130b', 'w1': 'ef294deaa30d361c', 'w2': '399c4e954b441da3'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=5.06e-05, grad_max_abs_diff_vs_ours_b2=3.965e-05, grad_max_abs_diff_vs_ours_w1=7.59e-05, grad_max_abs_diff_vs_ours_w2=3.952e-05, grad_max_rel_diff_vs_ours_b1=0.033320, grad_max_rel_diff_vs_ours_b2=0.001887, grad_max_rel_diff_vs_ours_w1=0.057112, grad_max_rel_diff_vs_ours_w2=0.004410, grads_finite=True, loss=2.798156, loss_abs_diff_vs_ours=7.153e-06, loss_finite=True, param_max_abs_diff_vs_ours_b1=2.53e-06, param_max_abs_diff_vs_ours_b2=1.983e-06, param_max_abs_diff_vs_ours_w1=3.795e-06, param_max_abs_diff_vs_ours_w2=1.978e-06, param_max_rel_diff_vs_ours_b1=4.05e-05, param_max_rel_diff_vs_ours_b2=5.188e-05, param_max_rel_diff_vs_ours_w1=6.069e-05, param_max_rel_diff_vs_ours_w2=4.459e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2.2 | 2.2..2.2 | 1 | 1.076 | - | 2.2 | - | - (stored whole) | 1.076 (whole/whole) | - | 3280.5 | 168.6 | grad_digests={'b1': '3d632415a197c6fe', 'b2': '359febf02628e2fd', 'w1': '2ccf5e70decdf81e', 'w2': '986ebb07878b46e2'}, grad_digests_equal_ours=False, grad_max_abs_diff_vs_ours_b1=5.06e-05, grad_max_abs_diff_vs_ours_b2=3.966e-05, grad_max_abs_diff_vs_ours_w1=7.59e-05, grad_max_abs_diff_vs_ours_w2=3.952e-05, grad_max_rel_diff_vs_ours_b1=0.033320, grad_max_rel_diff_vs_ours_b2=0.001887, grad_max_rel_diff_vs_ours_w1=0.057112, grad_max_rel_diff_vs_ours_w2=0.004410, grads_finite=True, loss=2.798155, loss_abs_diff_vs_ours=7.391e-06, loss_finite=True, param_max_abs_diff_vs_ours_b1=2.53e-06, param_max_abs_diff_vs_ours_b2=1.983e-06, param_max_abs_diff_vs_ours_w1=3.795e-06, param_max_abs_diff_vs_ours_w2=1.978e-06, param_max_rel_diff_vs_ours_b1=4.05e-05, param_max_rel_diff_vs_ours_b2=5.188e-05, param_max_rel_diff_vs_ours_w1=6.069e-05, param_max_rel_diff_vs_ours_w2=4.459e-05 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Session(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-eager-fp32`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-compile-fp32`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-eager-bf16`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`
- `torch-compile-bf16`: `torch.SGD(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., learning_rate=0.05, loss='cross_entropy', momentum=0, nesterov=False, optimizer='sgd', reduction='mean', seed=7, steps=1, weight_decay=0)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/200261/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| batch_size | 4096 | 4096 | 4096 | 4096 | 4096 |
| layers | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax cross_entropy mean"] |
| learning_rate | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |
| loss | "cross_entropy" | "cross_entropy" | "cross_entropy" | "cross_entropy" | "cross_entropy" |
| momentum | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| nesterov | false | false | false | false | false |
| optimizer | "sgd" | "sgd" | "sgd" | "sgd" | "sgd" |
| reduction | "mean" | "mean" | "mean" | "mean" | "mean" |
| seed | 7 | 7 | 7 | 7 | 7 |
| steps | 1 | 1 | 1 | 1 | 1 |
| weight_decay | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### program-run / gaussian (neural shape full: B4096 256-512-16 linear relu linear softmax, one Program.run)

race: done, driver rc 0, log `logs/neural.program-run.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 0.7 ms) = 1.884; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 0.6 ms) = 2.103. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 1.2 | 1.2..1.2 | 1 | - | - | 1.2 | - | - (stored whole) | - | - | 2044.6 | 1698.3 | finite=True, max_abs_err_vs_fp64=7.398e-08, output_digest=da6c27db289f0438 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 0.6 | 0.6..0.6 | 1 | 2.103 | - | 0.6 | - | - (stored whole) | 2.103 (whole/whole) | - | 2642.5 | 96.5 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=8.941e-08, max_abs_err_vs_fp64=3.382e-08, max_rel_diff_vs_ours=5.226e-07, output_digest=5494b1712226f419 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 0.9 | 0.9..0.9 | 1 | 1.360 | - | 0.9 | - | - (stored whole) | 1.360 (whole/whole) | - | 2853.7 | 88.8 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=8.941e-08, max_abs_err_vs_fp64=3.382e-08, max_rel_diff_vs_ours=5.226e-07, output_digest=84e22d5b4f750036 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 0.7 | 0.7..0.7 | 1 | 1.848 | - | 0.7 | - | - (stored whole) | 1.848 (whole/whole) | - | 2956.6 | 172.5 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=0.0004913, max_abs_err_vs_fp64=0.0004913, max_rel_diff_vs_ours=0.002871, output_digest=0a09f5744ab469ac | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 0.7 | 0.7..0.7 | 1 | 1.884 | - | 0.7 | - | - (stored whole) | 1.884 (whole/whole) | - | 3270.4 | 162.8 | digest_equal_ours=False, finite=True, max_abs_diff_vs_ours=0.0004913, max_abs_err_vs_fp64=0.0004913, max_rel_diff_vs_ours=0.002871, output_digest=cac5c8b205d0ee7c | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Program(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-eager-fp32`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-compile-fp32`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-eager-bf16`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`
- `torch-compile-bf16`: `torch.softmax(batch_size=4096, layers=['linear 256 512 bias', 'relu', 'linear 512 1..., mode='inference', seed=7, steps=1)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/201135/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| batch_size | 4096 | 4096 | 4096 | 4096 | 4096 |
| layers | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] | ["linear 256 512 bias", "relu", "linear 512 16 bias", "softmax"] |
| mode | "inference" | "inference" | "inference" | "inference" | "inference" |
| seed | 7 | 7 | 7 | 7 | 7 |
| steps | 1 | 1 | 1 | 1 | 1 |

### samba-decode / bytes (neural shape full: B2 L512 DM384 V256 H6 FF1024 layers mamba3+attention+mamba3+attention)

race: done, driver rc 0, log `logs/neural.samba-decode.bytes.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 3708.3 | 3708.3..3708.3 | 1 | - | - | 3708.3 | - | - (stored whole) | - | - | 2640.1 | 2233.2 | mean_nll=5.640151 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/201675/vram_* bytes for this pid at the round's end (not a peak)

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

race: done, driver rc 0, log `logs/neural.samba-forward.bytes.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 6.1 | 6.1..6.1 | 1 | - | - | 6.1 | - | - (stored whole) | - | - | 2250.3 | 2526.4 | mean_nll=5.640151 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "worker returned no protocol message: worker_exited", "event": "error", "read_failure": {"deadline_s": 1800, "elapsed_s": 4.291082305999225, "reason": "eof"}, "reason": "worker_exited", "ret) (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-fp32 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "worker returned no protocol message: worker_exited", "event": "error", "read_failure": {"deadline_s": 1800, "elapsed_s": 1.642168591999507, "reason": "eof"}, "reason": "worker_exited", "ret) (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-bf16 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-graph-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "worker returned no protocol message: worker_exited", "event": "error", "read_failure": {"deadline_s": 1800, "elapsed_s": 4.269703916999788, "reason": "eof"}, "reason": "worker_exited", "ret) (measured this run) |

calls:
- `torch-eager-fp32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-compile-fp32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-eager-bf16`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-compile-bf16`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`
- `torch-graph-fp32`: `mamba_ssm.Block(config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., dropout=0, eps=1e-05, max_grad_norm='n/a', rope_theta=10000, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/202284/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16, torch-graph-fp32: host not sampled; GPU not sampled

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 | torch-graph-fp32 |
|---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" |
| dropout | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| eps | 1e-05 | 1e-05 | 1e-05 | 1e-05 | 1e-05 | 1e-05 |
| max_grad_norm | "n/a" | "n/a" | "n/a" | "n/a" | "n/a" | "n/a" |
| rope_theta | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 |

### samba-train-step / bytes (neural shape full: B2 L512 DM384 V256 H6 FF1024 layers mamba3+attention+mamba3+attention)

race: done, driver rc 0, log `logs/neural.samba-train-step.bytes.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16: - (no completed torch bf16 arm); fp32 twin: ours IDENTICAL / torch fp32: - (no completed torch fp32 arm). Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 53.6 | 53.6..53.6 | 1 | - | - | 53.6 | - | - (stored whole) | - | - | 2253.3 | 2527.4 | loss_first_step=5.640152, loss_last_step=4.822321, steps=2 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "worker returned no protocol message: worker_exited", "event": "error", "read_failure": {"deadline_s": 1800, "elapsed_s": 4.2571971230008785, "reason": "eof"}, "reason": "worker_exited", "re) (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-fp32 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "worker returned no protocol message: worker_exited", "event": "error", "read_failure": {"deadline_s": 1800, "elapsed_s": 1.6224736569984088, "reason": "eof"}, "reason": "worker_exited", "re) (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "REFUSED: torch-compile-bf16 on cuda failed in round 0 (compile happens here): InductorError('AssertionError: \\n\\nSet TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this esp) (measured this run) |

calls:
- `torch-eager-fp32`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-compile-fp32`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-eager-bf16`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`
- `torch-compile-bf16`: `mamba_ssm.Block(accumulation_steps=1, amsgrad=False, betas=[0.9, 0.999], capturable=False, config_readback='{"d_model": 384, "head_dim": 64, "intermedia..., decoupled_weight_decay=True, differentiable=False, dropout=0, eps=1e-08, lr=0.001, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/203382/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host not sampled; GPU not sampled

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| accumulation_steps | 1 | 1 | 1 | 1 | 1 |
| amsgrad | false | false | false | false | false |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| capturable | - | false | false | false | false |
| config_readback | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" | "{\"d_model\": 384, \"head_dim\": 64, \"intermediate\": 1024, \"layers\": [\"mamba3\", \"attention\", \"mamba3\", \"attention\"], \"n_heads\": 6, \"n_kv_heads\": 6, \"norm_eps\": \"9.999999747378752e-06\", \"tied_head\": true, \"vocab\": 256}" |
| decoupled_weight_decay | true | true | true | true | true |
| differentiable | - | false | false | false | false |
| dropout | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| foreach | - | null | null | null | null |
| fused | - | null | null | null | null |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| max_grad_norm | "off" | "off" | "off" | "off" | "off" |
| maximize | false | false | false | false | false |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 |
| weight_decay | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |

accepted difference: torch-eager-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-fp32 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-fp32 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-eager-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-eager-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 capturable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 differentiable: no captured-graph or differentiable optimizer step is requested; our standalone update has neither mode

accepted difference: torch-compile-bf16 foreach: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

accepted difference: torch-compile-bf16 fused: torch's foreach/fused selects its own implementation of the same optimizer update; the raw execution choice remains recorded

### sequential-fit / synthetic (neural shape full: synthetic train 1000000 test 100000 32-128-64-1 b512 1 epoch adam + predict_proba)

race: done, driver rc 0, log `logs/neural.sequential-fit.synthetic.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-compile-bf16, 2092.2 ms) = 0.210; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 1661.0 ms) = 0.265. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 440.0 | 440.0..440.0 | 1 | - | - | 440.0 | - | - (stored whole) | - | - | 2185.1 | 1699.1 | accuracy=0.899070, auc=0.968973, held_out_rows=100000, log_loss=0.225010, loss_curve_length=1, train_loss_finite=True, train_loss_last_step=0.240776 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1661.0 | 1661.0..1661.0 | 1 | 0.265 | - | 1661.0 | - | - (stored whole) | 0.265 (whole/whole) | - | 4974.8 | 362.9 | accuracy=0.898840, accuracy_diff_vs_ours=-0.00023, auc=0.968881, auc_diff_vs_ours=-9.22e-05, held_out_rows=100000, log_loss=0.225140, log_loss_diff_vs_ours=0.0001306, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.196202 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1847.1 | 1847.1..1847.1 | 1 | 0.238 | - | 1847.1 | - | - (stored whole) | 0.238 (whole/whole) | - | 5224.0 | 362.9 | accuracy=0.898600, accuracy_diff_vs_ours=-0.00047, auc=0.968864, auc_diff_vs_ours=-0.0001094, held_out_rows=100000, log_loss=0.225195, log_loss_diff_vs_ours=0.0001857, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.198931 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2095.7 | 2095.7..2095.7 | 1 | 0.210 | - | 2095.7 | - | - (stored whole) | 0.210 (whole/whole) | - | 3259.8 | 330.9 | accuracy=0.898680, accuracy_diff_vs_ours=-0.00039, auc=0.968887, auc_diff_vs_ours=-8.646e-05, held_out_rows=100000, log_loss=0.225122, log_loss_diff_vs_ours=0.0001118, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.197198 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2092.2 | 2092.2..2092.2 | 1 | 0.210 | - | 2092.2 | - | - (stored whole) | 0.210 (whole/whole) | - | 3377.1 | 330.9 | accuracy=0.898850, accuracy_diff_vs_ours=-0.00022, auc=0.968878, auc_diff_vs_ours=-9.545e-05, held_out_rows=100000, log_loss=0.225149, log_loss_diff_vs_ours=0.0001394, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.199082 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/204175/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false |
| batch_size | 512 | 512 | 512 | 512 | 512 |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| epochs | 1 | 1 | 1 | 1 | 1 |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| layers | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| loss | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" |
| maximize | false | false | false | false | false |
| optimizer | "adam" | "adam" | "adam" | "adam" | "adam" |
| seed | 7 | 7 | 7 | 7 | 7 |
| shuffle | true | true | true | true | true |
| weight_decay | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### sequential-predict / synthetic (neural shape full: synthetic train 1000000 test 100000 32-128-64-1 b512 1 epoch adam, predict_proba 100000 rows timed)

race: done, driver rc 0, log `logs/neural.sequential-predict.synthetic.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 1.2 ms) = 3.406; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 1.1 ms) = 3.732. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 4.2 | 4.2..4.2 | 1 | - | - | 4.2 | - | - (stored whole) | - | - | 2181.4 | 1699.1 | accuracy=0.899070, auc=0.968973, held_out_rows=100000, log_loss=0.225010, loss_curve_length=1, train_loss_finite=True, train_loss_last_step=0.240776 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.1 | 1.1..1.1 | 1 | 3.732 | - | 1.1 | - | - (stored whole) | 3.732 (whole/whole) | - | 4973.5 | 228.3 | accuracy=0.898840, accuracy_diff_vs_ours=-0.00023, auc=0.968881, auc_diff_vs_ours=-9.22e-05, held_out_rows=100000, log_loss=0.225140, log_loss_diff_vs_ours=0.0001306, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.196202 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.5 | 1.5..1.5 | 1 | 2.876 | - | 1.5 | - | - (stored whole) | 2.876 (whole/whole) | - | 5143.3 | 212.3 | accuracy=0.898890, accuracy_diff_vs_ours=-0.00018, auc=0.968882, auc_diff_vs_ours=-9.159e-05, held_out_rows=100000, log_loss=0.225134, log_loss_diff_vs_ours=0.0001245, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.197984 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.2 | 1.2..1.2 | 1 | 3.406 | - | 1.2 | - | - (stored whole) | 3.406 (whole/whole) | - | 3261.4 | 196.3 | accuracy=0.898680, accuracy_diff_vs_ours=-0.00039, auc=0.968887, auc_diff_vs_ours=-8.646e-05, held_out_rows=100000, log_loss=0.225122, log_loss_diff_vs_ours=0.0001118, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.197198 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.5 | 1.5..1.5 | 1 | 2.901 | - | 1.5 | - | - (stored whole) | 2.901 (whole/whole) | - | 3542.5 | 188.3 | accuracy=0.898750, accuracy_diff_vs_ours=-0.00032, auc=0.968875, auc_diff_vs_ours=-9.826e-05, held_out_rows=100000, log_loss=0.225178, log_loss_diff_vs_ours=0.0001686, loss_curve_length=1954, train_loss_finite=True, train_loss_last_step=0.198718 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `ours`: `anonlib.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-fp32`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-eager-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`
- `torch-compile-bf16`: `torch.Sequential(amsgrad=False, batch_size=512, betas=[0.9, 0.999], epochs=1, eps=1e-08, layers=['linear 32 128 bias', 'relu', 'linear 128 64..., learning_rate=0.001, loss='bce_with_logits', maximize=False, optimizer='adam', seed=7, ...)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/205097/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 |
|---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| amsgrad | false | false | false | false | false |
| batch_size | 512 | 512 | 512 | 512 | 512 |
| betas | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] | [0.9, 0.999] |
| epochs | 1 | 1 | 1 | 1 | 1 |
| eps | 1e-08 | 1e-08 | 1e-08 | 1e-08 | 1e-08 |
| layers | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] | ["linear 32 128 bias", "relu", "linear 128 64 bias", "relu", "linear 64 1 bias"] |
| learning_rate | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| loss | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" | "bce_with_logits" |
| maximize | false | false | false | false | false |
| optimizer | "adam" | "adam" | "adam" | "adam" | "adam" |
| seed | 7 | 7 | 7 | 7 | 7 |
| shuffle | true | true | true | true | true |
| weight_decay | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### transformer-decode / gaussian (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024)

race: done, driver rc 0, log `logs/neural.transformer-decode.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 1094.0 ms) = 2.235; fp32 twin: ours IDENTICAL / torch fp32 (torch-eager-fp32, 929.1 ms) = 2.631. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 2444.7 | 2444.7..2444.7 | 1 | - | - | 2444.7 | - | - (stored whole) | - | - | 2063.6 | 1698.5 | host_reference=TransformerBlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 929.1 | 929.1..929.1 | 1 | 2.631 | - | 929.1 | - | - (stored whole) | 2.631 (whole/whole) | - | 3983.1 | 99.3 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1094.0 | 1094.0..1094.0 | 1 | 2.235 | - | 1094.0 | - | - (stored whole) | 2.235 (whole/whole) | - | 3704.2 | 178.7 | max_abs_diff_vs_ours=0.001819, max_rel_diff_vs_ours=0.0003893 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | - | REFUSED(error: {"error": "worker returned no protocol message: worker_exited", "event": "error", "read_failure": {"deadline_s": 1800, "elapsed_s": 6.896873755998968, "reason": "eof"}, "reason": "worker_exited", "ret) (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-eager-bf16`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-graph-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/206173/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-eager-bf16: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

memory, torch-graph-fp32: host not sampled; GPU not sampled

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-eager-bf16 | torch-eager-fp32 | torch-graph-fp32 |
|---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) |
| eps | 1e-06 | 1e-06 | 1e-06 | 1e-06 |
| rope_theta | 10000.0 | 10000.0 | 10000.0 | 10000.0 |
| seed | "none (deterministic)" | 7 | 7 | 7 |

### transformer-forward / gaussian (neural shape full: B1 L2048 DM384 H6 KV6 HD64 FF1024)

race: done, driver rc 0, log `logs/neural.transformer-forward.gaussian.shape-full.log`, ran on anonlib-amd-box

headline: ours IDENTICAL / torch bf16 (torch-eager-bf16, 1.7 ms) = 4.708; fp32 twin: ours IDENTICAL / torch fp32 (torch-compile-fp32, 1.4 ms) = 5.705. Note: torch bf16 uses tensor cores; IDENTICAL does not (vendor matrix units are not bit-identical across vendors): the gap is the identity tax.

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @79fd41139 | identical | 8.0 | 8.0..8.0 | 1 | - | - | 8.0 | - | - (stored whole) | - | - | 2060.0 | 2348.6 | host_reference=TransformerBlockInference, host_reference_atol=1e-06, host_reference_finite=True, host_reference_passed=True, host_reference_rtol=1e-05, host_reference_tolerance_ratio=0.000000, max_abs_diff_vs_host=0.000000, max_rel_diff_vs_host=0.000000, max_rel_diff_vs_torch_eager_fp32=0.015169, rel_fro_vs_torch_eager_fp32=5.717e-08 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-eager-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.6 | 1.6..1.6 | 1 | 5.053 | - | 1.6 | - | - (stored whole) | 5.053 (whole/whole) | - | 3796.1 | 116.8 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.4 | 1.4..1.4 | 1 | 5.705 | - | 1.4 | - | - (stored whole) | 5.705 (whole/whole) | - | 4003.3 | 109.8 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07, max_rel_diff_vs_torch_eager_fp32=0.005081, rel_fro_vs_torch_eager_fp32=3.096e-08 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-eager-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 1.7 | 1.7..1.7 | 1 | 4.708 | - | 1.7 | - | - (stored whole) | 4.708 (whole/whole) | - | 3510.0 | 183.6 | max_abs_diff_vs_ours=0.001819, max_rel_diff_vs_ours=0.0003893, max_rel_diff_vs_torch_eager_fp32=76.084014, rel_fro_vs_torch_eager_fp32=0.0002764 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-compile-bf16 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 2.2 | 2.2..2.2 | 1 | 3.660 | - | 2.2 | - | - (stored whole) | 3.660 (whole/whole) | - | 3758.2 | 175.5 | max_abs_diff_vs_ours=0.001819, max_rel_diff_vs_ours=0.0003893, max_rel_diff_vs_torch_eager_fp32=41.369141, rel_fro_vs_torch_eager_fp32=0.0002629 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |
| torch-graph-fp32 | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 0.9 | 0.9..0.9 | 1 | 8.642 | - | 0.9 | - | - (stored whole) | 8.642 (whole/whole) | - | 4349.6 | 241.8 | max_abs_diff_vs_ours=4.768e-07, max_rel_diff_vs_ours=1.02e-07, max_rel_diff_vs_torch_eager_fp32=0.000000, rel_fro_vs_torch_eager_fp32=0.000000 | - | LIKE-FOR-LIKE-SPAN | - | ok (measured this run) |

calls:
- `torch-eager-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-compile-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-eager-bf16`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-compile-bf16`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`
- `torch-graph-fp32`: `transformers.LlamaDecoderLayer(eps=1e-06, rope_theta=10000, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/207181/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-eager-fp32, torch-compile-fp32, torch-eager-bf16, torch-compile-bf16, torch-graph-fp32: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

config: the board's own settings (no NVIDIA harness entry)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-compile-bf16 | torch-compile-fp32 | torch-eager-bf16 | torch-eager-fp32 | torch-graph-fp32 |
|---|---||---|---||---|---||---|---||---|---||---|---|
| library (source) | anonlib (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) | torch (declared) |
| eps | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 | 1e-06 |
| rope_theta | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 | 10000.0 |
| seed | "none (deterministic)" | 7 | 7 | 7 | 7 | 7 |

## Not covered by this board

- Classical, wave 2: RadiusNeighbors, the preprocessing scalers, HDBSCAN's prediction data, Cholesky and the parallel_* and Distributed* wrappers are public and not raced here; taxi-derived time series are not used (the ARIMA and ExponentialSmoothing lanes fit seeded synthetic series, as the repo's own ARIMA quality work does).
- Classical, wave 2, not planned on this vendor: cuML: CUDA only; no ROCm build exists. cuVS's ROCm port, hipVS (amd-hipvs), is the IVF-Flat GPU arm (hipvs-gpu); it has no ivf_sq, refine, UMAP, spectral or k-NN estimators, so those lanes keep their CPU opponents.
- Classical, wave 2, not planned on this vendor: faiss-gpu: the pinned FAISS GPU builds are CUDA; faiss-cpu is the arm on this box.
- Classical, wave 2, not planned on this vendor: scikit-learn on linearsvc: refused, different algorithm and model: liblinear (dual='auto' takes its primal trust-region Newton here) with a penalized intercept; ours and cuML L-BFGS on the primal with an unpenalized intercept (2026-10-13 audit); no opponent on this box.
- Classical, wave 2, not planned on this vendor: scikit-learn on linearsvr: refused, different algorithm and model: liblinear dual coordinate descent with a penalized intercept; ours and cuML L-BFGS on the primal with an unpenalized intercept (2026-10-13 audit); no opponent on this box.
- Classical, wave 2, not planned on this vendor: scikit-learn on tsvd: refused, different algorithm: ours 'covariance_eigh' (the eigendecomposition of X^T X); scikit-learn TruncatedSVD has only 'arpack' (Lanczos on X) and 'randomized', and no CPU library has ours' algorithm (2026-10-13 audit); no opponent on this box.
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
- Neural, not planned on this vendor: torch-eager-tf32 / torch-compile-tf32: TF32 is an NVIDIA CUDA tensor-core matmul mode; torch on ROCm accepts the flag and changes nothing
- Neural, not planned on this vendor: torch-compile-* on mamba1-forward and mamba1-infer: the only torch Mamba-1 twin is the pure-PyTorch reference scan, a per-token Python loop that torch.compile would unroll L times; mamba1 races the eager arms only
- Neural, not planned on this vendor: gemm-bf16 races torch's bf16 settings only (bf16 operands, fp32 accumulate)
- Neural, not planned on this vendor: mamba1-decode, mamba2-decode, mamba3-decode and samba-decode race ours alone: the repo's torch Mamba references are full-sequence scans with no carried-state decode step (a torch decode twin is not written yet)
- Neural, not planned on this vendor: torch-compile-* on transformer-decode: the twin is a per-token loop over a growing KV cache; transformer-decode races the eager arms only
- Neural, not planned on this vendor: gemm-int8: torch._int_mm is a CUDA kernel; torch on ROCm has no int8 matmul, so ours races alone
- Neural, not planned on this vendor: mamba-ssm-tf32: TF32 is an NVIDIA CUDA mode; mamba_ssm races in float32 (mamba-ssm-fp32, from its ROCm/HIP source build) on AMD
- Neural, not planned on this vendor: mamba-ssm bf16: our Mamba blocks are float32, so mamba_ssm races in float32 (and its TF32 setting on NVIDIA)
- Neural, not planned on this vendor: mlx-fp32 on the fit lanes: MLX runs on Apple silicon only
- Neural, not planned on this vendor: torch-compile-* on causal-lm-generate*: transformers' generate is a per-token loop over a growing KV cache; the generate lanes race the eager arms only
- Neural, not planned on this vendor: mlx-fp32 on sequential-predict: no MLX prediction twin is written; it races the torch arms

