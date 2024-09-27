# 3D Parametric Surface Simulation with Torus Manifold Representation

## Overview

This repository contains a Python script that visualizes a parametric surface in 3D space using Matplotlib. The mathematical framework behind this simulation is based on parametric surfaces and vector fields, with a focus on the torus as a manifold. This visualization provides insights into the geometric structure and vector field behavior on a torus surface.

## Mathematical Explanation

### Parametric Equations and the Torus Manifold

A torus is a fundamental example of a 2-dimensional manifold, often represented parametrically in 3D space. The parametric equations of a torus are:

- $X(t_1, t_2) = (r_1 \cos(t_1) + r_2) \cos(t_2)$
- $Y(t_1, t_2) = (r_1 \cos(t_1) + r_2) \sin(t_2)$
- $Z(t_1) = r_1 \sin(t_1)$

Where:
- $t_1 \in [0, 2\pi]$ and $t_2 \in [0, 2\pi]$ are the parameters that sweep the surface.
- $r_1$ is the radius of the torus' tube.
- $r_2$ is the distance from the center of the hole to the center of the tube.

### Manifold Structure

A manifold is a topological space that locally resembles Euclidean space. The torus, denoted as $T^2$, is a smooth manifold, meaning that it behaves locally like $\mathbb{R}^2$. Globally, it exhibits periodicity in both $t_1$ and $t_2$.

The torus can be described as the product of two circles: $T^2 = S^1 \times S^1$, where $S^1$ is the 1-dimensional circle. Each point on the torus is determined by a pair of angles $(t_1, t_2)$, making the torus a compact manifold with no boundary.

### Derivative Approximation

The partial derivatives of the parametric functions with respect to $t_1$ and $t_2$ give the velocity vectors at each point. Using finite differences:

- $dX(t_1, t_2) \approx \frac{X(t_1+h, t_2+h) - X(t_1, t_2)}{h}$
- $dY(t_1, t_2) \approx \frac{Y(t_1+h, t_2+h) - Y(t_1, t_2)}{h}$
- $dZ(t_1) \approx \frac{Z(t_1+h) - Z(t_1)}{h}$

These approximations provide the rate of change of the parametric functions.

### Magnitude of the Gradient

The magnitude $Mag$ of the gradient vector at a point on the torus is computed as:

$$Mag = \sqrt{dX(t_1, t_2)^2 + dY(t_1, t_2)^2 + dZ(t_1)^2}$$

This gives a scalar measure of how fast the surface is changing at each point.

### Color Normalization

To visualize the magnitude of the gradient, we normalize it using the formula:

$$\text{norm}(mag) = \frac{mag - Mag_{\min}}{Mag_{\max} - Mag_{\min}}$$

This normalization maps the gradient magnitude to a color scale, allowing for a visual representation of surface curvature and speed.

### Vector Field Representation

The `quiver` function is used to represent the velocity vectors at different points on the surface. The position vector is also visualized, showing the direction from the origin to a point on the torus. The gradient vectors are color-coded based on the magnitude of the gradient, providing insight into the curvature and flow on the surface.
