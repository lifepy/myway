MongoDB设置
===========

* 下载安装MongoDB (version>1.8)
* 运行server: mongod
* 运行client: mongo
* 键入以下命令：::

    use admin
    db.addUser('yourusername','yourpassword')
    use test
    db.addUser('test','test')

其中，yourusername/yourpassword为你的管理员账户，test/test则为项目测试环境所使用的连接密码
* 关闭server，并且重启： `mongod --auth`
