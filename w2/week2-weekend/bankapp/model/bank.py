#!/usr/bin/env python3


from branch import Branch


"""Representation of a Bank"""
class Bank():
	def __init__(self, id_=0, name="", branches={}):
		self.id = id_
		self.name = name
		self.branches = branches


	def add_branch(self, branch):
		self.branches[branch.id] = branch


	def branch_exists(self, branch_id):
		return branch_id in self.branches
