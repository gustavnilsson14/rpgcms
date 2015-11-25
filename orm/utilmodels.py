#!/usr/bin/env python
# -*- coding: utf-8 -*-

import peewee
from customfields import *
from ormcore import *
import hashlib

class user(MyPeeweeModel):

    character = TextAreaField()
    password = peewee.TextField()
    session = peewee.TextField()
    cookie = peewee.TextField()

    @staticmethod
    def display_name(plural=True) :
        if plural :
            return "Användare"
        return "Användare"

    def set_password( self, password ) :
        self.password = hashlib.md5( password ).hexdigest()

    def compare_passwords( self, password ) :
        if self.password == hashlib.md5( password ).hexdigest() :
            return True
        return False
