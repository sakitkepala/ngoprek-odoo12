# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class openacademy(models.Model):
  # _name = 'openacademy.openacademy'

  # name = fields.Char()
  # value = fields.Integer()
  # value2 = fields.Float(compute="_value_pc", store=True)
  # description = fields.Text()

  # @api.depends('value')
  # def _value_pc(self):
  #     self.value2 = float(self.value) / 100

class Course(models.Model):
  _name = 'openacademy.course'
  _description = "Kelas-Kelas Open Academy"

  name = fields.Char(string='Title', required=True)
  description = fields.Text()

class Session(models.Model):
  _name = 'openacademy.session'
  _description = "Sesi-sesi Open Academy"

  name = fields.Char(required=True)
  start_date = fields.Datetime()
  duration = fields.Float(digits=(6,2), help="Durasi dalam hari")
  seats = fields.Integer(string="Jumlah kursi")
