# Core
import random

def random_float(min_val: float, max_val: float, decimals: int = 1) -> float:
    return round(random.uniform(min_val, max_val), decimals)

def random_choice(options: list):
    return random.choice(options)

def vary_value(current: float, variation_pct: float, min_val: float, max_val: float) -> float:
    """Apply small random variation to a value, clamped to min/max."""
    change = current * random.uniform(-variation_pct, variation_pct)
    new_value = current + change
    return round(max(min_val, min(max_val, new_value)), 2)
