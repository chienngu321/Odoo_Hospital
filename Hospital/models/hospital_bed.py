# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalBed(models.Model):
    _inherit = "product.template"

    # add new fields
    id_bed = fields.Char('Mã số giường', required=True)
    chucnang = fields.Selection([
        ('capcuu', 'Cấp cứu'),
        ('benh', 'Bệnh')
    ], string='Chức năng', required=True, default='benh')
    trangthai = fields.Selection([
        ('trong', 'Trống'),
        ('day', 'Đầy')
    ], string='Trạng thái', required=True, default='trong')
    chieudai = fields.Char('Chiều dài', required=True)
    chieurong = fields.Char('Chiều rộng', required=True)
    chieucao = fields.Char('Chiều cao', required=True)
    chatlieu = fields.Char('Chất liệu', required=True)
    trongluong = fields.Char('Trọng lượng giường', required=True)
    taitrong = fields.Char('Tải trọng tối đa', required=True)
    bn_image = fields.Binary("Ảnh bệnh nhân", attachment=True, help="Ảnh bệnh nhân")
    ten = fields.Char('Họ và tên bệnh nhân', required=True)
    tuoi = fields.Integer('Tuổi', required=True)
    gioitinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ')
    ], string='Giới tính', required=True, default='Nam')

    chuandoan = fields.Char('Chuẩn đoán bệnh', required=True)
    thoigian_nhapvien = fields.Date(string='Thời gian nhập viện', help="Nhập thời gian bắt đầu nhập viện.")
    songay_nhapvien = fields.Integer('Số ngày nhập viện', required=True)
    bacsi_phutrach = fields.Char('Bác sĩ phụ trách', required=True)
    phongbenh = fields.Char('Tên phòng', required=True)
    note = fields.Text('Ghi chú:', required=True)

    # modify old fields
    name = fields.Char('Tên giường', index=True, required=True, translate=True)
    loai = fields.Selection([
        ('coban', 'Giường y tế cơ bản'),
        ('dachucnang', 'Giường đa chức năng')
    ], string='Loại giường', default='coban', required=True)

