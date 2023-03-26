# -*- coding: utf-8 -*-
# from odoo import http


# class SalesCommision(http.Controller):
#     @http.route('/sales_commision/sales_commision', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_commision/sales_commision/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_commision.listing', {
#             'root': '/sales_commision/sales_commision',
#             'objects': http.request.env['sales_commision.sales_commision'].search([]),
#         })

#     @http.route('/sales_commision/sales_commision/objects/<model("sales_commision.sales_commision"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_commision.object', {
#             'object': obj
#         })
