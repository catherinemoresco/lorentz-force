# lorentz-force

A simulator of the effect of a magnetic force in an electric field, built with numpy and pyplot.

Parameters are hard-coded into the file; the area where they should be modified is clearly delineated, and the importance of the various variables are noted in the comments. Especially relevant is the comment on the limitation of the correctness of Euler's method of numerical integration; users should be careful to set their step size small enough to combat the existence of artifactual spiraling in what should be uniform circular motion--e.g. what occurs in a constant magnetic field. 

Here are some example outputs:
![Figure 1](catherinemoresco.github.com/lorentz-force/readme-assets/img/figure_1.png)

Here, we have three particle trajectories in a constant magnetic field. The black trajectory is a particle traveling wholly perpendicular to the magnetic field—its path is a circle, as expected. The red path is a particle with velocity components both parallel to and perpendicular to the field, resulting in a helix—it also has a greater mass, which results in a wider curvature of path. The blue line is a particle traveling completely parallel to the force—its motion is not affected at all.

With a wacky, arbitrary, physically implausible B field (`b = np.array([2, 0, .1*z]`), we get something sillier:
![Figure 2](catherinemoresco.github.com/lorentz-force/readme-assets/figure_2.png)

