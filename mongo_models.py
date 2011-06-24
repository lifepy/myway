# coding=utf-8
from mongoengine import *

connect('test', username='test', password='test')
class Photo(Document):
    #FIXME: doesn't have a FK reference to User
    author = StringField(required=True)
    description = StringField()
    file = FileField(required=True)

class Comment(EmbeddedDocument):
    #FIXME: doesn't have a FK reference to User
    author = StringField(required=True)
    value = StringField()

class Tag(EmbeddedDocument):
    value = StringField()
    count = IntField(default=1)

class LocalityTag(EmbeddedDocumentField):
    name = StringField()
    level = StringField()

class Place(Document):
    # Basics
    name = StringField(required=True, unique=True)
    category = StringField(required=True, choices=['dining','shopping','visiting'])
    city = StringField(required=True) # 所在城市
    address = StringField() # 详细地址
    url = URLField() # 网址
    tel = StringField() # 电话
    hours = StringField() # 营业时间
    description = StringField() # 描述
    direction = StringField() # 到达指南

    # Locality tags
    locality_tags = ListField(StringField())

    # Rating
    rating = FloatField()
    n_rating = IntField()
    
    # Tags
    tags = ListField(EmbeddedDocumentField(Tag))

    # Comments
    comments = ListField(EmbeddedDocumentField(Comment))

    # Photo
    photos = ListField(ReferenceField('Photo'))

    # from which site
    _src = StringField(default='original', choices=['original','dianping.com','koubei.com','daodao.com'])

class Hotel(Place):
    category = StringField(required=True, default="lodging")

class Shop(Place):
    category = StringField(required=True, default="shopping")

class Restraunt(Place):
    category = StringField(required=True, default="dining")
    avg_cost = FloatField()
    specialties = ListField(EmbeddedDocumentField(Tag)) # 特色菜

class Attraction(Place):
    category = StringField(required=True, default="visiting")


#p = Photo(author='simon',description='what')
#p.file = open('/media/share/mine/picture/DCIM/100SSCAM/SSL20038.JPG','r')
#p.file.content_type = 'image/jpeg'

#p.save()
'''
p = Photo.objects(author='simon').first()
f = p.file.read()
content_type = p.file.content_type

print content_type
o = open('x.jpg','w')
o.write(f)
o.close()
'''
