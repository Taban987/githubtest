# -*- coding: utf-8 -*-
# from odoo import http


# class Haditech(http.Controller):
#     @http.route('/haditech/haditech', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/haditech/haditech/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('haditech.listing', {
#             'root': '/haditech/haditech',
#             'objects': http.request.env['haditech.haditech'].search([]),
#         })

#     @http.route('/haditech/haditech/objects/<model("haditech.haditech"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('haditech.object', {
#             'object': obj
#         })
