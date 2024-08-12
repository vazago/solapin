# -*- coding: utf-8 -*-
from odoo import http

# class GduBase(http.Controller):
#     @http.route('/gdu_base/gdu_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gdu_base/gdu_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gdu_base.listing', {
#             'root': '/gdu_base/gdu_base',
#             'objects': http.request.env['gdu_base.gdu_base'].search([]),
#         })

#     @http.route('/gdu_base/gdu_base/objects/<model("gdu_base.gdu_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gdu_base.object', {
#             'object': obj
#         })