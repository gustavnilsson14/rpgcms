import peewee
from customfields import *
from peewee import *
from playhouse.migrate import *
from playhouse.shortcuts import model_to_dict

db = MySQLDatabase('rpg', user='rpg', passwd='rpggpr')
migrator = MySQLMigrator(db)

class MyPeeweeModel(peewee.Model):

    @staticmethod
    def is_link() :
        return False

    @staticmethod
    def display_name(plural=True) :
        return "Not implemented"

    def fields(self, include_id = 0) :
        dict = {}
        for field in self.__class__._meta.get_field_names() :
            if field == 'id' and include_id == 0 :
                continue
            dict[field] = self.__dict__.get('_data').get(field)
        return dict

    @staticmethod
    def get_element(field) :
        element = {
            'key': field[0],
            'element': '',
            'related_name': '',
        }
        if type(field[1]) is peewee.TextField :
            element['element'] = 'input'
        elif type(field[1]) is TextAreaField :
            element['element'] = 'textarea'
        elif type(field[1]) is PositionFieldX :
            element['element'] = 'map'
        elif type(field[1]) is PositionFieldY :
            element['element'] = 'map_hidden'
        elif type(field[1]) is peewee.ForeignKeyField :
            element['element'] = 'select'
            element['related_name'] = field[1].related_name
        elif type(field[1]) is OptionField :
            element['element'] = 'option'
        elif type(field[1]) is peewee.IntegerField :
            element['element'] = 'integer'
        elif type(field[1]) is JsonField :
            element['element'] = 'json'
        return element

    @staticmethod
    def is_foreign(model,key) :
        if type( getattr(model, key) ) is peewee.ForeignKeyField :
            return True
        return False

    @staticmethod
    def related_names() :
        return []

    @staticmethod
    def get_options(field) :
        return []

    @staticmethod
    def printmestatic(s = "") :
        if s != "" :
            print s
            return

    @staticmethod
    def typeof(object = None) :
        return type(object).__name__

    def printme(self, s = "") :
        if s != "" :
            print s
            return
        print self.__dict__

    class Meta:
        database = db

class MyModel(MyPeeweeModel):

    id = peewee.PrimaryKeyField()
    name = peewee.TextField()
    description = TextAreaField()

    @staticmethod
    def is_link() :
        return False

    @staticmethod
    def show_links() :
        return True

    @staticmethod
    def compare_selected(field_value, option) :
        if option == None :
            return False
        if field_value == "" or field_value == None:
            return False
        return ( field_value.id == option.id )

    @staticmethod
    def field_display_name(field_name) :
        if field_name == 'name':
            return 'Namn'
        if field_name == 'description':
            return 'Beskrivning'
        if field_name == 'pos_x':
            return 'Longitud'
        if field_name == 'pos_y':
            return 'Latitud'
        return field_name[0].upper() + field_name[1:]

    @classmethod
    def filter_link_instance_by_type(cls, instance) :
        if hasattr(instance,'type') == False :
            return True
        if instance.show_for_class(cls) == True :
            return True
        return False

    def get_links( self, link_model ) :
        links = []
        for link in getattr( self, link_model.__name__ + self.__class__.__name__ ) :
            links += [ getattr( link, self.__class__.__name__ + link_model.__name__ ).id ]
        return links

    def parse_related_links( self, model, link_model, link_list ) :
        related_links = []
        for link in link_list :
            if model in link.related_models() :
                if self.id == link.__dict__.get('_data').get( link_model.__name__ + model.__name__ ) :
                    related_links += [link]
        return related_links

    def show_for_class( self, cls ) :
        return True

    def available_for_user( self, handler ) :
        user = handler.current_user
        if hasattr( self, "knowledge" + self.__class__.__name__ ) == False:
            return True
        required_knowledge = getattr( self, "knowledge" + self.__class__.__name__ )
        if hasattr( user, "knowledgeuser" ) == False :
            return False
        user_knowledge = getattr( user, "knowledgeuser" )
        for required_knowledge_link in required_knowledge :
            for knowledge_link in user_knowledge :
                if knowledge_link.userknowledge.id == getattr( required_knowledge_link, self.__class__.__name__ + "knowledge" ).id :
                    if knowledge_link.value >= required_knowledge_link.value :
                        return True
                    else :
                        return False
        return False

class MyLink(MyPeeweeModel):

    id = peewee.PrimaryKeyField()
    value = TextAreaField(null=True)

    @staticmethod
    def is_link() :
        return True

    @staticmethod
    def related_models() :
        return []

    @classmethod
    def get_link_model(cls, calling_model) :
        for model in cls.related_models():
            if model != calling_model :
                return model

class user(MyModel) :

    player = peewee.TextField()
    json = JsonField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Spelarpersoner"
        return "Spelarperson"

    @staticmethod
    def field_display_name(field_name) :
        print field_name
        if field_name == 'player' :
            return 'Spelare'
        return MyModel.field_display_name(field_name)
