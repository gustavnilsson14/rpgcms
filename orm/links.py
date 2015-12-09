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

class alchemyIngredient(MyLink) :
    alchemyingredient = peewee.ForeignKeyField(ingredient, null=True, related_name='alchemyingredient')
    ingredientalchemy = peewee.ForeignKeyField(alchemy, null=True, related_name='ingredientalchemy')

    @staticmethod
    def related_models() :
        return [alchemy,ingredient]

    @staticmethod
    def display_name(plural=True) :
        return "Produkt kan göras med följande ingredienser"

class vegetationIngredient(MyLink) :
    vegetationingredient = peewee.ForeignKeyField(ingredient, null=True, related_name='vegetationingredient')
    ingredientvegetation = peewee.ForeignKeyField(vegetation, null=True, related_name='ingredientvegetation')

    @staticmethod
    def related_models() :
        return [vegetation,ingredient]

    @staticmethod
    def display_name(plural=True) :
        return "Växt innehåller ingredienser"


#STAT LINKS
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

class magictypeKnowledge(MyLink) :
    magictypeknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='magictypeknowledge')
    knowledgemagictype = peewee.ForeignKeyField(magictype, null=True, related_name='knowledgemagictype')

    @staticmethod
    def related_models() :
        return [magictype,knowledge]

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

class bloodlineKnowledge(MyLink) :
    bloodlineknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='bloodlineknowledge')
    knowledgebloodline = peewee.ForeignKeyField(bloodline, null=True, related_name='knowledgebloodline')

    @staticmethod
    def related_models() :
        return [bloodline,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " har kunskapen"


class alchemyKnowledge(MyLink) :
    alchemyknowledge = peewee.ForeignKeyField(knowledge, null=True, related_name='alchemyknowledge')
    knowledgealchemy = peewee.ForeignKeyField(alchemy, null=True, related_name='knowledgealchemy')

    @staticmethod
    def related_models() :
        return [alchemy,knowledge]

    @classmethod
    def display_name(cls, plural=True) :
        return cls.related_models()[0].display_name(False) + " har kunskapen"


#weapon LINKS
class creatureWeapon(MyLink) :
    creatureweapon = peewee.ForeignKeyField(weapon, null=True, related_name='creatureweapon')
    weaponcreature = peewee.ForeignKeyField(creature, null=True, related_name='weaponcreature')

    @staticmethod
    def related_models() :
        return [creature,weapon]

    @staticmethod
    def display_name(plural=True) :
        return "Varelse har vapen"

class placeWeapon(MyLink) :
    placeweapon = peewee.ForeignKeyField(weapon, null=True, related_name='placeweapon')
    weaponplace = peewee.ForeignKeyField(place, null=True, related_name='weaponplace')

    @staticmethod
    def related_models() :
        return [place,weapon]

    @staticmethod
    def display_name(plural=True) :
        return "Vapen finns tillgängligt på plats"

class personWeapon(MyLink) :
    personweapon = peewee.ForeignKeyField(weapon, null=True, related_name='personweapon')
    weaponperson = peewee.ForeignKeyField(person, null=True, related_name='weaponperson')

    @staticmethod
    def related_models() :
        return [person,weapon]

    @staticmethod
    def display_name(plural=True) :
        return "Person har vapen"

class creatureArmor(MyLink) :
    creaturearmor = peewee.ForeignKeyField(armor, null=True, related_name='creaturearmor')
    armorcreature = peewee.ForeignKeyField(creature, null=True, related_name='armorcreature')

    @staticmethod
    def related_models() :
        return [creature,armor]

    @staticmethod
    def display_name(plural=True) :
        return "Varelse har rustning"

class placeArmor(MyLink) :
    placearmor = peewee.ForeignKeyField(armor, null=True, related_name='placearmor')
    armorplace = peewee.ForeignKeyField(place, null=True, related_name='armorplace')

    @staticmethod
    def related_models() :
        return [place,armor]

    @staticmethod
    def display_name(plural=True) :
        return "Rustning finns tillgängligt på plats"

class personArmor(MyLink) :
    personarmor = peewee.ForeignKeyField(armor, null=True, related_name='personarmor')
    armorperson = peewee.ForeignKeyField(person, null=True, related_name='armorperson')

    @staticmethod
    def related_models() :
        return [person,armor]

    @staticmethod
    def display_name(plural=True) :
        return "Person har rustning"

class creatureTool(MyLink) :
    creaturetool = peewee.ForeignKeyField(tool, null=True, related_name='creaturetool')
    toolcreature = peewee.ForeignKeyField(creature, null=True, related_name='toolcreature')

    @staticmethod
    def related_models() :
        return [creature,tool]

    @staticmethod
    def display_name(plural=True) :
        return "Varelse har verktyg"

class placeTool(MyLink) :
    placetool = peewee.ForeignKeyField(tool, null=True, related_name='placetool')
    toolplace = peewee.ForeignKeyField(place, null=True, related_name='toolplace')

    @staticmethod
    def related_models() :
        return [place,tool]

    @staticmethod
    def display_name(plural=True) :
        return "Verktyg finns tillgängligt på plats"

class personTool(MyLink) :
    persontool = peewee.ForeignKeyField(tool, null=True, related_name='persontool')
    toolperson = peewee.ForeignKeyField(person, null=True, related_name='toolperson')

    @staticmethod
    def related_models() :
        return [person,tool]

    @staticmethod
    def display_name(plural=True) :
        return "Person har verktyg"

class creatureTravelitem(MyLink) :
    creaturetravelitem = peewee.ForeignKeyField(travelitem, null=True, related_name='creaturetravelitem')
    travelitemcreature = peewee.ForeignKeyField(creature, null=True, related_name='travelitemcreature')

    @staticmethod
    def related_models() :
        return [creature,travelitem]

    @staticmethod
    def display_name(plural=True) :
        return "Varelse har reseutrustning"

class placeTravelitem(MyLink) :
    placetravelitem = peewee.ForeignKeyField(travelitem, null=True, related_name='placetravelitem')
    travelitemplace = peewee.ForeignKeyField(place, null=True, related_name='travelitemplace')

    @staticmethod
    def related_models() :
        return [place,travelitem]

    @staticmethod
    def display_name(plural=True) :
        return "Reseutrustning finns tillgängligt på plats"

class personTravelitem(MyLink) :
    persontravelitem = peewee.ForeignKeyField(travelitem, null=True, related_name='persontravelitem')
    travelitemperson = peewee.ForeignKeyField(person, null=True, related_name='travelitemperson')

    @staticmethod
    def related_models() :
        return [person,travelitem]

    @staticmethod
    def display_name(plural=True) :
        return "Person har reseutrustning"
