# coding=utf-8

from django.shortcuts import render_to_response
from query_json.db import province_list
from mongo_models import *

from pymongo.objectid import ObjectId
from pymongo import Connection
import gridfs

from mongo_models import db_name, db_username, db_password
from django.http import HttpResponse
from django.utils import simplejson
db = Connection()[db_name]
db.authenticate(db_username, db_password)
fs = gridfs.GridFS(db)

def get_info(request):
    plist = [ (p['name'], p['region-code']) for p in province_list]
    return render_to_response('spot/info.html',{"province_list": plist})

def get_photolist_by_area(request, spot_name):
    ''' Get uploaded photos from GridFS (mongoDB) '''
    r = Restraunt.objects(name=spot_name).first()

    for photo in r.photos:
        print photo.id
    ret = [str(photo.id) for photo in r.photos]

    ret = simplejson.dumps(ret)
    return HttpResponse(ret)
