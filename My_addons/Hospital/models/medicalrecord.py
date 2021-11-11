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
    object_bn = fields.Selection([
        ('dv', 'Dịch Vụ'),
        ('hn', 'Hộ Nghèo'),
    ], string='Đối Tượng', default='dv')
    khoa = fields.Many2one('hr.department', string='Khoa')
    bed_bn = fields.Many2one('product.template', string='Giường')
    diagnostic = fields.Text(string='Chuẩn Đoán', required=True)
    treatment = fields.Selection([
        ('nhapvien', 'Nhập Viện Điều Trị'),
        ('capcuu', 'Cấp Cứu Khẩn Cấp'),
        ('kedon', 'Kê Đơn Thuốc')
    ], string='Hướng Điều Trị', default='nhapvien')
    banthan = fields.Char('Bản Thân', required=False)
    family = fields.Char('Gia Đình', required=False)
    diungthuoc = fields.Boolean(string='Dị Ứng Thuốc')
    start_date_hospital = fields.Date(string='Ngày Khám', required=True)
    doctor = fields.Many2one('hr.employee', string='Bác Sĩ', required=True)
    qtbly = fields.Char(string='Quá Trình Bệnh Lý', required=True)
    kham = fields.Char(string='Khám Lâm Sàng', required=True)
    heart = fields.Char(string='Nhịp Tim', required=False)
    temperature = fields.Char(string='Nhiệt Độ', required=False)
    huyetap = fields.Char(string='Huyết Áp', required=False)
    nhiptho = fields.Char(string='Nhịp Thở', required=False)
    cannang = fields.Char(string='Cân Nặng', required=False)
    chieucao = fields.Char(string='Chiều Cao', required=False)
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
    thuoc = fields.Many2one('medicine.hs', string="Tên Thuốc")
    product_qty = fields.Char(string="Số Lượng")
    tac_dung = fields.Text(related='thuoc.tac_dung', string="Tác Dụng")
    ghichu = fields.Text(string='Ghi Chú')
    medicine_id = fields.Many2one('medical.record')


