# anonlib benchmark board

Generated 2026-10-30T13:40:29Z from `board.json` (schema `anonlib-bench-board/1`).

## Box

| field | value |
|---|---|
| vendor / API | amd / hip |
| GPU | AMD Instinct MI300X VF |
| GPU driver | 6.19.14.31400000 |
| CPU | INTEL(R) XEON(R) PLATINUM 8568Y+ (20 logical cores) |
| memory bytes | 253347024896 |
| OS | Ubuntu 24.04.4 LTS |
| Python | 3.12.3 CPython |
| anonlib | 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl, sha256 ca912ce50c59efaeffd64d7b195215d4ea48c67e00c9dabd619475a6be4c1170) |
| script commit | 9c216a59c54f971a8016175f668ca7e18c3d6775 |
| patch sync | - |
| modes | identical |
| rounds | 1 timed after 1 warm-up, arms interleaved round by round |
| seed | 7 |
| opponent versions | catboost 1.2.10, amd_xgboost 3.2.0, scikit-learn 1.7.2, torch 2.13.0+rocm7.1, numpy 2.5.4 |

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

Races: 1 planned, 1 done, 0 failed, 0 unsupported, 0 pending. Cells: 6 (REFUSED 3, ok 3).

Inference cells: 8 (UNKNOWN 2, not-scored 3, ok 3).

## Quality at a glance

Per lane and dataset: our FAST value, our IDENTICAL value, and each opponent's.

| family | lane | dataset | metric | ours FAST | ours IDENTICAL | opponents |
|---|---|---|---|---|---|---|
| trees | gbdt-lossguide | taxi | logloss (lower is better) | - | 0.527894 | ours-gain0 0.527761; xgboost-gpu 0.527815; lightgbm-cuda -; lightgbm-cpu -; lightgbm-opencl - |
| trees | gbdt-lossguide | taxi | auc (higher is better) | - | 0.632011 | ours-gain0 0.631961; xgboost-gpu 0.631973; lightgbm-cuda -; lightgbm-cpu -; lightgbm-opencl - |

## Inference at a glance

Batch prediction, each arm with its own fitted model from the same race; medians in ms. `FAST = IDENTICAL bits` compares our two tiers' predictions on the same rows. Our CPU is never raced or reported.

| family | lane | dataset | batch | rows | ours FAST ms | ours IDENTICAL ms | FAST = IDENTICAL bits | opponents |
|---|---|---|---|---|---|---|---|---|
| trees | gbdt-lossguide | taxi | test | 500000 | - | 13.4 | - | xgboost-gpu 60.3 ms (IDENTICAL/arm 0.217); lightgbm-cuda - ms (IDENTICAL/arm -) |
| trees | gbdt-lossguide | taxi | large | 1000000 | - | 19.0 | - | xgboost-gpu 85.8 ms (IDENTICAL/arm 0.223); lightgbm-cuda - ms (IDENTICAL/arm -) |

## Trees

### gbdt-lossguide / taxi (rows full, shape taxi-4110786x16)

race: done, driver rc 0, log `raw/trees/gbdt-lossguide.taxi.rows-full.log`, ran on anonlib-amd-box

| arm | library | device | hardware | version | mode | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | peak host MB | peak GPU MB | quality | hash stable | comparability | installed_wheel | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL (ours, vs catboost-gpu) | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @9c216a59c | identical | 19180.6 | 19180.6..19180.6 | 1 | - | - | 19180.6 | - | - (stored whole) | - | - | 7239.6 | 2521.7 | auc=0.632011, logloss=0.527894 | yes | COMPARABLE | wheel | ok |
| anonlib IDENTICAL (ours-gain0, vs xgboost-*) | anonlib | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @9c216a59c | identical | 19538.6 | 19538.6..19538.6 | 1 | - | - | 19538.6 | - | - (stored whole) | - | - | 7314.5 | 2521.8 | auc=0.631961, logloss=0.527761 | yes | COMPARABLE | wheel | ok |
| xgboost-gpu | xgboost | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | xgboost 3.2.0 | opponent | 17700.8 | 17700.8..17700.8 | 1 | 1.104 | - | 17700.8 | - | - (stored whole) | 1.104 (whole/whole) | - | 8164.6 | 2521.8 | auc=0.631973, logloss=0.527815 | yes | COMPARABLE | - | ok (measured this run) |
| lightgbm-cuda | lightgbm | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | lightgbm version unknown (copied from this board's record) | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | COMPARABLE | - | REFUSED(asked for by --arms and not built here; built: xgboost-cpu,xgboost-gpu) (measured this run) |
| lightgbm-cpu | lightgbm | cpu | CPU INTEL(R) XEON(R) PLATINUM 8568Y+ (host anonlib-amd-box, AMD Instinct MI300X box) | lightgbm version unknown (copied from this board's record) | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | COMPARABLE | - | REFUSED(RuntimeError: MIN-CHILD: LightGBM 4.7.0 aborts at the lane's min_child_samples 1 and min_child_weight 0, and its default) (measured this run) |
| lightgbm-opencl | lightgbm | gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | lightgbm version unknown (copied from this board's record) | opponent | - | - | 0 | - | - | - | - | - | - | - | - | - | - | - | COMPARABLE | - | REFUSED(RuntimeError: MIN-CHILD: LightGBM 4.7.0 aborts at the lane's min_child_samples 1 and min_child_weight 0, and its default) (measured this run) |

calls:
- `ours`: `anonlib.GradientBoosting(bagging_temperature=1, best_model_min_trees=1, boost_from_average=False, boosting_type='Plain', bootstrap_type='No', border_build_max_samples=200000, border_count=254, class_weights=[1, 1.31013], ...)`
- `ours-gain0`: `anonlib.GradientBoosting(bagging_temperature=1, best_model_min_trees=1, boost_from_average=False, boosting_type='Plain', bootstrap_type='No', border_build_max_samples=0, border_count=254, class_weights=[1, 1.31013], ...)`
- `xgboost-gpu`: `xgboost.XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1, device='cuda', enable_categorical=False, gamma=0, grow_policy='lossguide', ...)`

memory, ours, ours-gain0, xgboost-gpu: host Linux VmHWM after clear_refs 5 (peak RSS over the round); GPU KFD /sys/class/kfd/kfd/proc/11766/vram_* bytes for this pid at the round's end (not a peak) (the process total: every arm in this one process)

memory, lightgbm-cuda, lightgbm-cpu, lightgbm-opencl: host not sampled; GPU not sampled

FSPEED-FIT-VERDICT: `lane=gbdt-lossguide arms=ours,ours-gain0,xgboost-gpu leaves=ours:128000,ours-gain0:128000,xgboost-gpu:128000 spread=0.0000 verdict=COMPARABLE`

config: NVIDIA gbm-bench, xgb/lgbm/cat shared_params, ntrees 500 (https://github.com/anon/anon/blob/73a976b036249ff9d8cb30cf9082bb414b911379/algorithms.py)

parameters (tools/bench_board_params.py, read back from each constructed arm; reference `ours`, seed 7): MATCHED

| parameter | ours | ours-gain0 | xgboost-gpu |
|---|---||---|---||---|---|
| library (source) | anonlib (get_params) | anonlib (get_params + input_binning (the harness's input block, speed_gbdt_arm.attach_input)) | xgboost (get_params + input_binning (the harness's input block, speed_gbdt_arm.attach_input)) |
| bagging_temperature | 1.0 | 1.0 | - |
| base_score | - | - | 0.5 |
| best_model_min_trees | 1 | 1 | - |
| boost_from_average | false | false | - |
| boosting_type | "Plain" | "Plain" | "gbtree" |
| bootstrap_type | "No" | "No" | - |
| border_build_max_samples | 200000 | 0 | - |
| callbacks | - | - | null |
| cat_features | null | null | - |
| colsample_bylevel | - | - | 1.0 |
| ctr_estimation_permutation_id | null | null | - |
| early_stopping_rounds | - | - | null |
| enable_categorical | - | - | false |
| eval_metric | - | - | null |
| feature_border_type | "GreedyLogSum" | "GreedyLogSum" | - |
| feature_fraction | 1.0 | 1.0 | 1.0 |
| feature_fraction_bynode | - | - | 1.0 |
| feature_types | - | - | null |
| feature_weights | - | - | null |
| fold_len_multiplier | 2.0 | 2.0 | - |
| fold_permutation_block | null | null | - |
| grow_policy | "Lossguide" | "Lossguide" | "lossguide" |
| input_binning | - | "pre-binned input on both arms (GreedyLogSum, 254 borders); bins sha256 52d044bc97e62c09622f914f31f0fe1f0b5dc065d51227ecdce876dfa1dadebc" | "pre-binned input on both arms (GreedyLogSum, 254 borders); bins sha256 52d044bc97e62c09622f914f31f0fe1f0b5dc065d51227ecdce876dfa1dadebc" |
| interaction_constraints | - | - | null |
| leaf_estimation_iterations | 1 | 1 | - |
| leaf_estimation_method | "Newton" | "Newton" | - |
| learning_rate | 0.1 | 0.1 | 0.1 |
| loss | "Logloss" | "Logloss" | - |
| loss_alpha | null | null | - |
| loss_border | null | null | - |
| loss_delta | null | null | - |
| loss_q | null | null | - |
| loss_variance_power | null | null | - |
| max_bin | 255 | 255 | 255 |
| max_cat_threshold | - | - | null |
| max_cat_to_onehot | - | - | null |
| max_delta_step | - | - | 0.0 |
| max_depth | 16 | 16 | 16 |
| max_leaves | 256 | 256 | 256 |
| min_child_weight | 0.0 | 0.0 | 0.0 |
| min_samples_leaf | 1 | 1 | - |
| min_split_gain | null | 0.0 | 0.0 |
| missing | - | - | NaN |
| monotone_constraints | - | - | null |
| multi_strategy | - | - | null |
| n_estimators | 500 | 500 | 500 |
| nan_mode | "Min" | "Min" | - |
| num_parallel_tree | - | - | null |
| objective | - | - | "binary:logistic" |
| od_pvalue | null | null | - |
| od_type | null | null | - |
| od_wait | null | null | - |
| one_hot_features | null | null | - |
| permutation_count | null | null | - |
| random_strength | 0.0 | 0.0 | - |
| reg_alpha | - | - | 0.0 |
| reg_lambda | 1.0 | 1.0 | 1.0 |
| sampling_method | - | - | null |
| scale_pos_weight | 1.3101271632087197 | 1.3101271632087197 | 1.3101271632087197 |
| score_function | "NewtonL2" | "NewtonL2" | - |
| seed | 7 | 7 | 7 |
| subsample | null | null | 1.0 |
| tree_method | - | - | "hist" |
| use_best_model | null | null | - |
| use_pointwise_searcher | false | false | - |

accepted difference: xgboost-gpu bagging_temperature: no row sampling on either arm: ours bootstrap_type 'No', XGBoost subsample 1.0

accepted difference: xgboost-gpu base_score: margin 0 on both: XGBoost base_score 0.5 (logit 0, learner.cc:172-173), ours boost_from_average False

accepted difference: xgboost-gpu best_model_min_trees: no eval set and no early stopping on either arm; ours' od_*/use_best_model unset

accepted difference: xgboost-gpu boost_from_average: margin 0 on both: ours boost_from_average False, XGBoost base_score 0.5 (logit 0)

accepted difference: xgboost-gpu boosting_type: different vocabularies: ours and CatBoost 'Plain' (not Ordered), XGBoost booster 'gbtree'; both plain gradient boosting

accepted difference: xgboost-gpu bootstrap_type: no row sampling on either arm: ours bootstrap_type 'No', XGBoost subsample 1.0

accepted difference: xgboost-gpu border_build_max_samples: the same pre-binned input on both arms (pre-binned input on both arms (GreedyLogSum, 254 borders); bins sha256 52d044bc97e62c09622f914f31f0fe1f0b5dc065d51227ecdce876dfa1dadebc): every bin id is its own bin on both (ours GreedyLogSum over every row, max_bin 255 on both)

accepted difference: xgboost-gpu callbacks: no eval set, early stopping or callback on either arm

accepted difference: xgboost-gpu cat_features: no categorical columns on either arm (XGBoost enable_categorical False)

accepted difference: xgboost-gpu colsample_bylevel: no column sampling on either arm (ours feature_fraction 1.0, XGBoost colsample_* 1.0)

accepted difference: xgboost-gpu ctr_estimation_permutation_id: no categorical columns on either arm (XGBoost enable_categorical False)

accepted difference: xgboost-gpu early_stopping_rounds: no eval set, early stopping or callback on either arm

accepted difference: xgboost-gpu enable_categorical: no categorical columns on either arm (XGBoost enable_categorical False, ours cat_features None)

accepted difference: xgboost-gpu eval_metric: no eval set, early stopping or callback on either arm

accepted difference: xgboost-gpu feature_border_type: the same pre-binned input on both arms (pre-binned input on both arms (GreedyLogSum, 254 borders); bins sha256 52d044bc97e62c09622f914f31f0fe1f0b5dc065d51227ecdce876dfa1dadebc): every bin id is its own bin on both (ours GreedyLogSum over every row, max_bin 255 on both)

accepted difference: xgboost-gpu feature_fraction_bynode: no column sampling on either arm (ours feature_fraction 1.0, XGBoost colsample_* 1.0)

accepted difference: xgboost-gpu feature_types: no categorical columns on either arm (XGBoost enable_categorical False, ours cat_features None)

accepted difference: xgboost-gpu feature_weights: feature_weights unset and unread: no column sampling on either arm

accepted difference: xgboost-gpu fold_len_multiplier: ours boosting_type 'Plain' with no categorical columns: no Ordered folds to match

accepted difference: xgboost-gpu fold_permutation_block: ours boosting_type 'Plain' with no categorical columns: no Ordered folds to match

accepted difference: xgboost-gpu interaction_constraints: no split constraints on either arm

accepted difference: xgboost-gpu leaf_estimation_iterations: one Newton step per leaf on both (XGBoost param.h CalcWeight, alpha 0, no clip)

accepted difference: xgboost-gpu leaf_estimation_method: one Newton step per leaf on both (XGBoost param.h CalcWeight, alpha 0, no clip)

accepted difference: xgboost-gpu loss: binary log loss on both: ours loss 'Logloss', XGBoost objective 'binary:logistic'

accepted difference: xgboost-gpu loss_alpha: binary log loss on both; ours' other-loss parameters unset and its Logloss border the default 0.5 (0/1 labels)

accepted difference: xgboost-gpu loss_border: binary log loss on both; ours' other-loss parameters unset and its Logloss border the default 0.5 (0/1 labels)

accepted difference: xgboost-gpu loss_delta: binary log loss on both; ours' other-loss parameters unset and its Logloss border the default 0.5 (0/1 labels)

accepted difference: xgboost-gpu loss_q: binary log loss on both; ours' other-loss parameters unset and its Logloss border the default 0.5 (0/1 labels)

accepted difference: xgboost-gpu loss_variance_power: binary log loss on both; ours' other-loss parameters unset and its Logloss border the default 0.5 (0/1 labels)

accepted difference: xgboost-gpu max_cat_threshold: no categorical columns on either arm (XGBoost enable_categorical False, ours cat_features None)

accepted difference: xgboost-gpu max_cat_to_onehot: no categorical columns on either arm (XGBoost enable_categorical False, ours cat_features None)

accepted difference: xgboost-gpu max_delta_step: max_delta_step 0: XGBoost's leaf weight and gain are -G/(H+lambda) and G^2/(H+lambda), as ours

accepted difference: xgboost-gpu min_samples_leaf: no row-count floor beyond a non-empty child on either arm (XGBoost expand_entry.cuh:37-39; ours min_data_in_leaf 1)

accepted difference: xgboost-gpu missing: NaN marks a missing value, and the data has none (the driver refuses XGBoost otherwise)

accepted difference: xgboost-gpu monotone_constraints: no split constraints on either arm

accepted difference: xgboost-gpu multi_strategy: one binary output: XGBoost's default one_output_per_tree, one tree per round as ours

accepted difference: xgboost-gpu nan_mode: no NaN in the data (the driver refuses XGBoost otherwise): neither missing-value rule is read

accepted difference: xgboost-gpu num_parallel_tree: one tree per boosting round on both (XGBoost num_parallel_tree default 1)

accepted difference: xgboost-gpu objective: binary log loss on both: XGBoost 'binary:logistic', ours 'Logloss'

accepted difference: xgboost-gpu od_pvalue: no eval set and no early stopping on either arm; ours' od_*/use_best_model unset

accepted difference: xgboost-gpu od_type: no eval set and no early stopping on either arm; ours' od_*/use_best_model unset

accepted difference: xgboost-gpu od_wait: no eval set and no early stopping on either arm; ours' od_*/use_best_model unset

accepted difference: xgboost-gpu one_hot_features: no categorical columns on either arm (XGBoost enable_categorical False)

accepted difference: xgboost-gpu permutation_count: ours boosting_type 'Plain' with no categorical columns: no Ordered folds to match

accepted difference: xgboost-gpu random_strength: no split-score noise on either arm (ours random_strength 0.0)

accepted difference: xgboost-gpu reg_alpha: reg_alpha 0: XGBoost's leaf weight and gain are -G/(H+lambda) and G^2/(H+lambda), as ours

accepted difference: xgboost-gpu sampling_method: no row sampling on either arm (XGBoost subsample 1.0, ours bootstrap_type 'No')

accepted difference: xgboost-gpu score_function: the Newton L2 gain on both (XGBoost param.h CalcGain, alpha 0, no clip)

accepted difference: xgboost-gpu subsample: no row sampling on any arm: ours and CatBoost bootstrap_type 'No' (neither accepts subsample beside it, so it stays unset), XGBoost and LightGBM subsample 1.0

accepted difference: xgboost-gpu tree_method: histogram growth on quantized features on both (bin count compared as max_bin)

accepted difference: xgboost-gpu use_best_model: no eval set and no early stopping on either arm; ours' od_*/use_best_model unset

accepted difference: xgboost-gpu use_pointwise_searcher: ours' greedy Depthwise/Lossguide searcher (the only one off SymmetricTree)

Inference (each arm predicts with its own model from the fit rounds above):

| arm | hardware | version | batch | rows | median ms | min..max ms | rounds | ours IDENTICAL / arm | ours FAST / arm | whole ms | kernel ms | copy ms (source) | ours IDENTICAL / arm (clock) | ours FAST / arm (clock) | quality | hash stable | comparability | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anonlib IDENTICAL (ours, vs catboost-gpu) | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @9c216a59c | test | 500000 | 13.4 | 13.4..13.4 | 1 | - | - | 13.4 | - | - (stored whole) | - | - | auc=0.632011, auc_matches_fit=True, logloss=0.527894, logloss_matches_fit=True | yes | COMPARABLE | ok |
| anonlib IDENTICAL (ours-gain0, vs xgboost-*) | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @9c216a59c | test | 500000 | 13.1 | 13.1..13.1 | 1 | - | - | 13.1 | - | - (stored whole) | - | - | auc=0.631961, auc_matches_fit=True, logloss=0.527761, logloss_matches_fit=True | yes | COMPARABLE | ok |
| xgboost-gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | xgboost 3.2.0 | test | 500000 | 60.3 | 60.3..60.3 | 1 | 0.217 | - | 60.3 | - | - (stored whole) | 0.217 (whole/whole) | - | auc=0.631973, auc_matches_fit=True, logloss=0.527815, logloss_matches_fit=True | yes | COMPARABLE | ok |
| lightgbm-cuda | AMD Instinct MI300X VF (host anonlib-amd-box) | lightgbm version unknown (copied from this board's record) | test | - | - | - | 0 | - | - | - | - | - | - | - | - | - | COMPARABLE | UNKNOWN(no inference lines) |
| anonlib IDENTICAL (ours, vs catboost-gpu) | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @9c216a59c | large | 1000000 | 19.0 | 19.0..19.0 | 1 | - | - | 19.0 | - | - (stored whole) | - | - | - | yes | COMPARABLE | not-scored: quality not scored (scorer failed): the race recorded no quality for this arm (its scorer did not run) |
| anonlib IDENTICAL (ours-gain0, vs xgboost-*) | AMD Instinct MI300X VF (host anonlib-amd-box) | anonlib 0.8.55 (wheel anonlib-0.8.55-py3-none-manylinux_2_35_x86_64.whl), scripts @9c216a59c | large | 1000000 | 19.1 | 19.1..19.1 | 1 | - | - | 19.1 | - | - (stored whole) | - | - | - | yes | COMPARABLE | not-scored: quality not scored (scorer failed): the race recorded no quality for this arm (its scorer did not run) |
| xgboost-gpu | AMD Instinct MI300X VF (host anonlib-amd-box) | xgboost 3.2.0 | large | 1000000 | 85.8 | 85.8..85.8 | 1 | 0.223 | - | 85.8 | - | - (stored whole) | 0.223 (whole/whole) | - | - | yes | COMPARABLE | not-scored: quality not scored (scorer failed): the race recorded no quality for this arm (its scorer did not run) |
| lightgbm-cuda | AMD Instinct MI300X VF (host anonlib-amd-box) | lightgbm version unknown (copied from this board's record) | large | - | - | - | 0 | - | - | - | - | - | - | - | - | - | COMPARABLE | UNKNOWN(no inference lines) |

inference call, ours: anonlib.GradientBoosting(bagging_temperature=1, best_model_min_trees=1, boost_from_average=False, boosting_type='Plain', bootstrap_type='No', border_build_max_samples=200000, border_count=254, class_weights=[1, 1.31013], ...); anonlib GradientBoosting.predict_proba(X), column 1

inference call, ours-gain0: anonlib.GradientBoosting(bagging_temperature=1, best_model_min_trees=1, boost_from_average=False, boosting_type='Plain', bootstrap_type='No', border_build_max_samples=0, border_count=254, class_weights=[1, 1.31013], ...); anonlib GradientBoosting.predict_proba(X), column 1

inference call, xgboost-gpu: xgboost.XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1, device='cuda', enable_categorical=False, gamma=0, grow_policy='lossguide', ...); xgboost Booster.inplace_predict(host X) on a CUDA booster (no cupy here, so XGBoost's own device-mismatch fallback), probability

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

