from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MeetingBookingAsset(models.Model):
    _name = "meeting.booking.asset"
    _description = "Booking Asset Line"

    booking_id = fields.Many2one(
        'meeting.booking',
        string="Booking",
        ondelete="cascade"
    )

    asset_id = fields.Many2one(
        'asset.asset',
        string="Asset",
        required=True
    )

    quantity = fields.Integer(
        string="Quantity",
        default=1
    )

    state = fields.Selection([
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('using', 'In Use')
    ], related='asset_id.state', store=True)

    note = fields.Char(string="Note")

    @api.constrains('asset_id', 'booking_id')
    def _check_duplicate_asset(self):
        for rec in self:
            domain = [
                ('booking_id', '=', rec.booking_id.id),
                ('asset_id', '=', rec.asset_id.id),
                ('id', '!=', rec.id)
            ]
            if self.search(domain):
                raise ValidationError(_("Asset already added in this booking."))

    @api.constrains('asset_id')
    def _check_asset_available(self):
        for rec in self:
            if rec.asset_id.state not in ['available']:
                raise ValidationError(
                    _("Asset %s is not available!") % rec.asset_id.name
                )