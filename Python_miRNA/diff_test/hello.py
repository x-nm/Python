#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


path = os.getcwd()
print path
newdir = 'diff'
new_path = os.path.join(path, newdir)
print new_path
