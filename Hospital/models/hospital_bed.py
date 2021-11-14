# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalBed(models.Model):
    _inherit = "product.template"

    # add new fields
    id_bed = fields.Char(string='GB', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))
    cn = fields.Integer('Chức năng', required=False)
    chucnang = fields.Selection([
        ('capcuu', 'Cấp cứu'),
        ('benh', 'Bệnh')
    ], string='Loại Hình', required=True, default='benh')
    so_luong = fields.Integer('Số Lượng', required=False)
    chieudai = fields.Char('Chiều dài', required=False)
    chieurong = fields.Char('Chiều rộng', required=False)
    chieucao = fields.Char('Chiều cao', required=False)
    chatlieu = fields.Char('Chất liệu', required=False)
    trongluong = fields.Char('Trọng lượng giường', required=False)
    taitrong = fields.Char('Tải trọng tối đa', required=False)
    tinh_trang = fields.Selection([
        ('new', 'Mới'),
        ('old', 'Cũ')
    ], string='Tình trạng giường', default='new')
    th_sudung = fields.Selection([
        ('a', '15 năm - 18 năm'),
        ('b', '18 năm - 20 năm'),
        ('c', '20 năm - 25 năm')
    ], string='Thời hạn sử dụng', default='a')
    tg_nhapgiuong = fields.Date(string='Thời gian nhập', help="Nhập thời gian bắt đầu nhập viện.")
    note = fields.Text('Ghi chú:', required=False)
    loai = fields.Selection([
        ('coban', 'Giường y tế cơ bản'),
        ('dachucnang', 'Giường đa chức năng')
    ], string='Loại giường', default='coban', required=True)
    tien = fields.Char('Giá tiền', required=False)
    bed_inf = fields.One2many('medical.record', 'bed_bn')

    @api.model
    def create(self, vals):
        if vals.get('id_bed', ('New')) == ('New'):
            vals['id_bed'] = self.env['ir.sequence'].next_by_code('product.template') or _('New')
        res = super(HospitalBed, self).create(vals)
        return res