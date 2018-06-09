#!/usr/bin/env python3


from person import Person


"""Representation of a account Manager"""
class Manager(Person):
	def __init__(self, id_=0, name=''):
		super.__init__(id_, name, 'M')
		#self.managed_accounts = {}