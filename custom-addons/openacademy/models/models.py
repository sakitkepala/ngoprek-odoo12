# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

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

  _sql_constraints = [
    ('check_name_description',
    'CHECK(name != description)',
    "Judulnya gak boleh sama deskripsinya"),

    ('name_unique',
    'UNIQUE(name)',
    "Judul pelajaran harus unik"),
  ]

class Session(models.Model):
  _name = 'openacademy.session'
  _description = "Sesi-sesi Open Academy"

  name = fields.Char(required=True)
  start_date = fields.Date(default=fields.Date.today)
  duration = fields.Float(digits=(6,2), help="Durasi dalam hari")
  seats = fields.Integer(string="Jumlah kursi")
  active = fields.Boolean(default=True)

  instructor_id = fields.Many2one('res.partner', string="Instructor",
    domain=['|',('instructor', '=', True),
      ('category_id.name', 'ilike', "Teacher")])
  course_id = fields.Many2one('openacademy.course',
    ondelete='cascade', string="Course", required=True)
  attendee_ids = fields.Many2many('res.partner', string="Peserta")

  taken_seats = fields.Float(string="Kursi yang sudah diambil", compute='_taken_seats')

  # dekorator depends() ini dipakai ketika nilai field kompyutednya
  # tergantung dari nilai field lain yang ada
  # di bawah ini contohnya tergantung pada field seats & attendee_ids
  @api.depends('seats', 'attendee_ids')
  def _taken_seats(self):
    # for loop ini agar SEMUA RECORD
    # dengan field taken_seats ini kena pengaruh kompyuted-nya
    for rec in self:
      if not rec.seats:
        rec.taken_seats = 0.0
      else:
        rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats

  @api.onchange('seats','attendee_ids')
  def _verify_valid_seats(self):
    if self.seats < 0:
      return {
        'warning': {
          'title': "Nilai 'seats' keliru",
          'message': "Jumlah kursi tersedia tidak boleh negatif",
        },
      }
    if self.seats < len(self.attendee_ids):
      return {
        'warning': {
          'title': "Terlalu banyak pesertanya",
          'message': "Naikkan jumlah kursinya atau kurangi kelebihan pesertanya",
        },
      }

  @api.constrains('instructor_id', 'attendee_ids')
  def _check_instructor_not_in_attendees(self):
    for rec in self:
      if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
        raise exceptions.ValidationError("Instruktor tidak bisa peserta")
