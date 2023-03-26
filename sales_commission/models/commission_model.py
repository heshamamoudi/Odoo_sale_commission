# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleCommission(models.Model):
    _name = 'sales.commission'


class salesCommissionSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sales_commission_setting = fields.Selection([
        ('payment', 'Customer Invoice Payment'),
        ('order', 'Order Confirm'),
        ('invoice', 'Invoice Confirm')
    ], default='payment', string="Commission Method",
        help="By picking the method generating commissions will be based on the picked method either on order confirm / invoice confirm / invoice registering payment")

    commission_calc = fields.Selection([
        ('team', 'Sales Team'),
        ('category', 'Product Category'),
        ('product', 'Product')
    ], default='team', string="Commission Calculation Method",
        help="By picking the calculating method generating commissions will be based on the picked method either on Sales Team / Product Category / Product")

    def set_values(self):
        res = super(salesCommissionSettings, self).set_values()
        if self.sales_commission_setting != 'payment':
            self.env['ir.config_parameter'].set_param('sales_commission.sales_commission_setting',
                                                      self.sales_commission_setting)
        if self.commission_calc != 'team':
            self.env['ir.config_parameter'].set_param('sales_commission.commission_calc',
                                                      self.commission_calc)
        return res

    @api.model
    def get_values(self):
        res = super(salesCommissionSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        commission_method = ICPSudo.get_param('sales_commission.sales_commission_setting')
        commission_method1 = ICPSudo.get_param('sales_commission.commission_calc')
        res.update(
            sales_commission_setting=commission_method,
            commission_calc=commission_method1
        )
        return res

