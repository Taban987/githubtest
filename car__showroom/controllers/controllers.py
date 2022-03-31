# -*- coding: utf-8 -*-
# from odoo import http


# class CarShowroom(http.Controller):
#     @http.route('/car__showroom/car__showroom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car__showroom/car__showroom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('car__showroom.listing', {
#             'root': '/car__showroom/car__showroom',
#             'objects': http.request.env['car__showroom.car__showroom'].search([]),
#         })

#     @http.route('/car__showroom/car__showroom/objects/<model("car__showroom.car__showroom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car__showroom.object', {
#             'object': obj
#         })
