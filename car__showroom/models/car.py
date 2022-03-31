# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields, api


class car_showroom(models.Model):
    _name = "car.data"
    name = fields.Char("Name")
    manufacturer = fields.Char("Manufacturer")
    model = fields.Char("Car Model")
    number_plate = fields.Char("Number Plate")
    color = fields.Char("Color")
    price=fields.Char("Price")
# class car__showroom(models.Model):
#     _name = 'car__showroom.car__showroom'
#     _description = 'car__showroom.car__showroom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
