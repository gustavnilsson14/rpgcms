#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *
from links import *
import sys, inspect

class RpgDatabase :
    def __init__(self) :
        self.links = []
        self.models = [
            continent,
            region,
            city,
            place,
            bloodline,
            person,
            magictype,
            magic,
            spell,
            legend,
            creaturetype,
            creature,
            itemtype,
            weapon,
            armor,
            tool,
            travelitem,
            mount,
            alchemy,
            vegetation,
            ingredient,
            stat,
            knowledge,
            user,
            comment,
            combatskill
        ]
        MyModel.rpgdb = self
        for name, obj in inspect.getmembers(sys.modules['links']):
            if inspect.isclass(obj):
                if issubclass(obj, MyLink) and obj != MyLink:
                    self.links += [obj]
        self.create_tables()
        print "Database upto date"

    def create_tables(self):
        for model in self.models :
            print "Creating model " + model.__name__
            model.create_table( True )
        for link in self.links :
            print "Creating link " + link.__name__
            link.create_table( True )

    def alter_tables(self):
        for model in self.models :
            model.alter()

    def to_dict(self, instance ) :
        return model_to_dict( instance )

    def get_model( self, model_name ) :
        for model in self.models:
            if model.__name__ == model_name :
                return model
        return 0

    def get_link( self, link_name ) :
        for link in self.links:
            if link.__name__ == link_name :
                return link
        return 0

    def get_links_by_model( self, model ) :
        links = []
        for link in self.links:
            if model in link.related_models() :
                links += [ link ]
        return links
