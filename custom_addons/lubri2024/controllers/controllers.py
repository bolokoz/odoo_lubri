# -*- coding: utf-8 -*-
# from odoo import http


# class Lubri2024(http.Controller):
#     @http.route('/lubri2024/lubri2024', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lubri2024/lubri2024/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lubri2024.listing', {
#             'root': '/lubri2024/lubri2024',
#             'objects': http.request.env['lubri2024.lubri2024'].search([]),
#         })

#     @http.route('/lubri2024/lubri2024/objects/<model("lubri2024.lubri2024"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lubri2024.object', {
#             'object': obj
#         })
