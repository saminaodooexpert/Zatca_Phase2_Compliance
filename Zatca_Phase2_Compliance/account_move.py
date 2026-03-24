Python
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        for move in self:
            if move.move_type in ['out_invoice', 'out_refund']:
                if not move.partner_id.vat:
                    raise UserError(_("ZATCA Phase 2: Customer VAT is required for Tax Invoices."))
                if not move.partner_id.street:
                    raise UserError(_("ZATCA Phase 2: Customer Address (Street) is required."))
        return super(AccountMove, self).action_post()
