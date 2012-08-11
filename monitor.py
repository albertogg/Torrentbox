#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import yaml


class Time(object):

    def timenow(self):
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

    def countnumber(self, mydir):
        """docstring for countnumber"""

        fnumber = len(os.listdir(mydir))
        if fnumber == 0:
            fflag = False
        else:
            fflag = True
        print fflag
        return fflag
        pass


class Parseryml(object):

    def fileparser(self):
        """ docstring for fileparser """

        with open('settings.yml', 'r') as f:
            doc = yaml.load(f)
        print doc
        return doc
        pass

    def extraction(self, internalinfo):
        """ docstring for extraction """

        txt = internalinfo["directory"]
        print txt
        return txt
        pass


def main():
    """doctring for main"""

    info = Parseryml()
    internalinfo = info.fileparser()
    mydir = info.extraction(internalinfo)
    monitor = Time()
    hora = monitor.timenow()
    outreq = monitor.machine()
    monitor.countnumber(mydir)
    monitor.writelog(hora, outreq)


if __name__ == '__main__':
    main()
