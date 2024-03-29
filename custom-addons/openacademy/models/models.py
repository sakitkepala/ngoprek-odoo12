# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, exceptions, _

class Course(models.Model):
  _name = 'openacademy.course'
  _description = "Pelajaran-Pelajaran Open Academy"

  name = fields.Char(string='Title', required=True)
  description = fields.Text()

  responsible_id = fields.Many2one('res.users',
    ondelete='set null', string="Responsible", index=True)
  session_ids = fields.One2many(
    'openacademy.session', 'course_id', string="Sesi-Sesi")
  
  @api.multi
  def copy(self, default=None):
    default = dict(default or {})

    copied_count = self.search_count(
      [('name', '=like', _(u"Copy of {}").format(self.name))]
    )
    if not copied_count:
      new_name = _(u"Copy of {}").format(self.name)
    else:
      new_name = _(u"Copy of {} ({})").format(self.name, copied_count)

    default['name'] = new_name
    return super(Course, self).copy(default)

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
  color = fields.Integer()

  instructor_id = fields.Many2one('res.partner', string="Instructor",
    domain=['|',('instructor', '=', True),
      ('category_id.name', 'ilike', "Teacher")])
  course_id = fields.Many2one('openacademy.course',
    ondelete='cascade', string="Course", required=True)
  attendee_ids = fields.Many2many('res.partner', string="Peserta")

  taken_seats = fields.Float(string="Kursi yang sudah diambil", compute='_taken_seats')

  end_date = fields.Date(string="Tanggal berakhir", store=True,
    compute='_get_end_date', inverse='_set_end_date')
  
  attendees_count = fields.Integer(
    string="Jumlah Peserta", compute='_get_attendees_count', store=True)

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
          'title': _("Nilai 'seats' keliru"),
          'message': _("Jumlah kursi tersedia tidak boleh negatif"),
        },
      }
    if self.seats < len(self.attendee_ids):
      return {
        'warning': {
          'title': _("Terlalu banyak pesertanya"),
          'message': _("Naikkan jumlah kursinya atau kurangi kelebihan pesertanya"),
        },
      }

  @api.constrains('instructor_id', 'attendee_ids')
  def _check_instructor_not_in_attendees(self):
    for rec in self:
      if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
        raise exceptions.ValidationError(_("Instruktor tidak bisa peserta"))

  @api.depends('start_date', 'duration')
  def _get_end_date(self):
    for rec in self:
      if not (rec.start_date and rec.duration):
        rec.end_date = rec.start_date
        continue

      duration = timedelta(days=rec.duration, seconds=-1)
      rec.end_date = rec.start_date + duration

  def _set_end_date(self):
    for rec in self:
      if not (rec.start_date and rec.end_date):
        continue

      duration = (rec.end_date - rec.start_date).days + 1

  @api.depends('attendee_ids')
  def _get_attendees_count(self):
    for rec in self:
      rec.attendees_count = len(rec.attendee_ids)
