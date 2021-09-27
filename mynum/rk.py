#!/usr/bin/python3
# -*- encoding:utf-8 -*-
# @author    : EastMagica
# @time      : 2021/09/27 11:50:56
# @file      : rk.py
# @project   : PythonTutorial
# @software  : VSCode
import numpy as np


def rk4(f, t0, y0, h, step=10):
    ys = [y0]

    for i in range(step):
        k1 = f(t0, ys[-1])
        k2 = f(t0 + 1/2 * h, ys[-1] + 1/2 * h * k1)
        k3 = f(t0 + 1/2 * h, ys[-1] + 1/2 * h * k2)
        k4 = f(t0 + h, ys[-1] + h * k3)
        ys.append(
            ys[-1] + h * (
                1/6 * k1 + 1/3 * k2 + 1/3 * k3 + 1/6 * k4
            )
        )
        t0 += h

    return np.array(ys)
