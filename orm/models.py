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
        },{
            'model': legend,
            'reference':'legends'
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
    population = UnitIntegerField()
    pos_x = PositionFieldX()
    pos_y = PositionFieldY()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Städer"
        return "Stad"

    @staticmethod
    def related_names() :
        return [{
            'model': place,
            'reference':'places'
        }]

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
    def related_names() :
        return [{
            'model': person,
            'reference':'persons'
        }]

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
                'Bibliotek',
                'Magisk plats'
            ]
        return []

class bloodline(MyModel):
    region = ForeignKeyField(region, null=True, related_name='bloodlines')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Ãtter"
        return "Ãtt"

class damagetype(MyModel):

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Skadetyper"
        return "Skadetyp"

    @staticmethod
    def related_names() :
        return [{
            'model': weapon,
            'reference':'weapons'
        }]

class person(MyModel):
    profession = OptionField()
    city = ForeignKeyField(city, null=True, related_name='persons')
    place = ForeignKeyField(place, null=True, related_name='persons')
    bloodline = ForeignKeyField(bloodline, null=True, related_name='persons')

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
                'Vakt',
                'Ãmbetsman',
            ]
        return []

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Personer"
        return "Person"

class magictype(MyModel):

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Magisfärer"
        return "Magisfär"

    @staticmethod
    def related_names() :
        return [{
            'model': magic,
            'reference':'magic'
        }]

class magic(MyModel):
    magictype = ForeignKeyField(magictype, related_name='magic')
    prerequisites = TextAreaField()
    actions = UnitIntegerField()
    difficulty = UnitIntegerField()
    powercost = UnitIntegerField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Magier"
        return "Magi"

    @staticmethod
    def related_names() :
        return [{
            'model': spell,
            'reference':'spells'
        }]

class spell(MyModel):
    magic = ForeignKeyField(magic, related_name='spells')
    magicstrengtheffect = TextAreaField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Besvärjelser"
        return "Besvärjelse"

class legend(MyModel):
    region = ForeignKeyField(region, null=True, related_name='legends')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Legender"
        return "Legend"

class diety(MyModel) :
    appearance = TextAreaField()
    sphere = TextAreaField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Gudomar"
        return "Gud"

class creaturetype(MyModel) :

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Varelsetyper"
        return "Varelsetyp"

    @staticmethod
    def related_names() :
        return [{
            'model': creature,
            'reference':'creatures'
        }]

class creature(MyModel) :
    nest = TextAreaField()
    food = TextAreaField()
    behaviour = TextAreaField()
    creaturetype = ForeignKeyField(creaturetype, null=True, related_name='creatures')

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

class itemtype(MyModel):

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Föremålstyper"
        return "Föremålstyp"


    @staticmethod
    def related_names() :
        return [{
            'model': ingredient,
            'reference':'ingredients'
        },{
            'model': weapon,
            'reference':'weapons'
        },{
            'model': armor,
            'reference':'armors'
        },{
            'model': tool,
            'reference':'tools'
        },{
            'model': alchemy,
            'reference':'alchemy'
        }]

class Item(MyModel):

    value = UnitIntegerField(unit="kopparmynt")
    weight = UnitIntegerField(unit="hekton")

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Föremål"
        return "Föremål"

    @staticmethod
    def field_display_name(field_name) :
        if field_name == 'itemtype' :
            return 'Föremålstyp'
        elif field_name == 'value' :
            return 'Värde i koppar'
        elif field_name == 'weight' :
            return 'Vikt i hekton'
        return MyModel.field_display_name(field_name)

class weapon(Item):

    damage = UnitIntegerField()
    damagetype = peewee.ForeignKeyField(damagetype, null=True, related_name='weapons')
    durability = UnitIntegerField()
    penetration = UnitIntegerField()
    hit = UnitIntegerField()
    throw = UnitIntegerField()
    range = UnitIntegerField()
    defensemelee = UnitIntegerField()
    defenseranged = UnitIntegerField()
    requiredstrength = UnitIntegerField()
    requireddexterity = UnitIntegerField()
    itemtype = peewee.ForeignKeyField(itemtype, related_name='weapons')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Vapen"
        return "Vapen"

    @staticmethod
    def field_display_name(field_name) :
        if field_name == 'damage' :
            return 'Skada'
        elif field_name == 'durability' :
            return 'Tålighet'
        elif field_name == 'hit' :
            return 'Träff'
        elif field_name == 'throw' :
            return 'Träff vid kast'
        elif field_name == 'range' :
            return 'Räckvidd'
        elif field_name == 'defensemelee' :
            return 'Skydd'
        elif field_name == 'defenseranged' :
            return 'Skydd mot projektiler'
        elif field_name == 'requiredstrength' :
            return 'Styrkekrav'
        elif field_name == 'requireddexterity' :
            return 'Smidighetskrav'
        return Item.field_display_name(field_name)

class armor(Item):

    armorvalue = UnitIntegerField()
    staminareduction = UnitIntegerField()
    speedreduction = UnitIntegerField()
    itemtype = peewee.ForeignKeyField(itemtype, related_name='armors')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Rustningar"
        return "Rustning"

    @staticmethod
    def field_display_name(field_name) :
        if field_name == 'armorvalue' :
            return 'Pansarvärde'
        elif field_name == 'staminareduction' :
            return 'Uthållighetsreduktion'
        elif field_name == 'speedreduction' :
            return 'Snabbhetsreduktion'
        return Item.field_display_name(field_name)

class tool(Item):

    useage = TextAreaField()
    itemtype = peewee.ForeignKeyField(itemtype, related_name='tools')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Verktyg"
        return "Verktyg"

class travelitem(Item):

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Reseutrustning"
        return "Reseutrustning"

class mount(Item):

    creature = ForeignKeyField(creature, related_name='mount')
    itemtype = peewee.ForeignKeyField(itemtype, related_name='mounts')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Arbetsdjur"
        return "Arbetsdjur"

class alchemy(Item):

    difficulty = UnitIntegerField()
    effects = TextAreaField()
    ingredientmin = UnitIntegerField(unit='stycken')
    ingredientmax = UnitIntegerField(unit='stycken')
    itemtype = peewee.ForeignKeyField(itemtype, related_name='alchemy')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Alkemiska produkter"
        return "Alkemisk produkt"

class ingredient(Item) :

    toxicity = UnitIntegerField()
    duration = UnitIntegerField(unit='minuter')
    delay = UnitIntegerField(unit='minuter')
    effects = TextAreaField()
    difficulty = UnitIntegerField()
    itemtype = peewee.ForeignKeyField(itemtype, related_name='ingredients')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Ingredienser"
        return "Ingrediens"

    @staticmethod
    def field_display_name(field_name) :
        if field_name == 'duration' :
            return 'Verkanstid'
        if field_name == 'delay' :
            return 'Upptagningstid'
        if field_name == 'effects' :
            return 'Effekter'
        if field_name == 'difficulty' :
            return 'Svårighetsgrad för att utvinna'
        return MyModel.field_display_name(field_name)

class randomtable(MyModel) :

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Slumptabeller"
        return "Slumptabell"

class randomevent(MyModel) :

    randomtable = peewee.ForeignKeyField(randomtable, related_name='randomevents')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Händelser"
        return "Händelse"

class combatskill(MyModel) :

    itemtype = peewee.ForeignKeyField(itemtype, related_name='combatskills')

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Stridsfärdigheter"
        return "Stridsfärdighet"
