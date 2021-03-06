#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import commands
import time

def run(ip,user,cmd):
    cmds = """ sudo ssh -oConnectTimeout=10 %s@%s "%s" """ % (user,ip,cmd)
    try:
        out = commands.getoutput(cmds)
    except Exception,e:
        out = "error"
    return out

def start_stop_ftp(action,ip,configfile):
    cmd = """ less %s |grep 'ftp:1'|wc -l """ % configfile
    out = commands.getoutput(cmd)
    if int(out) == 1:
        if action == "stop":
            cmd = """ service vsftpd stop """
            run(ip,'root',cmd)
            cmd = """ service vsftpd status """
            out = run(ip,'root',cmd)
            if re.search('is stopped',out):
                print "%s ftp stop sucess." % ip
            else:
                print "%s ftp stop fail." % ip
        elif action == "start":
            cmd = """ service vsftpd start """
            run(ip,'root',cmd)
            cmd = """ service vsftpd status """
            out = run(ip,'root',cmd)
            if re.search('is running',out):
                print "%s ftp start sucess." % ip
            else:
                print "%s ftp start fail." % ip
    else:
        pass
