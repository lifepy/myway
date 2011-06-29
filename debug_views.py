# coding=utf-8
from django.http import HttpResponse

from pymongo.objectid import ObjectId
from pymongo import Connection
import gridfs

from mongo_models import db_name, db_username, db_password
db = Connection()[db_name]
db.authenticate(db_username, db_password)
fs = gridfs.GridFS(db)

def serve_file_by_id(request, object_id):
    if request.method == 'GET':
        file = fs.get(ObjectId(object_id))
        response = HttpResponse(file.read())
        response['Content-Type'] = file.content_type
        return response
