from odoo import fields, models


class BookingWizard(models.TransientModel):
    _name = "booking.wizard"
    _description = "Booking Wizard"

    employee_id = fields.Many2one(
        "hr.employee",
        required=True
    )

    room_id = fields.Many2one(
        "meeting.room",
        required=True
    )

    asset_id = fields.Many2one(
        "asset.asset"
    )

    title = fields.Char(
        required=True
    )

    start_datetime = fields.Datetime(
        required=True
    )

    end_datetime = fields.Datetime(
        required=True
    )

    purpose = fields.Text()

    def action_create_booking(self):

        self.env["meeting.booking"].create({

            "title": self.title,

            "employee_id": self.employee_id.id,

            "room_id": self.room_id.id,

            "asset_id": self.asset_id.id,

            "start_datetime": self.start_datetime,

            "end_datetime": self.end_datetime,

            "purpose": self.purpose,

        })

        return {
            "type": "ir.actions.act_window_close"
        }