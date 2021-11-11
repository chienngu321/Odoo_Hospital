# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class QLBN(models.Model):
    _name = "my.patients"
    _description = "QLBN model"
    ten = fields.Char('Họ và Tên:', required=True)
    ngaysinh = fields.Date('Ngày sinh:', required=True)
    gioitinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], string='Giới tính:', default='nam')
    qg = fields.Many2one('res.country', 'Quốc gia:', required=True)
    cmnd = fields.Char('CMND:', required=False)
    nghenghiep = fields.Char('Nghề nghiệp:', required=False)
    noilv = fields.Char('Nơi làm việc:', required=False)
    diachi = fields.Char('Địa chỉ:', required=True)
    sdthoai = fields.Char('Số điện thoại:', required=True)
    chieucao = fields.Char('Chiều cao (cm):', required=False)
    cannang = fields.Char('Cân nặng (kg):', required=False)
    mau = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('o', 'O'),
        ('ab', 'AB')
    ], string='Nhóm máu:', default='a')
    tgvaovien = fields.Date('Thời gian vào viện:', required=True)
    tgravien = fields.Date('Thời gian ra viện:', required=False)
    sotheBHYT = fields.Char('Số thẻ BHYT:', required=True)
    noicap = fields.Text('Nơi đăng ký thẻ:', required=False)
    tuyen = fields.Selection([
        ('noi', 'Nội tuyến'),
        ('ngoai', 'Ngoại tuyến'),
        ('co', 'Có giấy CV')
    ], string='Tuyến:', default='noi')
    tungay = fields.Date('Từ ngày:', required=False)
    denngay = fields.Date('Đến ngày:', required=False)
    du = fields.Date('Đủ 5 năm:', required=False)
    khuvuc = fields.Selection([
        ('k1', 'K1'),
        ('k2', 'K2'),
        ('k3', 'K3')
    ], string='Khu vực:', default='k1')
    action = fields.One2many('family.action', 'family', string='Thông tin người thân', required=True)
    bn_image = fields.Binary("Ảnh thẻ", attachment=True, help="Ảnh thẻ")
    name = fields.Char(string='Mã bệnh nhân:', required=True, copy=False, readonly=True,
                              default=lambda seft: _('Mã BN'))
    benh_li = fields.One2many('medical.record', 'code_bn', string="Bệnh Lí:")

    @api.model
    def create(self, values):
        if values.get('name', ('Mã BN')) == ('Mã BN'):
            values['name'] = self.env['ir.sequence'].next_by_code('my.patients') or _('Mã BN')
        res = super(QLBN, self).create(values)
        return res

    @api.constrains('tgravien')
    def _check_tgravien(self):
        if (self.tgvaovien and self.tgravien) and (self.tgravien <= self.tgvaovien):
            raise ValidationError('Thời gian ra viện phải lớn hơn hoặc bằng thời gian vào viện! ')


class Family(models.Model):
    _name = "family.action"
    _description = "Action model"
    family = fields.Many2one('my.patients', string='Mã bệnh nhân:', required=True)
    name_action = fields.Char('Họ và tên:', required=True)
    quanhe = fields.Char('Quan hệ:', required=True)
    sdt = fields.Char('Số điện thoại:', required=True)
    diac = fields.Char('Địa chỉ:', required=True)
