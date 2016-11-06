#!/usr/bin/env python

# grab some data
import random

# this will be age in months, weight in lbs, length in inches

data = []

for i in range(1000):
    age = random.randint(0, 24)
    length = age + 20.0 + random.randint(-50, 50) / 10.0
    weight = age + 10.0 + random.randint(-50, 50)
    is_girl = random.randint(0, 1)
    data.append((age, length, weight, is_girl))


# BEGIN XXX
# LGT-1
# need to fill this in
# should return the who percentile
# http://www.cdc.gov/growthcharts/who/boys_length_weight.htm
# http://www.cdc.gov/growthcharts/who/girls_length_weight.htm
# those are 2 data charts for this (if is_girl = 1, use the girl chart)
# interpolate if between percentiles (linear interpolation is fine)
def compute_who_length_percentile(age, length, weight, is_girl):
    return 0.0

# DONE

bmis = []
who_length_percentiles = []
for age, length, weight, is_girl in data:
    bmi = weight / (length * length) * 703
    who_length_percentile = compute_who_length_percentile(
        age, length, weight, is_girl)

    bmis.append(bmi)
    who_length_percentiles.append(who_length_percentile)

print "Average BMI", sum(bmis) / len(bmis)
print "Average who_length_percentile", sum(who_length_percentiles) / len(who_length_percentiles)
