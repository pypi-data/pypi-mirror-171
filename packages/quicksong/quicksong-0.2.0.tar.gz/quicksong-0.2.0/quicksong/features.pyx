# -*- coding: utf-8 -*-
# -*- mode: python -*-
# distutils: language = c++
""" Module for calculating features from spectrograms """
cimport numpy as np
import numpy as np
import cython
from libc.math cimport log10, log, exp

cdef extern from "<complex.h>" namespace "std" nogil:
    double abs(double complex z)

@cython.boundscheck(False)
@cython.wraparound(False)
def total_power(np.ndarray [np.complex128_t, ndim=1] psd):
    cdef size_t i
    cdef size_t npoints = psd.size
    cdef double sum = 0
    for i in range(npoints):
        sum += abs(psd[i])
    return log10(sum)


@cython.boundscheck(False)
@cython.wraparound(False)
def wiener_entropy(np.ndarray [np.complex128_t, ndim=1] psd):
    cdef size_t i
    cdef size_t npoints = psd.size
    cdef double pow
    cdef double sum = 0
    cdef double logsum = 0
    for i in range(npoints):
        pow = abs(psd[i])
        sum += pow
        logsum += log(pow)
    return log10(exp(logsum / npoints) / (sum / npoints))

