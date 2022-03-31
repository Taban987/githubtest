from odoo import models, api, fields


class CourseModule(models.Model):
    _name = "course.details"
    name = fields.Char("Name")
    credit_hours = fields.Char("Credit Hours")
    fee = fields.Char("Fee")
    program = fields.Char("program")
