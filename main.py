#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# user inputs commands, client sends them off, gets response, appends it to content pane.


import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

from models import Player, Location, Exit

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

USERS = { } # user_id : location




class TextRequestHandler(webapp2.RequestHandler):
    def look(self):
        self.response.write("Name: "+self.request.current_location.name+"</br>")
        self.response.write("Desc: "+self.request.current_location.description+"</br>")
        exit = self.request.current_location.exits.get()
        self.response.write("&nbsp;Exit:"+exit.description+"("+exit.command+")"+"</br>")

    def get(self):
        location_key = ndb.Key('Location', 'HomeBase')
        exit_key = ndb.Key('Exit', 'HomeBase')


        # LOCATION_MAP = [ home_base, kitchen]
        command = self.request.get("command")

        exit = Exit(name="exit", description="exit desc", command="go exit")
        exit_key= exit.put()
        home_base = Location(name="asd", description="DESC", exits=exit_key)
        exit = exit_key.get()
        home_key = home_base.put()
        exit.target_loc = home_key
        exit_key = exit.put()


        user = users.get_current_user() #is this supposed to be None?

        if user is None:
            self.response.write('Please log in to continue...')
            self.response.headers['Content-Type'] = 'text/plain'
            return

        self.response.write('>> ' + command + "<br>")

        if None not in USERS:
            #set up initial user
            USERS[None] = home_base
            current_location = home_base
        else:
            current_location = USERS[None]

        self.request.current_location = current_location
        user = users.get_current_user()
        if command == "look":
            self.look()
        exit = current_location.exits.get()
        if command == exit.command:
            self.response.write("Changing location")
            USERS[None] = exit.target_loc.get()
            self.request.current_location = exit.target_loc.get()
            self.look()

        self.response.headers['Content-Type'] = 'text/plain'

    def post(self):
        user = users.get_current_user()

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('what up')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template = JINJA_ENVIRONMENT.get_template('templates/landing.html')
        self.response.write(template.render({'login_url': users.create_login_url('/'), 'logout_url':users.create_logout_url('/'), 'current_user': user}))

app = webapp2.WSGIApplication([
    ('/test', TextRequestHandler),
    ('/', MainHandler)
], debug=True)
