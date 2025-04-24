import re

UNIT_MULTIPLIERS = {
    "million": 1_000_000,
    "millions": 1_000_000,
    "billion": 1_000_000_000,
    "billions": 1_000_000_000,
    "thousand": 1_000,
    "k": 1_000,
    "m": 1_000_000,
    "b": 1_000_000_000
}

UNIT_MULTIPLIERS_LIST = list(UNIT_MULTIPLIERS.keys())

def get_multiplier(section):
    # Find the first occurrence of a unit in the section
    for unit in UNIT_MULTIPLIERS_LIST:
        if re.search(r'\b' + re.escape(unit) + r'\b', section, re.IGNORECASE):
            return UNIT_MULTIPLIERS[unit]
    return 1  # Default multiplier if no unit is found
