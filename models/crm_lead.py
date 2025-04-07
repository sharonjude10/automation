from odoo import models,fields,api

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    # recent_cc = fields.Char('Recent Cc')
    recent_cc = fields.Char('Recent Cc', compute="_compute_recent_cc", store=True,readonly=False)


#both code works it searches if the contact exists using email and if contact exists then add it to recent cc
    # @api.depends('email_cc')
    # def _compute_recent_cc(self):
    #     print("calleddddddddd")
    #     for lead in self:
    #         if lead.email_cc:
    #             email_list = []
    #             formatted_cc_emails = lead._extract_email_addresses(lead.email_cc)
    #             print(formatted_cc_emails,"eamilsss")
    #             contacts = self.env['res.partner'].search([('email', 'in', formatted_cc_emails)])
    #             print(contacts,"contacts")
    #             email_list = contacts.mapped('email')
    #             lead.recent_cc = ','.join(email_list) if email_list else ''
    #
    # def _extract_email_addresses(self, email_cc_str):
    #     """Extracts email addresses from a string like: 'Name <email@example.com>'"""
    #     email_list = []
    #     if email_cc_str:
    #         email_parts = email_cc_str.split(',')
    #         for email in email_parts:
    #             email = email.strip()
    #             if '<' in email and '>' in email:
    #                 email = email.split('<')[1].split('>')[0]
    #             email_list.append(email)
    #     return email_list

    @api.depends('email_cc')
    def _compute_recent_cc(self):
        print("called _compute_recent_cc")
        for lead in self:
            if lead.email_cc:
                formatted_cc_emails = lead._extract_email_addresses(lead.email_cc)
                print(formatted_cc_emails, "emails")

                lead.recent_cc = ','.join(formatted_cc_emails) if formatted_cc_emails else ''
            else:
                lead.recent_cc = ''

    def _extract_email_addresses(self, email_cc_str):
        """Extracts email addresses from a string like: 'Name <email@example.com>'"""
        email_list = []
        if email_cc_str:
            email_parts = email_cc_str.split(',')
            for email in email_parts:
                email = email.strip()
                if '<' in email and '>' in email:
                    email = email.split('<')[1].split('>')[0]
                email_list.append(email)
        return email_list
