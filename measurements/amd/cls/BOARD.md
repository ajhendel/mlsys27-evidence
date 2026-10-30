# anonlib benchmark board

Generated 2026-10-30T07:01:00Z from `board.json` (schema `anonlib-bench-board/1`).

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
| script commit | 4e927c92495a43695bd5a8f524a47caef52c00bd |
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

Races: 26 planned, 26 done, 0 failed, 0 unsupported, 0 pending. Cells: 28 (REFUSED 2, ok 26).

Inference cells: 8 (ok 8).

## Quality at a glance

Per lane and dataset: our FAST value, our IDENTICAL value, and each opponent's.

| family | lane | dataset | metric | ours FAST | ours IDENTICAL | opponents |
|---|---|---|---|---|---|---|
| classical | hdbscan | istella | n_clusters | - | 47 | - |
| classical | hdbscan | istella | noise_fraction | - | 0.253810 | - |
| classical | hdbscan | istella | rows | - | 100000 | - |
| classical | hdbscan | istella | silhouette (higher is better) | - | -0.003856 | - |
| classical | hdbscan | taxi | n_clusters | - | 161 | - |
| classical | hdbscan | taxi | noise_fraction | - | 0.140550 | - |
| classical | hdbscan | taxi | rows | - | 100000 | - |
| classical | hdbscan | taxi | silhouette (higher is better) | - | 0.001505 | - |
| classical | kde | istella | mean_log_likelihood (higher is better) | - | -222.270583 | - |
| classical | kde | istella | rows_without_density | - | 0 | - |
| classical | kde | taxi | mean_log_likelihood (higher is better) | - | -14.826436 | - |
| classical | kde | taxi | rows_without_density | - | 0 | - |
| classical | ols | istella | r2 (higher is better) | - | 0.332506 | torch-gpu nan |
| classical | ols | istella | rmse (lower is better) | - | 0.681740 | torch-gpu nan |
| classical | ols | taxi | r2 (higher is better) | - | 0.908837 | torch-gpu 0.908837 |
| classical | ols | taxi | rmse (lower is better) | - | 4.696477 | torch-gpu 4.696472 |
| classical | pca | istella | explained_variance_ratio_sum (higher is better) | - | 1.000000 | - |
| classical | pca | taxi | explained_variance_ratio_sum (higher is better) | - | 0.999997 | - |
| classical | svc | istella | accuracy (higher is better) | - | 0.922200 | - |
| classical | svc | istella | n_support | - | 2400 | - |
| classical | svc | taxi | accuracy (higher is better) | - | 0.767500 | - |
| classical | svc | taxi | n_support | - | 5527 | - |
| classical2 | kernel-ridge | istella | r2 (higher is better) | - | 0.385427 | - |
| classical2 | kernel-ridge | istella | rmse (lower is better) | - | 0.646407 | - |
| classical2 | kernel-ridge | taxi | r2 (higher is better) | - | 0.726543 | - |
| classical2 | kernel-ridge | taxi | rmse (lower is better) | - | 8.330373 | - |
| classical2 | knn-clf | istella | accuracy (higher is better) | - | 0.926250 | - |
| classical2 | knn-clf | taxi | accuracy (higher is better) | - | 0.741750 | - |
| classical2 | knn-reg | istella | r2 (higher is better) | - | 0.418145 | - |
| classical2 | knn-reg | istella | rmse (lower is better) | - | 0.625388 | - |
| classical2 | knn-reg | taxi | r2 (higher is better) | - | 0.937323 | - |
| classical2 | knn-reg | taxi | rmse (lower is better) | - | 3.842028 | - |
| classical2 | linearsvc | istella | accuracy (higher is better) | - | 0.923470 | - |
| classical2 | linearsvc | taxi | accuracy (higher is better) | - | 0.763330 | - |
| classical2 | linearsvr | istella | r2 (higher is better) | - | -0.106761 | - |
| classical2 | linearsvr | istella | rmse (lower is better) | - | 0.878794 | - |
| classical2 | linearsvr | taxi | r2 (higher is better) | - | 0.899814 | - |
| classical2 | linearsvr | taxi | rmse (lower is better) | - | 5.041273 | - |
| classical2 | svr | istella | r2 (higher is better) | - | 0.318258 | - |
| classical2 | svr | istella | rmse (lower is better) | - | 0.680816 | - |
| classical2 | svr | taxi | r2 (higher is better) | - | 0.767551 | - |
| classical2 | svr | taxi | rmse (lower is better) | - | 7.680395 | - |
| classical2 | tsvd | istella | explained_variance_ratio_sum (higher is better) | - | 1.000000 | - |
| classical2 | tsvd | istella | relative_reconstruction_error (lower is better) | - | 0.0001314 | - |
| classical2 | tsvd | taxi | explained_variance_ratio_sum (higher is better) | - | 0.999965 | - |
| classical2 | tsvd | taxi | relative_reconstruction_error (lower is better) | - | 0.003257 | - |

## Inference at a glance

Batch prediction, each arm with its own fitted model from the same race; medians in ms. `FAST = IDENTICAL bits` compares our two tiers' predictions on the same rows. Our CPU is never raced or reported.

| family | lane | dataset | batch | rows | ours FAST ms | ours IDENTICAL ms | FAST = IDENTICAL bits | opponents |
|---|---|---|---|---|---|---|---|---|
| classical | ols | istella | Xq | 500000 | - | 20.5 | - | torch-gpu 0.2 ms (IDENTICAL/arm 93.658) |
| classical | ols | taxi | Xq | 500000 | - | 3.5 | - | torch-gpu 0.1 ms (IDENTICAL/arm 29.755) |
| classical | pca | istella | Xq | 500000 | - | 30.2 | - | - |
| classical | pca | taxi | Xq | 500000 | - | 13.7 | - | - |
| classical | svc | istella | Xq | 10000 | - | 10.3 | - | - |
| classical | svc | taxi | Xq | 10000 | - | 11.7 | - | - |

## Classical

### dbscan / istella (rows full, shape 1000000x220)

race: done, driver rc 0, log `logs/classical.dbscan.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | wheel | REFUSED(error: {"error": "Exception('DBSCAN has no memory left for a single batch row: the fixed cost is 5000000 bytes against a budget of -22000000')", "event": "error", "stage": "round 0"}) |

calls:
- `ours`: `anonlib.DBSCAN(algorithm='brute', eps=3, metric='euclidean', min_samples=2, prediction_data=False)`

settings: eps=3, min_samples=2 (the cuML benchmark's DBSCAN) on every arm; metric='euclidean'. Rows: dbscan block: 1,000,000 rows, standardized. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: algorithm='brute' on every raced arm (ours, cuml-gpu, scikit-learn: the cuML benchmark's cpu_args); ours' default 'rbc' is not raced, and cuml-gpu-rbc (overflows at 1,000,000 rows) is not on the roster

mismatch: leaf_size=30 and n_jobs=-1: scikit-learn only

config: cuML benchmark (RAPIDS), DBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "brute" |
| eps | 3.0 |
| max_iterations | null |
| max_mbytes_per_batch | null |
| metric | "euclidean" |
| min_samples | 2 |
| prediction_data | false |
| seed | "none (deterministic)" |

### dbscan / taxi (rows full, shape 1000000x11)

race: done, driver rc 0, log `logs/classical.dbscan.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | LIKE-FOR-LIKE-SPAN | wheel | REFUSED(timeout: null) |

calls:
- `ours`: `anonlib.DBSCAN(algorithm='brute', eps=3, metric='euclidean', min_samples=2, prediction_data=False)`

settings: eps=3, min_samples=2 (the cuML benchmark's DBSCAN) on every arm; metric='euclidean'. Rows: dbscan block: 1,000,000 rows, standardized. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: algorithm='brute' on every raced arm (ours, cuml-gpu, scikit-learn: the cuML benchmark's cpu_args); ours' default 'rbc' is not raced, and cuml-gpu-rbc (overflows at 1,000,000 rows) is not on the roster

mismatch: leaf_size=30 and n_jobs=-1: scikit-learn only

config: cuML benchmark (RAPIDS), DBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "brute" |
| eps | 3.0 |
| max_iterations | null |
| max_mbytes_per_batch | null |
| metric | "euclidean" |
| min_samples | 2 |
| prediction_data | false |
| seed | "none (deterministic)" |

### hdbscan / istella (rows full, shape 100000x220)

race: done, driver rc 0, log `logs/classical.hdbscan.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 1057.4 | 1057.4..1057.4 | 1 | - | - | 1057.4 | 1055.7 | 1.67 (upload_ms_separate) | - | - | 3161.6 | 2056.8 | n_clusters=47, noise_fraction=0.253810, rows=100000, silhouette=-0.003856, silhouette_library=sklearn.metrics.silhouette_score, silhouette_library_version=1.7.2, silhouette_scope=all consumed rows; noise is a label group; no sampling | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.HDBSCAN(allow_single_cluster=False, alpha=1, cluster_selection_epsilon=0, cluster_selection_method='eom', max_cluster_size=0, metric='euclidean', min_cluster_size=100, min_samples=10, prediction_data=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/169249/vram_* bytes for this pid at the round's end (not a peak)

settings: min_samples=10 (scikit-learn 11: the same core distance, the 10th neighbour besides the point), min_cluster_size=100, metric='euclidean', cluster_selection_method='eom', cluster_selection_epsilon=0.0, alpha=1.0, allow_single_cluster=False. Rows: the dbscan block's first 100,000 rows. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: max_cluster_size: ours and cuML 0, scikit-learn None (both mean no limit)

mismatch: spanning tree: ours and scikit-learn build the exact minimum spanning tree of the full mutual-reachability graph; cuML builds it over the symmetrized (min_samples + 1)-NN graph in mutual-reachability space and joins its components (cuVS cluster/detail/single_linkage.cuh:75-135, mst.cuh cross_component_nn), an approximate tree where groups of duplicate rows split that graph (taxi)

mismatch: min_samples: ours and cuML 10, scikit-learn 11. The SAME k-th neighbour: cuML's runner.h:68-80 (ours transcribes it) runs the k-NN at min_samples + 1 including the point itself; scikit-learn's kneighbors(X, min_samples) counts the point itself (its HDBSCAN Notes say so). tools/bench_board_params.py maps both to one canonical value

mismatch: k-NN graph: exact brute force on every arm; cuML build_algo='brute_force' pinned (as ours); scikit-learn algorithm='brute' (FAIRNESS FIX 2026-10-13: it was 'auto', a KD/ball tree), leaf_size=40 unused, n_jobs=-1

config: cuML benchmark (RAPIDS), HDBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| allow_single_cluster | false |
| alpha | 1.0 |
| cluster_selection_epsilon | 0.0 |
| cluster_selection_method | "eom" |
| max_cluster_size | 0 |
| metric | "euclidean" |
| min_cluster_size | 100 |
| min_samples | 10 |
| prediction_data | false |
| seed | "none (deterministic)" |

### hdbscan / taxi (rows full, shape 100000x11)

race: done, driver rc 0, log `logs/classical.hdbscan.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 347.2 | 347.2..347.2 | 1 | - | - | 347.2 | 347.1 | 0.13 (upload_ms_separate) | - | - | 2268.2 | 1876.8 | n_clusters=161, noise_fraction=0.140550, rows=100000, silhouette=0.001505, silhouette_library=sklearn.metrics.silhouette_score, silhouette_library_version=1.7.2, silhouette_scope=all consumed rows; noise is a label group; no sampling | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.HDBSCAN(allow_single_cluster=False, alpha=1, cluster_selection_epsilon=0, cluster_selection_method='eom', max_cluster_size=0, metric='euclidean', min_cluster_size=100, min_samples=10, prediction_data=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/169742/vram_* bytes for this pid at the round's end (not a peak)

settings: min_samples=10 (scikit-learn 11: the same core distance, the 10th neighbour besides the point), min_cluster_size=100, metric='euclidean', cluster_selection_method='eom', cluster_selection_epsilon=0.0, alpha=1.0, allow_single_cluster=False. Rows: the dbscan block's first 100,000 rows. Timed: fit.

mismatch: seed: no arm has a seed argument (deterministic)

mismatch: max_cluster_size: ours and cuML 0, scikit-learn None (both mean no limit)

mismatch: spanning tree: ours and scikit-learn build the exact minimum spanning tree of the full mutual-reachability graph; cuML builds it over the symmetrized (min_samples + 1)-NN graph in mutual-reachability space and joins its components (cuVS cluster/detail/single_linkage.cuh:75-135, mst.cuh cross_component_nn), an approximate tree where groups of duplicate rows split that graph (taxi)

mismatch: min_samples: ours and cuML 10, scikit-learn 11. The SAME k-th neighbour: cuML's runner.h:68-80 (ours transcribes it) runs the k-NN at min_samples + 1 including the point itself; scikit-learn's kneighbors(X, min_samples) counts the point itself (its HDBSCAN Notes say so). tools/bench_board_params.py maps both to one canonical value

mismatch: k-NN graph: exact brute force on every arm; cuML build_algo='brute_force' pinned (as ours); scikit-learn algorithm='brute' (FAIRNESS FIX 2026-10-13: it was 'auto', a KD/ball tree), leaf_size=40 unused, n_jobs=-1

config: cuML benchmark (RAPIDS), HDBSCAN (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| allow_single_cluster | false |
| alpha | 1.0 |
| cluster_selection_epsilon | 0.0 |
| cluster_selection_method | "eom" |
| max_cluster_size | 0 |
| metric | "euclidean" |
| min_cluster_size | 100 |
| min_samples | 10 |
| prediction_data | false |
| seed | "none (deterministic)" |

### kde / istella (rows full, shape 100000x220)

race: done, driver rc 0, log `logs/classical.kde.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 29.6 | 29.6..29.6 | 1 | - | - | 29.6 | 27.6 | 2.05 (upload_ms_separate) | - | - | 2481.7 | 2195.1 | mean_log_likelihood=-222.270583, rows_without_density=0 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KernelDensity(algorithm='auto', atol=0, bandwidth=1, breadth_first=True, kernel='gaussian', leaf_size=40, metric='euclidean', rtol=0)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/170377/vram_* bytes for this pid at the round's end (not a peak)

settings: bandwidth=1.0, kernel='gaussian' (the cuML benchmark's KernelDensity), metric='euclidean' on every arm; ours and scikit-learn atol=0, rtol=0, algorithm='auto', leaf_size=40, breadth_first=True. Rows: kde block: 100,000 fit rows, 2,000 queries, standardized. Timed: score_samples; the fit is before the clock on every arm.

mismatch: seed: no arm has a seed argument (exact density)

mismatch: cuML has no atol, rtol, algorithm, leaf_size or breadth_first (exact brute force)

config: cuML benchmark (RAPIDS), KernelDensity (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "auto" |
| atol | 0.0 |
| bandwidth | 1.0 |
| breadth_first | true |
| kernel | "gaussian" |
| leaf_size | 40 |
| metric | "euclidean" |
| metric_params | null |
| rtol | 0.0 |
| seed | "none (deterministic)" |

### kde / taxi (rows full, shape 100000x11)

race: done, driver rc 0, log `logs/classical.kde.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 3.9 | 3.9..3.9 | 1 | - | - | 3.9 | 3.8 | 0.14 (upload_ms_separate) | - | - | 2400.4 | 2195.1 | mean_log_likelihood=-14.826436, rows_without_density=0 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KernelDensity(algorithm='auto', atol=0, bandwidth=1, breadth_first=True, kernel='gaussian', leaf_size=40, metric='euclidean', rtol=0)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/170572/vram_* bytes for this pid at the round's end (not a peak)

settings: bandwidth=1.0, kernel='gaussian' (the cuML benchmark's KernelDensity), metric='euclidean' on every arm; ours and scikit-learn atol=0, rtol=0, algorithm='auto', leaf_size=40, breadth_first=True. Rows: kde block: 100,000 fit rows, 2,000 queries, standardized. Timed: score_samples; the fit is before the clock on every arm.

mismatch: seed: no arm has a seed argument (exact density)

mismatch: cuML has no atol, rtol, algorithm, leaf_size or breadth_first (exact brute force)

config: cuML benchmark (RAPIDS), KernelDensity (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "auto" |
| atol | 0.0 |
| bandwidth | 1.0 |
| breadth_first | true |
| kernel | "gaussian" |
| leaf_size | 40 |
| metric | "euclidean" |
| metric_params | null |
| rtol | 0.0 |
| seed | "none (deterministic)" |

### ols / istella (rows full, shape 2043304x220)

race: done, driver rc 0, log `logs/classical.ols.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 446.3 | 446.3..446.3 | 1 | - | - | 446.3 | 412.8 | 33.43 (upload_ms_separate) | - | - | 4543.1 | 2115.8 | finite=True, r2=0.332506, rmse=0.681740 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-gpu | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 6972.1 | 6972.1..6972.1 | 1 | 0.064 | - | 7122.7 | 6972.1 | 150.60 (upload_ms_untimed) | 0.059 (kernel/kernel) | - | 3959.9 | 5304.1 | finite=False, r2=nan, rmse=nan | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearRegression(fit_intercept=True)`
- `torch-gpu`: `torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/170959/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

settings: fit_intercept=True. Rows: big block, raw; R2 and RMSE on the 500,000 eval rows. Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

mismatch: solver (no parameter on ours): ours' IDENTICAL fit centers X and y and runs a blocked Householder TSQR of [X / y], then the SVD of its small R with a pseudo-inverse cutoff (python/anonlib/linear_model.py _ols_tsqr_centered; tall designs, at most 511 columns; the condition number is not squared); its FAST fit (Apple) solves the equilibrated normal equations. cuML algorithm='qr' (geqrf, R x = Q^T y: the same QR of the tall design, no rank cutoff); scikit-learn scipy lstsq gelsd (SVD)

mismatch: torch-gpu: torch.linalg.lstsq(driver='gels') on the centered data, torch's own least-squares routine (QR without pivoting, full rank assumed; the only driver torch has on CUDA and ROCm; MPS has no lstsq, so Apple has no torch arm)

mismatch: torch-gpu-eigh: refused, harness-written (REFUSED_ARMS)

mismatch: scikit-learn positive=False and copy_X=True: parameters ours does not have

config: cuML benchmark (RAPIDS), LinearRegression (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-gpu |
|---|---||---|---|
| library (source) | anonlib (get_params) | torch (declared) |
| driver | - | "gels" |
| fit_intercept | true | true |
| seed | "none (deterministic)" | 7 |

accepted difference: torch-gpu driver: QR least squares on both: torch driver='gels' (QR, no pivoting) and ours' TSQR of the centered design; fit_intercept is compared

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 20.5 | 20.5..20.5 | 1 | - | - | 20.5 | - | - (stored whole) | - | - | predict_max_rel_err_own_fp64=8.451e-06, r2_eval=0.332506, rmse_eval=0.681740 | yes | LIKE-FOR-LIKE-SPAN | ok |
| torch-gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | Xq | 500000 | 0.2 | 0.2..0.2 | 1 | 93.658 | - | 9.7 | 0.2 | 9.45 (upload_ms_untimed (the predict rows' own upload)) | 2.120 (whole/whole (kernel not derivable)) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=nan, predict_max_rel_err_own_fp64=nan, r2_eval=nan, rmse_eval=nan | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.LinearRegression(fit_intercept=True); anonlib LinearRegression.predict(Xq), host rows in, host result out

inference call, torch-gpu: torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7); torch Xq @ coef + intercept; Xq uploaded before the clock, which ends at the device synchronize

### ols / taxi (rows full, shape 4000000x11)

race: done, driver rc 0, log `logs/classical.ols.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 13.2 | 13.2..13.2 | 1 | - | - | 13.2 | 9.9 | 3.30 (upload_ms_separate) | - | - | 2604.3 | 2115.6 | finite=True, r2=0.908837, rmse=4.696477 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |
| torch-gpu | torch | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | opponent | 114.4 | 114.4..114.4 | 1 | 0.115 | - | 238.8 | 114.4 | 124.38 (upload_ms_untimed) | 0.086 (kernel/kernel) | - | 1938.0 | 695.4 | finite=True, r2=0.908837, rmse=4.696472 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | - | ok (measured this run) |

calls:
- `ours`: `anonlib.LinearRegression(fit_intercept=True)`
- `torch-gpu`: `torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/171330/vram_* bytes for this pid at the round's end (not a peak)

memory, torch-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU torch.cuda.max_memory_allocated, reset before the round (caching allocator peak; the context is not in it)

settings: fit_intercept=True. Rows: big block, raw; R2 and RMSE on the 500,000 eval rows. Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

mismatch: solver (no parameter on ours): ours' IDENTICAL fit centers X and y and runs a blocked Householder TSQR of [X / y], then the SVD of its small R with a pseudo-inverse cutoff (python/anonlib/linear_model.py _ols_tsqr_centered; tall designs, at most 511 columns; the condition number is not squared); its FAST fit (Apple) solves the equilibrated normal equations. cuML algorithm='qr' (geqrf, R x = Q^T y: the same QR of the tall design, no rank cutoff); scikit-learn scipy lstsq gelsd (SVD)

mismatch: torch-gpu: torch.linalg.lstsq(driver='gels') on the centered data, torch's own least-squares routine (QR without pivoting, full rank assumed; the only driver torch has on CUDA and ROCm; MPS has no lstsq, so Apple has no torch arm)

mismatch: torch-gpu-eigh: refused, harness-written (REFUSED_ARMS)

mismatch: scikit-learn positive=False and copy_X=True: parameters ours does not have

config: cuML benchmark (RAPIDS), LinearRegression (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | torch-gpu |
|---|---||---|---|
| library (source) | anonlib (get_params) | torch (declared) |
| driver | - | "gels" |
| fit_intercept | true | true |
| seed | "none (deterministic)" | 7 |

accepted difference: torch-gpu driver: QR least squares on both: torch driver='gels' (QR, no pivoting) and ours' TSQR of the centered design; fit_intercept is compared

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 3.5 | 3.5..3.5 | 1 | - | - | 3.5 | - | - (stored whole) | - | - | predict_max_rel_err_own_fp64=9.438e-08, r2_eval=0.908837, rmse_eval=4.696477 | yes | LIKE-FOR-LIKE-SPAN | ok |
| torch-gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | torch 2.13.0+rocm7.1 | Xq | 500000 | 0.1 | 0.1..0.1 | 1 | 29.755 | - | 1.0 | 0.1 | 0.88 (upload_ms_untimed (the predict rows' own upload)) | 3.540 (whole/whole (kernel not derivable)) | - | bits_equal_vs_ours=False, max_abs_diff_vs_ours=0.001099, predict_max_rel_err_own_fp64=9.855e-08, r2_eval=0.908837, rmse_eval=4.696472 | yes | SPAN-ASYMMETRIC(upload_outside_its_clock) | ok |

inference call, ours: anonlib.LinearRegression(fit_intercept=True); anonlib LinearRegression.predict(Xq), host rows in, host result out

inference call, torch-gpu: torch.linalg_lstsq(driver='gels', fit_intercept=True, seed=7); torch Xq @ coef + intercept; Xq uploaded before the clock, which ends at the device synchronize

### pca / istella (rows full, shape 2043304x220)

race: done, driver rc 0, log `logs/classical.pca.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 87.0 | 87.0..87.0 | 1 | - | - | 87.0 | 53.6 | 33.42 (upload_ms_separate) | - | - | 4542.9 | 2705.4 | explained_variance_ratio_sum=1.000000 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/171591/vram_* bytes for this pid at the round's end (not a peak)

settings: n_components=10 (the cuML benchmark's PCA), whiten=False, random_state=7; ours and scikit-learn svd_solver='covariance_eigh'. Rows: big block, raw. Timed: fit.

mismatch: svd_solver: cuML has no 'covariance_eigh'; cuml-gpu runs svd_solver='full' (cuML's COV_EIG_DQ: the eigendecomposition of the covariance, ours' algorithm)

mismatch: torch-gpu: refused (fairness audit 2026-10-13): torch has no PCA estimator of this algorithm; the old arm was a covariance eigh our harness wrote from torch ops, not an opponent (torch.pca_lowrank is a randomized method, a different algorithm)

mismatch: random_state is read by none of the covariance solvers; set to 7 on every arm

config: cuML benchmark (RAPIDS), PCA (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| copy | true |
| iterated_power | "auto" |
| n_components | 10 |
| n_oversamples | 10 |
| power_iteration_normalizer | "auto" |
| seed | 7 |
| svd_solver | "covariance_eigh" |
| tol | 0.0 |
| whiten | false |

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 30.2 | 30.2..30.2 | 1 | - | - | 30.2 | - | - (stored whole) | - | - | transform_max_rel_err_own_fp64=3.69e-07 | yes | LIKE-FOR-LIKE-SPAN | ok |

inference call, ours: anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False); anonlib PCA.transform(Xq), host rows in, host result out

### pca / taxi (rows full, shape 4000000x11)

race: done, driver rc 0, log `logs/classical.pca.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 10.4 | 10.4..10.4 | 1 | - | - | 10.4 | 7.1 | 3.31 (upload_ms_separate) | - | - | 2603.4 | 2055.3 | explained_variance_ratio_sum=0.999997 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/171980/vram_* bytes for this pid at the round's end (not a peak)

settings: n_components=10 (the cuML benchmark's PCA), whiten=False, random_state=7; ours and scikit-learn svd_solver='covariance_eigh'. Rows: big block, raw. Timed: fit.

mismatch: svd_solver: cuML has no 'covariance_eigh'; cuml-gpu runs svd_solver='full' (cuML's COV_EIG_DQ: the eigendecomposition of the covariance, ours' algorithm)

mismatch: torch-gpu: refused (fairness audit 2026-10-13): torch has no PCA estimator of this algorithm; the old arm was a covariance eigh our harness wrote from torch ops, not an opponent (torch.pca_lowrank is a randomized method, a different algorithm)

mismatch: random_state is read by none of the covariance solvers; set to 7 on every arm

config: cuML benchmark (RAPIDS), PCA (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| copy | true |
| iterated_power | "auto" |
| n_components | 10 |
| n_oversamples | 10 |
| power_iteration_normalizer | "auto" |
| seed | 7 |
| svd_solver | "covariance_eigh" |
| tol | 0.0 |
| whiten | false |

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 500000 | 13.7 | 13.7..13.7 | 1 | - | - | 13.7 | - | - (stored whole) | - | - | transform_max_rel_err_own_fp64=9.857e-08 | yes | LIKE-FOR-LIKE-SPAN | ok |

inference call, ours: anonlib.PCA(copy=True, iterated_power='auto', n_components=10, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, svd_solver='covariance_eigh', tol=0, whiten=False); anonlib PCA.transform(Xq), host rows in, host result out

### svc / istella (rows full, shape 10000x220)

race: done, driver rc 0, log `logs/classical.svc.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 43.0 | 43.0..43.0 | 1 | - | - | 43.0 | 42.7 | 0.23 (upload_ms_separate) | - | - | 2441.9 | 5276.0 | accuracy=0.922200, n_support=2400 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/172175/vram_* bytes for this pid at the round's end (not a peak)

settings: C=1.0, kernel='rbf', gamma=1/d, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB, class_weight=None. Rows: svc block: 10,000 fit rows, 10,000 eval rows, standardized. Timed: fit.

mismatch: seed: scikit-learn and cuML random_state=7 (read only with probability=True); ours refuses random_state without probability=True, so ours stays None

mismatch: cache_size=2000 on every arm; ours honors it only as the prediction buffer (DEVIATION 871), so its training is unaffected

mismatch: shrinking=True: scikit-learn only; nochange_steps=1000: ours and cuML only

config: cuML benchmark (RAPIDS), SVC-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| break_ties | false |
| cache_size | 2000.0 |
| class_weight | null |
| coef0 | 0.0 |
| decision_function_shape | "ovo" |
| degree | 3 |
| gamma | 0.004545454545454545 |
| kernel | "rbf" |
| max_iter | -1 |
| nochange_steps | 1000 |
| probability | false |
| seed | null |
| tol | 0.001 |

accepted difference: ours seed: anonlib SVC refuses random_state without probability=True (the fit draws nothing); scikit-learn and cuML get 7

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 10000 | 10.3 | 10.3..10.3 | 1 | - | - | 10.3 | - | - (stored whole) | - | - | accuracy_eval=0.922200 | yes | LIKE-FOR-LIKE-SPAN | ok |

inference call, ours: anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False); anonlib SVC.predict(Xq), host rows in, host result out

### svc / taxi (rows full, shape 10000x11)

race: done, driver rc 0, log `logs/classical.svc.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 1052.5 | 1052.5..1052.5 | 1 | - | - | 1052.5 | 1052.4 | 0.10 (upload_ms_separate) | - | - | 2402.1 | 2055.9 | accuracy=0.767500, n_support=5527 | yes | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/172358/vram_* bytes for this pid at the round's end (not a peak)

settings: C=1.0, kernel='rbf', gamma=1/d, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB, class_weight=None. Rows: svc block: 10,000 fit rows, 10,000 eval rows, standardized. Timed: fit.

mismatch: seed: scikit-learn and cuML random_state=7 (read only with probability=True); ours refuses random_state without probability=True, so ours stays None

mismatch: cache_size=2000 on every arm; ours honors it only as the prediction buffer (DEVIATION 871), so its training is unaffected

mismatch: shrinking=True: scikit-learn only; nochange_steps=1000: ours and cuML only

config: cuML benchmark (RAPIDS), SVC-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| break_ties | false |
| cache_size | 2000.0 |
| class_weight | null |
| coef0 | 0.0 |
| decision_function_shape | "ovo" |
| degree | 3 |
| gamma | 0.09090909090909091 |
| kernel | "rbf" |
| max_iter | -1 |
| nochange_steps | 1000 |
| probability | false |
| seed | null |
| tol | 0.001 |

accepted difference: ours seed: anonlib SVC refuses random_state without probability=True (the fit draws nothing); scikit-learn and cuML get 7

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | Xq | 10000 | 11.7 | 11.7..11.7 | 1 | - | - | 11.7 | - | - (stored whole) | - | - | accuracy_eval=0.767500 | yes | LIKE-FOR-LIKE-SPAN | ok |

inference call, ours: anonlib.SVC(C=1, break_ties=False, cache_size=2000, coef0=0, decision_function_shape='ovo', degree=3, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, probability=False, tol=0.001, verbose=False); anonlib SVC.predict(Xq), host rows in, host result out

## Classical, wave 2

### kernel-ridge / istella (rows full, shape X 10000x220; Xq 10000x220; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.kernel-ridge.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 1651.1 | 1651.1..1651.1 | 1 | - | - | 1651.1 | - | - (stored whole) | - | - | 3157.5 | 4445.9 | finite=True, r2=0.385427, rmse=0.646407 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KernelRidge(alpha=1, coef0=1, degree=3, gamma=0.00454545, kernel='rbf')`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/172566/vram_* bytes for this pid at the round's end (not a peak)

settings: alpha=1.0, kernel='rbf', gamma=1/d, degree=3, coef0=1.0. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

config: cuML benchmark (RAPIDS), KernelRidge (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| alpha | 1.0 |
| coef0 | 1.0 |
| degree | 3 |
| gamma | 0.004545454545454545 |
| kernel | "rbf" |
| seed | "none (deterministic)" |

### kernel-ridge / taxi (rows full, shape X 10000x11; Xq 10000x11; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.kernel-ridge.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 1657.9 | 1657.9..1657.9 | 1 | - | - | 1657.9 | - | - (stored whole) | - | - | 2264.7 | 2045.9 | finite=True, r2=0.726543, rmse=8.330373 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KernelRidge(alpha=1, coef0=1, degree=3, gamma=0.0909091, kernel='rbf')`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/172745/vram_* bytes for this pid at the round's end (not a peak)

settings: alpha=1.0, kernel='rbf', gamma=1/d, degree=3, coef0=1.0. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: seed: no arm has a seed argument (closed-form fit)

config: cuML benchmark (RAPIDS), KernelRidge (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| alpha | 1.0 |
| coef0 | 1.0 |
| degree | 3 |
| gamma | 0.09090909090909091 |
| kernel | "rbf" |
| seed | "none (deterministic)" |

### knn-clf / istella (rows full, shape X 200000x220; Xq 4000x220; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-clf.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 32.4 | 32.4..32.4 | 1 | - | - | 32.4 | - | - (stored whole) | - | - | 3132.5 | 1878.7 | accuracy=0.926250 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KNeighborsClassifier(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/172934/vram_* bytes for this pid at the round's end (not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the cls block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsClassifier (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "brute" |
| metric | "euclidean" |
| n_neighbors | 10 |
| p | 2 |
| query_tile | 0 |
| seed | "none (deterministic)" |
| weights | "uniform" |

### knn-clf / taxi (rows full, shape X 200000x11; Xq 4000x11; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-clf.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 11.0 | 11.0..11.0 | 1 | - | - | 11.0 | - | - (stored whole) | - | - | 2093.0 | 1702.7 | accuracy=0.741750 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KNeighborsClassifier(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/173126/vram_* bytes for this pid at the round's end (not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the cls block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsClassifier (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "brute" |
| metric | "euclidean" |
| n_neighbors | 10 |
| p | 2 |
| query_tile | 0 |
| seed | "none (deterministic)" |
| weights | "uniform" |

### knn-reg / istella (rows full, shape X 200000x220; Xq 4000x220; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-reg.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 31.3 | 31.3..31.3 | 1 | - | - | 31.3 | - | - (stored whole) | - | - | 3130.0 | 1878.4 | finite=True, r2=0.418145, rmse=0.625388 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KNeighborsRegressor(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/173312/vram_* bytes for this pid at the round's end (not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the reg block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsRegressor (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "brute" |
| metric | "euclidean" |
| n_neighbors | 10 |
| p | 2 |
| query_tile | 0 |
| seed | "none (deterministic)" |
| weights | "uniform" |

### knn-reg / taxi (rows full, shape X 200000x11; Xq 4000x11; y 200000; yq 4000)

race: done, driver rc 0, log `logs/classical2.knn-reg.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 9.1 | 9.1..9.1 | 1 | - | - | 9.1 | - | - (stored whole) | - | - | 2090.7 | 1698.4 | finite=True, r2=0.937323, rmse=3.842028 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.KNeighborsRegressor(algorithm='brute', metric='euclidean', n_neighbors=10, p=2, query_tile=0, weights='uniform')`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/173498/vram_* bytes for this pid at the round's end (not a peak)

settings: n_neighbors=10, weights='uniform', metric='euclidean', algorithm='brute'. Rows: 200000 fit rows, 4000 queries (stride subsets of the reg block, standardized by the fit rows). Timed: fit + predict of the queries.

mismatch: seed: no arm has a seed argument (exact search)

config: cuML benchmark (RAPIDS), KNeighborsRegressor (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "brute" |
| metric | "euclidean" |
| n_neighbors | 10 |
| p | 2 |
| query_tile | 0 |
| seed | "none (deterministic)" |
| weights | "uniform" |

### linearsvc / istella (rows full, shape X 1000000x220; Xq 100000x220; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvc.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 498.6 | 498.6..498.6 | 1 | - | - | 498.6 | - | - (stored whole) | - | - | 3191.0 | 1876.0 | accuracy=0.923470 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.LinearSVC(C=1, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='squared_hinge', max_iter=1000, multi_class='ovr', penalized_intercept=False, penalty='l2', tol=0.0001)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/173677/vram_* bytes for this pid at the round's end (not a peak)

settings: penalty='l2', loss='squared_hinge', C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True, class_weight=None; ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0, random_state=7. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: solver: ours and cuML L-BFGS on the primal with an unpenalized intercept; scikit-learn liblinear (dual='auto'), which penalizes the intercept

mismatch: seed: ours and cuML LinearSVC have no seed argument

config: cuML benchmark (RAPIDS), LinearSVC (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| class_weight | null |
| fit_intercept | true |
| lbfgs_memory | 5 |
| linesearch_max_iter | 100 |
| loss | "squared_hinge" |
| max_iter | 1000 |
| multi_class | "ovr" |
| penalized_intercept | false |
| penalty | "l2" |
| seed | "none (deterministic)" |
| tol | 0.0001 |

### linearsvc / taxi (rows full, shape X 1000000x11; Xq 100000x11; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvc.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 69.0 | 69.0..69.0 | 1 | - | - | 69.0 | - | - (stored whole) | - | - | 2313.8 | 1876.0 | accuracy=0.763330 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.LinearSVC(C=1, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='squared_hinge', max_iter=1000, multi_class='ovr', penalized_intercept=False, penalty='l2', tol=0.0001)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/173849/vram_* bytes for this pid at the round's end (not a peak)

settings: penalty='l2', loss='squared_hinge', C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True, class_weight=None; ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0, random_state=7. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: solver: ours and cuML L-BFGS on the primal with an unpenalized intercept; scikit-learn liblinear (dual='auto'), which penalizes the intercept

mismatch: seed: ours and cuML LinearSVC have no seed argument

config: cuML benchmark (RAPIDS), LinearSVC (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| class_weight | null |
| fit_intercept | true |
| lbfgs_memory | 5 |
| linesearch_max_iter | 100 |
| loss | "squared_hinge" |
| max_iter | 1000 |
| multi_class | "ovr" |
| penalized_intercept | false |
| penalty | "l2" |
| seed | "none (deterministic)" |
| tol | 0.0001 |

### linearsvr / istella (rows full, shape X 1000000x220; Xq 100000x220; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvr.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 104.2 | 104.2..104.2 | 1 | - | - | 104.2 | - | - (stored whole) | - | - | 3140.9 | 1875.8 | finite=True, r2=-0.106761, rmse=0.878794 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.LinearSVR(C=1, epsilon=0, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='epsilon_insensitive', max_iter=1000, penalized_intercept=False, penalty='l2', tol=0.0001)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/174205/vram_* bytes for this pid at the round's end (not a peak)

settings: penalty='l2', loss='epsilon_insensitive', epsilon=0.0, C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: penalty='l2' set on ours and cuML (their default is 'l1'); scikit-learn has only l2

mismatch: solver: ours and cuML L-BFGS on the primal; scikit-learn liblinear dual coordinate descent (dual=True, the only form for this loss)

mismatch: intercept: ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0 (liblinear penalizes it)

mismatch: seed: ours and cuML LinearSVR have no seed argument; scikit-learn 7

config: cuML benchmark (RAPIDS), LinearSVR (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| epsilon | 0.0 |
| fit_intercept | true |
| lbfgs_memory | 5 |
| linesearch_max_iter | 100 |
| loss | "epsilon_insensitive" |
| max_iter | 1000 |
| penalized_intercept | false |
| penalty | "l2" |
| seed | "none (deterministic)" |
| tol | 0.0001 |

### linearsvr / taxi (rows full, shape X 1000000x11; Xq 100000x11; y 1000000; yq 100000)

race: done, driver rc 0, log `logs/classical2.linearsvr.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 39.3 | 39.3..39.3 | 1 | - | - | 39.3 | - | - (stored whole) | - | - | 2263.9 | 1875.8 | finite=True, r2=0.899814, rmse=5.041273 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.LinearSVR(C=1, epsilon=0, fit_intercept=True, lbfgs_memory=5, linesearch_max_iter=100, loss='epsilon_insensitive', max_iter=1000, penalized_intercept=False, penalty='l2', tol=0.0001)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/174441/vram_* bytes for this pid at the round's end (not a peak)

settings: penalty='l2', loss='epsilon_insensitive', epsilon=0.0, C=1.0, tol=1e-4, max_iter=1000, fit_intercept=True. Rows: 1000000 fit and 100000 held-out stride rows (standardized by the fit rows). Timed: fit.

mismatch: penalty='l2' set on ours and cuML (their default is 'l1'); scikit-learn has only l2

mismatch: solver: ours and cuML L-BFGS on the primal; scikit-learn liblinear dual coordinate descent (dual=True, the only form for this loss)

mismatch: intercept: ours and cuML penalized_intercept=False; scikit-learn intercept_scaling=1.0 (liblinear penalizes it)

mismatch: seed: ours and cuML LinearSVR have no seed argument; scikit-learn 7

config: cuML benchmark (RAPIDS), LinearSVR (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| epsilon | 0.0 |
| fit_intercept | true |
| lbfgs_memory | 5 |
| linesearch_max_iter | 100 |
| loss | "epsilon_insensitive" |
| max_iter | 1000 |
| penalized_intercept | false |
| penalty | "l2" |
| seed | "none (deterministic)" |
| tol | 0.0001 |

### svr / istella (rows full, shape X 10000x220; Xq 10000x220; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.svr.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 86.1 | 86.1..86.1 | 1 | - | - | 86.1 | - | - (stored whole) | - | - | 3190.4 | 5096.3 | finite=True, r2=0.318258, rmse=0.680816 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.SVR(C=1, cache_size=2000, coef0=0, degree=3, epsilon=0.1, gamma=0.00454545, kernel='rbf', max_iter=-1, nochange_steps=1000, tol=0.001, verbose=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/174614/vram_* bytes for this pid at the round's end (not a peak)

settings: kernel='rbf', gamma=1/d, C=1.0, epsilon=0.1, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: cache_size=2000 on every arm; ours honors it at predict only (DEVIATION 871); libsvm is single-threaded; shrinking=True is scikit-learn's only

mismatch: seed: no arm has a seed argument

config: cuML benchmark (RAPIDS), SVR-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| cache_size | 2000.0 |
| coef0 | 0.0 |
| degree | 3 |
| epsilon | 0.1 |
| gamma | 0.004545454545454545 |
| kernel | "rbf" |
| max_iter | -1 |
| nochange_steps | 1000 |
| seed | "none (deterministic)" |
| tol | 0.001 |

### svr / taxi (rows full, shape X 10000x11; Xq 10000x11; y 10000; yq 10000)

race: done, driver rc 0, log `logs/classical2.svr.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 102.6 | 102.6..102.6 | 1 | - | - | 102.6 | - | - (stored whole) | - | - | 2267.8 | 1876.2 | finite=True, r2=0.767551, rmse=7.680395 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.SVR(C=1, cache_size=2000, coef0=0, degree=3, epsilon=0.1, gamma=0.0909091, kernel='rbf', max_iter=-1, nochange_steps=1000, tol=0.001, verbose=False)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/174801/vram_* bytes for this pid at the round's end (not a peak)

settings: kernel='rbf', gamma=1/d, C=1.0, epsilon=0.1, tol=1e-3, degree=3, coef0=0.0, max_iter=-1, cache_size=2000 MB. Rows: 10000 fit and 10000 held-out stride rows of the reg block (standardized by the fit rows). Timed: fit.

mismatch: cache_size=2000 on every arm; ours honors it at predict only (DEVIATION 871); libsvm is single-threaded; shrinking=True is scikit-learn's only

mismatch: seed: no arm has a seed argument

config: cuML benchmark (RAPIDS), SVR-RBF (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| C | 1.0 |
| cache_size | 2000.0 |
| coef0 | 0.0 |
| degree | 3 |
| epsilon | 0.1 |
| gamma | 0.09090909090909091 |
| kernel | "rbf" |
| max_iter | -1 |
| nochange_steps | 1000 |
| seed | "none (deterministic)" |
| tol | 0.001 |

### tsvd / istella (rows full, shape X 1000000x220)

race: done, driver rc 0, log `logs/classical2.tsvd.istella.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 47.6 | 47.6..47.6 | 1 | - | - | 47.6 | - | - (stored whole) | - | - | 3054.2 | 2526.0 | explained_variance_ratio_sum=1.000000, relative_reconstruction_error=0.0001314 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.TruncatedSVD(algorithm='covariance_eigh', n_components=10, n_iter=5, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, tol=0)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/174976/vram_* bytes for this pid at the round's end (not a peak)

settings: n_components=10 (the cuML benchmark's tSVD), tol=0.0, n_iter=5, n_oversamples=10, random_state=7. Rows: 1000000 stride rows of the train split, raw (sentinel cleaned, not scaled). Timed: fit.

mismatch: algorithm: ours 'covariance_eigh' (eigh of X^T X), scikit-learn 'arpack' (tol=0, exact to ARPACK's tolerance), cuML 'full'

config: cuML benchmark (RAPIDS), tSVD (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "covariance_eigh" |
| n_components | 10 |
| n_iter | 5 |
| n_oversamples | 10 |
| power_iteration_normalizer | "auto" |
| seed | 7 |
| tol | 0.0 |

### tsvd / taxi (rows full, shape X 1000000x11)

race: done, driver rc 0, log `logs/classical2.tsvd.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @4e927c924 | identical | 4.7 | 4.7..4.7 | 1 | - | - | 4.7 | - | - (stored whole) | - | - | 2254.9 | 1876.0 | explained_variance_ratio_sum=0.999965, relative_reconstruction_error=0.003257 | - | LIKE-FOR-LIKE-SPAN | wheel | ok |

calls:
- `ours`: `anonlib.TruncatedSVD(algorithm='covariance_eigh', n_components=10, n_iter=5, n_oversamples=10, power_iteration_normalizer='auto', random_state=7, tol=0)`

memory, ours: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/175170/vram_* bytes for this pid at the round's end (not a peak)

settings: n_components=10 (the cuML benchmark's tSVD), tol=0.0, n_iter=5, n_oversamples=10, random_state=7. Rows: 1000000 stride rows of the train split, raw (sentinel cleaned, not scaled). Timed: fit.

mismatch: algorithm: ours 'covariance_eigh' (eigh of X^T X), scikit-learn 'arpack' (tol=0, exact to ARPACK's tolerance), cuML 'full'

config: cuML benchmark (RAPIDS), tSVD (https://github.com/anon/anon/blob/e0f7a4e31578c8eeef376f3ce715d846bfee8d4c/python/cuml/cuml/benchmark/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours |
|---|---|
| library (source) | anonlib (get_params) |
| algorithm | "covariance_eigh" |
| n_components | 10 |
| n_iter | 5 |
| n_oversamples | 10 |
| power_iteration_normalizer | "auto" |
| seed | 7 |
| tol | 0.0 |

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

