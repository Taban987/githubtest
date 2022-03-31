from odoo import fields,models,api



class Employee(models.Model):
    _name = "employee.data"
    name =fields.Char(string="Employee Data")
    id = fields.Char(string="Id")
    phone = fields.Char(requried=True)
    start_date = fields.Date(string="Start Date ")
    end_date = fields.Date(string="Start Date ")
