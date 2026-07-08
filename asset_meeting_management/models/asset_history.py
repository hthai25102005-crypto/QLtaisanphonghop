from odoo import fields, models


class AssetHistory(models.Model):
    _name = "asset.history"
    _description = "Asset Usage History"
    _order = "date desc"

    asset_id = fields.Many2one(
        "asset.asset",
        string="Asset",
        required=True
    )

    employee_id = fields.Many2one(
        "hr.employee",
        string="Employee"
    )

    room_id = fields.Many2one(
        "meeting.room",
        string="Room"
    )

    booking_id = fields.Many2one(
        "meeting.booking",
        string="Booking"
    )

    action = fields.Selection([
        ("create", "Created"),
        ("reserve", "Reserved"),
        ("use", "In Use"),
        ("return", "Returned"),
        ("repair", "Repair"),
        ("lost", "Lost"),
        ("booking", "Booking"),
    ], string="Action")

    date = fields.Datetime(
        default=fields.Datetime.now
    )

    description = fields.Text(
        string="Description"
    )