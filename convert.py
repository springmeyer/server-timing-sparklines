#!/usr/bin/env python3

import fileinput

rows = []

for line in fileinput.input():
    line_lower = line.lower();
    parts = line_lower.split(' ')
    print(parts[0],1000*float(parts[1]))