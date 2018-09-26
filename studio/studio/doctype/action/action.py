# -*- coding: utf-8 -*-
# Copyright (c) 2018, Maxwell Morais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from uuid import uuid4

class Action(Document):
	def autoname(self):
		self.name = str(uuid4())
