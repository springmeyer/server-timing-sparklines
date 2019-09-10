#!/usr/bin/env python3

import fileinput

rows = []

for line in fileinput.input():
    line_lower = line.lower();
    if line_lower.startswith('server-timing:'):
        data = line_lower.strip().replace("server-timing:","")
        parts = data.strip().split(',')
        for part in parts:
            p = part.strip().split(';')
            if len(p) == 3:
                id = p[0].strip()
                dur = p[1].strip().replace('dur=','')
                name = p[2].strip().replace('desc=',"").replace(" ",'-')
                rows.append({'name':name,'dur':dur})
            elif len(p) == 2:
                id = p[0].strip()
                dur = p[1].strip().replace('dur=','')
                rows.append({'name':id,'dur':dur})

#rows.sort(key=lambda x: x['dur'], reverse=True)

for r in rows:
    print (r['name'] + ' ' + r['dur'])
