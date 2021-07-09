#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as r
import multiprocessing as m
import datetime as dt

k=0
n=100000000

def in_circle(_):
    return (r.random()**2 + r.random()**2) < 1

if __name__ == "__main__":
    time = dt.datetime.now()
    with m.Pool(4) as pool:
        k = sum(pool.map(in_circle, range(n)))
    print('parallel', dt.datetime.now() - time)
    print(4 * k / n)
    
    time = dt.datetime.now()
    k = sum([in_circle(x) for x in range(n)])
    print('not parallel', dt.datetime.now() - time)
    print(4 * k / n)