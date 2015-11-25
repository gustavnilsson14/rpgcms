import os
import json
import tornado.ioloop
import tornado.web
import tornado.template
from models import *
from utilmodels import *
from links import *

class MyHandler(tornado.web.RequestHandler):

    def initialize(self, database):
        self.database = database
        self.loader = tornado.template.Loader("")
        if self.get_cookie('user') != None :
            user_id = int(self.get_cookie('user'))
            self.current_user = user.select().where(user.id == user_id)[0]

    def output( self, template, page_data ) :
        page_data[ 'loader' ] = self.loader
        output = self.loader.load("public/templates/" + template + ".html").generate(page_data=page_data)
        self.write(output)

    def get_post_list( self ) :
        list = []
        for pair in self.request.body.split('&') :
            key_value = pair.split('=')
            list += [{
                'key': key_value[0],
                'value': key_value[1]
            }]
        return list

    def compile_links( self ) :
        links = {}
        for link in self.get_post_list() :
            link_definition = link.get('key').split('--')
            if link_definition[0] == 'link' :
                if link_definition[1] not in links :
                    links[link_definition[1]] = {
                        'references': []
                    }
                if link_definition[-1] == 'value':
                    continue
                if link_definition[-1] == 'origin':
                    links[link_definition[1]]['origin'] = link_definition[2]
                    continue
                value = ''
                for link_value in self.get_post_list():
                    link_value_definition = link_value.get('key').split('--')
                    if link_value_definition[-1] != 'value' :
                        continue
                    if link_value_definition[:2] != link_definition[:2] :
                        continue
                    if link.get('value') == link_value_definition[3] :
                        value = link_value.get('value')
                links[link_definition[1]]['references'] += [{
                    'model': link_definition[2],
                    'id': link.get('value'),
                    'value': value
                }]
        return links

class PublicHandler(MyHandler):

    def get(self):
        cookie = self.get_cookie('user')
        if cookie != None:
            self.redirect('/article')
        page_data = {
            'users': user.select()
        }
        self.output("anon", page_data)

    def post(self) :
        post = self.get_post_list()

        for field in post :
            if field.get( 'key' ) != 'id':
                continue
            selected_user = user.select().where( user.id == field.get('value') )[0]
            self.set_cookie( 'user', str(selected_user.id) )
            self.redirect('/article')

class ArticleHandler(MyHandler):

    def get(self, model = None, id = -1):
        if self.get_cookie('user') == None :
            self.redirect('/')
            return
        if model == None :
            model = "continent"
        model = self.database.get_model(model)
        links = self.database.get_links_by_model(model)
        page_data = {
            'model': model,
            'links': links,
            'handler': self
        }
        if id == -1:
            instances = model.select()
            page_data['instances'] = instances
        else :
            instance = model.select().where(model.id == id)
            page_data['instances'] = instance
        if os.path.isfile("public/templates/models/" + model.__name__) :
            self.output("models/" + model.__name__, page_data)
            return
        self.output("models/default", page_data)

class AdminHandler(MyHandler):

    def get(self):
        page_data = self.get_data()
        self.output("admin", page_data)

    def post(self) :
        model_name = self.get_argument('model')
        model = self.database.get_model(model_name)

        dict = {}
        for key in model._meta.get_field_names() :
            value = self.get_argument(key)
            if value != '':
                dict[key] = value
            if value == 'null':
                dict[key] = None
        if dict.get('id') != None :
            instances = model.select().where(model.id==dict.get('id'))
            instance = instances[0]
            for key, value in dict.items() :
                setattr(instance,key,value)
            instance.save()
            for model_name, definition in self.compile_links().items() :
                link_model = self.database.get_link(model_name)
                target_model = link_model.get_link_model(model)
                delete_stmt = 'DELETE FROM ' + link_model.__name__.lower() + ' WHERE ' + target_model.__name__ + definition.get('origin') + '_id = ' + instance.id
                query = link_model.raw( delete_stmt )
                query.execute()
                self.save_links( instance, definition, link_model )
        else :
            instance = model.create(**dict)
            instance.save()
            for model, definition in self.compile_links().items() :
                link_model = self.database.get_link(model)
                self.save_links( instance, definition, link_model )
        self.redirect('/admin?form-success=' + model_name)

    def save_links( self, instance, definition, link_model ) :
        for reference in definition.get('references') :
            reference_id = reference.get('id')
            if reference_id == '' :
                continue
            link_instance = link_model.create()
            setattr(link_instance,definition.get('origin') + reference.get('model'),reference.get('id'))
            setattr(link_instance,reference.get('model') +definition.get('origin'),instance.id)
            setattr(link_instance,'value',reference.get('value'))
            link_instance.save()

    def get_data( self ) :
        page_data = {
            'models': {},
            'links': {},
            'content': {},
            'content_links': {},
            'handler': self
        }
        #page_data['models'] = self.database.models
        for model in self.database.models :
            page_data['models'][model.__name__] = model
        for link in self.database.links :
            page_data['links'][link.__name__] = link
        for model in self.database.models :
            page_data['content'][model.__name__] = []
            instances = model.select()
            for instance in instances :
                page_data['content'][model.__name__].append(instance)
        for link in self.database.links :
            page_data['content_links'][link.__name__] = []
            instances = link.select()
            for instance in instances :
                page_data['content_links'][link.__name__].append(instance)
        return page_data

class UserHandler(MyHandler):

    def get(self):
        if self.get_cookie('user') == None :
            self.redirect('/')
            return
        user_json = {}
        if self.current_user.json != None :
            user_json = json.loads( self.current_user.json )
        page_data = {
            'user': self.current_user,
            'json': user_json
        }
        self.output("user", page_data)

    def post(self) :
        post = self.get_post_list()
        user_json = {}
        if self.current_user.json != None :
            user_json = json.loads( self.current_user.json )
        for field in post :
            user_json[field.get('key')] = field.get('value')
        user_json = json.dumps( user_json )
        self.current_user.json = user_json
        self.current_user.save()
