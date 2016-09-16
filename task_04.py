#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A little docstring"""


def too_many_kittens(kittens, litterboxes, catfood):
    """This function checks if catfood exists and if we have enough
       litterboxes

       Args:
       kittens (int): number of kittens.
       litterboxes (int): number of available litterboxes.
       catfood (boolean): represents whether or not there is catfood.

       Returns:
       boolean: True if we have enough litterboxes;
       False if we do not.

       Examples:

       >>> too_many_kittens(12, 12, False)
       True
       >>> too_many_kittens(13, 12, True)
       True
       >>> too_many_kittens(12, 13, True)
       False
    """
    return not (litterboxes >= kittens and catfood)
