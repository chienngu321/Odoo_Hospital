# -*- coding: utf-8 -*-
import datetime

from odoo import api, fields, models, _


class MedicalRecord(models.Model):
    _name = "medical.record"
    name = fields.Char(string='HSBA', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    # code_bn = fields.Char(string='Mã Bệnh Nhân', required=True)
    code_bn = fields.Many2one('my.patients', string='Mã Bệnh Nhân')
    patient_name = fields.Char(string='Tên Bệnh Nhân', required=True, translate=True)
    bdate = fields.Date(string='Ngày Sinh', required=True)
    patient_age = fields.Char(string='Tuổi', compute="_get_age_from_patient")
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    # ], default='male')
    gender = fields.Selection([('male', 'Nam'),
                               ('female', 'Nữ')], string='Giới Tính', default='male')
    job = fields.Char(string='Nghề Nghiệp', required=True, translate=True)
    address = fields.Char(string='Địa Chỉ', required=True, translate=True)
    workplace = fields.Char(string='Nơi Làm Việc', required=True, translate=True)
    object_bn = fields.Char(string='Đối Tượng', required=True)
    khoa = fields.Many2one('hr.department', string='Khoa')
    bed_bn = fields.Char(string='Giường')
    diagnostic = fields.Text(string='Chuẩn Đoán', required=True)
    treatment = fields.Selection([
        ('nhapvien', 'Nhập Viện Điều Trị'),
        ('capcuu', 'Cấp Cứu Khẩn Cấp'),
        ('kedon', 'Kê Đơn Thuốc')
    ], string='Hướng Điều Trị', default='nhapvien')
    banthan = fields.Char('Bản Thân', required=True)
    family = fields.Char('Gia Đình', required=True)
    diungthuoc = fields.Boolean(string='Dị Ứng Thuốc')
    start_date_hospital = fields.Date(string='Ngày Khám')
    doctor = fields.Many2one('hr.employee', string='Bác Sĩ', required=True)
    qtbly = fields.Char(string='Quá Trình Bệnh Lý', required=True)
    kham = fields.Char(string='Khám Lâm Sàng', required=True)
    heart = fields.Char(string='Nhịp Tim', required=True)
    temperature = fields.Char(string='Nhiệt Độ', required=True)
    huyetap = fields.Char(string='Huyết Áp', required=True)
    nhiptho = fields.Char(string='Nhịp Thở', required=True)
    cannang = fields.Char(string='Cân Nặng', required=True)
    chieucao = fields.Char(string='Chiều Cao', required=True)
    benhkem = fields.Char(string='Bệnh Kèm Theo', required=True)
    note_sick = fields.Text(string='Mô Tả Kết Luận')
    image = fields.Binary(string='Hình Ảnh')
    medicine_lines = fields.One2many('medicine.lines', 'medicine_id')

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('medical.record') or _('New')
        res = super(MedicalRecord, self).create(vals)
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


class MedicineLines(models.Model):
    _name = "medicine.lines"
    product_id = fields.Many2one('product.template', string="Tên Thuốc")
    product_qty = fields.Char(string="Số Lượng")
    ghichu = fields.Text(string='Ghi Chú')
    medicine_id = fields.Many2one('medical.record')