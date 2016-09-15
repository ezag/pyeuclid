import math

import numpy as np

import euclid


try:
    xrange
except NameError:
    xrange = range


def test_m2quat():
    """
    Test the euclid Matrix4 to Quaterion code.

    Lorenzo Riano <lorenzo.riano@gmail.com>
    """
    ntrials = 10000
    tol = 1e-5
    for t in xrange(ntrials):
        rot_x, rot_y, rot_z = np.random.uniform(-np.pi, np.pi, 3)
        m = euclid.Matrix4.new_rotate_euler(rot_y, rot_x, rot_z)
        newm = m.get_quaternion().get_matrix()
        assert np.allclose(np.array(m[:]), np.array(newm[:]))


def test_m3inv():
    """
    Test the euclid Matrix3 inversion code.

    Dov Grobgeld <dov.grobgeld@gmail.com>
    Sunday 2011-03-13 00:13
    """
    syms = 'abcefgijk'
    def assert_m3_unity(m):
        """Assert that matrix is a unity"""
        epsilon = 1e-8
        for s in 'afk':
            assert abs(m.__getattribute__(s) - 1.0) < epsilon
        for s in 'bcegij':
            assert abs(m.__getattribute__(s)) < epsilon

    # Create a "random" matrix and calculate its inverse
    m = euclid.Matrix3().rotate(1.0).translate(3, 4).scale(1.5, 0.7)
    minv = m.inverse()
    assert_m3_unity(minv * m)
