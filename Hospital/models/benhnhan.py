# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
class Patients(models.Model):
    _name = "my.patients"
    _description = "Patients model"
    ten = fields.Char('Họ và tên:', required=True)
    tuoi = fields.Integer('Tuổi:', required=True)
    gioitinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], string='Giới tính:', default='Nam')
    ngaysinh = fields.Date('Ngày sinh:', required=False)
    sotheBHYT = fields.Char('Số thẻ BHYT:', required=True)
    noicap = fields.Text('Nơi cấp thẻ:')
    dt = fields.Selection([
        ('mot', '1'),
        ('hai', '2'),
        ('ba', '3')
    ], string='Đối tượng miễn giảm:', default='mot')
    cmnd = fields.Char('CMND:', required=True)
    nghenghiep = fields.Char('Nghề nghiệp:', required=True)
    diachi = fields.Char('Địa chỉ:', required=True)
    sdthoai = fields.Char('Số điện thoại:', required=True)
    Dantoc = fields.Char('Dân tộc:', required=True)
    chieucao = fields.Char('Chiều cao:', required=True)
    cannang = fields.Char('Cân nặng:', required=True)
    mau = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('o', 'O'),
        ('ab', 'AB'),
        ('hiem', 'Hiếm')
    ], string='Nhóm máu:', default='a')
    tgvaovien = fields.Date('Thời gian vào viện:', required=False)
    khoadt = fields.Selection([
        ('noi', 'Khoa Nội'),
        ('ngoai', 'Khoa Ngoại'),
        ('phusan', 'Khoa Phụ Sản'),
        ('tnhiem', 'Khoa Truyền Nhiễm'),
        ('capcuu', 'Khoa Cấp Cứu')
    ], string='Khoa điều trị:', default='Khoa Nội')
    bacsi = fields.Char('Bác sĩ điều trị:', required=True)
    trieuchungcu = fields.Text('Triệu chứng cũ:')
    benhchinh = fields.Text('Bệnh chính:')
    benhphu = fields.Text('Bệnh kèm theo:')
    Huongdt = fields.Selection([
        ('nhapvien', 'Nhập viện điều trị'),
        ('duathuoc', 'Kê đơn thuốc và về nhà'),
    ], string='Hướng điều trị:', default='nhapvien')
    tgravien = fields.Date('Thời gian ra viện:', required=False)
    tinhtrang = fields.Text('Tình trạng ra viện:')
    tennt = fields.Char('Họ và tên:', required=True)
    quanhe = fields.Char('Quan hệ:', required=True)
    sdt = fields.Char('Số điện thoại:', required=True)
    diac = fields.Char('Địa chỉ:', required=True)
    benhnhan_id = fields.Char('Mã bệnh nhân:', required=True)
    bn_image = fields.Binary("Ảnh thẻ", attachment=True, help="Ảnh thẻ")