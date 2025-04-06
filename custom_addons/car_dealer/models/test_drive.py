from odoo import api, fields, models


class TestDrive(models.Model):
    _name = 'test.drive'
    _description = 'Test Drive Customers'

    customer_id = fields.Many2one('car.customer', string='Customer')
    car_id = fields.Many2one('car.collection', string='Car')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'),
                              ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft', tracking=True)
    booking_date = fields.Date(string='Booking Date')
    contact = fields.Char(related='customer_id.contact', store=True)


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