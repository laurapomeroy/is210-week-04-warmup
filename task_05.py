#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A little docstring"""


def defaults(my_optional=True, my_required=None):
    """This function compares two parameters

    Args:
        my_optional (mixed): has a default value of zero.
        my_required (mixed): is a required param and has no default value.


    Returns:
        boolean: True if the parameters are the same;
        False if the parameters are different.

    Examples:

        >>> defaults(True)
        False
        >>> defaults(True, False)
        False
        >>> defaults(False, False)
        True
    """
    return my_optional is my_required
