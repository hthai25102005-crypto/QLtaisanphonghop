from odoo import api, fields, models


class MeetingRoom(models.Model):
    _name = "meeting.room"
    _description = "Meeting Room"

    name = fields.Char(
        string="Tên phòng",
        required=True
    )

    code = fields.Char(
        string="Mã phòng",
        required=True
    )

    floor = fields.Char(
        string="Tầng"
    )

    building = fields.Char(
        string="Tòa nhà"
    )

    capacity = fields.Integer(
        string="Sức chứa"
    )

    projector = fields.Boolean(
        string="Máy chiếu"
    )

    television = fields.Boolean(
        string="TV"
    )

    speaker = fields.Boolean(
        string="Loa"
    )

    air_condition = fields.Boolean(
        string="Điều hòa"
    )

    internet = fields.Boolean(
        string="Internet"
    )

    description = fields.Text()

    active = fields.Boolean(
        default=True
    )

    state = fields.Selection([
        ("available", "Trống"),
        ("busy", "Đang sử dụng"),
        ("repair", "Đang sửa")
    ], default="available")

    booking_ids = fields.One2many(
        "meeting.booking",
        "room_id"
    )

    booking_count = fields.Integer(
        compute="_compute_booking_count"
    )

    @api.depends('booking_ids')
    def _compute_booking_count(self):
        for rec in self:
            rec.booking_count = len(rec.booking_ids)

    _sql_constraints = [
        ("room_code_unique",
         "unique(code)",
         "Mã phòng đã tồn tại!")
    ]

