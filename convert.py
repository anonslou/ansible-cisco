#!/usr/bin/env python


import re


print('Serial Number,Device Name / Hostname,Tags,Notes,Software Version')
with open('invent.csv') as f:
    for line in f:
        serial, devicename, tags, location, software, ip, model = line[:-1].split(';')
        for ser in serial.split(','):
            if not tags:
                tags = location.split(', ')[0]
            if software:
                software = re.sub(r'0(?=\d)', '', software) # Опережающая проверка:
                # '04.06.15 12.2(50)SE5   15.0(2)EX5  16.06.02  01.04.10' ->
                # -> '4.6.15 12.2(50)SE5   15.0(2)EX5  16.6.2  1.4.10'
                # т.е. удаляем ведущие нули только перед цифрами!
            print('{},{},{},"{}",{}'.format(ser,devicename,tags,location,software))
