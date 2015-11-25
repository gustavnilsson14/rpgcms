#!/usr/bin/env python
# -*- coding: utf-8 -*-

import peewee
from customfields import *
from ormcore import *

class continent(MyModel):

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Kontinenter"
        return "Kontinent"

    @staticmethod
    def related_names() :
        return [{
            'model': region,
            'reference':'regions'
        }]

class region(MyModel):
    continent = peewee.ForeignKeyField(continent, related_name='regions')
    climate = TextAreaField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Regioner"
        return "Region"

    @staticmethod
    def related_names() :
        return [{
            'model': city,
            'reference':'cities'
        }]

    @staticmethod
    def field_display_name(field_name) :
        if field_name == 'climate' :
            return 'Klimat'
        return MyModel.field_display_name(field_name)

class city(MyModel):
    region = ForeignKeyField(region, related_name='cities')
    industry = TextAreaField()
    diversity = TextAreaField()
    population = IntegerField()
    pos_x = PositionFieldX()
    pos_y = PositionFieldY()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Städer"
        return "Stad"

    @staticmethod
    def field_display_name(field_name) :
        if field_name == 'population' :
            return 'Stads­befolk­ning'
        if field_name == 'diversity' :
            return 'Mångfald'
        if field_name == 'industri' :
            return 'Näringsliv'
        return MyModel.field_display_name(field_name)

class place(MyModel):
    region = ForeignKeyField(region, null=True, related_name='places')
    city = ForeignKeyField(city, null=True, related_name='places')
    location = TextAreaField(null=True)
    type = OptionField()
    pos_x = PositionFieldX(null=True)
    pos_y = PositionFieldY(null=True)

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Platser"
        return "Plats"

    @staticmethod
    def get_options(field_name) :
        if field_name == 'type' :
            return [
                'Marknad',
                'Tempel',
                'Taverna',
                'Gille',
                'Statshus',
                'Garrison',
                'Skola',
                'Herrgård',
                'By',
                'Magisk plats'
            ]
        return []


class person(MyModel):
    profession = OptionField()
    city = ForeignKeyField(city, null=True, related_name='persons')
    place = ForeignKeyField(place, null=True, related_name='persons')

    @staticmethod
    def get_options(field_name) :
        if field_name == 'profession' :
            return [
                'Krigare',
                'Magiker',
                'Tjuv',
                'Handelsman',
                'Präst',
                'Hantverkare',
                'Tavernavärd',
                'Vakt'
            ]
        return []

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Personer"
        return "Person"

class itemtype(MyModel):

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Föremålstyp"
        return "Föremålstyp"

class itemsubtype(MyModel):

    itemtype = ForeignKeyField(itemtype, related_name='itemsubtypes')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Föremålssubtyp"
        return "Föremålssubtyp"

class item(MyModel):

    itemsubtype = ForeignKeyField(itemsubtype, related_name='items')
    value = peewee.IntegerField

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Föremål"
        return "Föremål"

class magic(MyModel):

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Magi"
        return "Magi"

class spell(MyModel):
    magic = ForeignKeyField(magic, related_name='spells')
    prerequisites = TextAreaField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Besvärjelser"
        return "Besvärjelse"

class legend(MyModel):
    region = ForeignKeyField(region, related_name='legends')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Legender"
        return "Legend"

class creature(MyModel) :

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Varelser"
        return "Varelse"

class vegetation(MyModel) :

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Växter"
        return "Växt"

class ingredient(MyModel) :

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Ingredienser"
        return "Ingrediens"

class stat(MyModel) :

    type = OptionField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Värden"
        return "Värde"

    @staticmethod
    def get_options(field_name) :
        if field_name == 'type' :
            return [
                'spell',
                'item',
                'creature',
                'ingredient'
            ]
        return []

    @staticmethod
    def show_links() :
        return False

    def show_for_class( self, cls ) :
        class_name = cls.__name__
        if class_name == 'person' :
            class_name = 'creature'
        if class_name == self.type :
            return True
        return False

class knowledge(MyModel) :

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Kunskaper"
        return "Kunskap"

    @staticmethod
    def show_links() :
        return False
