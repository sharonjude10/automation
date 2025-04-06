from odoo import api, fields, models


class CarPurchase(models.Model):
    _name = 'car.sale'
    _description = 'The Purchased Cars'
    _rec_names_search = ['reference', 'customer_id']
   # _rec_name = 'customer_id'

    reference = fields.Char(string="Reference", default="New")
    customer_id = fields.Many2one('car.customer', string='Customer Name')
    contact = fields.Char(related='customer_id.contact', string='Contact')
    car_id = fields.Many2one('car.collection', string='Car')
    cost = fields.Float(related='car_id.price', string='Price')
    tax = fields.Float(compute='_compute_car_tax', string='Tax (5%)')
    total_cost = fields.Float(compute='_compute_car_cost', string='Ex-showroom Price')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'),
                              ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft', tracking=True)

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.customer_id.name} : {rec.reference}"

    @api.model_create_multi
    def create(self, va_list):
        for va in va_list:
            if not va.get('reference') or va['reference'] == 'New':
                va['reference'] = self.env['ir.sequence'].next_by_code('car.sale')
        return super().create(va_list)

    @api.depends('car_id') #trigger a recomputation, if we change the car name
    def _compute_car_tax(self):
        for rec in self:
            rec.tax = rec.car_id.price * 0.05

    @api.depends('car_id') #trigger a recomputation, if we change the car name
    def _compute_car_cost(self):
        for rec in self:
            rec.total_cost = rec.cost + rec.tax

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'