#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:26:21 2021

@author: mahan
"""

import numpy as np
import matplotlib.pyplot as plt
np.random.RandomState(seed=10)

u1 = [np.random.uniform(0,1) for _ in range(10000)]

u2 = list(u1)
np.random.shuffle(u2)

z1 = ((-2*np.log(u1)) ** (0.5)) * np.cos(np.dot(2*np.pi, u2))
