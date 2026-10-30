# anonlib benchmark board

Generated 2026-10-30T08:57:13Z from `board.json` (schema `anonlib-bench-board/1`).

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
| script commit | 4e927c92495a43695bd5a8f524a47caef52c00bd |
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

Races: 30 planned, 30 done, 0 failed, 0 unsupported, 0 pending. Cells: 62 (ok 62).

Inference cells: 18 (ok 18).

## Quality at a glance

Per lane and dataset: our FAST value, our IDENTICAL value, and each opponent's.

| family | lane | dataset | metric | ours FAST | ours IDENTICAL | opponents |
|---|---|---|---|---|---|---|
| classical | dbscan | istella | n_clusters | - | 40131 | cuml-gpu 40131 |
| classical | dbscan | istella | noise_fraction | - | 0.219391 | cuml-gpu 0.219391 |
| classical | dbscan | istella | rows | - | 1000000 | cuml-gpu 1000000 |
| classical | dbscan | istella | ari_vs_ours (1 is our partition exactly) | - | - | cuml-gpu 1.000000 |
| classical | dbscan | istella | noise_agreement_vs_ours | - | - | cuml-gpu 1.000000 |
| classical | dbscan | taxi | n_clusters | - | 36 | cuml-gpu 36 |
| classical | dbscan | taxi | noise_fraction | - | 0.000174 | cuml-gpu 0.000174 |
| classical | dbscan | taxi | rows | - | 1000000 | cuml-gpu 1000000 |
| classical | dbscan | taxi | ari_vs_ours (1 is our partition exactly) | - | - | cuml-gpu 1.000000 |
| classical | dbscan | taxi | noise_agreement_vs_ours | - | - | cuml-gpu 1.000000 |
| classical | hdbscan | istella | n_clusters | - | 47 | cuml-gpu 53 |
| classical | hdbscan | istella | noise_fraction | - | 0.253810 | cuml-gpu 0.256280 |
| classical | hdbscan | istella | rows | - | 100000 | cuml-gpu 100000 |
| classical | hdbscan | istella | silhouette (higher is better) | - | -0.003856 | cuml-gpu -0.018228 |
| classical | hdbscan | istella | ari_vs_ours (1 is our partition exactly) | - | - | cuml-gpu 0.857120 |
| classical | hdbscan | istella | noise_agreement_vs_ours | - | - | cuml-gpu 0.940610 |
| classical | hdbscan | taxi | n_clusters | - | 161 | cuml-gpu 159 |
| classical | hdbscan | taxi | noise_fraction | - | 0.140550 | cuml-gpu 0.130970 |
| classical | hdbscan | taxi | rows | - | 100000 | cuml-gpu 100000 |
| classical | hdbscan | taxi | silhouette (higher is better) | - | 0.001505 | cuml-gpu 0.011960 |
| classical | hdbscan | taxi | ari_vs_ours (1 is our partition exactly) | - | - | cuml-gpu 0.917885 |
| classical | hdbscan | taxi | noise_agreement_vs_ours | - | - | cuml-gpu 0.984420 |
| classical | kde | istella | mean_log_likelihood (higher is better) | - | -222.270583 | cuml-gpu -222.270582 |
| classical | kde | istella | rows_without_density | - | 0 | cuml-gpu 0 |
| classical | kde | taxi | mean_log_likelihood (higher is better) | - | -14.826436 | cuml-gpu -14.826437 |
| classical | kde | taxi | rows_without_density | - | 0 | cuml-gpu 0 |
| classical | kmeans | istella | inertia (lower is better) | - | 6.051e+17 | cuml-gpu 6.111e+17 |
| classical | kmeans | istella | inertia_over_ours | - | 1.000000 | cuml-gpu 1.009914 |
| classical | kmeans | istella | n_iter | - | 33 | cuml-gpu 20 |
| classical | kmeans | istella | n_iter_over_ours | - | 1.000000 | cuml-gpu 0.606061 |
| classical | kmeans | taxi | inertia (lower is better) | - | 3.093e+08 | cuml-gpu 3.166e+08 |
| classical | kmeans | taxi | inertia_over_ours | - | 1.000000 | cuml-gpu 1.023712 |
| classical | kmeans | taxi | n_iter | - | 91 | cuml-gpu 39 |
| classical | kmeans | taxi | n_iter_over_ours | - | 1.000000 | cuml-gpu 0.428571 |
| classical | knn | istella | recall_at_k (higher is better) | - | 0.976250 | cuml-gpu 0.976402 |
| classical | knn | istella | rows_with_repeated_ids | - | 0 | cuml-gpu 0 |
| classical | knn | taxi | recall_at_k (higher is better) | - | 0.999754 | cuml-gpu 0.999742 |
| classical | knn | taxi | rows_with_repeated_ids | - | 0 | cuml-gpu 0 |
| classical | ols | istella | r2 (higher is better) | - | 0.332506 | cuml-gpu nan; torch-gpu nan |
| classical | ols | istella | rmse (lower is better) | - | 0.681740 | cuml-gpu nan; torch-gpu nan |
| classical | ols | taxi | r2 (higher is better) | - | 0.908837 | cuml-gpu 0.908836; torch-gpu 0.908836 |
| classical | ols | taxi | rmse (lower is better) | - | 4.696477 | cuml-gpu 4.696479; torch-gpu 4.696480 |
| classical | pca | istella | explained_variance_ratio_sum (higher is better) | - | 1.000000 | cuml-gpu 1.000000 |
| classical | pca | taxi | explained_variance_ratio_sum (higher is better) | - | 0.999997 | cuml-gpu 0.999996 |
| classical | svc | istella | accuracy (higher is better) | - | 0.922200 | cuml-gpu 0.922200 |
| classical | svc | istella | n_support | - | 2400 | cuml-gpu 2401 |
| classical | svc | taxi | accuracy (higher is better) | - | 0.767500 | cuml-gpu 0.767500 |
| classical | svc | taxi | n_support | - | 5527 | cuml-gpu 5541 |
| classical2 | kernel-ridge | istella | r2 (higher is better) | - | 0.385427 | cuml-gpu 0.385427 |
| classical2 | kernel-ridge | istella | rmse (lower is better) | - | 0.646407 | cuml-gpu 0.646407 |
| classical2 | kernel-ridge | taxi | r2 (higher is better) | - | 0.726543 | cuml-gpu 0.726543 |
| classical2 | kernel-ridge | taxi | rmse (lower is better) | - | 8.330373 | cuml-gpu 8.330375 |
| classical2 | knn-clf | istella | accuracy (higher is better) | - | 0.926250 | cuml-gpu 0.926250 |
| classical2 | knn-clf | taxi | accuracy (higher is better) | - | 0.741750 | cuml-gpu 0.741750 |
| classical2 | knn-reg | istella | r2 (higher is better) | - | 0.418145 | cuml-gpu 0.418145 |
| classical2 | knn-reg | istella | rmse (lower is better) | - | 0.625388 | cuml-gpu 0.625388 |
| classical2 | knn-reg | taxi | r2 (higher is better) | - | 0.937323 | cuml-gpu 0.937323 |
| classical2 | knn-reg | taxi | rmse (lower is better) | - | 3.842028 | cuml-gpu 3.842028 |
| classical2 | linearsvc | istella | accuracy (higher is better) | - | 0.923470 | cuml-gpu 0.922870 |
| classical2 | linearsvc | taxi | accuracy (higher is better) | - | 0.763330 | cuml-gpu 0.762990 |
| classical2 | linearsvr | istella | r2 (higher is better) | - | -0.106761 | cuml-gpu -0.106761 |
| classical2 | linearsvr | istella | rmse (lower is better) | - | 0.878794 | cuml-gpu 0.878795 |
| classical2 | linearsvr | taxi | r2 (higher is better) | - | 0.899814 | cuml-gpu 0.899813 |
| classical2 | linearsvr | taxi | rmse (lower is better) | - | 5.041273 | cuml-gpu 5.041302 |
| classical2 | svr | istella | r2 (higher is better) | - | 0.318258 | cuml-gpu 0.318232 |
| classical2 | svr | istella | rmse (lower is better) | - | 0.680816 | cuml-gpu 0.680829 |
| classical2 | svr | taxi | r2 (higher is better) | - | 0.767551 | cuml-gpu 0.767551 |
| classical2 | svr | taxi | rmse (lower is better) | - | 7.680395 | cuml-gpu 7.680405 |
| classical2 | tsvd | istella | explained_variance_ratio_sum (higher is better) | - | 1.000000 | cuml-gpu 1.000000 |
| classical2 | tsvd | istella | relative_reconstruction_error (lower is better) | - | 0.0001314 | cuml-gpu 0.0001472 |
| classical2 | tsvd | taxi | explained_variance_ratio_sum (higher is better) | - | 0.999965 | cuml-gpu 0.999964 |
| classical2 | tsvd | taxi | relative_reconstruction_error (lower is better) | - | 0.003257 | cuml-gpu 0.003257 |

## Inference at a glance

Batch prediction, each arm with its own fitted model from the same race; medians in ms. `FAST = IDENTICAL bits` compares our two tiers' predictions on the same rows. Our CPU is never raced or reported.

| family | lane | dataset | batch | rows | ours FAST ms | ours IDENTICAL ms | FAST = IDENTICAL bits | opponents |
|---|---|---|---|---|---|---|---|---|
| classical | kmeans | istella | Xq | 500000 | - | 38.6 | - | cuml-gpu 5.2 ms (IDENTICAL/arm 7.453) |
| classical | kmeans | taxi | Xq | 500000 | - | 3.1 | - | cuml-gpu 2.3 ms (IDENTICAL/arm 1.335) |
| classical | ols | istella | Xq | 500000 | - | 39.4 | - | cuml-gpu 2.4 ms (IDENTICAL/arm 16.179); torch-gpu 1.0 ms (IDENTICAL/arm 40.902) |
| classical | ols | taxi | Xq | 500000 | - | 5.5 | - | cuml-gpu 1.3 ms (IDENTICAL/arm 4.159); torch-gpu 0.3 ms (IDENTICAL/arm 16.476) |
| classical | pca | istella | Xq | 500000 | - | 51.9 | - | cuml-gpu 10.4 ms (IDENTICAL/arm 4.976) |
| classical | pca | taxi | Xq | 500000 | - | 18.6 | - | cuml-gpu 2.4 ms (IDENTICAL/arm 7.842) |
| classical | svc | istella | Xq | 10000 | - | 11.0 | - | cuml-gpu 4.9 ms (IDENTICAL/arm 2.240) |
| classical | svc | taxi | Xq | 10000 | - | 6.1 | - | cuml-gpu 4.6 ms (IDENTICAL/arm 1.307) |

## Classical

### dbscan / istella (rows full, shape 1000000x220)

race: done, driver rc 0, log `logs/classical.dbscan.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 602959.0 | 602959.0..602959.0 | 1 | - | - | 602959.0 | 602922.4 | 36.64 (upload_ms_separate) | - | - | 5644.0 | 3498.0 | n_clusters=40131, noise_fraction=0.219391, rows=1000000 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 65399.7 | 65399.7..65399.7 | 1 | 9.220 | - | 66020.5 | 65399.7 | 620.86 (upload_ms_untimed) | 9.133 (whole/whole) | - | 2684.6 | 1932.0 | ari_vs_ours=1.000000, n_clusters=40131, noise_agreement_vs_ours=1.000000, noise_fraction=0.219391, rows=1000000 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.DBSCAN(algorithm='brute', eps=3, metric='euclidean', min_samples=2, prediction_data=False)`
- `cuml-gpu`: `cuml.DBSCAN(algorithm='brute', calc_core_sample_indices=True, eps=3, metric='euclidean', min_samples=2, output_type='cupy', verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: eps=3, min_samples=2 (the cuML benchmark's DBSCAN) on every arm; metric='euclidean'. Rows: dbscan block: 1,000,000 rows, standardized. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: algorithm='brute' on every raced arm (ours, cuml-gpu, scikit-learn: the cuML benchmark's cpu_args); ours' default 'rbc' is not raced, and cuml-gpu-rbc (overflows at 1,000,000 rows) is not on the roster

mismatch: leaf_size=30 and n_jobs=-1: scikit-learn only

config: cuML benchmark (RAPIDS), DBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algorithm | "brute" | "brute" |
| calc_core_sample_indices | true | - |
| eps | 3.0 | 3.0 |
| max_iterations | - | null |
| max_mbytes_per_batch | null | null |
| metric | "euclidean" | "euclidean" |
| min_samples | 2 | 2 |
| prediction_data | - | false |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu calc_core_sample_indices: our DBSCAN always produces core_sample_indices_ and components_; cuML is explicitly set to retain both

accepted difference: cuml-gpu max_iterations: both propagate labels to the fixed point; cuML exposes no iteration cap, and our None requests completion

accepted difference: cuml-gpu max_mbytes_per_batch: both libraries choose distance-batch memory automatically; neither setting subsamples the input

accepted difference: cuml-gpu prediction_data: no additional prediction cache is requested; cuML DBSCAN exposes no prediction-data option

### dbscan / taxi (rows full, shape 1000000x11)

race: done, driver rc 0, log `logs/classical.dbscan.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 1.582e+06 | 1.582e+06..1.582e+06 | 1 | - | - | 1.582e+06 | 1.582e+06 | 1.93 (upload_ms_separate) | - | - | 1786.8 | 7338.0 | n_clusters=36, noise_fraction=0.000174, rows=1000000 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 439493.6 | 439493.6..439493.6 | 1 | 3.600 | - | 439532.6 | 439493.6 | 39.02 (upload_ms_untimed) | 3.600 (whole/whole) | - | 889.3 | 520.0 | ari_vs_ours=1.000000, n_clusters=36, noise_agreement_vs_ours=1.000000, noise_fraction=0.000174, rows=1000000 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.DBSCAN(algorithm='brute', eps=3, metric='euclidean', min_samples=2, prediction_data=False)`
- `cuml-gpu`: `cuml.DBSCAN(algorithm='brute', calc_core_sample_indices=True, eps=3, metric='euclidean', min_samples=2, output_type='cupy', verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: eps=3, min_samples=2 (the cuML benchmark's DBSCAN) on every arm; metric='euclidean'. Rows: dbscan block: 1,000,000 rows, standardized. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: algorithm='brute' on every raced arm (ours, cuml-gpu, scikit-learn: the cuML benchmark's cpu_args); ours' default 'rbc' is not raced, and cuml-gpu-rbc (overflows at 1,000,000 rows) is not on the roster

mismatch: leaf_size=30 and n_jobs=-1: scikit-learn only

config: cuML benchmark (RAPIDS), DBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algorithm | "brute" | "brute" |
| calc_core_sample_indices | true | - |
| eps | 3.0 | 3.0 |
| max_iterations | - | null |
| max_mbytes_per_batch | null | null |
| metric | "euclidean" | "euclidean" |
| min_samples | 2 | 2 |
| prediction_data | - | false |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu calc_core_sample_indices: our DBSCAN always produces core_sample_indices_ and components_; cuML is explicitly set to retain both

accepted difference: cuml-gpu max_iterations: both propagate labels to the fixed point; cuML exposes no iteration cap, and our None requests completion

accepted difference: cuml-gpu max_mbytes_per_batch: both libraries choose distance-batch memory automatically; neither setting subsamples the input

accepted difference: cuml-gpu prediction_data: no additional prediction cache is requested; cuML DBSCAN exposes no prediction-data option

### hdbscan / istella (rows full, shape 100000x220)

race: done, driver rc 0, log `logs/classical.hdbscan.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 1192.6 | 1192.6..1192.6 | 1 | - | - | 1192.6 | 1189.0 | 3.67 (upload_ms_separate) | - | - | 2442.6 | 1194.0 | n_clusters=47, noise_fraction=0.253810, rows=100000, silhouette=-0.003856, silhouette_library=sklearn.metrics.silhouette_score, silhouette_library_version=1.7.2, silhouette_scope=all consumed rows; noise is a label group; no sampling | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 825.3 | 825.3..825.3 | 1 | 1.445 | - | 905.2 | 825.3 | 79.93 (upload_ms_untimed) | 1.318 (whole/whole) | - | 1895.1 | 526.0 | ari_vs_ours=0.857120, n_clusters=53, noise_agreement_vs_ours=0.940610, noise_fraction=0.256280, rows=100000, silhouette=-0.018228, silhouette_library=sklearn.metrics.silhouette_score, silhouette_library_version=1.7.2, silhouette_scope=all consumed rows; noise is a label group; no sampling | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.HDBSCAN(allow_single_cluster=False, alpha=1, cluster_selection_epsilon=0, cluster_selection_method='eom', max_cluster_size=0, metric='euclidean', min_cluster_size=100, min_samples=10, prediction_data=False)`
- `cuml-gpu`: `cuml.HDBSCAN(allow_single_cluster=False, alpha=1, build_algo='brute_force', cluster_selection_epsilon=0, cluster_selection_method='eom', gen_min_span_tree=False, max_cluster_size=0, metric='euclidean', min_cluster_size=100, min_samples=10, ...)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: min_samples=10 (scikit-learn 11: the same core distance, the 10th neighbour besides the point), min_cluster_size=100, metric='euclidean', cluster_selection_method='eom', cluster_selection_epsilon=0.0, alpha=1.0, allow_single_cluster=False. Rows: the dbscan block's first 100,000 rows. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: max_cluster_size: ours and cuML 0, scikit-learn None (both mean no limit)

mismatch: spanning tree: ours and scikit-learn build the exact minimum spanning tree of the full mutual-reachability graph; cuML builds it over the symmetrized (min_samples + 1)-NN graph in mutual-reachability space and joins its components (cuVS cluster/detail/single_linkage.cuh:75-135, mst.cuh cross_component_nn), an approximate tree where groups of duplicate rows split that graph (taxi)

mismatch: min_samples: ours and cuML 10, scikit-learn 11. The SAME k-th neighbour: cuML's runner.h:68-80 (ours transcribes it) runs the k-NN at min_samples + 1 including the point itself; scikit-learn's kneighbors(X, min_samples) counts the point itself (its HDBSCAN Notes say so). tools/bench_board_params.py maps both to one canonical value

mismatch: k-NN graph: exact brute force on every arm; cuML build_algo='brute_force' pinned (as ours); scikit-learn algorithm='brute' (FAIRNESS FIX 2026-10-13: it was 'auto', a KD/ball tree), leaf_size=40 unused, n_jobs=-1

config: cuML benchmark (RAPIDS), HDBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| allow_single_cluster | false | false |
| alpha | 1.0 | 1.0 |
| build_algo | "brute_force" | - |
| build_kwds | null | - |
| cluster_selection_epsilon | 0.0 | 0.0 |
| cluster_selection_method | "eom" | "eom" |
| device_ids | null | - |
| gen_min_span_tree | false | - |
| max_cluster_size | 0 | 0 |
| metric | "euclidean" | "euclidean" |
| min_cluster_size | 100 | 100 |
| min_samples | 10 | 10 |
| p | null | - |
| prediction_data | false | false |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu build_algo: our HDBSCAN fixes exhaustive neighbors; cuML explicitly selects the same exact brute-force graph construction

accepted difference: cuml-gpu build_kwds: cuML's exact graph uses the default unpartitioned single-device path; no approximate or multi-device overrides are requested

accepted difference: cuml-gpu device_ids: cuML's exact graph uses the default unpartitioned single-device path; no approximate or multi-device overrides are requested

accepted difference: cuml-gpu gen_min_span_tree: both construct the internal MST for clustering; neither requests an additional exported minimum-spanning-tree object

accepted difference: cuml-gpu p: p only parameterizes Minkowski distance; both arms explicitly use Euclidean distance

### hdbscan / taxi (rows full, shape 100000x11)

race: done, driver rc 0, log `logs/classical.hdbscan.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 423.1 | 423.1..423.1 | 1 | - | - | 423.1 | 422.9 | 0.27 (upload_ms_separate) | - | - | 1553.6 | 682.0 | n_clusters=161, noise_fraction=0.140550, rows=100000, silhouette=0.001505, silhouette_library=sklearn.metrics.silhouette_score, silhouette_library_version=1.7.2, silhouette_scope=all consumed rows; noise is a label group; no sampling | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 356.2 | 356.2..356.2 | 1 | 1.188 | - | 364.8 | 356.2 | 8.53 (upload_ms_untimed) | 1.160 (whole/whole) | - | 941.1 | 448.0 | ari_vs_ours=0.917885, n_clusters=159, noise_agreement_vs_ours=0.984420, noise_fraction=0.130970, rows=100000, silhouette=0.011960, silhouette_library=sklearn.metrics.silhouette_score, silhouette_library_version=1.7.2, silhouette_scope=all consumed rows; noise is a label group; no sampling | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.HDBSCAN(allow_single_cluster=False, alpha=1, cluster_selection_epsilon=0, cluster_selection_method='eom', max_cluster_size=0, metric='euclidean', min_cluster_size=100, min_samples=10, prediction_data=False)`
- `cuml-gpu`: `cuml.HDBSCAN(allow_single_cluster=False, alpha=1, build_algo='brute_force', cluster_selection_epsilon=0, cluster_selection_method='eom', gen_min_span_tree=False, max_cluster_size=0, metric='euclidean', min_cluster_size=100, min_samples=10, ...)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: min_samples=10 (scikit-learn 11: the same core distance, the 10th neighbour besides the point), min_cluster_size=100, metric='euclidean', cluster_selection_method='eom', cluster_selection_epsilon=0.0, alpha=1.0, allow_single_cluster=False. Rows: the dbscan block's first 100,000 rows. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: max_cluster_size: ours and cuML 0, scikit-learn None (both mean no limit)

mismatch: spanning tree: ours and scikit-learn build the exact minimum spanning tree of the full mutual-reachability graph; cuML builds it over the symmetrized (min_samples + 1)-NN graph in mutual-reachability space and joins its components (cuVS cluster/detail/single_linkage.cuh:75-135, mst.cuh cross_component_nn), an approximate tree where groups of duplicate rows split that graph (taxi)

mismatch: min_samples: ours and cuML 10, scikit-learn 11. The SAME k-th neighbour: cuML's runner.h:68-80 (ours transcribes it) runs the k-NN at min_samples + 1 including the point itself; scikit-learn's kneighbors(X, min_samples) counts the point itself (its HDBSCAN Notes say so). tools/bench_board_params.py maps both to one canonical value

mismatch: k-NN graph: exact brute force on every arm; cuML build_algo='brute_force' pinned (as ours); scikit-learn algorithm='brute' (FAIRNESS FIX 2026-10-13: it was 'auto', a KD/ball tree), leaf_size=40 unused, n_jobs=-1

config: cuML benchmark (RAPIDS), HDBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| allow_single_cluster | false | false |
| alpha | 1.0 | 1.0 |
| build_algo | "brute_force" | - |
| build_kwds | null | - |
| cluster_selection_epsilon | 0.0 | 0.0 |
| cluster_selection_method | "eom" | "eom" |
| device_ids | null | - |
| gen_min_span_tree | false | - |
| max_cluster_size | 0 | 0 |
| metric | "euclidean" | "euclidean" |
| min_cluster_size | 100 | 100 |
| min_samples | 10 | 10 |
| p | null | - |
| prediction_data | false | false |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu build_algo: our HDBSCAN fixes exhaustive neighbors; cuML explicitly selects the same exact brute-force graph construction

accepted difference: cuml-gpu build_kwds: cuML's exact graph uses the default unpartitioned single-device path; no approximate or multi-device overrides are requested

accepted difference: cuml-gpu device_ids: cuML's exact graph uses the default unpartitioned single-device path; no approximate or multi-device overrides are requested

accepted difference: cuml-gpu gen_min_span_tree: both construct the internal MST for clustering; neither requests an additional exported minimum-spanning-tree object

accepted difference: cuml-gpu p: p only parameterizes Minkowski distance; both arms explicitly use Euclidean distance

### kde / istella (rows full, shape 100000x220)

race: done, driver rc 0, log `logs/classical.kde.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 34.5 | 34.5..34.5 | 1 | - | - | 34.5 | 30.7 | 3.73 (upload_ms_separate) | - | - | 1582.7 | 682.0 | mean_log_likelihood=-222.270583, rows_without_density=0 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 6.5 | 6.5..6.5 | 1 | 5.341 | - | 75.5 | 6.5 | 69.00 (upload_ms_untimed) | 0.457 (whole/whole) | - | 998.2 | 514.0 | mean_log_likelihood=-222.270582, rows_without_density=0 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KernelDensity(algorithm='auto', atol=0, bandwidth=1, breadth_first=True, kernel='gaussian', leaf_size=40, metric='euclidean', rtol=0)`
- `cuml-gpu`: `cuml.KernelDensity(bandwidth=1, kernel='gaussian', metric='euclidean', output_type='cupy', verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: bandwidth=1.0, kernel='gaussian' (the cuML benchmark's KernelDensity), metric='euclidean' on every arm; ours and scikit-learn atol=0, rtol=0, algorithm='auto', leaf_size=40, breadth_first=True. Rows: kde block: 100,000 fit rows, 2,000 queries, standardized. Timed: score_samples; the fit is before the clock on every arm.

mismatch: seed: no arm has a seed argument (exact density)

mismatch: cuML has no atol, rtol, algorithm, leaf_size or breadth_first (exact brute force)

config: cuML benchmark (RAPIDS), KernelDensity (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algorithm | - | "auto" |
| atol | - | 0.0 |
| bandwidth | 1.0 | 1.0 |
| breadth_first | - | true |
| kernel | "gaussian" | "gaussian" |
| leaf_size | - | 40 |
| metric | "euclidean" | "euclidean" |
| metric_params | null | null |
| rtol | - | 0.0 |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu algorithm: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu atol: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu breadth_first: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu leaf_size: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu metric_params: None means no metric keyword overrides, p=2 on both implementations (density.py; kernel_density.pyx)

accepted difference: cuml-gpu rtol: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

### kde / taxi (rows full, shape 100000x11)

race: done, driver rc 0, log `logs/classical.kde.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 6.0 | 6.0..6.0 | 1 | - | - | 6.0 | 5.7 | 0.30 (upload_ms_separate) | - | - | 1501.4 | 682.0 | mean_log_likelihood=-14.826436, rows_without_density=0 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 2.0 | 2.0..2.0 | 1 | 2.973 | - | 12.4 | 2.0 | 10.40 (upload_ms_untimed) | 0.482 (whole/whole) | - | 796.9 | 436.0 | mean_log_likelihood=-14.826437, rows_without_density=0 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KernelDensity(algorithm='auto', atol=0, bandwidth=1, breadth_first=True, kernel='gaussian', leaf_size=40, metric='euclidean', rtol=0)`
- `cuml-gpu`: `cuml.KernelDensity(bandwidth=1, kernel='gaussian', metric='euclidean', output_type='cupy', verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: bandwidth=1.0, kernel='gaussian' (the cuML benchmark's KernelDensity), metric='euclidean' on every arm; ours and scikit-learn atol=0, rtol=0, algorithm='auto', leaf_size=40, breadth_first=True. Rows: kde block: 100,000 fit rows, 2,000 queries, standardized. Timed: score_samples; the fit is before the clock on every arm.

mismatch: seed: no arm has a seed argument (exact density)

mismatch: cuML has no atol, rtol, algorithm, leaf_size or breadth_first (exact brute force)

config: cuML benchmark (RAPIDS), KernelDensity (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algorithm | - | "auto" |
| atol | - | 0.0 |
| bandwidth | 1.0 | 1.0 |
| breadth_first | - | true |
| kernel | "gaussian" | "gaussian" |
| leaf_size | - | 40 |
| metric | "euclidean" | "euclidean" |
| metric_params | null | null |
| rtol | - | 0.0 |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu algorithm: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu atol: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu breadth_first: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu leaf_size: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

accepted difference: cuml-gpu metric_params: None means no metric keyword overrides, p=2 on both implementations (density.py; kernel_density.pyx)

accepted difference: cuml-gpu rtol: both implementations use exact brute-force KDE; ours refuses nondefault tree controls and cuML exposes no tree (density.py; kernel_density.pyx)

### kmeans / istella (rows full, shape 2043304x220)

race: done, driver rc 0, log `logs/classical.kmeans.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 462.3 | 462.3..462.3 | 1 | - | - | 462.3 | 387.5 | 74.73 (upload_ms_separate) | - | - | 3661.2 | 2474.0 | inertia=6.051e+17, inertia_over_ours=1.000000, n_iter=33, n_iter_over_ours=1.000000 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 463.3 | 463.3..463.3 | 1 | 0.998 | - | 1566.2 | 463.3 | 1102.92 (upload_ms_untimed) | 0.295 (whole/whole) | - | 4965.5 | 2154.0 | inertia=6.111e+17, inertia_over_ours=1.009914, n_iter=20, n_iter_over_ours=0.606061 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KMeans(init='k-means++', max_iter=300, metric='euclidean', n_clusters=8, n_init=1, oversampling_factor=0, random_state=7, tol=1e-07)`
- `cuml-gpu`: `cuml.KMeans(device_buffer_samples=0, init='k-means++', init_size=0, max_iter=300, max_samples_per_batch=32768, n_clusters=8, n_init=1, output_type='cupy', oversampling_factor=0, random_state=7, tol=1e-07, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_clusters=8, init='k-means++', max_iter=300, n_init=1 (the cuML benchmark's KMeans), oversampling_factor=0 on ours and cuML (its cuml_args; the classic sequential seeding), tol=1e-7 (an absolute squared center shift on every arm; scikit-learn's relative tol rescaled to it), metric='euclidean', Lloyd; seed 7 (ours, scikit-learn and cuML random_state=7). Rows: big block: 4,000,000 taxi rows or the Istella-S train split, raw. Timed: fit (the k-means++ seeding included on every arm).

mismatch: k-means++: each library draws its own start from its own generator seeded 7, so the starts differ and so may n_iter; scikit-learn greedy k-means++ (2 + log k candidates per center), ours and cuML the sequential k-means++ of cuML (oversampling_factor=0)

mismatch: stopping rule, the same on every arm: total squared center shift below 1e-7 (absolute) or max_iter=300. ours and cuML tol=1e-7 is that threshold (cuVS kmeans.cuh sqrdNormError < tol; inertia_check off); scikit-learn's tol is relative to mean(var(X)), so it gets 1e-7 / mean(var(X)) of the same rows (the same absolute threshold; it also stops when no label changes, a zero shift). n_iter and n_iter_over_ours are in every quality cell

mismatch: algorithm: scikit-learn algorithm='lloyd'; ours and cuML have no such parameter (Lloyd)

mismatch: torch-gpu: refused, not an opponent (the harness's own k-means from torch ops); hipvs-gpu (AMD): hipVS cuvs.cluster.kmeans, init_method='KMeansPlusPlus' with oversampling_factor=0, tol=1e-7 under cuVS's rule, squared L2, no seed argument

config: cuML benchmark (RAPIDS), KMeans (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| device_buffer_samples | 0 | - |
| init | "k-means++" | "k-means++" |
| init_centroids | - | null |
| init_size | 0 | - |
| max_iter | 300 | 300 |
| max_samples_per_batch | 32768 | - |
| metric | - | "euclidean" |
| n_clusters | 8 | 8 |
| n_init | 1 | 1 |
| oversampling_factor | 0.0 | 0.0 |
| seed | 7 | 7 |
| tol | 1e-07 | 1e-07 |

accepted difference: cuml-gpu device_buffer_samples: cuML device_buffer_samples=0 uses the full in-memory dataset; init_size only applies to its out-of-core path (kmeans.pyx)

accepted difference: cuml-gpu init_centroids: no supplied centroids; both use the separately compared init method (cluster.py; kmeans.pyx)

accepted difference: cuml-gpu init_size: cuML device_buffer_samples=0 uses the full in-memory dataset; init_size only applies to its out-of-core path (kmeans.pyx)

accepted difference: cuml-gpu max_samples_per_batch: cuML distance-computation batch size partitions all rows without subsampling; library implementation tiling is retained, not a model setting (kmeans.pyx)

accepted difference: cuml-gpu metric: cuML KMeans fixes DistanceType.L2Expanded, matching our squared Euclidean objective (kmeans.pyx set_params)

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 38.6 | 38.6..38.6 | 1 | - | - | 38.6 | - | - (stored whole) | - | - | eval_inertia=1.417e+17, label_agreement_own_centers=1.000000 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 500000 | 5.2 | 5.2..5.2 | 1 | 7.453 | - | 266.3 | 5.2 | 261.08 (upload_ms_untimed (the predict rows' own upload)) | 0.145 (whole/whole) | - | agreement_vs_ours=0.766430, bits_equal_vs_ours=False, eval_inertia=1.442e+17, label_agreement_own_centers=0.999998 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.KMeans(init='k-means++', max_iter=300, metric='euclidean', n_clusters=8, n_init=1, oversampling_factor=0, random_state=7, tol=1e-07); anonlib KMeans.predict(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.KMeans(device_buffer_samples=0, init='k-means++', init_size=0, max_iter=300, max_samples_per_batch=32768, n_clusters=8, n_init=1, output_type='cupy', oversampling_factor=0, random_state=7, tol=1e-07, verbose=False); cuml KMeans.predict(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

### kmeans / taxi (rows full, shape 4000000x11)

race: done, driver rc 0, log `logs/classical.kmeans.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 185.6 | 185.6..185.6 | 1 | - | - | 185.6 | 178.2 | 7.34 (upload_ms_separate) | - | - | 1742.9 | 1194.0 | inertia=3.093e+08, inertia_over_ours=1.000000, n_iter=91, n_iter_over_ours=1.000000 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 376.9 | 376.9..376.9 | 1 | 0.492 | - | 526.2 | 376.9 | 149.24 (upload_ms_untimed) | 0.353 (whole/whole) | - | 1249.5 | 614.0 | inertia=3.166e+08, inertia_over_ours=1.023712, n_iter=39, n_iter_over_ours=0.428571 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KMeans(init='k-means++', max_iter=300, metric='euclidean', n_clusters=8, n_init=1, oversampling_factor=0, random_state=7, tol=1e-07)`
- `cuml-gpu`: `cuml.KMeans(device_buffer_samples=0, init='k-means++', init_size=0, max_iter=300, max_samples_per_batch=32768, n_clusters=8, n_init=1, output_type='cupy', oversampling_factor=0, random_state=7, tol=1e-07, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_clusters=8, init='k-means++', max_iter=300, n_init=1 (the cuML benchmark's KMeans), oversampling_factor=0 on ours and cuML (its cuml_args; the classic sequential seeding), tol=1e-7 (an absolute squared center shift on every arm; scikit-learn's relative tol rescaled to it), metric='euclidean', Lloyd; seed 7 (ours, scikit-learn and cuML random_state=7). Rows: big block: 4,000,000 taxi rows or the Istella-S train split, raw. Timed: fit (the k-means++ seeding included on every arm).

mismatch: k-means++: each library draws its own start from its own generator seeded 7, so the starts differ and so may n_iter; scikit-learn greedy k-means++ (2 + log k candidates per center), ours and cuML the sequential k-means++ of cuML (oversampling_factor=0)

mismatch: stopping rule, the same on every arm: total squared center shift below 1e-7 (absolute) or max_iter=300. ours and cuML tol=1e-7 is that threshold (cuVS kmeans.cuh sqrdNormError < tol; inertia_check off); scikit-learn's tol is relative to mean(var(X)), so it gets 1e-7 / mean(var(X)) of the same rows (the same absolute threshold; it also stops when no label changes, a zero shift). n_iter and n_iter_over_ours are in every quality cell

mismatch: algorithm: scikit-learn algorithm='lloyd'; ours and cuML have no such parameter (Lloyd)

mismatch: torch-gpu: refused, not an opponent (the harness's own k-means from torch ops); hipvs-gpu (AMD): hipVS cuvs.cluster.kmeans, init_method='KMeansPlusPlus' with oversampling_factor=0, tol=1e-7 under cuVS's rule, squared L2, no seed argument

config: cuML benchmark (RAPIDS), KMeans (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| device_buffer_samples | 0 | - |
| init | "k-means++" | "k-means++" |
| init_centroids | - | null |
| init_size | 0 | - |
| max_iter | 300 | 300 |
| max_samples_per_batch | 32768 | - |
| metric | - | "euclidean" |
| n_clusters | 8 | 8 |
| n_init | 1 | 1 |
| oversampling_factor | 0.0 | 0.0 |
| seed | 7 | 7 |
| tol | 1e-07 | 1e-07 |

accepted difference: cuml-gpu device_buffer_samples: cuML device_buffer_samples=0 uses the full in-memory dataset; init_size only applies to its out-of-core path (kmeans.pyx)

accepted difference: cuml-gpu init_centroids: no supplied centroids; both use the separately compared init method (cluster.py; kmeans.pyx)

accepted difference: cuml-gpu init_size: cuML device_buffer_samples=0 uses the full in-memory dataset; init_size only applies to its out-of-core path (kmeans.pyx)

accepted difference: cuml-gpu max_samples_per_batch: cuML distance-computation batch size partitions all rows without subsampling; library implementation tiling is retained, not a model setting (kmeans.pyx)

accepted difference: cuml-gpu metric: cuML KMeans fixes DistanceType.L2Expanded, matching our squared Euclidean objective (kmeans.pyx set_params)

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 3.1 | 3.1..3.1 | 1 | - | - | 3.1 | - | - (stored whole) | - | - | eval_inertia=4.824e+07, label_agreement_own_centers=0.999998 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 500000 | 2.3 | 2.3..2.3 | 1 | 1.335 | - | 20.2 | 2.3 | 17.83 (upload_ms_untimed (the predict rows' own upload)) | 0.155 (whole/whole) | - | agreement_vs_ours=0.497542, bits_equal_vs_ours=False, eval_inertia=5.036e+07, label_agreement_own_centers=1.000000 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.KMeans(init='k-means++', max_iter=300, metric='euclidean', n_clusters=8, n_init=1, oversampling_factor=0, random_state=7, tol=1e-07); anonlib KMeans.predict(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.KMeans(device_buffer_samples=0, init='k-means++', init_size=0, max_iter=300, max_samples_per_batch=32768, n_clusters=8, n_init=1, output_type='cupy', oversampling_factor=0, random_state=7, tol=1e-07, verbose=False); cuml KMeans.predict(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

### knn / istella (rows full, shape 400000x220)

race: done, driver rc 0, log `logs/classical.knn.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 43.0 | 43.0..43.0 | 1 | - | - | 43.0 | 28.3 | 14.71 (upload_ms_separate) | - | - | 1847.8 | 2474.0 | recall_at_k=0.976250, rows_with_repeated_ids=0 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 71.9 | 71.9..71.9 | 1 | 0.598 | - | 332.6 | 71.9 | 260.64 (upload_ms_untimed) | 0.129 (whole/whole) | - | 1622.8 | 772.0 | recall_at_k=0.976402, rows_with_repeated_ids=0 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.NearestNeighbors(algorithm='brute', metric='euclidean', n_neighbors=64, p=2, query_tile=0)`
- `cuml-gpu`: `cuml.NearestNeighbors(algorithm='brute', metric='euclidean', n_neighbors=64, output_type='cupy', p=2, radius=1, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_neighbors=64 (the cuML benchmark's NearestNeighbors), metric='euclidean', algorithm='brute' (ours, scikit-learn, cuML). Rows: knn block: 400,000 index rows, 4,000 queries, raw. Timed: kneighbors; the fit (index) is before the clock on every arm.

mismatch: seed: no arm has a seed argument (exact search)

mismatch: query_tile: ours only (tiling, results unchanged); n_jobs=-1: scikit-learn only

mismatch: torch-gpu: refused, not an opponent (the harness's own cdist + topk kNN); hipvs-gpu (AMD): hipVS cuvs.neighbors.brute_force, built before the clock, search timed

config: cuML benchmark (RAPIDS), NearestNeighbors (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algo_params | null | - |
| algorithm | "brute" | "brute" |
| metric | "euclidean" | "euclidean" |
| metric_params | null | - |
| n_neighbors | 64 | 64 |
| p | 2 | 2 |
| query_tile | - | 0 |
| radius | 1.0 | - |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu algo_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu metric_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu query_tile: our query_tile partitions all queries without changing k or the exact distance metric; internal tiling is logged (neighbors.py)

accepted difference: cuml-gpu radius: kneighbors uses the compared n_neighbors, never the radius-neighbors query option (nearest_neighbors.pyx)

### knn / taxi (rows full, shape 400000x11)

race: done, driver rc 0, log `logs/classical.knn.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 24.6 | 24.6..24.6 | 1 | - | - | 24.6 | 23.8 | 0.81 (upload_ms_separate) | - | - | 1525.4 | 1706.0 | recall_at_k=0.999754, rows_with_repeated_ids=0 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 30.8 | 30.8..30.8 | 1 | 0.798 | - | 51.8 | 30.8 | 21.03 (upload_ms_untimed) | 0.474 (whole/whole) | - | 818.7 | 452.0 | recall_at_k=0.999742, rows_with_repeated_ids=0 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.NearestNeighbors(algorithm='brute', metric='euclidean', n_neighbors=64, p=2, query_tile=0)`
- `cuml-gpu`: `cuml.NearestNeighbors(algorithm='brute', metric='euclidean', n_neighbors=64, output_type='cupy', p=2, radius=1, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_neighbors=64 (the cuML benchmark's NearestNeighbors), metric='euclidean', algorithm='brute' (ours, scikit-learn, cuML). Rows: knn block: 400,000 index rows, 4,000 queries, raw. Timed: kneighbors; the fit (index) is before the clock on every arm.

mismatch: seed: no arm has a seed argument (exact search)

mismatch: query_tile: ours only (tiling, results unchanged); n_jobs=-1: scikit-learn only

mismatch: torch-gpu: refused, not an opponent (the harness's own cdist + topk kNN); hipvs-gpu (AMD): hipVS cuvs.neighbors.brute_force, built before the clock, search timed

config: cuML benchmark (RAPIDS), NearestNeighbors (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algo_params | null | - |
| algorithm | "brute" | "brute" |
| metric | "euclidean" | "euclidean" |
| metric_params | null | - |
| n_neighbors | 64 | 64 |
| p | 2 | 2 |
| query_tile | - | 0 |
| radius | 1.0 | - |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu algo_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu metric_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu query_tile: our query_tile partitions all queries without changing k or the exact distance metric; internal tiling is logged (neighbors.py)

accepted difference: cuml-gpu radius: kneighbors uses the compared n_neighbors, never the radius-neighbors query option (nearest_neighbors.pyx)

### ols / istella (rows full, shape 2043304x220)

race: done, driver rc 0, log `logs/classical.ols.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 503.8 | 503.8..503.8 | 1 | - | - | 503.8 | 429.0 | 74.83 (upload_ms_separate) | - | - | 3645.4 | 4266.0 | finite=True, r2=0.332506, rmse=0.681740 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 555.8 | 555.8..555.8 | 1 | 0.906 | - | 1650.3 | 555.8 | 1094.46 (upload_ms_untimed) | 0.305 (whole/whole) | - | 5071.8 | 2154.0 | finite=False, r2=nan, rmse=nan | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |
| torch-gpu | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 580.6 | 580.6..580.6 | 1 | 0.868 | - | 655.9 | 580.6 | 75.35 (upload_ms_untimed) | 0.739 (kernel/kernel) | - | 3012.3 | 8894.4 | finite=False, r2=nan, rmse=nan | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearRegression(fit_intercept=True)`
- `cuml-gpu`: `cuml.LinearRegression(algorithm='qr', copy_X=True, fit_intercept=True, output_type='cupy', verbose=False)`
- `torch-gpu`: `torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

settings: fit_intercept=True. Rows: big block, raw; R2 and RMSE on the 500,000 eval rows. Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

mismatch: solver (no parameter on ours): ours' IDENTICAL fit centers X and y and runs a blocked Householder TSQR of [X / y], then the SVD of its small R with a pseudo-inverse cutoff (python/anonlib/linear_model.py _ols_tsqr_centered; tall designs, at most 511 columns; the condition number is not squared); its FAST fit (Apple) solves the equilibrated normal equations. cuML algorithm='qr' (geqrf, R x = Q^T y: the same QR of the tall design, no rank cutoff); scikit-learn scipy lstsq gelsd (SVD)

mismatch: torch-gpu: torch.linalg.lstsq(driver='gels') on the centered data, torch's own least-squares routine (QR without pivoting, full rank assumed; the only driver torch has on CUDA and ROCm; MPS has no lstsq, so Apple has no torch arm)

mismatch: torch-gpu-eigh: refused, harness-written (REFUSED_ARMS)

mismatch: scikit-learn positive=False and copy_X=True: parameters ours does not have

config: cuML benchmark (RAPIDS), LinearRegression (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours | torch-gpu |
|---|---||---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) | torch (declared) |
| algorithm | "qr" | - | - |
| copy_X | true | - | - |
| driver | - | - | "gels" |
| fit_intercept | true | true | true |
| seed | "none (deterministic)" | "none (deterministic)" | 7 |

accepted difference: cuml-gpu algorithm: QR least squares on both: cuML algorithm='qr' (Rx = Q^T y) and ours' TSQR of the centered design

accepted difference: cuml-gpu copy_X: neither arm mutates the caller's X: cuML copy_X=True; ours centers a device copy

accepted difference: torch-gpu driver: QR least squares on both: torch driver='gels' (QR, no pivoting) and ours' TSQR of the centered design; fit_intercept is compared

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 39.4 | 39.4..39.4 | 1 | - | - | 39.4 | - | - (stored whole) | - | - | predict_max_rel_err_own_fp64=8.451e-06, r2_eval=0.332506, rmse_eval=0.681740 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 500000 | 2.4 | 2.4..2.4 | 1 | 16.179 | - | 267.4 | 2.4 | 264.93 (upload_ms_untimed (the predict rows' own upload)) | 0.147 (whole/whole) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=nan, predict_max_rel_err_own_fp64=nan, r2_eval=nan, rmse_eval=nan | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |
| torch-gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | Xq | 500000 | 1.0 | 1.0..1.0 | 1 | 40.902 | - | 19.5 | 1.0 | 18.53 (upload_ms_untimed (the predict rows' own upload)) | 2.022 (whole/whole (kernel not derivable)) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=nan, predict_max_rel_err_own_fp64=nan, r2_eval=nan, rmse_eval=nan | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.LinearRegression(fit_intercept=True); anonlib LinearRegression.predict(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.LinearRegression(algorithm='qr', copy_X=True, fit_intercept=True, output_type='cupy', verbose=False); cuml LinearRegression.predict(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

inference call, torch-gpu: torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7); torch Xq @ coef + intercept; Xq uploaded before the clock, which ends at the device synchronize

### ols / taxi (rows full, shape 4000000x11)

race: done, driver rc 0, log `logs/classical.ols.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 16.5 | 16.5..16.5 | 1 | - | - | 16.5 | 8.9 | 7.55 (upload_ms_separate) | - | - | 1706.1 | 1194.0 | finite=True, r2=0.908837, rmse=4.696477 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 51.0 | 51.0..51.0 | 1 | 0.323 | - | 199.1 | 51.0 | 148.07 (upload_ms_untimed) | 0.083 (whole/whole) | - | 1318.0 | 614.0 | finite=True, r2=0.908836, rmse=4.696479 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |
| torch-gpu | torch | gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | opponent | 39.1 | 39.1..39.1 | 1 | 0.421 | - | 47.7 | 39.1 | 8.64 (upload_ms_untimed) | 0.228 (kernel/kernel) | - | 1080.5 | 4649.6 | finite=True, r2=0.908836, rmse=4.696480 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearRegression(fit_intercept=True)`
- `cuml-gpu`: `cuml.LinearRegression(algorithm='qr', copy_X=True, fit_intercept=True, output_type='cupy', verbose=False)`
- `torch-gpu`: `torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

memory, torch-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

settings: fit_intercept=True. Rows: big block, raw; R2 and RMSE on the 500,000 eval rows. Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

mismatch: solver (no parameter on ours): ours' IDENTICAL fit centers X and y and runs a blocked Householder TSQR of [X / y], then the SVD of its small R with a pseudo-inverse cutoff (python/anonlib/linear_model.py _ols_tsqr_centered; tall designs, at most 511 columns; the condition number is not squared); its FAST fit (Apple) solves the equilibrated normal equations. cuML algorithm='qr' (geqrf, R x = Q^T y: the same QR of the tall design, no rank cutoff); scikit-learn scipy lstsq gelsd (SVD)

mismatch: torch-gpu: torch.linalg.lstsq(driver='gels') on the centered data, torch's own least-squares routine (QR without pivoting, full rank assumed; the only driver torch has on CUDA and ROCm; MPS has no lstsq, so Apple has no torch arm)

mismatch: torch-gpu-eigh: refused, harness-written (REFUSED_ARMS)

mismatch: scikit-learn positive=False and copy_X=True: parameters ours does not have

config: cuML benchmark (RAPIDS), LinearRegression (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours | torch-gpu |
|---|---||---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) | torch (declared) |
| algorithm | "qr" | - | - |
| copy_X | true | - | - |
| driver | - | - | "gels" |
| fit_intercept | true | true | true |
| seed | "none (deterministic)" | "none (deterministic)" | 7 |

accepted difference: cuml-gpu algorithm: QR least squares on both: cuML algorithm='qr' (Rx = Q^T y) and ours' TSQR of the centered design

accepted difference: cuml-gpu copy_X: neither arm mutates the caller's X: cuML copy_X=True; ours centers a device copy

accepted difference: torch-gpu driver: QR least squares on both: torch driver='gels' (QR, no pivoting) and ours' TSQR of the centered design; fit_intercept is compared

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 5.5 | 5.5..5.5 | 1 | - | - | 5.5 | - | - (stored whole) | - | - | predict_max_rel_err_own_fp64=9.438e-08, r2_eval=0.908837, rmse_eval=4.696477 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 500000 | 1.3 | 1.3..1.3 | 1 | 4.159 | - | 19.0 | 1.3 | 17.68 (upload_ms_untimed (the predict rows' own upload)) | 0.287 (whole/whole) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=0.0004578, predict_max_rel_err_own_fp64=1.124e-07, r2_eval=0.908836, rmse_eval=4.696479 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |
| torch-gpu | NVIDIA L40S (host nv-box) | torch 2.13.0+cu129 | Xq | 500000 | 0.3 | 0.3..0.3 | 1 | 16.476 | - | 1.9 | 0.3 | 1.56 (upload_ms_untimed (the predict rows' own upload)) | 2.887 (whole/whole (kernel not derivable)) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=0.0004578, predict_max_rel_err_own_fp64=1.093e-07, r2_eval=0.908836, rmse_eval=4.696479 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.LinearRegression(fit_intercept=True); anonlib LinearRegression.predict(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.LinearRegression(algorithm='qr', copy_X=True, fit_intercept=True, output_type='cupy', verbose=False); cuml LinearRegression.predict(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

inference call, torch-gpu: torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7); torch Xq @ coef + intercept; Xq uploaded before the clock, which ends at the device synchronize

### pca / istella (rows full, shape 2043304x220)

race: done, driver rc 0, log `logs/classical.pca.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 176.1 | 176.1..176.1 | 1 | - | - | 176.1 | 101.3 | 74.74 (upload_ms_separate) | - | - | 3644.0 | 2474.0 | explained_variance_ratio_sum=1.000000 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 74.4 | 74.4..74.4 | 1 | 2.366 | - | 1172.7 | 74.4 | 1098.29 (upload_ms_untimed) | 0.150 (whole/whole) | - | 5090.1 | 2190.0 | explained_variance_ratio_sum=1.000000 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False)`
- `cuml-gpu`: `cuml.PCA(copy=True, iterated_power=15, n_components=10, output_type='cupy', svd_solver='full', tol=1e-07, verbose=False, whiten=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_components=10 (the cuML benchmark's PCA), whiten=False, random_state=7; ours and scikit-learn svd_solver='covariance_eigh'. Rows: big block, raw. Timed: fit.

mismatch: svd_solver: cuML has no 'covariance_eigh'; cuml-gpu runs svd_solver='full' (cuML's COV_EIG_DQ: the eigendecomposition of the covariance, ours' algorithm)

mismatch: torch-gpu: refused (fairness audit 2026-10-13): torch has no PCA estimator of this algorithm; the old arm was a covariance eigh our harness wrote from torch ops, not an opponent (torch.pca_lowrank is a randomized method, a different algorithm)

mismatch: random_state is read by none of the covariance solvers; set to 7 on every arm

config: cuML benchmark (RAPIDS), PCA (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| copy | true | true |
| iterated_power | 15 | "auto" |
| n_components | 10 | 10 |
| n_oversamples | - | 10 |
| power_iteration_normalizer | - | "auto" |
| seed | "none (deterministic)" | 7 |
| svd_solver | "covariance_eigh" | "covariance_eigh" |
| tol | 1e-07 | 0.0 |
| whiten | false | false |

accepted difference: cuml-gpu iterated_power: covariance eigendecomposition on both arms: randomized/Jacobi iteration controls are inactive (cuML pca.pyx; anonlib decomposition.py)

accepted difference: cuml-gpu n_oversamples: covariance eigendecomposition on both arms: randomized/Jacobi iteration controls are inactive (cuML pca.pyx; anonlib decomposition.py)

accepted difference: cuml-gpu power_iteration_normalizer: covariance eigendecomposition on both arms: randomized/Jacobi iteration controls are inactive (cuML pca.pyx; anonlib decomposition.py)

accepted difference: cuml-gpu tol: cuML PCA's tol is read only by its 'jacobi' solver (cuml/decomposition/pca.pyx: 'Used if algorithm = "jacobi"'); the raced 'full' solver, COV_EIG_DQ, the covariance eigendecomposition of ours' covariance_eigh, has no tolerance. cuML's own scikit-learn interop maps scikit-learn's tol 0.0 to its 1e-7

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 51.9 | 51.9..51.9 | 1 | - | - | 51.9 | - | - (stored whole) | - | - | transform_max_rel_err_own_fp64=3.69e-07 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 500000 | 10.4 | 10.4..10.4 | 1 | 4.976 | - | 270.7 | 10.4 | 260.26 (upload_ms_untimed (the predict rows' own upload)) | 0.192 (whole/whole) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=118908.242188, transform_max_rel_err_own_fp64=3.694e-07 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False); anonlib PCA.transform(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.PCA(copy=True, iterated_power=15, n_components=10, output_type='cupy', svd_solver='full', tol=1e-07, verbose=False, whiten=False); cuml PCA.transform(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

### pca / taxi (rows full, shape 4000000x11)

race: done, driver rc 0, log `logs/classical.pca.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 17.1 | 17.1..17.1 | 1 | - | - | 17.1 | 8.4 | 8.67 (upload_ms_separate) | - | - | 1704.1 | 938.0 | explained_variance_ratio_sum=0.999997 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 19.2 | 19.2..19.2 | 1 | 0.890 | - | 166.8 | 19.2 | 147.61 (upload_ms_untimed) | 0.102 (whole/whole) | - | 1305.9 | 642.0 | explained_variance_ratio_sum=0.999996 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False)`
- `cuml-gpu`: `cuml.PCA(copy=True, iterated_power=15, n_components=10, output_type='cupy', svd_solver='full', tol=1e-07, verbose=False, whiten=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_components=10 (the cuML benchmark's PCA), whiten=False, random_state=7; ours and scikit-learn svd_solver='covariance_eigh'. Rows: big block, raw. Timed: fit.

mismatch: svd_solver: cuML has no 'covariance_eigh'; cuml-gpu runs svd_solver='full' (cuML's COV_EIG_DQ: the eigendecomposition of the covariance, ours' algorithm)

mismatch: torch-gpu: refused (fairness audit 2026-10-13): torch has no PCA estimator of this algorithm; the old arm was a covariance eigh our harness wrote from torch ops, not an opponent (torch.pca_lowrank is a randomized method, a different algorithm)

mismatch: random_state is read by none of the covariance solvers; set to 7 on every arm

config: cuML benchmark (RAPIDS), PCA (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| copy | true | true |
| iterated_power | 15 | "auto" |
| n_components | 10 | 10 |
| n_oversamples | - | 10 |
| power_iteration_normalizer | - | "auto" |
| seed | "none (deterministic)" | 7 |
| svd_solver | "covariance_eigh" | "covariance_eigh" |
| tol | 1e-07 | 0.0 |
| whiten | false | false |

accepted difference: cuml-gpu iterated_power: covariance eigendecomposition on both arms: randomized/Jacobi iteration controls are inactive (cuML pca.pyx; anonlib decomposition.py)

accepted difference: cuml-gpu n_oversamples: covariance eigendecomposition on both arms: randomized/Jacobi iteration controls are inactive (cuML pca.pyx; anonlib decomposition.py)

accepted difference: cuml-gpu power_iteration_normalizer: covariance eigendecomposition on both arms: randomized/Jacobi iteration controls are inactive (cuML pca.pyx; anonlib decomposition.py)

accepted difference: cuml-gpu tol: cuML PCA's tol is read only by its 'jacobi' solver (cuml/decomposition/pca.pyx: 'Used if algorithm = "jacobi"'); the raced 'full' solver, COV_EIG_DQ, the covariance eigendecomposition of ours' covariance_eigh, has no tolerance. cuML's own scikit-learn interop maps scikit-learn's tol 0.0 to its 1e-7

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 18.6 | 18.6..18.6 | 1 | - | - | 18.6 | - | - (stored whole) | - | - | transform_max_rel_err_own_fp64=9.857e-08 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 500000 | 2.4 | 2.4..2.4 | 1 | 7.842 | - | 19.9 | 2.4 | 17.51 (upload_ms_untimed (the predict rows' own upload)) | 0.936 (whole/whole) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=0.005283, transform_max_rel_err_own_fp64=1.067e-07 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False); anonlib PCA.transform(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.PCA(copy=True, iterated_power=15, n_components=10, output_type='cupy', svd_solver='full', tol=1e-07, verbose=False, whiten=False); cuml PCA.transform(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

### svc / istella (rows full, shape 10000x220)

race: done, driver rc 0, log `logs/classical.svc.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 32.7 | 32.7..32.7 | 1 | - | - | 32.7 | 32.2 | 0.46 (upload_ms_separate) | - | - | 1543.6 | 682.0 | accuracy=0.922200, n_support=2400 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 23.3 | 23.3..23.3 | 1 | 1.404 | - | 46.2 | 23.3 | 22.94 (upload_ms_untimed) | 0.707 (whole/whole) | - | 1062.2 | 464.0 | accuracy=0.922200, n_support=2401 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False)`
- `cuml-gpu`: `cuml.SVC(C=1, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, output_type='cupy', random_state=7, tol=0.001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: C=1.0, kernel='rbf', gamma=1/d, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB, class_weight=None. Rows: svc block: 10,000 fit rows, 10,000 eval rows, standardized. Timed: fit.

mismatch: seed: scikit-learn and cuML random_state=7 (read only with probability=True); ours refuses random_state without probability=True, so ours stays None

mismatch: cache_size=2000 on every arm; ours honors it only as the prediction buffer (DEVIATION 871), so its training is unaffected

mismatch: shrinking=True: scikit-learn only; nochange_steps=1000: ours and cuML only

config: cuML benchmark (RAPIDS), SVC-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| break_ties | - | false |
| cache_size | 2000.0 | 2000.0 |
| class_weight | null | null |
| coef0 | 0.0 | 0.0 |
| decision_function_shape | "ovo" | "ovo" |
| degree | 3 | 3 |
| gamma | 0.004545454545454545 | 0.004545454545454545 |
| kernel | "rbf" | "rbf" |
| max_iter | -1 | -1 |
| nochange_steps | 1000 | 1000 |
| probability | - | false |
| seed | 7 | null |
| tol | 0.001 | 0.001 |

accepted difference: ours seed: anonlib SVC refuses random_state without probability=True (the fit draws nothing); scikit-learn and cuML get 7

accepted difference: cuml-gpu break_ties: break_ties is inactive under the compared decision_function_shape='ovo' (ours refuses True there)

accepted difference: cuml-gpu class_weight: None (unweighted) set explicitly on every arm

accepted difference: cuml-gpu probability: no Platt-scaling cross-validation fits: ours probability=False; cuML SVC has no probability option

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 10000 | 11.0 | 11.0..11.0 | 1 | - | - | 11.0 | - | - (stored whole) | - | - | accuracy_eval=0.922200 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 10000 | 4.9 | 4.9..4.9 | 1 | 2.240 | - | - | 4.9 | - (stored kernel) | 2.240 (MIXED ours whole / arm kernel) | - | accuracy_eval=0.922200, agreement_vs_ours=1.000000, bits_equal_vs_ours=True | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False); anonlib SVC.predict(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.SVC(C=1, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, output_type='cupy', random_state=7, tol=0.001, verbose=False); cuml SVC.predict(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

### svc / taxi (rows full, shape 10000x11)

race: done, driver rc 0, log `logs/classical.svc.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 760.5 | 760.5..760.5 | 1 | - | - | 760.5 | 760.3 | 0.22 (upload_ms_separate) | - | - | 1505.7 | 682.0 | accuracy=0.767500, n_support=5527 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 378.2 | 378.2..378.2 | 1 | 2.011 | - | 383.4 | 378.2 | 5.21 (upload_ms_untimed) | 1.983 (whole/whole) | - | 942.4 | 440.0 | accuracy=0.767500, n_support=5541 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False)`
- `cuml-gpu`: `cuml.SVC(C=1, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, output_type='cupy', random_state=7, tol=0.001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: C=1.0, kernel='rbf', gamma=1/d, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB, class_weight=None. Rows: svc block: 10,000 fit rows, 10,000 eval rows, standardized. Timed: fit.

mismatch: seed: scikit-learn and cuML random_state=7 (read only with probability=True); ours refuses random_state without probability=True, so ours stays None

mismatch: cache_size=2000 on every arm; ours honors it only as the prediction buffer (DEVIATION 871), so its training is unaffected

mismatch: shrinking=True: scikit-learn only; nochange_steps=1000: ours and cuML only

config: cuML benchmark (RAPIDS), SVC-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| break_ties | - | false |
| cache_size | 2000.0 | 2000.0 |
| class_weight | null | null |
| coef0 | 0.0 | 0.0 |
| decision_function_shape | "ovo" | "ovo" |
| degree | 3 | 3 |
| gamma | 0.09090909090909091 | 0.09090909090909091 |
| kernel | "rbf" | "rbf" |
| max_iter | -1 | -1 |
| nochange_steps | 1000 | 1000 |
| probability | - | false |
| seed | 7 | null |
| tol | 0.001 | 0.001 |

accepted difference: ours seed: anonlib SVC refuses random_state without probability=True (the fit draws nothing); scikit-learn and cuML get 7

accepted difference: cuml-gpu break_ties: break_ties is inactive under the compared decision_function_shape='ovo' (ours refuses True there)

accepted difference: cuml-gpu class_weight: None (unweighted) set explicitly on every arm

accepted difference: cuml-gpu probability: no Platt-scaling cross-validation fits: ours probability=False; cuML SVC has no probability option

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 10000 | 6.1 | 6.1..6.1 | 1 | - | - | 6.1 | - | - (stored whole) | - | - | accuracy_eval=0.767500 | yes | LIKE-FOR-LIKE-SPAN | ok |
| cuml-gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | Xq | 10000 | 4.6 | 4.6..4.6 | 1 | 1.307 | - | - | 4.6 | - (stored kernel) | 1.307 (MIXED ours whole / arm kernel) | - | accuracy_eval=0.767500, agreement_vs_ours=1.000000, bits_equal_vs_ours=True | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False); anonlib SVC.predict(Xq), host rows in, host result out

inference call, cuml-gpu: cuml.SVC(C=1, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, output_type='cupy', random_state=7, tol=0.001, verbose=False); cuml SVC.predict(Xq on the device, output_type cupy); Xq uploaded before the clock, which ends at the device synchronize

## Classical, wave 2

### kernel-ridge / istella (rows full, shape X 10000x220; Xq 10000x220; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.kernel-ridge.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 532.7 | 532.7..532.7 | 1 | - | - | 532.7 | - | - (stored whole) | - | - | 2442.7 | 1450.0 | finite=True, r2=0.385427, rmse=0.646407 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 324.2 | 324.2..324.2 | 1 | 1.643 | - | 340.6 | 324.2 | 16.37 (upload_ms_untimed) | 1.564 (whole/whole) | - | 1936.4 | 494.0 | finite=True, r2=0.385427, rmse=0.646407 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KernelRidge(alpha=1, coef0=1, degree=3, gamma=0.00454545, kernel='rbf')`
- `cuml-gpu`: `cuml.KernelRidge(alpha=1, coef0=1, degree=3, gamma=0.00454545, kernel='rbf', output_type='cupy', verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: alpha=1.0, kernel='rbf', gamma=1/d, degree=3, coef0=1.0. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

config: cuML benchmark (RAPIDS), KernelRidge (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| alpha | 1.0 | 1.0 |
| coef0 | 1.0 | 1.0 |
| degree | 3 | 3 |
| gamma | 0.004545454545454545 | 0.004545454545454545 |
| kernel | "rbf" | "rbf" |
| kernel_params | null | - |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu kernel_params: cuML's named kernel uses gamma/degree/coef0; kernel_params=None supplies no callable-kernel overrides

### kernel-ridge / taxi (rows full, shape X 10000x11; Xq 10000x11; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.kernel-ridge.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 533.2 | 533.2..533.2 | 1 | - | - | 533.2 | - | - (stored whole) | - | - | 1549.2 | 1194.0 | finite=True, r2=0.726543, rmse=8.330373 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 324.4 | 324.4..324.4 | 1 | 1.644 | - | 337.0 | 324.4 | 12.66 (upload_ms_untimed) | 1.582 (whole/whole) | - | 908.4 | 474.0 | finite=True, r2=0.726543, rmse=8.330375 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KernelRidge(alpha=1, coef0=1, degree=3, gamma=0.0909091, kernel='rbf')`
- `cuml-gpu`: `cuml.KernelRidge(alpha=1, coef0=1, degree=3, gamma=0.0909091, kernel='rbf', output_type='cupy', verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: alpha=1.0, kernel='rbf', gamma=1/d, degree=3, coef0=1.0. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

config: cuML benchmark (RAPIDS), KernelRidge (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| alpha | 1.0 | 1.0 |
| coef0 | 1.0 | 1.0 |
| degree | 3 | 3 |
| gamma | 0.09090909090909091 | 0.09090909090909091 |
| kernel | "rbf" | "rbf" |
| kernel_params | null | - |
| seed | "none (deterministic)" | "none (deterministic)" |

accepted difference: cuml-gpu kernel_params: cuML's named kernel uses gamma/degree/coef0; kernel_params=None supplies no callable-kernel overrides

### knn-clf / istella (rows full, shape X 200000x220; Xq 4000x220; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-clf.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 40.8 | 40.8..40.8 | 1 | - | - | 40.8 | - | - (stored whole) | - | - | 2602.8 | 938.0 | accuracy=0.926250 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 39.3 | 39.3..39.3 | 1 | 1.038 | - | 201.1 | 39.3 | 161.85 (upload_ms_untimed) | 0.203 (whole/whole) | - | 2110.1 | 710.0 | accuracy=0.926250 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KNeighborsClassifier(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`
- `cuml-gpu`: `cuml.KNeighborsClassifier(algorithm='brute', metric='euclidean', n_neighbors=10, output_type='cupy', p=2, verbose=False, weights='uniform')`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the cls block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsClassifier (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algo_params | null | - |
| algorithm | "brute" | "brute" |
| metric | "euclidean" | "euclidean" |
| metric_params | null | - |
| n_neighbors | 10 | 10 |
| p | 2 | 2 |
| query_tile | - | 0 |
| seed | "none (deterministic)" | "none (deterministic)" |
| weights | "uniform" | "uniform" |

accepted difference: cuml-gpu algo_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu metric_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu query_tile: our query_tile partitions all queries without changing k or the exact distance metric; internal tiling is logged (neighbors.py)

### knn-clf / taxi (rows full, shape X 200000x11; Xq 4000x11; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-clf.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 14.2 | 14.2..14.2 | 1 | - | - | 14.2 | - | - (stored whole) | - | - | 1563.3 | 682.0 | accuracy=0.741750 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 25.4 | 25.4..25.4 | 1 | 0.559 | - | 40.5 | 25.4 | 15.12 (upload_ms_untimed) | 0.350 (whole/whole) | - | 942.0 | 440.0 | accuracy=0.741750 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KNeighborsClassifier(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`
- `cuml-gpu`: `cuml.KNeighborsClassifier(algorithm='brute', metric='euclidean', n_neighbors=10, output_type='cupy', p=2, verbose=False, weights='uniform')`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the cls block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsClassifier (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algo_params | null | - |
| algorithm | "brute" | "brute" |
| metric | "euclidean" | "euclidean" |
| metric_params | null | - |
| n_neighbors | 10 | 10 |
| p | 2 | 2 |
| query_tile | - | 0 |
| seed | "none (deterministic)" | "none (deterministic)" |
| weights | "uniform" | "uniform" |

accepted difference: cuml-gpu algo_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu metric_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu query_tile: our query_tile partitions all queries without changing k or the exact distance metric; internal tiling is logged (neighbors.py)

### knn-reg / istella (rows full, shape X 200000x220; Xq 4000x220; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-reg.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 38.2 | 38.2..38.2 | 1 | - | - | 38.2 | - | - (stored whole) | - | - | 2596.3 | 938.0 | finite=True, r2=0.418145, rmse=0.625388 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 36.1 | 36.1..36.1 | 1 | 1.057 | - | 202.6 | 36.1 | 166.41 (upload_ms_untimed) | 0.189 (whole/whole) | - | 1955.7 | 602.0 | finite=True, r2=0.418145, rmse=0.625388 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KNeighborsRegressor(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`
- `cuml-gpu`: `cuml.KNeighborsRegressor(algorithm='brute', metric='euclidean', n_neighbors=10, output_type='cupy', p=2, verbose=False, weights='uniform')`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the reg block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsRegressor (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algo_params | null | - |
| algorithm | "brute" | "brute" |
| metric | "euclidean" | "euclidean" |
| metric_params | null | - |
| n_neighbors | 10 | 10 |
| p | 2 | 2 |
| query_tile | - | 0 |
| seed | "none (deterministic)" | "none (deterministic)" |
| weights | "uniform" | "uniform" |

accepted difference: cuml-gpu algo_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu metric_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu query_tile: our query_tile partitions all queries without changing k or the exact distance metric; internal tiling is logged (neighbors.py)

### knn-reg / taxi (rows full, shape X 200000x11; Xq 4000x11; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-reg.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 11.5 | 11.5..11.5 | 1 | - | - | 11.5 | - | - (stored whole) | - | - | 1556.7 | 682.0 | finite=True, r2=0.937323, rmse=3.842028 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 5.2 | 5.2..5.2 | 1 | 2.231 | - | 20.5 | 5.2 | 15.34 (upload_ms_untimed) | 0.562 (whole/whole) | - | 834.5 | 440.0 | finite=True, r2=0.937323, rmse=3.842028 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.KNeighborsRegressor(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`
- `cuml-gpu`: `cuml.KNeighborsRegressor(algorithm='brute', metric='euclidean', n_neighbors=10, output_type='cupy', p=2, verbose=False, weights='uniform')`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the reg block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsRegressor (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algo_params | null | - |
| algorithm | "brute" | "brute" |
| metric | "euclidean" | "euclidean" |
| metric_params | null | - |
| n_neighbors | 10 | 10 |
| p | 2 | 2 |
| query_tile | - | 0 |
| seed | "none (deterministic)" | "none (deterministic)" |
| weights | "uniform" | "uniform" |

accepted difference: cuml-gpu algo_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu metric_params: no algorithm or distance keyword overrides on the explicit brute-force kneighbors call (nearest_neighbors.pyx)

accepted difference: cuml-gpu query_tile: our query_tile partitions all queries without changing k or the exact distance metric; internal tiling is logged (neighbors.py)

### linearsvc / istella (rows full, shape X 1000000x220; Xq 100000x220; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvc.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 468.3 | 468.3..468.3 | 1 | - | - | 468.3 | - | - (stored whole) | - | - | 2476.7 | 2218.0 | accuracy=0.923470 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 270.0 | 270.0..270.0 | 1 | 1.735 | - | 877.5 | 270.0 | 607.50 (upload_ms_untimed) | 0.534 (whole/whole) | - | 3028.5 | 1366.0 | accuracy=0.922870 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearSVC(C=1, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='squared_hinge', max_iter=1000, multi_class='ovr', penalized_intercept=False, penalty='l2', tol=0.0001)`
- `cuml-gpu`: `cuml.LinearSVC(C=1, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='squared_hinge', max_iter=1000, multi_class='ovr', n_streams=1, output_type='cupy', penalized_intercept=False, penalty='l2', tol=0.0001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: penalty='l2', loss='squared_hinge', C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True, class_weight=None; ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0, random_state=7. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: solver: ours and cuML L-BFGS on the primal with an unpenalized intercept; scikit-learn liblinear (dual='auto'), which penalizes the intercept

mismatch: seed: ours and cuML LinearSVC have no seed argument

config: cuML benchmark (RAPIDS), LinearSVC (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| class_weight | null | null |
| fit_intercept | true | true |
| lbfgs_memory | 5 | 5 |
| linesearch_max_iter | 100 | 100 |
| loss | "squared_hinge" | "squared_hinge" |
| max_iter | 1000 | 1000 |
| multi_class | "ovr" | "ovr" |
| n_streams | 1 | - |
| penalized_intercept | false | false |
| penalty | "l2" | "l2" |
| seed | "none (deterministic)" | "none (deterministic)" |
| tol | 0.0001 | 0.0001 |

accepted difference: cuml-gpu class_weight: None (unweighted) set explicitly on every arm

accepted difference: cuml-gpu n_streams: cuML n_streams schedules fitting in parallel streams; loss, penalty, multiclass strategy and stopping controls are compared separately

### linearsvc / taxi (rows full, shape X 1000000x11; Xq 100000x11; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvc.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 68.7 | 68.7..68.7 | 1 | - | - | 68.7 | - | - (stored whole) | - | - | 1599.9 | 682.0 | accuracy=0.763330 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 8.0 | 8.0..8.0 | 1 | 8.546 | - | 61.0 | 8.0 | 52.94 (upload_ms_untimed) | 1.127 (whole/whole) | - | 1051.8 | 490.0 | accuracy=0.762990 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearSVC(C=1, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='squared_hinge', max_iter=1000, multi_class='ovr', penalized_intercept=False, penalty='l2', tol=0.0001)`
- `cuml-gpu`: `cuml.LinearSVC(C=1, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='squared_hinge', max_iter=1000, multi_class='ovr', n_streams=1, output_type='cupy', penalized_intercept=False, penalty='l2', tol=0.0001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: penalty='l2', loss='squared_hinge', C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True, class_weight=None; ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0, random_state=7. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: solver: ours and cuML L-BFGS on the primal with an unpenalized intercept; scikit-learn liblinear (dual='auto'), which penalizes the intercept

mismatch: seed: ours and cuML LinearSVC have no seed argument

config: cuML benchmark (RAPIDS), LinearSVC (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| class_weight | null | null |
| fit_intercept | true | true |
| lbfgs_memory | 5 | 5 |
| linesearch_max_iter | 100 | 100 |
| loss | "squared_hinge" | "squared_hinge" |
| max_iter | 1000 | 1000 |
| multi_class | "ovr" | "ovr" |
| n_streams | 1 | - |
| penalized_intercept | false | false |
| penalty | "l2" | "l2" |
| seed | "none (deterministic)" | "none (deterministic)" |
| tol | 0.0001 | 0.0001 |

accepted difference: cuml-gpu class_weight: None (unweighted) set explicitly on every arm

accepted difference: cuml-gpu n_streams: cuML n_streams schedules fitting in parallel streams; loss, penalty, multiclass strategy and stopping controls are compared separately

### linearsvr / istella (rows full, shape X 1000000x220; Xq 100000x220; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvr.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 135.2 | 135.2..135.2 | 1 | - | - | 135.2 | - | - (stored whole) | - | - | 2427.2 | 1450.0 | finite=True, r2=-0.106761, rmse=0.878794 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 105.7 | 105.7..105.7 | 1 | 1.279 | - | 713.7 | 105.7 | 607.96 (upload_ms_untimed) | 0.189 (whole/whole) | - | 2931.1 | 1374.0 | finite=True, r2=-0.106761, rmse=0.878795 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearSVR(C=1, epsilon=0, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='epsilon_insensitive', max_iter=1000, penalized_intercept=False, penalty='l2', tol=0.0001)`
- `cuml-gpu`: `cuml.LinearSVR(C=1, epsilon=0, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='epsilon_insensitive', max_iter=1000, output_type='cupy', penalized_intercept=False, penalty='l2', tol=0.0001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: penalty='l2', loss='epsilon_insensitive', epsilon=0.0, C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: penalty='l2' set on ours and cuML (their default is 'l1'); scikit-learn has only l2

mismatch: solver: ours and cuML L-BFGS on the primal; scikit-learn liblinear dual coordinate descent (dual=True, the only form for this loss)

mismatch: intercept: ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0 (liblinear penalizes it)

mismatch: seed: ours and cuML LinearSVR have no seed argument; scikit-learn 7

config: cuML benchmark (RAPIDS), LinearSVR (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| epsilon | 0.0 | 0.0 |
| fit_intercept | true | true |
| lbfgs_memory | 5 | 5 |
| linesearch_max_iter | 100 | 100 |
| loss | "epsilon_insensitive" | "epsilon_insensitive" |
| max_iter | 1000 | 1000 |
| penalized_intercept | false | false |
| penalty | "l2" | "l2" |
| seed | "none (deterministic)" | "none (deterministic)" |
| tol | 0.0001 | 0.0001 |

### linearsvr / taxi (rows full, shape X 1000000x11; Xq 100000x11; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvr.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 35.1 | 35.1..35.1 | 1 | - | - | 35.1 | - | - (stored whole) | - | - | 1550.1 | 682.0 | finite=True, r2=0.899814, rmse=5.041273 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 17.1 | 17.1..17.1 | 1 | 2.053 | - | 68.8 | 17.1 | 51.72 (upload_ms_untimed) | 0.510 (whole/whole) | - | 958.4 | 498.0 | finite=True, r2=0.899813, rmse=5.041302 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearSVR(C=1, epsilon=0, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='epsilon_insensitive', max_iter=1000, penalized_intercept=False, penalty='l2', tol=0.0001)`
- `cuml-gpu`: `cuml.LinearSVR(C=1, epsilon=0, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='epsilon_insensitive', max_iter=1000, output_type='cupy', penalized_intercept=False, penalty='l2', tol=0.0001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: penalty='l2', loss='epsilon_insensitive', epsilon=0.0, C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: penalty='l2' set on ours and cuML (their default is 'l1'); scikit-learn has only l2

mismatch: solver: ours and cuML L-BFGS on the primal; scikit-learn liblinear dual coordinate descent (dual=True, the only form for this loss)

mismatch: intercept: ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0 (liblinear penalizes it)

mismatch: seed: ours and cuML LinearSVR have no seed argument; scikit-learn 7

config: cuML benchmark (RAPIDS), LinearSVR (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| epsilon | 0.0 | 0.0 |
| fit_intercept | true | true |
| lbfgs_memory | 5 | 5 |
| linesearch_max_iter | 100 | 100 |
| loss | "epsilon_insensitive" | "epsilon_insensitive" |
| max_iter | 1000 | 1000 |
| penalized_intercept | false | false |
| penalty | "l2" | "l2" |
| seed | "none (deterministic)" | "none (deterministic)" |
| tol | 0.0001 | 0.0001 |

### svr / istella (rows full, shape X 10000x220; Xq 10000x220; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.svr.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 63.9 | 63.9..63.9 | 1 | - | - | 63.9 | - | - (stored whole) | - | - | 2475.1 | 908.0 | finite=True, r2=0.318258, rmse=0.680816 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 42.6 | 42.6..42.6 | 1 | 1.499 | - | 58.8 | 42.6 | 16.21 (upload_ms_untimed) | 1.086 (whole/whole) | - | 1792.4 | 462.0 | finite=True, r2=0.318232, rmse=0.680829 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.SVR(C=1, cache_size=2000, coef0=0, degree=3, epsilon=0.1, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, tol=0.001, verbose=False)`
- `cuml-gpu`: `cuml.SVR(C=1, cache_size=2000, coef0=0, degree=3, epsilon=0.1, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, output_type='cupy', tol=0.001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: kernel='rbf', gamma=1/d, C=1.0, epsilon=0.1, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: cache_size=2000 on every arm; ours honors it at predict only (DEVIATION 871); libsvm is single-threaded; shrinking=True is scikit-learn's only

mismatch: seed: no arm has a seed argument

config: cuML benchmark (RAPIDS), SVR-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| cache_size | 2000.0 | 2000.0 |
| coef0 | 0.0 | 0.0 |
| degree | 3 | 3 |
| epsilon | 0.1 | 0.1 |
| gamma | 0.004545454545454545 | 0.004545454545454545 |
| kernel | "rbf" | "rbf" |
| max_iter | -1 | -1 |
| nochange_steps | 1000 | 1000 |
| seed | "none (deterministic)" | "none (deterministic)" |
| tol | 0.001 | 0.001 |

### svr / taxi (rows full, shape X 10000x11; Xq 10000x11; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.svr.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 65.3 | 65.3..65.3 | 1 | - | - | 65.3 | - | - (stored whole) | - | - | 1553.2 | 938.0 | finite=True, r2=0.767551, rmse=7.680395 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 44.2 | 44.2..44.2 | 1 | 1.478 | - | 49.1 | 44.2 | 4.94 (upload_ms_untimed) | 1.330 (whole/whole) | - | 906.0 | 442.0 | finite=True, r2=0.767551, rmse=7.680405 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.SVR(C=1, cache_size=2000, coef0=0, degree=3, epsilon=0.1, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, tol=0.001, verbose=False)`
- `cuml-gpu`: `cuml.SVR(C=1, cache_size=2000, coef0=0, degree=3, epsilon=0.1, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, output_type='cupy', tol=0.001, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: kernel='rbf', gamma=1/d, C=1.0, epsilon=0.1, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: cache_size=2000 on every arm; ours honors it at predict only (DEVIATION 871); libsvm is single-threaded; shrinking=True is scikit-learn's only

mismatch: seed: no arm has a seed argument

config: cuML benchmark (RAPIDS), SVR-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| C | 1.0 | 1.0 |
| cache_size | 2000.0 | 2000.0 |
| coef0 | 0.0 | 0.0 |
| degree | 3 | 3 |
| epsilon | 0.1 | 0.1 |
| gamma | 0.09090909090909091 | 0.09090909090909091 |
| kernel | "rbf" | "rbf" |
| max_iter | -1 | -1 |
| nochange_steps | 1000 | 1000 |
| seed | "none (deterministic)" | "none (deterministic)" |
| tol | 0.001 | 0.001 |

### tsvd / istella (rows full, shape X 1000000x220)

race: done, driver rc 0, log `logs/classical2.tsvd.istella.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 91.6 | 91.6..91.6 | 1 | - | - | 91.6 | - | - (stored whole) | - | - | 2337.3 | 2986.0 | explained_variance_ratio_sum=1.000000, relative_reconstruction_error=0.0001314 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 35.5 | 35.5..35.5 | 1 | 2.576 | - | 603.1 | 35.5 | 567.58 (upload_ms_untimed) | 0.152 (whole/whole) | - | 2734.6 | 1314.0 | explained_variance_ratio_sum=1.000000, relative_reconstruction_error=0.0001472 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.TruncatedSVD(algorithm='covariance_eigh', n_components=10, n_iter=5, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, tol=0)`
- `cuml-gpu`: `cuml.TruncatedSVD(algorithm='full', n_components=10, n_iter=15, output_type='cupy', random_state=7, tol=1e-07, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_components=10 (the cuML benchmark's tSVD), tol=0.0, n_iter=5, n_oversamples=10, random_state=7. Rows: 1000000 stride rows of the train split, raw (sentinel cleaned, not scaled). Timed: fit.

mismatch: algorithm: ours 'covariance_eigh' (eigh of X^T X), scikit-learn 'arpack' (tol=0, exact to ARPACK's tolerance), cuML 'full'

config: cuML benchmark (RAPIDS), tSVD (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algorithm | "full" | "covariance_eigh" |
| n_components | 10 | 10 |
| n_iter | 15 | 5 |
| n_oversamples | - | 10 |
| power_iteration_normalizer | - | "auto" |
| seed | 7 | 7 |
| tol | 1e-07 | 0.0 |

accepted difference: cuml-gpu algorithm: cuML TruncatedSVD has no 'covariance_eigh'; it runs 'full'

accepted difference: cuml-gpu n_iter: cuML TruncatedSVD's n_iter is read only by its 'jacobi' solver (cuml/decomposition/tsvd.pyx: 'Used in Jacobi solver'); the raced 'full' solver, COV_EIG_DQ, a covariance eigendecomposition, iterates nothing. cuML's own scikit-learn interop maps n_iter 5 to its 15

accepted difference: cuml-gpu n_oversamples: randomized-solver controls are inactive: ours covariance_eigh and cuML 'full' are eigendecompositions

accepted difference: cuml-gpu power_iteration_normalizer: randomized-solver controls are inactive: ours covariance_eigh and cuML 'full' are eigendecompositions

accepted difference: cuml-gpu tol: cuML TruncatedSVD's tol is read only by its 'jacobi' solver (cuml/decomposition/tsvd.pyx: 'Used if algorithm = "jacobi"'); the raced 'full' solver has no tolerance. cuML's own scikit-learn interop maps tol 0.0 to its 1e-7

### tsvd / taxi (rows full, shape X 1000000x11)

race: done, driver rc 0, log `logs/classical2.tsvd.taxi.rows-full.log`, ran on nv-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | NVIDIA L40S (host nv-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 5.5 | 5.5..5.5 | 1 | - | - | 5.5 | - | - (stored whole) | - | - | 1538.6 | 682.0 | explained_variance_ratio_sum=0.999965, relative_reconstruction_error=0.003257 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |
| cuml-gpu | cuml | gpu | NVIDIA L40S (host nv-box) | cuml 26.08.00 | opponent | 5.8 | 5.8..5.8 | 1 | 0.943 | - | 50.3 | 5.8 | 44.47 (upload_ms_untimed) | 0.110 (whole/whole) | - | 966.5 | 516.0 | explained_variance_ratio_sum=0.999964, relative_reconstruction_error=0.003257 | - | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.TruncatedSVD(algorithm='covariance_eigh', n_components=10, n_iter=5, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, tol=0)`
- `cuml-gpu`: `cuml.TruncatedSVD(algorithm='full', n_components=10, n_iter=15, output_type='cupy', random_state=7, tol=1e-07, verbose=False)`

memory, ours, cuml-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU nvidia-smi --query-compute-apps used_memory for this pid at the round's end (context and pools; not a peak)

settings: n_components=10 (the cuML benchmark's tSVD), tol=0.0, n_iter=5, n_oversamples=10, random_state=7. Rows: 1000000 stride rows of the train split, raw (sentinel cleaned, not scaled). Timed: fit.

mismatch: algorithm: ours 'covariance_eigh' (eigh of X^T X), scikit-learn 'arpack' (tol=0, exact to ARPACK's tolerance), cuML 'full'

config: cuML benchmark (RAPIDS), tSVD (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | cuml-gpu | ours |
|---|---||---|---|
| library (source) | cuml (get_params) | anonlib (get_params) |
| algorithm | "full" | "covariance_eigh" |
| n_components | 10 | 10 |
| n_iter | 15 | 5 |
| n_oversamples | - | 10 |
| power_iteration_normalizer | - | "auto" |
| seed | 7 | 7 |
| tol | 1e-07 | 0.0 |

accepted difference: cuml-gpu algorithm: cuML TruncatedSVD has no 'covariance_eigh'; it runs 'full'

accepted difference: cuml-gpu n_iter: cuML TruncatedSVD's n_iter is read only by its 'jacobi' solver (cuml/decomposition/tsvd.pyx: 'Used in Jacobi solver'); the raced 'full' solver, COV_EIG_DQ, a covariance eigendecomposition, iterates nothing. cuML's own scikit-learn interop maps n_iter 5 to its 15

accepted difference: cuml-gpu n_oversamples: randomized-solver controls are inactive: ours covariance_eigh and cuML 'full' are eigendecompositions

accepted difference: cuml-gpu power_iteration_normalizer: randomized-solver controls are inactive: ours covariance_eigh and cuML 'full' are eigendecompositions

accepted difference: cuml-gpu tol: cuML TruncatedSVD's tol is read only by its 'jacobi' solver (cuml/decomposition/tsvd.pyx: 'Used if algorithm = "jacobi"'); the raced 'full' solver has no tolerance. cuML's own scikit-learn interop maps tol 0.0 to its 1e-7

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

