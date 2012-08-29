#!/bin/bash

# shell script example to use with crontab.
#
# to modify or add a task to cron use
# crontab -e
#
# if you want to run the script every 30 min, as I do, you have to do this.
#
# */30 * * * * sh /path/to/pycronjob.sh

#env
cd $HOME/monitor/agent
$HOME/Envs/mon/bin/python monitor.py