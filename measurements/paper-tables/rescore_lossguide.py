#!/usr/bin/env python3
"""Re-score the two gbdt-lossguide races in the paper's 0.8.55 boards under the corrected tooling (archive branch
archive/paper-v0855-fair-opponents): (1) bench_board_evidence 0c78975820 -- an arm refused at fit is exempt from the
timed read-back, so drop "timed parameter read-back missing: <arm>" for such arms; (2) race_fairness da4c291677 --
one enumerated setting under two spellings is one setting. Only these races are touched; each change is noted."""
import copy, json, sys, datetime
sys.path.insert(0, "/home/user/anonlib-wt/v0855-fair-opponents/tools")
import race_fairness as RF
R = "/home/user/CascadeProjects/mlsys/results/boards-20261030-0855/"
NOTE = ("re-scored 2026-10-30 under corrected tooling (archive/paper-v0855-fair-opponents 0c78975820 refused-arm "
        "read-back exemption; da4c291677 enumerated-setting spelling)")
for fn, rid in (("amd.json", "trees/gbdt-lossguide/taxi/rows=full"), ("nvidia.json", "trees/gbdt-lossguide/taxi/rows=full")):
    board = json.load(open(R + fn)); race = board["races"][rid]
    refused = {}
    for c in race.get("cells") or []:
        refused[c["arm"]] = refused.get(c["arm"], True) and str(c.get("status") or "").startswith("REFUSED")
    dropped = 0
    for c in (race.get("cells") or []) + (race.get("infer_cells") or []):
        m = c.get("measurement") or {}
        miss = m.get("missing") or []
        keep = [x for x in miss if not (x.startswith("timed parameter read-back missing: ")
                                        and refused.get(x.split(": ", 1)[1]))]
        if len(keep) != len(miss):
            dropped += len(miss) - len(keep)
            m["missing"] = keep
            if not keep:
                m["completeness"] = "complete"
            m.setdefault("rescore_notes", []).append(NOTE)
    before = {k: v.get("verdict") for k, v in race["audit"].items() if isinstance(v, dict)}
    mini = {"races": {rid: race}}
    RF.apply(mini, prev=copy.deepcopy(mini))
    race = mini["races"][rid]; board["races"][rid] = race
    after = {k: v.get("verdict") for k, v in race["audit"].items() if isinstance(v, dict)}
    print(fn, rid, "dropped", dropped, "before", before, "after", after)
    json.dump(board, open(R + fn, "w"), indent=2, sort_keys=True)
