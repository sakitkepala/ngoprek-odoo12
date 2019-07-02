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
  _description = "Pelajaran-Pelajaran Open Academy"

  name = fields.Char(string='Title', required=True)
  description = fields.Text()

  responsible_id = fields.Many2one('res.users',
    ondelete='set null', string="Responsible", index=True)
  session_ids = fields.One2many(
    'openacademy.session', 'course_id', string="Sesi-Sesi")

class Session(models.Model):
  _name = 'openacademy.session'
  _description = "Sesi-sesi Open Academy"

  name = fields.Char(required=True)
  start_date = fields.Datetime()
  duration = fields.Float(digits=(6,2), help="Durasi dalam hari")
  seats = fields.Integer(string="Jumlah kursi")

  instructor_id = fields.Many2one('res.partner', string="Instructor",
    domain=['|',('instructor', '=', True),
      ('category_id.name', 'ilike', "Teacher")])
  course_id = fields.Many2one('openacademy.course',
    ondelete='cascade', string="Course", required=True)
  attendee_ids = fields.Many2many('res.partner', string="Peserta")
