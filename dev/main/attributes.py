#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
attributes file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import attributes as C

class Attributes(object):
    ''' Base Atributes for any item in the game '''

    def __init__(self, strength=0, agility=0, vitality=0, wisdom=0, inteligence=0,
        charisma=0):
        '''
        Initializes the attributes.
            "strength": char strength,
            "agility": char agility,
            "vitality": char vitality,
            "wisdom": char wisdom,
            "inteligence": char inteligence}
            # "charisma": char charisma} - not implemented so far
        '''
        self.strength = strength
        self.agility = agility
        self.vitality = vitality
        self.wisdom = wisdom
        self.inteligence = inteligence
        self.charisma = charisma

    @property
    def str_mod(self):
        return self.strength/2 - 5

    @property
    def agi_mod(self):
        return self.agility/2 - 5

    @property
    def vit_mod(self):
        return self.vitality/2 - 5

    @property
    def wis_mod(self):
        return self.wisdom/2 - 5

    @property
    def int_mod(self):
        return self.inteligence/2 - 5

    @property
    def cha_mod(self):
        return self.charisma/2 - 5


if __name__ == '__main__':
    Attr1 = Attributes()
    assert type(Attr1.strength) is int
    assert type(Attr1.str_mod) is int

    assert type(Attr1.agility) is int
    assert type(Attr1.agi_mod) is int

    assert type(Attr1.vitality) is int
    assert type(Attr1.vit_mod) is int

    assert type(Attr1.wisdom) is int
    assert type(Attr1.wis_mod) is int

    assert type(Attr1.inteligence) is int
    assert type(Attr1.int_mod) is int

    assert type(Attr1.charisma) is int
    assert type(Attr1.cha_mod) is int
    print 'All tests ok!'