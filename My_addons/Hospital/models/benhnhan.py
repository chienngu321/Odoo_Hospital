# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
class Patients(models.Model):
    _name = "my.patients"
    _description = "Patients model"
    ten = fields.Char('Họ và tên:', required=False)
    tuoi = fields.Integer('Tuổi:', required=False)
    gioitinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], string='Giới tính:', default='Nam')
    ngaysinh = fields.Date('Ngày sinh:', required=False)
    cmnd = fields.Char('CMND:', required=False)
    nghenghiep = fields.Char('Nghề nghiệp:', required=False)
    noilv = fields.Char('Nơi làm việc:', required=False)
    diachi = fields.Char('Địa chỉ:', required=False)
    sdthoai = fields.Char('Số điện thoại:', required=False)
    Dantoc = fields.Selection([
        ('kinh', 'Kinh'),
        ('thieuso', 'Thiểu số'),
        ('khac', 'Khác')
    ], string='Dân tộc:', default='kinh')
    quocgia = fields.Selection([
        ('Vietnam', 'Việt Nam'),
        ('nuocngoai', 'Nước Ngoài'),
        ('khac', 'Khác')
    ], string='Quốc gia:', default='quocgia')
    chieucao = fields.Char('Chiều cao:', required=False)
    cannang = fields.Char('Cân nặng:', required=False)
    mau = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('o', 'O'),
        ('ab', 'AB'),
        ('hiem', 'Hiếm')
    ], string='Nhóm máu:', default='a')
    tgvaovien = fields.Date('Thời gian vào viện:', required=False)
    lydo = fields.Char('Lý do vào viện:', required=False)
    khoadt = fields.Selection([
        ('noi', 'Khoa Nội'),
        ('ngoai', 'Khoa Ngoại'),
        ('phusan', 'Khoa Phụ Sản'),
        ('tnhiem', 'Khoa Truyền Nhiễm'),
        ('capcuu', 'Khoa Cấp Cứu')
    ], string='Khoa điều trị:', default='Khoa Nội')
    kham = fields.Char('Khám:')
    tgravien = fields.Date('Thời gian ra viện:', required=False)
    dt = fields.Selection([
        ('bh', 'Bảo hiểm y tế'),
        ('kh', 'Không sử dụng thẻ BHYT'),
    ], string='Đối tượng:', default='bh')
    sotheBHYT = fields.Char('Số thẻ BHYT:', required=False)
    noicap = fields.Text('Nơi đăng ký thẻ:')
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
    tennt = fields.Char('Họ và tên:', required=False)
    quanhe = fields.Char('Quan hệ:', required=False)
    sdt = fields.Char('Số điện thoại:', required=False)
    diac = fields.Char('Địa chỉ:', required=False)
    bn_image = fields.Binary("Ảnh thẻ", attachment=True, help="Ảnh thẻ")
    benhnhan_id = fields.Char(string='Mã bệnh nhân:', required=True, copy=False, readonly=True,
                              default=lambda seft: _('New ID'))
    @api.model
    def create(self, values):
        if values.get('benhnhan_id', ('Mã BN')) == ('Mã BN'):
            values['benhnhan_id'] = self.env['ir.sequence'].next_by_code('my.patients') or _('Mã BN')
        res = super(Patients, self).create(values)
        return res

    phong = fields.Many2many(comodel_name='product.template',
                             string="Phòng khám",
                             relation='patients_product_rel',
                             column1='col_phong',
                             column2='col_phongbenh')
