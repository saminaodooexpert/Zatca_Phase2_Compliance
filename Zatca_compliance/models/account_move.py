Python
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        for move in self:
            if move.move_type in ['out_invoice', 'out_refund']:
                if not move.partner_id.vat:
                    raise UserError(_("ZATCA Phase 2 Error: Customer VAT number is missing! Please add it before confirming."))
        return super(AccountMove, self).action_post()
