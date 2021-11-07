# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalBed(models.Model):
    _inherit = "product.template"

    # add new fields
    id_bed = fields.Char(string='GB', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))
    chucnang = fields.Selection([
        ('capcuu', 'Cấp cứu'),
        ('benh', 'Bệnh')
    ], string='Chức năng', required=True, default='benh')
    trangthai = fields.Selection([
        ('trong', 'Trống'),
        ('day', 'Đầy')
    ], string='Trạng thái', required=True, default='trong')
    chieudai = fields.Char('Chiều dài', required=False)
    chieurong = fields.Char('Chiều rộng', required=False)
    chieucao = fields.Char('Chiều cao', required=False)
    chatlieu = fields.Char('Chất liệu', required=False)
    trongluong = fields.Char('Trọng lượng giường', required=False)
    taitrong = fields.Char('Tải trọng tối đa', required=False)
    bn_image = fields.Binary("Ảnh bệnh nhân", attachment=False, help="Ảnh bệnh nhân")
    code_bn = fields.Many2one('my.patients', string='Mã Bệnh Nhân')
    ten = fields.Char('Họ và tên bệnh nhân', required=False)
    tuoi = fields.Integer('Tuổi', required=False)
    gioitinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ')
    ], string='Giới tính', default='nam')

    chuandoan = fields.Char('Chuẩn đoán bệnh', required=False)
    thoigian_nhapvien = fields.Date(string='Thời gian nhập viện', help="Nhập thời gian bắt đầu nhập viện.")
    songay_nhapvien = fields.Integer('Số ngày nhập viện', required=False)
    khoa = fields.Many2one('hr.department', string='Khoa')
    phongbenh = fields.Char('Tên phòng', required=False)
    note = fields.Text('Ghi chú:', required=False)
    loai = fields.Selection([
        ('coban', 'Giường y tế cơ bản'),
        ('dachucnang', 'Giường đa chức năng')
    ], string='Loại giường', default='coban', required=True)
    benh_li = fields.Many2many('medical.record', string="Danh sách bệnh nhân nằm")

    @api.model
    def create(self, vals):
        if vals.get('id_bed', ('New')) == ('New'):
            vals['id_bed'] = self.env['ir.sequence'].next_by_code('product.template') or _('New')
        res = super(HospitalBed, self).create(vals)
        return res
