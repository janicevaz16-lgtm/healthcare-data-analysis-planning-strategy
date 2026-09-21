"""Healthcare classification metric helpers."""

def specificity(tn: int, fp: int) -> float:
    """TN / (TN + FP)."""
    denominator = tn + fp
    return tn / denominator if denominator else 0.0

def sensitivity(tp: int, fn: int) -> float:
    """TP / (TP + FN), equivalent to recall."""
    denominator = tp + fn
    return tp / denominator if denominator else 0.0
