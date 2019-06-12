"""Mathematical functions."""

from typing import List

import math


def information_content(p: float):
    """Calculate information content.

    Arguments:
        p {float} -- probability

    Returns:
        [float] -- information content

    """
    return math.log2(1/p)


def entropy(ps: List[float]):
    """Calculate entropy.

    Arguments:
        ps {List[float]} -- list of probabilities

    Returns:
        float -- entropy

    """
    return sum(p * information_content(p) for p in ps)


def expected_length(ps: List[float], ls: List[int]):
    """Calculate expected length.

    Arguments:
        ps {List[float]} -- list of probabilities
        ls {List[int]} -- list of codelengths

    Returns:
        float -- expected codelength

    """
    return sum(p*l for p, l in zip(ps, ls))


def meet_kraft_inequity(ls: List[int], verbose: bool = False):
    """Check given list of lengths meet the kraft inequity.

    Arguments:
        ls {[type]} -- [description]

    Keyword Arguments:
        verbose {bool} -- [description] (default: {False})

    Returns:
        [type] -- [description]

    """
    zs = [2**(-l) for l in ls]
    z = sum(zs)

    if verbose:
        print(zs)

    if verbose and z == 1:
        print('Complete')

    return z <= 1
