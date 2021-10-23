# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # add new fields
    id_bed = fields.Char('Mã số giường:', required=True)
    chucnang = fields.Selection([
        ('capcuu', 'Cấp cứu'),
        ('benh', 'Bệnh'),
    ], string='Chức năng :', default='Bệnh')
    trangthai = fields.Selection([
        ('trong', 'Trống'),
        ('day', 'Đầy')
    ], string='Trạng thái :', default='Trống')
    chieudai = fields.Char('Kích thước (Chiều dài) :', required=True)
    chieurong = fields.Char('Kích thước (Chiều rộng) :', required=True)
    chieucao = fields.Char('Kích thước (Chiều cao) :', required=True)
    chatlieu = fields.Char('Chất liệu :', required=True)
    trongluong = fields.Char('Trọng lượng giường :', required=True)
    taitrong = fields.Char('Tải trọng tối đa :', required=True)
    bn_image = fields.Binary("Ảnh bệnh nhân", attachment=True, help="Ảnh bệnh nhân")
    ten = fields.Char('Họ và tên bệnh nhân:', required=True)
    tuoi = fields.Integer('Tuổi:', required=True)
    gioitinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ')
    ], string='Giới tính:', default='Nam')
    id_benhnhan = fields.Char('Mã bệnh nhân:', required=True)
    chuandoan = fields.Char('Chuẩn đoán bệnh:', required=True)
    thoigian_nhapvien = fields.Date(string='Thời gian nhập viện: ', help="Nhập thời gian bắt đầu nhập viện.")
    songay_nhapvien = fields.Integer('Số ngày nhập viện:', required=True)
    bacsi_phutrach = fields.Char('Bác sĩ phụ trách:', required=True)
    id_phongbenh = fields.Char('Mã phòng bệnh:', required=True)
    note = fields.Text('Ghi chú:', required=True)

    # modify old fields
    name = fields.Char('Tên giường', index=True, required=True, translate=True)
    barcode = fields.Char('Mã vạch', compute='_compute_barcode', inverse='_set_barcode', search='_search_barcode')
    type = fields.Selection([
        ('coban', 'Giường y tế cơ bản'),
        ('dachucnang', 'Giường đa chức năng')
    ], string='Loại giường :', default='Giường y tế cơ bản', required=True,)