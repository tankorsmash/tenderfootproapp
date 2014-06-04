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

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class TextRequestHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('>> ' + self.request.get("name"))

	def post(self):
		user = users.get_current_user()

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('what up')

class MainHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()

		if user:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write('Hello, ' + user.nickname())
		else:
			template = JINJA_ENVIRONMENT.get_template('templates/landing.html')
			self.response.write(template.render({}))

app = webapp2.WSGIApplication([
('/test', TextRequestHandler),
('/', MainHandler)
], debug=True)
