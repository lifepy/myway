通过mod-wsgi连接Apache与Django
==============================
1.安装

*Ubuntu* : `sudo apt-get install libapache2-mod-wsgi`

2.配置

在Django工程目录下，建立文件夹apache，并创立两个文件，其中django.wsgi是通用描述文件，apache_wsgi.conf中则保存了绝对路径，所以需要根据环境进行修改。文件内容如下：::

    # filename: django.wsgi
    import os, sys
    from os.path import join, pardir, abspath, dirname

    #Calculate the path based on the location of the WSGI script.
    apache_configuration= dirname(__file__)
    project_dir = join(apache_configuration, pardir)

    #tags_dir = os.path.join(src_dir, 'myway')

    # append source dir
    if project_dir not in sys.path:
        sys.path.append(project_dir)

    # append tag dir
    #if tags_dir not in sys.path:
    #    sys.path.append(tags_dir)

    sys.stdout = sys.stderr
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    os.environ['SCRIPT_NAME'] = '/myway/'

    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()

::

    # filename: apache_wsgi.conf
    XSendFile On
    Alias /static "/workspace/myway/static"
    <Directory "/workspace/myway/static">
        Options Indexes
        Order allow,deny
        allow from all
    </Directory>

    <Directory "/opt/www/upload">
        Options Indexes
        Order allow,deny
        allow from all
    </Directory>

    <Directory "/opt/www/share">
        XSendFilePath /opt/www/share
        Options Indexes
        Order allow,deny
        allow from all
    </Directory>

    WSGIScriptAlias / "/workspace/myway/apache/django.wsgi"

    <Directory "/workspace/myway/apache">
    Allow from all
    </Directory>

然后，在/etc/apache2/sites-enabled/000-default中加入::

    Include "/path/to/apache_wsgi.conf"

3.重启Apache::

    sudo service apache2 restart
