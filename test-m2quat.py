#!/usr/bin/python
"""
Test the euclid Matrix4 to Quaterion code.

Lorenzo Riano <lorenzo.riano@gmail.com>
"""

import euclid
import numpy as np

ntrials = 10000
tol = 1e-5
for t in range(ntrials):
    rot_x, rot_y, rot_z = np.random.uniform(-np.pi, np.pi, 3)
    m = euclid.Matrix4.new_rotate_euler(rot_y, rot_x, rot_z)
    newm = m.get_quaternion().get_matrix()

    assert( np.allclose(np.array(m[:]), np.array(newm[:])))



print("OK")
