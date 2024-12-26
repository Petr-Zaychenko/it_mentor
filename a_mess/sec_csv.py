import csv

data = [['atime','ctime', 'package-name', 'mru-program', 'tag'],
	[1387295797, 1367633260, 'perl-base', '/usr/bin/perl', None],
	[1387295796, 1354370480, 'login', '/bin/su', None],
	[1387295743, 1354341275, 'libtalloc2', '/usr/lib/x86_64-linux-gnu/libtalloc.so.2.0.7', None],
	[1387295743, 1387224204, 'libwbclient0', '/usr/lib/x86_64-linux-gnu/libwbclient.so.0',],
	[1387295742, 1354341253, 'libselinux1',	'/lib/x86_64-linux-gnu/libselinux.so.1', None]
]
with open('tab_task.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)