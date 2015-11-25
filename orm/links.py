#!/usr/bin/env python
# -*- coding: utf-8 -*-

import peewee
from customfields import *
from ormcore import *
from models import *

class regionCreature(MyLink) :
    regioncreature = peewee.ForeignKeyField(creature, null=True, related_name='regioncreature')
    creatureregion = peewee.ForeignKeyField(region, null=True, related_name='creatureregion')

    @staticmethod
    def related_models() :
        return [region,creature]

    @staticmethod
    def display_name(plural=True) :
        return "Region innehåller varelser"

class regionVegetation(MyLink) :
    regionvegetation = peewee.ForeignKeyField(vegetation, null=True, related_name='regionvegetation')
    vegetationregion = peewee.ForeignKeyField(region, null=True, related_name='vegetationregion')

    @staticmethod
    def related_models() :
        return [region,vegetation]

    @staticmethod
    def display_name(plural=True) :
        return "Region innehåller växtlighet"


#MAGIC LINKS

class personMagic(MyLink) :
    personmagic = peewee.ForeignKeyField(magic, null=True, related_name='personmagic')
    magicperson = peewee.ForeignKeyField(person, null=True, related_name='magicperson')

    @staticmethod
    def related_models() :
        return [person,magic]

    @staticmethod
    def display_name(plural=True) :
        return "Person kan magi"



#ITEM LINKS
class creatureItem(MyLink) :
    creatureitem = peewee.ForeignKeyField(item, null=True, related_name='creatureitem')
    itemcreature = peewee.ForeignKeyField(creature, null=True, related_name='itemcreature')

    @staticmethod
    def related_models() :
        return [creature,item]

    @staticmethod
    def display_name(plural=True) :
        return "Varelse har föremål"

class placeItem(MyLink) :
    placeitem = peewee.ForeignKeyField(place, null=True, related_name='placeitem')
    itemplace = peewee.ForeignKeyField(item, null=True, related_name='itemplace')

    @staticmethod
    def related_models() :
        return [place,item]

    @staticmethod
    def display_name(plural=True) :
        return "Föremål finns tillgängligt på plats"

class personItem(MyLink) :
    personitem = peewee.ForeignKeyField(item, null=True, related_name='personitem')
    itemperson = peewee.ForeignKeyField(person, null=True, related_name='itemperson')

    @staticmethod
    def related_models() :
        return [person,item]

    @staticmethod
    def display_name(plural=True) :
        return "Person har föremål"


#INGREDIENT LINKS
class creatureIngredient(MyLink) :
    creatureingredient = peewee.ForeignKeyField(ingredient, null=True, related_name='creatureingredient')
    ingredientcreature = peewee.ForeignKeyField(creature, null=True, related_name='ingredientcreature')

    @staticmethod
    def related_models() :
        return [creature,ingredient]

    @staticmethod
    def display_name(plural=True) :
        return "Varelse innehåller ingredienser"

class vegetationIngredient(MyLink) :
    vegetationingredient = peewee.ForeignKeyField(ingredient, null=True, related_name='vegetationingredient')
    ingredientvegetation = peewee.ForeignKeyField(vegetation, null=True, related_name='ingredientvegetation')

    @staticmethod
    def related_models() :
        return [vegetation,ingredient]

    @staticmethod
    def display_name(plural=True) :
        return "Växt innehåller ingredienser"

class itemIngredient(MyLink) :
    itemingredient = peewee.ForeignKeyField(ingredient, null=True, related_name='itemingredient')
    ingredientitem = peewee.ForeignKeyField(item, null=True, related_name='ingredientitem')

    @staticmethod
    def related_models() :
        return [item,ingredient]

    @staticmethod
    def display_name(plural=True) :
        return "Föremål består av ingredienser"


#STAT LINKS
class itemStat(MyLink) :
    itemstat = peewee.ForeignKeyField(stat, null=True, related_name='itemstat')
    statitem = peewee.ForeignKeyField(item, null=True, related_name='statitem')

    @staticmethod
    def related_models() :
        return [item,stat]

    @staticmethod
    def display_name(plural=True) :
        return "Föremål har värden"

class ingredientStat(MyLink) :
    ingredientstat = peewee.ForeignKeyField(stat, null=True, related_name='ingredientstat')
    statingredient = peewee.ForeignKeyField(ingredient, null=True, related_name='statingredient')

    @staticmethod
    def related_models() :
        return [ingredient,stat]

    @staticmethod
    def display_name(plural=True) :
        return "Ingrediens har värden"

class spellStat(MyLink) :
    spellstat = peewee.ForeignKeyField(stat, null=True, related_name='spellstat')
    statspell = peewee.ForeignKeyField(spell, null=True, related_name='statspell')

    @staticmethod
    def related_models() :
        return [spell,stat]

    @staticmethod
    def display_name(plural=True) :
        return "Besvärjelse har värden"

class creatureStat(MyLink) :
    creaturestat = peewee.ForeignKeyField(stat, null=True, related_name='creaturestat')
    statcreature = peewee.ForeignKeyField(creature, null=True, related_name='statcreature')

    @staticmethod
    def related_models() :
        return [creature,stat]

    @staticmethod
    def display_name(plural=True) :
        return "Varelse har värden"

class personStat(MyLink) :
    personstat = peewee.ForeignKeyField(stat, null=True, related_name='personstat')
    statperson = peewee.ForeignKeyField(person, null=True, related_name='statperson')

    @staticmethod
    def related_models() :
        return [person,stat]

    @staticmethod
    def display_name(plural=True) :
        return "Person har värden"



#KNOWLEDGE LINKS

class regionKnowledge(MyLink) :
    regionknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='regionknowledge')
    knowledgeregion = peewee.ForeignKeyField(region, null=True, related_name='knowledgeregion')

    @staticmethod
    def related_models() :
        return [region,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class cityKnowledge(MyLink) :
    cityknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='cityknowledge')
    knowledgecity = peewee.ForeignKeyField(city, null=True, related_name='knowledgecity')

    @staticmethod
    def related_models() :
        return [city,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class placeKnowledge(MyLink) :
    placeknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='placeknowledge')
    knowledgeplace = peewee.ForeignKeyField(place, null=True, related_name='knowledgeplace')

    @staticmethod
    def related_models() :
        return [place,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class itemKnowledge(MyLink) :
    itemknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='itemknowledge')
    knowledgeitem = peewee.ForeignKeyField(item, null=True, related_name='knowledgeitem')

    @staticmethod
    def related_models() :
        return [item,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class magicKnowledge(MyLink) :
    magicknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='magicknowledge')
    knowledgemagic = peewee.ForeignKeyField(magic, null=True, related_name='knowledgemagic')

    @staticmethod
    def related_models() :
        return [magic,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class legendKnowledge(MyLink) :
    legendknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='legendknowledge')
    knowledgelegend = peewee.ForeignKeyField(legend, null=True, related_name='knowledgelegend')

    @staticmethod
    def related_models() :
        return [legend,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class creatureKnowledge(MyLink) :
    creatureknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='creatureknowledge')
    knowledgecreature = peewee.ForeignKeyField(creature, null=True, related_name='knowledgecreature')

    @staticmethod
    def related_models() :
        return [creature,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class vegetationKnowledge(MyLink) :
    vegetationknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='vegetationknowledge')
    knowledgevegetation = peewee.ForeignKeyField(vegetation, null=True, related_name='knowledgevegetation')

    @staticmethod
    def related_models() :
        return [vegetation,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class ingredientKnowledge(MyLink) :
    ingredientknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='ingredientknowledge')
    knowledgeingredient = peewee.ForeignKeyField(ingredient, null=True, related_name='knowledgeingredient')

    @staticmethod
    def related_models() :
        return [ingredient,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " kräver kunskapen"

class userKnowledge(MyLink) :
    userknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='userknowledge')
    knowledgeuser = peewee.ForeignKeyField(user, null=True, related_name='knowledgeuser')

    @staticmethod
    def related_models() :
        return [user,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " har kunskapen"
