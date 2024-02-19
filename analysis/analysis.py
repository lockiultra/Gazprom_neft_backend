import numpy as np

def collect_data_from_stats_dict(stats_dict: dict) -> dict:
    res_dict = {stat: [] for stat in ("x", "y", "z")}
    for data in stats_dict:
        for stat in ("x", "y", "z"):
            res_dict[stat].append(data.__dict__[stat])
    return res_dict

def compute_analysis(stats_dict: dict) -> dict:
    res_dict = {stat: {} for stat in stats_dict.keys()}
    for stat in stats_dict.keys():
        res_dict[stat]['min'] = min(stats_dict[stat])
        res_dict[stat]['max'] = max(stats_dict[stat])
        res_dict[stat]['count'] = len(stats_dict[stat])
        res_dict[stat]['sum'] = sum(stats_dict[stat])
        res_dict[stat]['median'] = np.median(stats_dict[stat])
    return res_dict

def get_analysis(stats_dict: dict) -> dict:
    return compute_analysis(collect_data_from_stats_dict(stats_dict))