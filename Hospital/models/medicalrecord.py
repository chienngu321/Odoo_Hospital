# -*- coding: utf-8 -*-
import datetime

from odoo import api, fields, models, _


class InventoryGoods(models.Model):
    _name = "medical.record"
    _description = "Medical Record"
    code = fields.Char(string='HSBA', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    patient_name = fields.Char(string='Patient Name', required=True, translate=True)
    bdate = fields.Date(string='Date of birth', required=True)
    patient_age = fields.Char(string='Age', compute="_get_age_from_patient")
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    # ], default='male')
    gender = fields.Selection([('male', 'Male'),
                              ('female', 'Female')], default='male')
    phone = fields.Char(string='Phone', required=True)
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
    code_object = fields.Char(string='Code BHYT', required=True)
    place = fields.Text('PLace')
    start_date = fields.Date(string='Start Date', help="Enter the start date of health insurance.")
    end_date = fields.Date(string='End Date', help="Enter the end date of health insurance.")
    cmnd = fields.Char(string='CMND', required=True)
    height = fields.Char('Height', required=True)
    weight = fields.Char('Weight', required=True)
    blood_group = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('o', 'O'),
        ('ab', 'AB')
    ], string='Blood Group', default='a')
    note = fields.Text(string='Description of contact information')
    start_date_hospital = fields.Date(string='Hospitalized Day', help="Enter the hospital admission date.")
    end_date_hospital = fields.Date(string='Hospital Discharge Date', help="Enter the hospital discharge date.")
    department = fields.Char(string='Department', required=True)
    hospital_room = fields.Char(string='Hospital Room', required=True)
    hospital_bed = fields.Char(string='Hospital Bed', required=True)
    doctor = fields.Char(string='Doctor', required=True)
    nurse = fields.Char(string='Nurse')
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
    note_sick = fields.Text(string='Description of illness information')

    @api.model
    def create(self, vals):
        if vals.get('code', ('New')) == ('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('medical.record') or _('New')
        res = super(InventoryGoods, self).create(vals)
        return res

    def _get_age_from_patient(self):
        today_date = datetime.date.today()
        for patient in self:
            if patient.bdate:
                bdate = fields.Datetime.to_datetime(patient.bdate).date()
                age = str(int((today_date - bdate).days / 365))
                patient.patient_age = age
            else:
                patient.patient_age = ""

