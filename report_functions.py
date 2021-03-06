#!/usr/bin/env python
#coding=utf-8
import os
import prettytable
import psutil
from pdf import *
from reportlab.platypus import  Table
from spreadsheettable import SpreadsheetTable
#获取系统信息（是否集群）
def function():
	pass

#获取CPU信息
def function():
	pass


#磁盘指标格式化
"""
List all mounted disk partitions

Device               Total     Used     Free  Use %      Type  Mount
/dev/sdb3            18.9G    14.7G     3.3G    77%      ext4  /
/dev/sda6           345.9G    83.8G   244.5G    24%      ext4  /home
/dev/sda1           296.0M    43.1M   252.9M    14%      vfat  /boot/efi
/dev/sda2           600.0M   312.4M   287.6M    52%   fuseblk  /media/Recovery
"""
def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

#获取磁盘信息
def get_diskinfo():
    table = prettytable.PrettyTable(border=False, header=True, left_padding_width=2, padding_width=1)
    table.field_names = ["Device", "Total", "Used", "Free", "Use%", "Type", "Mount"]
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        if 'docker' in part.mountpoint and 'aufs' in part.mountpoint:
            continue
        usage = psutil.disk_usage(part.mountpoint)

        table.add_row([part.device,
                       bytes2human(usage.total),
                       bytes2human(usage.used),
                       bytes2human(usage.free),
                       str(int(usage.percent)) + '%',
                       part.fstype,
                       part.mountpoint])
    for field in table.field_names:
        table.align[field] = "l"
    print table

#获取集群状态
def function():
	pass

#获取集群磁盘状态
def function():
	pass

#获取集群文件备份状态
def function():
	pass

#获取集群日志
def function():
	pass

#连接oracle数据库
def function():
	pass

#获取oracle表空间信息
def function():
	pass

#获取oracle表空间信息
def function():
	pass

#获取oracle日志信息
def function():
	pass

#获取数据库备份信息
def function():
	pass
