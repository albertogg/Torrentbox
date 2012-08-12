#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import yaml
import json


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


class Sender(object):

    def json_obj(self, hora, outreq, myflag):
        """ docstring for json_obj """

        obj_to_send = [{'time':hora, 'statistics':(outreq), 'fill':myflag}]
        print 'JSON:', json.dumps(obj_to_send)
        print 'INDENT:', json.dumps(obj_to_send, sort_keys=True, indent=2)
        return obj_to_send
        pass


def main():
    """doctring for main"""

    info = Parseryml()
    internalinfo = info.fileparser()
    mydir = info.extraction(internalinfo)
    monitor = Time()
    oh = Sender()
    hora = monitor.timenow()
    outreq = monitor.machine()
    myflag = monitor.countnumber(mydir)
    monitor.writelog(hora, outreq)
    oh.json_obj(hora, outreq, myflag)


if __name__ == '__main__':
    main()
