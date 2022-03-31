from odoo import models, api, fields


class SchoolModule(models.Model):
    _name = "school.details"
    name = fields.Char("Name")
    location = fields.Char("Location")
    branch = fields.Char("Branch")
    program = fields.Char("program")
    city = fields.Char("City")
    type = fields.Char("Type")
