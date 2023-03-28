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
        help="By picking the method generating commissions will be based on the picked method either on order confirm / invoice confirm / invoice registering payment",
        config_parameter="sales_commission.sales_commission_setting")

    commission_calc = fields.Selection([
        ('team', 'Sales Team'),
        ('category', 'Product Category'),
        ('product', 'Product')
    ], default='team', string="Commission Calculation Method",
        help="By picking the calculating method generating commissions will be based on the picked method either on Sales Team / Product Category / Product",
        config_parameter="sales_commission.commission_calc")

    sale_manager_comm = fields.Float(string="Sales Manager Commission (%)",
                                     help="By setting the percentage of the Commission; Sales Manager Commission will get calculated base on it",
                                     default=1, config_parameter="sales_commission.sale_manager_comm")
    sale_person_comm = fields.Float(string="Sales Person Commission (%)",
                                    help="By setting the percentage of the Commission; Sales Person Commission will get calculated base on it",
                                    default=1, config_parameter="sales_commission.sale_person_comm")
