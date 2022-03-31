# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class haditech(models.Model):
#     _name = 'haditech.haditech'
#     _description = 'haditech.haditech'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class MinimalModel(models.Model):
    _name = 'employees.data'
    name =fields.Char(string="Employee Name", required=True)
    email = fields.Char(required=True)
    phone=fields.Char()




