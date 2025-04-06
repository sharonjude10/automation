from odoo import api,fields,models


class CarColor(models.Model):
    _name = 'car.color'
    _description = 'The Car Colors'
    _order = 'sequence,id'
    _rec_name = 'color_name' #if this not given in the drop down while choosing color tags would show like this: car.color,1
    #                                                                                                            car.color,2


    color_name = fields.Char(string="Color Name", required=True)
    sequence = fields.Integer(default=10)
