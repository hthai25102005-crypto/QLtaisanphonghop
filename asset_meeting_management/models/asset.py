from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Asset(models.Model):
    _name = "asset.asset"
    _description = "Company Asset"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "name"
    _order = "id desc"

    name = fields.Char(
        string="Tên tài sản",
        required=True,
        tracking=True
    )

    code = fields.Char(
        string="Mã tài sản",
        required=True,
        copy=False,
        tracking=True
    )

    serial = fields.Char(
        string="Serial Number"
    )

    barcode = fields.Char(
        string="Barcode"
    )

    category_id = fields.Many2one(
        "asset.category",
        string="Danh mục",
        required=True
    )

    employee_id = fields.Many2one(
        "hr.employee",
        string="Người sử dụng"
    )

    purchase_date = fields.Date(
        string="Ngày mua"
    )

    warranty_date = fields.Date(
        string="Hết bảo hành"
    )

    supplier = fields.Char(
        string="Nhà cung cấp"
    )

    location = fields.Char(
        string="Vị trí"
    )

    price = fields.Float(
        string="Nguyên giá"
    )

    depreciation = fields.Float(
        string="Khấu hao (%)"
    )

    image = fields.Binary(
        string="Hình ảnh"
    )

    note = fields.Text()

    state = fields.Selection([
        ("available", "Sẵn sàng"),
        ("using", "Đang sử dụng"),
        ("repair", "Đang sửa"),
        ("broken", "Hỏng"),
        ("liquidated", "Thanh lý"),
    ],
        default="available",
        tracking=True
    )

    history_ids = fields.One2many(
        "asset.history",
        "asset_id",
        string="Lịch sử"
    )

    booking_ids = fields.One2many(
        "meeting.booking",
        "asset_id"
    )

    booking_count = fields.Integer(
        compute="_compute_booking_count"
    )

    @api.depends("booking_ids")
    def _compute_booking_count(self):
        for rec in self:
            rec.booking_count = len(rec.booking_ids)

    @api.constrains("price")
    def _check_price(self):
        for rec in self:
            if rec.price < 0:
                raise ValidationError("Giá không hợp lệ.")

    _sql_constraints = [
        ("asset_code_unique",
         "unique(code)",
         "Mã tài sản đã tồn tại!")
    ]