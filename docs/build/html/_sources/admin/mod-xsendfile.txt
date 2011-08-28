安装mod-xsendfile处理文件下载
=============================

安装
----
在Apache上安装mod-xsendfile，要下载源代码并修改编译。

修改代码
^^^^^^^^

* 下载 [mod-xsendfile.c](https://tn123.org/mod_xsendfile/)
* 参照以下diff，修改文件内容（增加中文文件名支持）

.. code-block:: diff

    --- mod_xsendfile.c.orig	2010-09-13 22:21:40.000000000 -0400
    +++ mod_xsendfile.c	2011-03-14 12:37:51.930341000 -0400
    @@ -55,6 +55,7 @@
     #include "http_protocol.h" /* ap_hook_insert_error_filter */
     
     #define AP_XSENDFILE_HEADER "X-SENDFILE"
    +#define AP_XSENDFILE_ENCODING_HEADER "X-SENDFILE-ENCODING"
     
     module AP_MODULE_DECLARE_DATA xsendfile_module;
     
    @@ -218,7 +219,6 @@
       const char **paths;
       int i;
     
    -
     #ifdef _DEBUG
       ap_log_error(APLOG_MARK, APLOG_DEBUG, 0, r->server, "xsendfile: path is %s", root);
     #endif
    @@ -269,6 +269,7 @@
       apr_file_t *fd = NULL;
       apr_finfo_t finfo;
     
    +  const char *encoding = NULL;
       const char *file = NULL;
       char *translated = NULL;
     
    @@ -316,6 +317,23 @@
         return ap_pass_brigade(f->next, in);
       }
     
    +  /* should we decode the path? */
    +  encoding = apr_table_get(r->headers_out, AP_XSENDFILE_ENCODING_HEADER);
    +  apr_table_unset(r->headers_out, AP_XSENDFILE_ENCODING_HEADER);
    +
    +  /* cgi/fastcgi will put the stuff into err_headers_out */
    +  if (!encoding || !*encoding) {
    +    encoding = apr_table_get(r->err_headers_out, AP_XSENDFILE_ENCODING_HEADER);
    +    apr_table_unset(r->err_headers_out, AP_XSENDFILE_ENCODING_HEADER);
    +  }
    +
    +  if (encoding) {
    +    if (!strcasecmp(encoding, "url")) {
    +        /* don't worry about the return value */
    +        ap_unescape_url(file);
    +    }
    +  }
    +
       /*
         drop *everything*
         might be pretty expensive to generate content first that goes straight to the bitbucket,

编译安装
^^^^^^^^
::

    sudo apt-get install apache2-prefork-dev
    sudo apxs2 -cia mod-xsendfile.c

注意！Ubuntu源里的xsendfile版本不支持中文文件名，而且版本较老，不推荐使用，**不要使用以下命令**：::

    # don't use this
    sudo apt-get install libapache2-mod-xsendfile
    sudo a2enmod xsendfile

配置
----

将以下几行酌情加入 Apache Virtual Host 配置文件中：::

    XSendFile On
    <Directory "/opt/www/share">
        XSendFilePath /opt/www/share
        Option Indexes
        Order allow,deny
        allow from all
    </Directory>

启用
^^^^
启用方式非常简单，重启Apache服务器即可

Django中使用xsendfile
---------------------

::

    response = HttpResponse(mimetype='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' %basename(relative_path)
    response['X-Sendfile'] = urllib2.quote(cur_dir) #deal with chinese characters
    response['X-SendFile-Encoding'] = url
    return response
