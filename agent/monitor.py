#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys
import yaml
import json
import requests


class Time(object):

    def timenow(self):
        """docstring for writelog"""

        hora = str(datetime.datetime.today())
        return hora

    def machine(self):
        """docstring for machine"""

        outreq = []
        i = 0
        osreq = ['uptime', 'hostname']
        for req in osreq:
            sup = os.popen(req).read().strip('\n')
            outreq.append(sup)
            i = i + 1
        return outreq

    def writelog(self, hora, outreq):
        """docstring for writelog"""

        sysout = ""
        for req in outreq[:-1:]:
            sysout = sysout + ' ' + req
        try:
            logfile = open(os.path.abspath("monitor.log"), "a")
            try:
                logfile.write("[" + hora + "]" + sysout + "\n")
            finally:
                logfile.close()
        except IOError:
            pass

    def countnumber(self, internalinfo):
        """docstring for countnumber"""

        fnumber = len(os.listdir(internalinfo['directory']))
        if fnumber == 0:
            fflag = False
        else:
            fflag = True
        return fflag
        pass


class Parseryml(object):

    def fileparser(self):
        """ docstring for fileparser """

        with open(os.path.abspath('settings.yml'), 'r') as f:
            doc = yaml.load(f)
        return doc
        pass


class Sender(object):

    def json_obj(self, hora, outreq, myflag, internalinfo):
        """ docstring for json_obj """

        obj_to_send = {'time': hora, 'statistics': (outreq), 'fill': myflag,
                        'username': internalinfo['username']}
        return obj_to_send
        pass

    def send_json(self, j, internalinfo):
        """ docstring for send_json """

        url = internalinfo['url']
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(j), headers=headers)
        if r.status_code == requests.codes.ok:
            print r.text
        else:
            print "this request gave error status"
            sys.exit(1)
        pass


def main():
    """doctring for main"""

    info = Parseryml()
    internalinfo = info.fileparser()
    monitor = Time()
    oh = Sender()
    hora = monitor.timenow()
    outreq = monitor.machine()
    myflag = monitor.countnumber(internalinfo)
    monitor.writelog(hora, outreq)
    j = oh.json_obj(hora, outreq, myflag, internalinfo)
    oh.send_json(j, internalinfo)


if __name__ == '__main__':
    main()
