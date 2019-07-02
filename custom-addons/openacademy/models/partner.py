from odoo import models, fields

class Partner(models.Model):
  _inherit = 'res.partner'

  # nambah field instructor pada model res.partner
  instructor = fields.Boolean("Instructor", default=False)

  # nambah field session_ids yang berelasi (many to many) dengan
  # model openacademy.session
  session_ids = fields.Many2many('openacademy.session',
    string="Sesi-sesi yang dihadiri", readonly=True)
