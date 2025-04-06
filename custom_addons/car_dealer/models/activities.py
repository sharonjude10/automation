from odoo import api, fields, models


class CarActivities(models.Model):
    _name = 'car.activities'
    _description = 'The Car Service'
    #_order = 'sequence,id'


    activity_name = fields.Char(string="Works Done", required=True)

