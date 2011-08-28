myway环境配置 [Ubuntu篇]
========================

以下介绍了网站开发、爬虫开发和辅助环境中所必须的软件及Python模块，其中所有的安装方法均为在Ubuntu下。

在Ubuntu下所有python库，均可以直接下载解压，然后运行setup.py进行安装，需要sudo权限: ``sudo python setup.py install``

网站开发
--------

* **网页服务器**
    - nginx 1.1.0: 请看:ref:`install-nginx`
    - Apache 2.2: ``sudo apt-get install apache2 libapache2-mod-wsgi apache2-mpm-prefork``
* **数据库**
    - MySQL 5: ``sudo apt-get install mysql-server-5.1 mysql-client-5.1 libmysqlclient-dev``
    - MongoDB 1.8.3:  `Tutorial <http://www.mongodb.org/downloads>`_ ,据此安装即可。主要步骤有三：
        1. 在/etc/apt/sources.list中添加 ``deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen``
        2. 更新GPG Key: ``sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10``
        3. 安装 ``sudo apt-get update; sudo apt-get install mongodb-10gen``
* Python 2.6.6:   ``sudo apt-get install python2.6 python2.6-dev python-setuptools``
* **Python模块**
    - Django 1.3: 参照python库安装， `下载链接 <https://www.djangoproject.com/download/>`_
    - pymongo 1.11: ``sudo easy_install pymongo``
    - MySQLdb:    ``sudo apt-get install python-mysqldb``
    - mongoengine: ``sudo easy_install mongoengine``
    - html5lib: ``sudo easy_install html5lib``
    - lxml 2.3: :: ``sudo apt-get install libxml2 libxslt1-dev python2.6-dev; sudo easy_install lxml==2.3``
    - django_compressor 0.9.2 (需要lxml, BeautifulSoup and html5lib): ``sudo easy_install django_compressor``

爬虫开发
--------

* MongoDB 1.8.3: 安装方法同上
* Python 2.6.6: 安装方法同上
* **Python 模块**
    - pymongo 1.11: ``sudo easy_install pymongo``
    - `Scrapy 0.12 <http://scrapy.org/>`_ : ``sudo easy_install -U Scrapy``
    - `BeautifulSoup 3.2.0 <http://www.crummy.com/software/BeautifulSoup/>`_: 请参考python库安装方法（切忌使用 ``sudo apt-get install python-beautifulsoup``）

辅助
----

* ipython: ``sudo apt-get install ipython``
* SQLAlchemy: ``sudo apt-get install python-sqlalchemy``
* gvim: ``sudo apt-get install vim-gnome``
* screen, telnet: ``sudo apt-get install screen telnet``
