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
    armor1 = items.Equipable.Armor('gato')
    armor1.evade = 10
    char.equipment.put(armor1, 'armor')
    char.attributes.strength = 20
    print char.attributes.strength
    print char.attributes.str_mod
    print char.attributes.roll_str()
    # print char.equipment.armor.evade
    print char.EVD
    char.run_effects()
