from google.appengine.ext import ndb

class Player(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

class Location(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()
    exits = ndb.KeyProperty("Exit")

class Exit(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()
    target_loc = ndb.KeyProperty("Location")
    command = ndb.TextProperty()



