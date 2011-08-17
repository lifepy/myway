# coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext

from pymongo import Connection
import gridfs

from query_json.db import province_list
from mongo_models import db_name, db_username, db_password
db = Connection()[db_name]
db.authenticate(db_username, db_password)
fs = gridfs.GridFS(db)

def place_details(request):
    plist = [ (p['name'], p['region-code']) for p in province_list]
    return render_to_response('place/details.html',{"province_list": plist}, context_instance=RequestContext(request))

