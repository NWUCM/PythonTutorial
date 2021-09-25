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
import numpy as np
import matplotlib.pyplot as plt


plot_config = {
    "linewidth": 2.,
    "marker": '.',
    "markersize": 16,
    "markeredgecolor": "black",
    "alpha": 1.,
}


def f(t, u):
    return t * u + t ** 3


def u_true(t, u0):
    return (2 + u0) * np.e ** (t**2 / 2) - t ** 2 - 2


if __name__ == "__main__":
    # Constant
    # --------
    y0 = 1.

    # Vector Field
    # ------------
    t_step = 10
    t_span = (0, 1.)
    t_delta = (t_span[1] - t_span[0]) / t_step

    u_step = 10
    u_span = (0, 2.)

    x_eval = np.linspace(*t_span, t_step + 1)
    y_eval = np.linspace(*u_span, u_step + 1)
    x, y = np.meshgrid(x_eval, y_eval)
    x = x.flatten()
    y = y.flatten()

    u = np.full_like(x, 1.)
    v = f(x, y)

    fig, ax = plt.subplots(
        1, 1,
        figsize=(8, 6),
    )
    ax.quiver(
        x, y, u, v,
        np.hypot(u, v),
        units="xy",
    )

    # Flow Data: Euler
    # ----------------
    color = "tab:blue"

    ys = [y0]

    for i in x_eval[:-1]:
        ys.append(
            ys[-1] + t_delta * f(i, ys[-1])
        )

    ys_euler = np.array(ys)

    ax.plot(
        x_eval, ys_euler,
        color=color,
        label="Euler",
        **plot_config,
    )

    # Flow Data: RK4
    # ----------------
    color = "tab:green"

    ys = [y0]

    for i in x_eval[:-1]:
        k1 = f(i, ys[-1])
        k2 = f(i + 1/2 * t_delta, ys[-1] + 1/2 * t_delta * k1)
        k3 = f(i + 1/2 * t_delta, ys[-1] + 1/2 * t_delta * k2)
        k4 = f(i + t_delta, ys[-1] + t_delta * k3)
        ys.append(
            ys[-1] + t_delta * (
                1/6 * k1 + 1/3 * k2 + 1/3 * k3 + 1/6 * k4
            )
        )

    ys_rk4 = np.array(ys)

    ax.plot(
        x_eval, ys_rk4,
        color=color,
        label="RK4",
        **plot_config,
    )

    # Flow Data: Exact
    # ----------------
    color = "tab:red"

    ys_exact = u_true(x_eval, y0)

    ax.plot(
        x_eval, ys_exact,
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

    for k, v in enumerate(x_eval[1:], start=1):
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
