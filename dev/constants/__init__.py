#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
json parameters parser

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import json
from os.path import dirname, abspath

FOLDER_PATH = dirname(abspath(__file__))+'/'
DEFAULT_BASE = FOLDER_PATH+'base.json'
DEFAULT_CHAR = FOLDER_PATH+'char.json'
DEFAULT_ATTRIBUTES = FOLDER_PATH+'attributes.json'
DEFAULT_SKILLS = FOLDER_PATH+'skills.json'
DEFAULT_DEFENSES = FOLDER_PATH+'defenses.json'
DEFAULT_RESISTS = FOLDER_PATH+'resists.json'
DEFAULT_EFFECTS = FOLDER_PATH+'effects.json'
DEFAULT_INVENTORY = FOLDER_PATH+'inventory.json'

class AttributeDict(dict):
    def __getattr__(self, attr):
        return self[attr]
        def __setattr__(self, attr, value):
            self[attr] = value

with open(DEFAULT_BASE, 'r') as text:
    base = AttributeDict(json.loads(text.read()))

with open(DEFAULT_CHAR, 'r') as text:
    char = AttributeDict(json.loads(text.read()))

with open(DEFAULT_ATTRIBUTES, 'r') as text:
    attributes = AttributeDict(json.loads(text.read()))

with open(DEFAULT_SKILLS, 'r') as text:
    skills = AttributeDict(json.loads(text.read()))

with open(DEFAULT_DEFENSES, 'r') as text:
    defenses = AttributeDict(json.loads(text.read()))

with open(DEFAULT_RESISTS, 'r') as text:
    resists = AttributeDict(json.loads(text.read()))

with open(DEFAULT_EFFECTS, 'r') as text:
    effects = AttributeDict(json.loads(text.read()))

with open(DEFAULT_INVENTORY, 'r') as text:
    inventory = AttributeDict(json.loads(text.read()))

if __name__ == '__main__':
    assert char
    assert attributes
    assert skills
    assert defenses
    assert resists
    assert effects
    assert base
    print 'All tests ok!'