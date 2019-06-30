from odoo import models, fields, api

class CarRequest(models.Model):
  _name = 'car.request'
  _description = 'Car Request'

  name = fields.Char(string='Request', required=True)
  date_from = fields.Datetime(string='Starting Date', default=fields.Datetime.now())
  date_to = fields.Datetime(string='End Date', required=False)
  employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', required=True)
  car_id = fields.Many2one(comodel_name='fleet.vehicle', string='Car', required=True)
  state = fields.Selection(
    string='Status',
    selection=[
      ('draft','Draft'),
      ('confirmed','Confirmed'),
      ('validated','Validated'),
      ('refused','Refused'),
      ('approved','Approved'),
    ],
    default='draft'
  )

  @api.multi
  def confirm_request(self):
    self.state = 'confirmed'

  @api.multi
  def validate_request(self):
    self.state = 'validated'

  @api.multi
  def refuse_request(self):
    self.state = 'refused'

  @api.multi
  def approve_request(self):
    self.state = 'approved'
