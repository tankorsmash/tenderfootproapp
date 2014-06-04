class Player(db.Model):
	name = db.StringProperty()
	description = db.TextProperty()
	created = db.DateTimeProperty(auto_now_add=True)

class Room(db.Model):
	name = db.StringProperty()
	description = db.TextProperty()

