.. _install-nginx:

安装nginx：从源码开始
=====================
注：之所以要这么做，完全是因为nginx-gridfs需要从源码开始编译……

gridfs是mongodb的内部文件存储系统，nginx+nginx-gridfs比nginx+ext3慢了10%左右，然而gridfs方案提供的优势远远大于这些性能损失。

编译安装
--------

* 下载 `nginx <http://nginx.org/en/download.html>`_ 并解压
* 下载 `nginx-gridfs <https://github.com/mdirolf/nginx-gridfs>`_ 并解压
* 在nginx解压目录下，执行以下几句。注意，要把/path/to/nginx-gridfs换成实际路径::

    .configure --with-http_ssl_module --sbin-path=/usr/sbin --add-module=/path/to/nginx-gridfs
    sudo make
    sudo make install

配置
----

配置nginx-gridfs
^^^^^^^^^^^^^^^^
参考 `nginx-gridfs doc <https://github.com/mdirolf/nginx-gridfs>`_ ，在nginx.conf中添加： ::
    location /gridfs/ {
        gridfs <db_name> user=<username> pass=<password>
    }

如果你是从源码开始安装nginx的，nginx.conf应该会在/usr/local/nginx/conf/nginx.conf。否则，看看/etc/nginx/nginx.conf吧。

开启/停止脚本
^^^^^^^^^^^^^

从源代码安装的nginx是不会成为ubuntu的service的，我们只能手工写一个启动/停止脚本，存放在/etc/init.d/nginx，具体内容如下：

.. code-block:: bash

    #! /bin/sh

    ### BEGIN INIT INFO
    # Provides:          nginx
    # Required-Start:    $local_fs $remote_fs $network $syslog
    # Required-Stop:     $local_fs $remote_fs $network $syslog
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: starts the nginx web server
    # Description:       starts nginx using start-stop-daemon
    ### END INIT INFO

    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
    DAEMON=/usr/sbin/nginx
    NAME=nginx
    DESC=nginx

    test -x $DAEMON || exit 0

    # Include nginx defaults if available
    if [ -f /etc/default/nginx ] ; then
        . /etc/default/nginx
    fi

    set -e

    . /lib/lsb/init-functions

    test_nginx_config() {
      if $DAEMON -t $DAEMON_OPTS >/dev/null 2>&1
      then
        return 0
      else
        $DAEMON -t $DAEMON_OPTS
        return $?
      fi
    }

    case "$1" in
      start)
        echo -n "Starting $DESC: "
            test_nginx_config
        start-stop-daemon --start --quiet --pidfile /usr/local/nginx/logs/$NAME.pid \
            --exec $DAEMON -- $DAEMON_OPTS || true
        echo "$NAME."
        ;;
      stop)
        echo -n "Stopping $DESC: "
        start-stop-daemon --stop --quiet --pidfile /usr/local/nginx/logs/$NAME.pid \
            --exec $DAEMON || true
        echo "$NAME."
        ;;
      restart|force-reload)
        echo -n "Restarting $DESC: "
        start-stop-daemon --stop --quiet --pidfile /usr/local/nginx/logs/$NAME.pid \
            --exec $DAEMON || true
        sleep 1
            test_nginx_config
        start-stop-daemon --start --quiet --pidfile /usr/local/nginx/logs/$NAME.pid \
            --exec $DAEMON -- $DAEMON_OPTS || true
        echo "$NAME."
        ;;
      reload)
            echo -n "Reloading $DESC configuration: "
            test_nginx_config
            start-stop-daemon --stop --signal HUP --quiet --pidfile /usr/local/nginx/logs/$NAME.pid \
                --exec $DAEMON || true
            echo "$NAME."
            ;;
      configtest)
            echo -n "Testing $DESC configuration: "
            if test_nginx_config
            then
              echo "$NAME."
            else
              exit $?
            fi
            ;;
      status)
        status_of_proc -p /var/run/$NAME.pid "$DAEMON" nginx && exit 0 || exit $?
        ;;
      *)
        echo "Usage: $NAME {start|stop|restart|reload|force-reload|status|configtest}" >&2
        exit 1
        ;;
    esac

    exit 0
启动
----

如果你用了我提供的脚本，键入`sudo service nginx start`即可。
然后打开浏览器看看http://localhost吧，如果看到'Welcome to nginx!'，那恭喜啦，你成功鸟！不然的话，嘿嘿，再读一遍本文吧

如果你已经有文件在mongodb内，可以访问 ``http://localhost/gridfs/<object_id>`` 来下载文件


