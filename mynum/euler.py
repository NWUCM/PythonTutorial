#!/usr/bin/python3
# -*- encoding:utf-8 -*-
# @author    : EastMagica
# @time      : 2021/09/27 11:48:19
# @file      : euler.py
# @project   : PythonTutorial
# @software  : VSCode
import numpy as np


def euler_explicit(f, t0, y0, h, step=10):
    ys = [y0]

    for i in range(step):
        ys.append(
            ys[-1] + h * f(t0 + i*h, ys[-1])
        )

    return np.array(ys)



