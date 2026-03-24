Python
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        for move in self:
            # Check if it is a Saudi Customer Invoice
            if move.move_type in ['out_invoice', 'out_refund'] and move.company_id.country_id.code == 'SA':
                
                # 1. VAT Number must be 15 digits
                if not move.company_id.vat or len(move.company_id.vat) != 15:
                    raise ValidationError(_("ZATCA Error: Company VAT number must be exactly 15 digits."))

                # 2. Building Number (Street 2) must be 4 digits
                if not move.company_id.street2 or not re.match(r'^\d{4}$', move.company_id.street2):
                    raise ValidationError(_("ZATCA Error: Building Number (Street 2) must be 4 digits."))

                # 3. Postal Code must be 5 digits
                if not move.company_id.zip or len(move.company_id.zip) != 5:
                    raise ValidationError(_("ZATCA Error: Postal Code must be 5 digits."))

        return super(AccountMove, self).action_post()
