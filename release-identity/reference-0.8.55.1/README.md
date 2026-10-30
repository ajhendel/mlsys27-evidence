# Reference table of the 0.8.55.1 maintenance release

`reference-table-0.8.55.1.json.gz` is the verifier reference table shipped by the 0.8.55.1 maintenance release. It differs
from the table shipped in 0.8.55 in exactly 36 entries, all in three optimizer lanes (sequence-adamax 9,
sequence-nadam 9, sequence-lr-schedulers 18), whose 0.8.55 entries were recorded before an optimizer update in that
release and were not refreshed. All other 41,175 entries are unchanged.

Checked against this table, every reference-checked part in this folder's evidence matches: 13,743 parts on each GPU
target (routine and neural-training profiles together) and 13,608 on the Arm CPU, zero mismatches.

To check a 0.8.55 installation against it (gunzip first):

    python -m anonlib verify --all --reference-table reference-table-0.8.55.1.json
