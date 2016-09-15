#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function does some math, returns a string, trims/strips letters,
        and formats.

    Args:
        retstr (mixed): Arg to be retstr
        nudges (mixed): Arg to multiply and remove first and last letter.
        winks (mixed): Arg to be multiplied and stripped of first and last letter.
        numwink (str, optional): A numerical string. Default: 2

    Returns:
        str: All arguments concatenated with commas.


    Raises:
        AttributeError: 'int' object has no attribute 'strip'.

    Examples:

        >>> know_what_i_mean(2,3)

        Traceback (most recent call last):
        File "<pyshell#0>", line 1, in <module>
        know_what_i_mean(2,3)
        File "/home/vagrant/Desktop/is210-week-04-warmup/task_01.py", line 26, in know_what_i_mean
        winks = (wink * numwink).strip()
        AttributeError: 'int' object has no attribute 'strip'>>> know_what_i_mean(2, 3) 
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
