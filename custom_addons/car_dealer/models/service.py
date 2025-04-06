from odoo import api, fields, models

class CarService(models.Model):
    _name = 'car.service'
    _description = 'The Car Service Model'

    customer_id = fields.Many2one('car.sale',string='Customer')
    car_id = fields.Many2one('car.collection', string='Model')
