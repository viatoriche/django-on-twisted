# -*- coding: utf-8 -*-
"""
 Copyright 2005 Spike^ekipS <spikeekips@gmail.com>

    This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

import os, sys
import conf

try :
	site = sys.argv[1]
except :
	print "Usage: %s {start|stop|restart}" % sys.argv[0]
	sys.exit()

try :
	action = sys.argv[2]
except :
	print "Usage: %s {start|stop|restart}" % sys.argv[0]
	sys.exit()

def run (cmd) :
	os.system(cmd)

prog_stop = \
"""kill -9 `cat log/%(port)s.pid`"""

prog_stand = \
"""ENV_WWW_PORT=%(port)s twistd -ny ../run.py --pidfile=log/%(port)s.pid"""


prog_start = \
"""ENV_WWW_PORT=%(port)s twistd -y ../run.py --pidfile=log/%(port)s.pid --logfile=log/%(port)s.log"""

os.chdir(site)
os.putenv("DJANGO_SETTINGS_MODULE", "settings")

for i in dir(conf) :
	if not i.startswith("__") and type(getattr(conf, i)) in (str, unicode, int, long, ) :
		os.putenv("DOT_%s" % i, getattr(conf, i))

if action == "stand" :
	print "Standing"
	for i in conf.PORTS :
		run(prog_stand % {"port" : i })
		break
elif action == "start" :
	print "Starting"
	for i in conf.PORTS :
		run(prog_start % {"port" : i, })
elif action == "stop" :
	print "Stopping"
	for i in conf.PORTS :
		run(prog_stop % {"port" : i, })
elif action == "restart" :
	print "Restarting"
	for i in conf.PORTS :
		run(prog_stop % {"port" : i, })
		run(prog_start % {"port" : i, })
else :
	print "Usage: %s {start|stop|restart}" % sys.argv[0]
	sys.exit()


"""
Description
-----------


ChangeLog
---------


Usage
-----


"""

__author__ =  "Spike^ekipS <spikeekips@gmail.com>"
__version__=  "0.1"
__nonsense__ = ""


