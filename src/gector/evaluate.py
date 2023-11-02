import json
from pprint import pprint
from utils.metric_utils import final_f1_score

def get_metric(path):
  with open(path, "r") as fp:
    sources = []
    preds = []
    targets = []
    for d in fp.readlines():
      d = json.loads(d)
      sources.append(d["input_text"])
      preds.append(d["predict_after"])
      targets.append(d["target_text"])

  pprint(final_f1_score(sources, preds, targets, log_fp='logs/f1_score.log'))