# This is DOT(Django On Twisted) #

Normally, django runs on Apache web server as production server or `runserver` feature in django for development, but under Apache, it takes too much time to (re)start and is difficult to combine other python-based network applications, like `pydirector` for load-balancing, so I use this script for running django on Twisted.web2 framework.


---

The DOT is the derived work of [jnoetzelman's work](http://code.djangoproject.com/ticket/172) in Django development trac.

---


# Requirement #
  * Python 2.5(or later)
  * twisted framework 2.5(or later or svn)
  * twisted.web2 0.2.0(or later or svn)

# Installation #
Download the `DOT`(Django On Twisted) and uncompress the tarball.
```
spike@bebop:/bebop/work/django_test$ pwd
/bebop/work/django_test
spike@bebop:/bebop/work/django_test$ v
total 0
drwxr-xr-x 6 spike spike  54 2008-01-24 12:48 .
drwxr-xr-x 7 spike spike 143 2008-01-24 12:45 ..
drwxr-xr-x 3 spike spike  49 2008-01-24 12:45 db
drwxr-xr-x 5 spike spike 110 2008-01-24 12:48 django_test
```
`django_test` was created by `django-admin.py startproject django_test`, yeah, it's django project home directory.

And we download the source from SVN and copy it in current directory.
```
spike@bebop:/bebop/work/django_test$ /usr/bin/svn checkout http://django-on-twisted.googlecode.com/svn/trunk/ 
A    trunk/init.py
A    trunk/run.py
A    trunk/conf.py
A    trunk/init.sh
Checked out revision 9.
spike@bebop:/bebop/work/django_test$ cp trunk/*.* .
spike@bebop:/bebop/work/django_test$ ls -al
total 20
drwxr-xr-x 7 spike spike  121 Jan 24 12:51 .
drwxr-xr-x 7 spike spike  143 Jan 24 12:45 ..
-rw-r--r-- 1 spike spike 1043 Jan 24 12:51 conf.py
drwxr-xr-x 3 spike spike   49 Jan 24 12:45 db
drwxr-xr-x 5 spike spike  110 Jan 24 12:48 django_test
-rw-r--r-- 1 spike spike 2041 Jan 24 12:51 init.py
-rw-r--r-- 1 spike spike  961 Jan 24 12:51 init.sh
drwxr-xr-x 2 spike spike   27 Jan 24 12:47 log
-rw-r--r-- 1 spike spike 4692 Jan 24 12:51 run.py
drwxr-xr-x 3 spike spike   72 Jan 24 12:51 trunk
```

All thing done.

# Configuration #
In the DOT's default configuration file, `conf.py`, you can edit the default configuration. This is default `conf.py`.
```
# ports to be run.
PORTS = (9000, )

# private key path
SSL_PRIVATE_KEY_PATH = None

# logging style, 'apache' or None
LOG_STYLE = None
```

## PORTS ##
The DOT supports the multiple instance of your django project, that is you can run the sam e project in the many instance, which runs with another `port`. `PORTS` is the tuple datatype of python, so you append the other ports inside tuple like this,
```
PORTS = (9000, 9001, 9002, 9003, 9004, )
```

## SSL\_PRIVATE\_KEY\_PATH ##
The DOT supports SSL, it rely on the Twisted SSL feature(twisted.internet.ssl). If you set the pem file path in the `SSL_PRIVATE_KEY_PATH`, if `SSL_PRIVATE_KEY_PATH` is set, DOT automatically runs your django project in SSL.

## LOG\_STYLE ##
The `Twisted.web2` print out the apache-style log, but for the purpose of debuggin, DOT support the managed-style log. If you set the `apache` in `LOG_STYLE`, you can have the apache-style log.

All the log will be stored in `log/` directory and log name is `<port number>.log`.

# Run Your Django Project #
After the configuration, you are ready to run the DOT, just simply type like this,
```
spike@bebop:/bebop/work/django_test$ sh init.sh django_test start
```
As I alreay mentioned, the `django_test` is your django project name. `init.sh` support 4 actions like the init script of UNIX.

  * Actions of init.sh
|start | start your django project |
|:-----|:--------------------------|
|stop | stop it |
|restart | restart it |
|stand | don't fork it as sub-process, so all the log can monitor in there |

```
spike@bebop:/bebop/work/django_test$ sh init.sh django_test stand
Standing
Removing stale pidfile /home/bebop/work/django_test/log/9000.pid
2008/01/24 13:07 +0900 [-] Log opened.
2008/01/24 13:07 +0900 [-] twistd 2.5.0 (/usr/bin/python 2.5.1) starting up
2008/01/24 13:07 +0900 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008/01/24 13:07 +0900 [-] Loading run.py...
2008/01/24 13:07 +0900 [-] Loaded.
2008/01/24 13:07 +0900 [-] twisted.web2.channel.http.HTTPFactory starting on 9000
2008/01/24 13:07 +0900 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xd3af38>
```

If you don't have any errors, open up your django project in your web browser.