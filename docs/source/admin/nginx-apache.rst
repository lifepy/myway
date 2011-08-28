nginx与apache并存
=================

首先要肯定的是Apache是一个很好的服务器，但要是论响应速度，尤其是静态内容的响应速度，那还是远远比不上nginx。因此，我们尝试着使用nginx作为前端服务器，用来处理静态文件请求，而动态请求则转交给Apache处理。这里的静态文件由mongodb的GridFS中取出。：

配置nginx
---------

在nginx.conf中，将server中的location改为类似：::

        location /gridfs/ {
            gridfs test user=test pass=test;
        }

        location / {
            
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_pass http://127.0.0.1:81;
            #root   /opt/www;
            #index  index.html index.htm;
        }

这表示，只有/gridfs/开头的URL会被nginx处理，处理方式为连接mongodb。而其他一切内容，均由apache提供

配置Apache
----------

把端口号设置为81，修改文件包括：

* /etc/apache2/apache2.conf
* /etc/apache2/sites-enabled/*
