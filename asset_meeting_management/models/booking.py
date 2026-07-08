from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MeetingBooking(models.Model):
    _name = "meeting.booking"
    _description = "Meeting Booking"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "start_datetime desc"

    name = fields.Char(
        string="Mã phiếu",
        default="New",
        readonly=True,
        copy=False
    )

    title = fields.Char(
        string="Tiêu đề cuộc họp",
        required=True,
        tracking=True
    )

    room_id = fields.Many2one(
        "meeting.room",
        string="Phòng họp",
        required=True,
        tracking=True
    )

    employee_id = fields.Many2one(
        "hr.employee",
        string="Người đặt",
        required=True,
        tracking=True
    )

    department = fields.Char(
        related="employee_id.department_id.name",
        string="Phòng ban",
        store=True
    )

    asset_id = fields.Many2one(
        "asset.asset",
        string="Tài sản sử dụng",
        tracking=True
    )

    start_datetime = fields.Datetime(
        string="Bắt đầu",
        required=True,
        tracking=True
    )

    end_datetime = fields.Datetime(
        string="Kết thúc",
        required=True,
        tracking=True
    )

    participant = fields.Integer(
        string="Số người tham dự"
    )

    purpose = fields.Text(
        string="Mục đích"
    )

    note = fields.Text(
        string="Ghi chú"
    )

    duration = fields.Float(
        string="Số giờ",
        compute="_compute_duration",
        store=True
    )

    state = fields.Selection([
        ("draft", "Nháp"),
        ("confirm", "Chờ duyệt"),
        ("approved", "Đã duyệt"),
        ("done", "Hoàn thành"),
        ("cancel", "Hủy")
    ],
        default="draft",
        tracking=True
    )

    @api.depends("start_datetime", "end_datetime")
    def _compute_duration(self):
        for rec in self:
            rec.duration = 0
            if rec.start_datetime and rec.end_datetime:
                delta = rec.end_datetime - rec.start_datetime
                rec.duration = delta.total_seconds() / 3600

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "meeting.booking"
            ) or "BOOK0001"
        return super().create(vals)

    @api.constrains("start_datetime", "end_datetime")
    def _check_datetime(self):
        for rec in self:
            if rec.end_datetime <= rec.start_datetime:
                raise ValidationError("Thời gian kết thúc phải lớn hơn thời gian bắt đầu.")

    @api.constrains("room_id", "start_datetime", "end_datetime")
    def _check_overlap(self):
        for rec in self:
            bookings = self.search([
                ("room_id", "=", rec.room_id.id),
                ("id", "!=", rec.id),
                ("state", "!=", "cancel"),
                ("start_datetime", "<", rec.end_datetime),
                ("end_datetime", ">", rec.start_datetime),
            ])
            if bookings:
                raise ValidationError("Phòng họp đã được đặt trong khoảng thời gian này.")

    def action_confirm(self):
        self.write({"state": "confirm"})
        self.activity_schedule(
            'mail.mail_activity_data_todo',
            summary='Phê duyệt đặt phòng',
            note=self.title,
            user_id=self.env.ref('base.user_admin').id
        )

    def action_approve(self):
        self.write({"state": "approved"})
        for rec in self:
            if rec.room_id:
                rec.room_id.state = "busy"
            if rec.asset_id:
                rec.asset_id.state = "using"
            rec._create_history("reserve")

    def action_done(self):
        self.write({"state": "done"})
        for rec in self:
            if rec.room_id:
                rec.room_id.state = "available"
            if rec.asset_id:
                rec.asset_id.state = "available"
            rec._create_history("return")

    def action_cancel(self):
        self.write({"state": "cancel"})
        for rec in self:
            if rec.room_id:
                rec.room_id.state = "available"
            if rec.asset_id:
                rec.asset_id.state = "available"

    def action_reset(self):
        self.write({"state": "draft"})

    def _create_history(self, action_type):
        for rec in self:
            if not rec.asset_id:
                continue
            self.env["asset.history"].create({
                "asset_id": rec.asset_id.id,
                "employee_id": rec.employee_id.id,
                "room_id": rec.room_id.id,
                "booking_id": rec.id,
                "action": action_type,
                "date": fields.Datetime.now(),
                "description": rec.title,
            })
