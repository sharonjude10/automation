from odoo import api, fields, models


class Customers(models.Model):
    _name = 'car.customer'
    _description = 'The Car Customers'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    age = fields.Integer(string='Age')
    contact = fields.Char(string='Contact Number', required=True)
    address = fields.Text(string='Address')