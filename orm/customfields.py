import peewee
from peewee import *

class TextAreaField(peewee.TextField) :
    pass

class PositionFieldX(peewee.IntegerField) :
    pass

class PositionFieldY(peewee.IntegerField) :
    pass

class JsonField(peewee.TextField) :
    pass

class OptionField(peewee.TextField) :
    pass
