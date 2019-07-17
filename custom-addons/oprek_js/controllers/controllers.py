# -*- coding: utf-8 -*-
from odoo import http

# class OprekJs(http.Controller):
#     @http.route('/oprek_js/oprek_js/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oprek_js/oprek_js/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oprek_js.listing', {
#             'root': '/oprek_js/oprek_js',
#             'objects': http.request.env['oprek_js.oprek_js'].search([]),
#         })

#     @http.route('/oprek_js/oprek_js/objects/<model("oprek_js.oprek_js"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oprek_js.object', {
#             'object': obj
#         })