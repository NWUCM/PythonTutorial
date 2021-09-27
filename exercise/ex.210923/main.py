#!/usr/bin/python
# -*- coding:utf-8 -*-
# @file     : ex.210923.py.py
# @time     : 2021/09/25 22:45:22
# @author   : eastmagica
# @contact  : eastmagica@outlook.com
# @software : VS Code
r"""
u'=4 t u^{1/2}
u(0) = 1
"""
import os, sys
sys.path.append(".")

import numpy as np
import matplotlib.pyplot as plt

from mynum.euler import euler_explicit
from mynum.rk import rk4
from mynum.field import vector_field


# Constant
# --------

plot_config = {
    "linewidth": 2.,
    "marker": '.',
    "markersize": 16,
    "markeredgecolor": "black",
    "alpha": 1.,
}


# Functions
# ---------


def f(t, u):
    return t * u + t ** 3


def u_true(t, u0):
    return (2 + u0) * np.e ** (t**2 / 2) - t ** 2 - 2


if __name__ == "__main__":
    # Constant
    # --------
    y0 = 1.

    t_step = 10
    t_span = (0, 1.)
    t_delta = (t_span[1] - t_span[0]) / t_step
    t_eval = np.linspace(*t_span, t_step + 1)

    u_step = 10
    u_span = (0, 2.)

    # Vector Field
    # ------------
    t, y, dt, dy = vector_field(
        f, t_span, t_step, u_span, u_step
    )

    fig, ax = plt.subplots(
        1, 1,
        figsize=(8, 6),
    )

    ax.quiver(
        t, y, dt, dy,
        np.hypot(dt, dy),
        units="xy",
    )

    # ax.streamplot(
    #     t.reshape(-1, 11), y.reshape(-1, 11),
    #     dt.reshape(-1, 11), dy.reshape(-1, 11),
    #     color=np.hypot(dt, dy).reshape(-1, 11),
    #     arrowstyle="->",
    # )

    # Flow Data: Euler
    # ----------------
    color = "tab:blue"

    ys_euler = euler_explicit(f, t_span[0], y0, t_delta, t_step)

    ax.plot(
        t_eval, ys_euler,
        color=color,
        label="Euler",
        **plot_config,
    )

    # Flow Data: RK4
    # ----------------
    color = "tab:green"

    ys_rk4 = rk4(f, t_span[0], y0, t_delta, t_step)

    ax.plot(
        t_eval, ys_rk4,
        color=color,
        label="RK4",
        **plot_config,
    )

    # Flow Data: Exact
    # ----------------
    color = "tab:red"

    ys_exact = u_true(t_eval, y0)

    ax.plot(
        t_eval, ys_exact,
        color=color,
        label="Exact",
        linestyle="--",
        **plot_config,
    )

    # Print Error
    # -----------
    err_euler = ys_euler - ys_exact
    err_rk4 = ys_rk4 - ys_exact

    print(" Exact Flow\t Euler Error\t RK4 Error")

    print(f"{ys_exact[0]: .4e}")

    for k, v in enumerate(t_eval[1:], start=1):
        print(f"{ys_exact[k]: .4e}\t{err_euler[k]: .4e}\t{err_rk4[k]: .4e}")

    # Plot Config
    # -----------

    ax.legend(
        loc="upper center",
        prop={
            "size": 18,
            "family": "Arial"
        },
        framealpha=0.9,
    )

    ax.set_xlabel("t")
    ax.set_ylabel("u")

    plt.show()
