# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _
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
    loai = fields.Selection([
        ('coban', 'Giường y tế cơ bản'),
        ('dachucnang', 'Giường đa chức năng')
    ], string='Loại giường', default='coban', required=True)
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
    ], string='Giới tính', required=True, default='nam')
    chuandoan = fields.Char('Chuẩn đoán bệnh', required=True)
    thoigian_nhapvien = fields.Date(string='Thời gian nhập viện', help="Nhập thời gian bắt đầu nhập viện.")
    songay_nhapvien = fields.Char(string='Số ngày nhập viện', compute="_get_date")
    bacsi_phutrach = fields.Char('Bác sĩ phụ trách', required=True)
    phongbenh = fields.Char('Tên phòng', required=True)
    note = fields.Text('Ghi chú:', required=True)

    @api.constrains('id_bed')
    def _check_id_bed(self):
        exists = self.env['product.template'].search(
            [('id_bed', '=', self.id_bed), ('id', '!=', self.id)])
        if exists:
            raise ValidationError(_('Mã giường  ' + self.id_bed + ' đã tồn tại.'))

    def copy(self, default={}):
        if self.id_bed == False:
            default['id_bed'] = str(self.id) + " (Bản sao)"
        else:
            default['id_bed'] = self.id_bed + " (Bản sao)"

        res = super(HospitalBed, self).copy(default=default)
        return res

    @api.model
    def _get_date(self):
        today_date = datetime.date.today()
        for bed in self:
            if bed.thoigian_nhapvien:
                thoigian_nhapvien = fields.Datetime.to_datetime(bed.thoigian_nhapvien).date()
                dem = str(int((today_date - thoigian_nhapvien).days))
                bed.songay_nhapvien = dem
            else:
                bed.songay_nhapvien = ""