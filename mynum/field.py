#!/usr/bin/python3
# -*- encoding:utf-8 -*-
# @author    : EastMagica
# @time      : 2021/09/27 12:15:20
# @file      : field.py
# @project   : PythonTutorial
# @software  : VSCode
import numpy as np


def vector_field(f, t_span, t_step, u_span, u_step):
    t_delta = (t_span[1] - t_span[0]) / t_step

    t_eval = np.linspace(*t_span, t_step + 1)
    y_eval = np.linspace(*u_span, u_step + 1)

    t, y = np.meshgrid(t_eval, y_eval)

    t = t.flatten()
    y = y.flatten()

    dt = np.full_like(t, 1.)  # t_delta
    dy = f(t, y)

    return t, y, dt, dy
