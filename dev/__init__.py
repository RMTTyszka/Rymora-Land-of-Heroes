#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
__init__ file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

from main import *

if __name__ == '__main__':
    char = Char.blank('boi')
    print char.EVD
    char.run_effects()
