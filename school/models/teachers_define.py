from odoo import models, api, fields


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"
    first_name = fields.Char("First Name")
    middle_name = fields.Char("Middle Name")
    last_name = fields.Char("Last Name")
    # Gender = fields.Selection("Male")
    Gender = fields.Selection([('Female', 'Male'), ('away', 'Male'), ('offline', 'Male')], 'Gender',
                              default='Female')
    date_of_birth = fields.Date("date")
    national_id = fields.Char("National Id")


class TeachersModule(models.Model):
    _name = "teachers.details"
    name = fields.Char("Name")
    subject = fields.Char("Branch")
    cnic = fields.Integer("Cnic")
    location = fields.Char("Location")
    city = fields.Char("City")
    type = fields.Char("Type")