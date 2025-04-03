from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('invoice_line_ids')
    def _apply_rg5329_tax(self):
        threshold = 3000.0
        tax = self.env.ref('rg5329_tax_module.tax_rg5329_pais_25', raise_if_not_found=False)
        if not tax:
            return
        total_tax = sum(line.price_total - line.price_subtotal for line in self.invoice_line_ids)
        for line in self.invoice_line_ids:
            if total_tax > threshold and line.product_id.apply_rg5329:
                if tax not in line.tax_ids:
                    line.tax_ids += tax
            else:
                if tax in line.tax_ids:
                    line.tax_ids -= tax
