# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MedicineHS(models.Model):
    _name = "medicine.hs"
    name = fields.Char(string="Tên Thuốc")
    tac_dung = fields.Text(string="Tác Dụng")