# coding=utf-8
import os
import time
from stat import ST_SIZE, ST_CTIME
from os.path import join, isdir

from django.utils import simplejson
from django.http import HttpResponse

alias_dict = {
    'share': '/opt/www/share',
    'upload': '/opt/www/upload',
}

def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def list_dir(path):
    file_list = []
    if isdir(path):
        for filename in os.listdir(path):
            fullpath = join(path, filename)
            ret = {
                'name':filename,
                'isdir': isdir(fullpath),
                'path': fullpath,
                'size': sizeof_fmt(os.stat(fullpath)[ST_SIZE]),
                'creation_time': time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(os.stat(fullpath)[ST_CTIME])),
            }
            file_list.append( ret )
    return file_list

def get_file_list(request, base_dir_alias, relative_path):
    if relative_path:
        relative_path = relative_path.encode('utf-8')
    else:
        relative_path = ''
    base_dir = alias_dict[base_dir_alias]
    path = join(base_dir, relative_path)
    file_list = list_dir(path)

    return HttpResponse(simplejson.dumps(file_list))

def get_file_list_for_data_table(request, base_dir_alias, relative_path):
    '''
    To work with dataTable 
    '''
    if relative_path:
        relative_path = relative_path.encode('utf-8')
    else:
        relative_path = ''
    base_dir = alias_dict[base_dir_alias]
    path = join(base_dir, relative_path)
    file_list = list_dir(path)

    if relative_path.strip() == '':
        aaData = []
    else:
        aaData = [["<a href='../'>../</a>", "",""],]
    for file_info in file_list:
        name = file_info['name']
        if file_info['isdir']:
            name += '/'
        path = file_info['path'].decode('utf-8')
        path = path.replace(alias_dict[base_dir_alias], '/'+base_dir_alias)
        path = path.encode('utf-8')

        aaData.append([ "<a href='%s'>%s</a>" % (path, name), file_info['size'], file_info['creation_time'] ])
        
    return HttpResponse(simplejson.dumps({'aaData':aaData}))
