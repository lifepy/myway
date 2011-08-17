
from django.utils import simplejson
from django.http import HttpResponse

from query_json.db import attrs_of
from mongo_models import Restraunt

# TODO: think about other types, such as attractions?
def get_photolist_by_area(request, place_name):
    ''' Get uploaded photos from GridFS (mongoDB) '''
    r = Restraunt.objects(name=place_name).first()

    ret = [str(photo.file.grid_id) for photo in r.photos]

    ret = simplejson.dumps(ret)
    return HttpResponse(ret)


def get_restraunt_list(request, region_code):
    region = attrs_of(region_code)['name']
    
    restraunts = Restraunt.objects(locality_tags=region).all()
    for r in restraunts:
        print r.name
    ret = [r.name for r in restraunts]

    ret = simplejson.dumps(ret)
    return HttpResponse(ret)
