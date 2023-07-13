#!/usr/bin/python3
"""Multiply two matrices using numpy"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply matrix m_a by matrix m_b using numpy"""
    return numpy.matmul(m_a, m_b)
