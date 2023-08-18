import sys
from stats_util import Stats

if len(sys.argv) <= 1:
    sys.exit("Usage: python stats.py [number1] [number2] ...")
nums = list(map(int, sys.argv[1:]))

# Create a Stats object
data = Stats(nums)

p = input("Enter percentile:")
value = data.value_from_percentile(float(p))

print("Value corresponding to entered percentile is :", value)
