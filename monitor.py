#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os


class Time(object):

    def hola(self):
        """docstring for writelog"""

        hora = str(datetime.datetime.today())
        return hora

    def machine(self):
        """docstring for machine"""

        outreq = []
        i = 0
        osreq = ['uptime', 'hostname', 'uname -s']
        for req in osreq:
            sup = os.popen(req).read().strip('\n')
            outreq.append(osreq[i] + ': ' + sup)
            i = i + 1
        print outreq
        return outreq

    def writelog(self, hora, outreq):
        """docstring for writelog"""

        sysout = ""
        for req in outreq[:-1:]:
            sysout = sysout + ' ' + req
        try:
            logfile = open("monitor.log", "a")
            try:
                logfile.write("[" + hora + "]" + sysout + "\n")
            finally:
                logfile.close()
        except IOError:
            pass


def main():
    """doctring for main"""
    monitor = Time()
    hora = monitor.hola()
    outreq = monitor.machine()
    monitor.writelog(hora, outreq)


if __name__ == '__main__':
    main()
