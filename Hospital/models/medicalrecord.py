# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InventoryGoods(models.Model):
    _name = "medical.record"
    _description = "Medical Record"
    patient_name = fields.Char(string='Patient Name', required=True, translate=True)
    date = fields.Date(string='Date of birth', required=True)
    age = fields.Integer('Age', required=True)
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    # ], default='male')
    gender = fields.Selection([('male', 'Male'),
                              ('female', 'Female')], default='male')
    job = fields.Char(string='Job', required=True, translate=True)
    nation = fields.Char(string='Nation', required=True, translate=True)
    address = fields.Char(string='Address', required=True, translate=True)
    workplace = fields.Char(string='Workplace', required=True, translate=True)
    object = fields.Selection([
        ('insurance', 'Health Insurance'),
        ('fee', 'Fee'),
        ('exempt', 'Exempt'),
        ('other', 'Other'),
    ], default='insurance')
    start_date = fields.Date(string='Start Date', help="Enter the start date of health insurance.")
    end_date = fields.Date(string='End Date', help="Enter the end date of health insurance.")
    note = fields.Text(string='Description of contact information')
    start_date_hospital = fields.Date(string='Hospitalized Day', help="Enter the hospital admission date.")
    end_date_hospital = fields.Date(string='Hospital Discharge Date', help="Enter the hospital discharge date.")
    department = fields.Char(string='Department', required=True)
    hospital_room = fields.Char(string='Hospital Room', required=True)
    hospital_bed = fields.Char(string='Hospital Bed', required=True)
    doctor = fields.Char(string='Doctor', required=True)
    patient_test = fields.Char(string='Patient Test', required=True)
    image = fields.Binary(string='Images')
    treatments = fields.Char(string='Treatments', required=True)
    result = fields.Selection([
        ('cured', 'Cured'),
        ('better', 'Better'),
        ('constant', 'Constant'),
        ('sicker', 'Get Sicker'),
        ('dead', 'Dead'),
    ], default='cured')