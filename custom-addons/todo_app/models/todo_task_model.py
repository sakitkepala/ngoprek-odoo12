# -*- coding: utf-8 -*-
from odoo import fields, models

class TodoTask(models.Model):
  _name = 'todo.task'
  _description = 'To-Do Task'

  name = fields.Char(string='Description', required=True)
  is_done = fields.Boolean('Done?')
  active = fields.Boolean(string='Active?', default=True)
  user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
  teams_ids = fields.Many2many('res.partner', string='Team')
