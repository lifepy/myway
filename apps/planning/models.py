# coding=utf-8
from mongoengine import *
from mongo_models import Place, Activity

class PlanElement(Document):
    start = DateTimeField()
    end = DateTimeField()
    place = ReferenceField(Place)
    activities = EmbeddedDocumentField(Activity)

class Plan(Document):
    author = StringField()
    description = StringField()
    details = ListField(ReferenceField(PlanElement))
