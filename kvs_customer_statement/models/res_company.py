from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    company_stamp = fields.Image(
        string='Company Stamp',
        max_width=512, max_height=512,
        help="Company stamp printed at the bottom of the Customer Statement.",
    )
