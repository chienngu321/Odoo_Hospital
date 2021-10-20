from odoo import _, models, fields, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _inherit = "hr.employee"

    code = fields.Char("Mã nhân viên", required=True)
    x_job = fields.Selection([
        ('one', 'Bác sĩ'),
        ('two', 'Dược sĩ'),
        ('three', 'Y sỹ'),
        ('four', 'Điều dưỡng'),
        ('five', 'Y tá'),
        ("six", "Kỹ thuật viên xét nghiệm")], string='Chức vụ', required=True, default='one')
    x_date_start = fields.Date("Ngày bắt đầu làm việc", required=True)
    x_end = fields.Date("Thời gian hết thử việc", required=True)

    @api.constrains('code')
    def _check_code(self):
        exists = self.env['hr.employee'].search(
            [('code', '=', self.code), ('id', '!=', self.id)])
        if exists:
            raise ValidationError(_('Mã nhân viên  ' + self.code + ' đã tồn tại.'))

    def copy(self, default={}):
        if self.code == False:
            default['code'] = str(self.id) + " (Bản sao)"
        else:
            default['code'] = self.code + " (Bản sao)"

        res = super(Employee, self).copy(default=default)
        return res

    @api.constrains('x_end')
    def onchange_end_dates(self):
        if (self.x_date_start and self.x_end) and (self.x_end < self.x_date_start):
            raise ValidationError(_('Ngày kết thúc phải lớn hơn hoặc bằng ngày bắt đầu làm việc.'))