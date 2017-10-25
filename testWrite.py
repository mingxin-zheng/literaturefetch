#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:47:20 2017

@author: mingxin
"""
import os

with open('input.txt') as f:
    content = f.readlines()

os.system('rm *.bib')
for phrase in content:
    command = 'python scholar.py -c 1 --phrase "'+phrase+'" --citation=bt'
    os.system(command)