# Exercise for Python Seminar

2021.09.23


## Numerical Method

### 1. Explicit Euler

### 2. Explicit Runge-Kutta

Tips: using 4-order explicit tableau:
$$
\begin{array}{c|ccc}
0   &     &     &     &     \\
1/2 & 1/2 &     &     &     \\
1/2 & 0   & 1/2 &     &     \\
1   & 0   & 0   & 1   &     \\ \hline
    & 1/6 & 1/3 & 1/3 & 1/6 \\
\end{array}
$$

ref: [Runge-Kutta by Wikipedia](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) 

## Exercise

### 1. simple initial value problem

$$
\begin{cases}
u' = 4 t u^{\frac{1}{2}} \\
u(0) = 1
\end{cases}
$$

which exact solution is  

$$
u(t)=(1+t^2)^2
$$

Task: take $h=0.1, 0.5, 1.0$, calculate the numerical solution and error respectively.

### 2. Pendulum Problem


$$
H(p, q)=\frac{1}{2}p^2+(1-\cos(q))
$$

ODE form is as follows:

$$
\begin{cases}
\dot{p} &= - \nabla_q H(p, q) &= \sin(q) \\
\dot{q} &= \nabla_p H(p, q) &= p \\
\end{cases}
$$
