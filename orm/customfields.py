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

class UnitIntegerField(peewee.IntegerField) :

    def __init__( self, **kwargs ) :
        self.unit = kwargs.get('unit')
        peewee.IntegerField.__init__(self,kwargs)
