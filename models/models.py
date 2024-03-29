#!/usr/bin/env python

from google.appengine.ext import ndb
from datetime import date

DEFAULT_GUESTBOOK_NAME = date(2011,12,12)

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
	"""Constructs a Datastore key for a Guestbook entity with guestbook_name."""
	return ndb.Key('Guestbook', guestbook_name)

class Greeting(ndb.Model):
	"""Models an individual Guestbook entry."""
    
	author = ndb.UserProperty()
	content = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)

#########################

class Bed(ndb.Model):
	"""Models an individual Guestbook entry."""
	room = ndb.StringProperty()
	number = ndb.IntegerProperty()	
	
class Guest(ndb.Model):
	"""Models an individual Guestbook entry."""
	name = ndb.StringProperty()
	nationality = ndb.StringProperty()
	birthday = ndb.DateTimeProperty()

	
class Booking(ndb.Model):
	"""Models an individual Guestbook entry."""
	check_in_date = ndb.DateProperty(auto_now_add=True)
	check_out_date = ndb.DateProperty(auto_now_add=True)
	price = ndb.IntegerProperty()
	bed = ndb.StructuredProperty(Bed)
	guest = ndb.StructuredProperty(Guest)