#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:00:01 2021

@author: mahan
"""

import numpy as np
import math

def factorial(number):
    return number * factorial(number - 1) if number > 1 else 1

# only two possible outcomes that are mutually exclusive but can have different probabilities
p = 0.5

# Bernoulli Distribution, probability of success in one trial
prob = p
dist = np.random.choice(['success', 'failure'], p = [p, (1 - p)])

# Binomial Distribution
# Bernoullin repeated n times, probability of c successes in n trials
n = 5
c = 2
prob = (factorial(n) / factorial(c) * factorial(n-c)) * (p ** n / (1 - p) ** (n - c))
dist = np.random.binomial(n, p, 1000)

# Geometric Distribution
# Probability being the kth trial will be a success
k = 3
prob = p * (1 - p) ** (k - 1)

dist = []
failure = 0
while n < 1000:
    if np.random.choice(['success', 'failure'], p = [p, 1-p]) == 'failure':
        failure += 1
    else:
        dist += [failure]
        failure = 0
        n += 1

# multiple outcomes
# Uniform Distribution
dist = np.random.uniform(0,1,size=10000)

# Normal Distribution
mu = 0
sigma = 1
x = 0.1

prob = math.e ** ((-1/2) * ((x - mu)/sigma) ** 2) / (sigma * 2 * math.pi)
dist = np.random.normal(mu, sigma, 1000)

# Poisson Distribution
# number of event occurred k times in a time interval whille lam is average number of events in the same time interval
lam = 2.5
k = 2
prob = (lam ** k) * (math.e ** (-lam)) / factorial(k)
dist = np.random.poisson(lam, size = 1000)
print(prob)

# Exponential Distribution
# probability of no event occured in w time intervals / waiting time
w = 1
prob = lam * math.e ** (-lam * w)
dist = np.random.exponential(lam, size = 1000)
print(prob)