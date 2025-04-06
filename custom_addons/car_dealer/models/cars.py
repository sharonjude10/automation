from odoo import api, fields, models


class CarCollection(models.Model):
    _name = 'car.collection'
    _description = 'The Car Collection'
    _inherit = ['mail.thread']

    name = fields.Char(string="Model", required=True, tracking=True)
    color_ids = fields.Many2many('car.color', 'car_color_rel', 'car_id', 'color_id', string='Color',  tracking=True)
    price = fields.Float(string="Price", required=True, tracking=True, digits=(7, 2)) #digits=(precision, scale)
    fuel_type = fields.Selection([('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')],
                                 required=True, string="Fuel", tracking=True)
    build_date = fields.Date(string="Manufactured Date", default='2024-01-01', tracking=True)
    # count = fields.Integer(string='Units', required=True, compute='_compute_car_count', store=True)