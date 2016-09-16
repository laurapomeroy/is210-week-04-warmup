#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function does some math, returns a string, trims/strips letters,
        and formats.

    Args:
        retstr (mixed): Arg to be retstr
        nudges (mixed): Arg to multiply and remove first and last letter.
        winks (mixed): Arg to be multiplied and stripped of first and last
        letter.
        numwink (str, optional): A numerical string. Default: 2

    Returns:
        str: A function that knows what you mean.


    Examples:
        >>> know_what_i_mean('wink', 2)
        'Know what I mean? winkwink, nudgenudge'
        >>> know_what_i_mean('numwink', 3)
        'Know what I mean? numwinknumwinknumwink, nudgenudgenudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
