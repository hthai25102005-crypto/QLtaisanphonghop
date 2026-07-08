from odoo import api, fields, models


class AssetDashboard(models.TransientModel):
    _name = 'asset.dashboard'
    _description = 'Asset Dashboard'

    total_assets = fields.Integer(string='Tổng tài sản', compute='_compute_kpi')
    available_assets = fields.Integer(string='Sẵn sàng', compute='_compute_kpi')
    using_assets = fields.Integer(string='Đang sử dụng', compute='_compute_kpi')
    repair_assets = fields.Integer(string='Đang sửa', compute='_compute_kpi')
    broken_assets = fields.Integer(string='Hỏng', compute='_compute_kpi')

    total_rooms = fields.Integer(string='Tổng phòng', compute='_compute_kpi')
    available_rooms = fields.Integer(string='Phòng trống', compute='_compute_kpi')
    busy_rooms = fields.Integer(string='Đang sử dụng', compute='_compute_kpi')

    total_bookings = fields.Integer(string='Tổng lượt đặt', compute='_compute_kpi')
    bookings_today = fields.Integer(string='Hôm nay', compute='_compute_kpi')
    pending_bookings = fields.Integer(string='Chờ duyệt', compute='_compute_kpi')
    approved_bookings = fields.Integer(string='Đã duyệt', compute='_compute_kpi')
    done_bookings = fields.Integer(string='Hoàn thành', compute='_compute_kpi')
    cancelled_bookings = fields.Integer(string='Đã hủy', compute='_compute_kpi')

    total_asset_value = fields.Float(string='Tổng giá trị (VNĐ)', compute='_compute_kpi')

    @api.depends
    def _compute_kpi(self):
        today = fields.Datetime.now()
        today_start = today.replace(hour=0, minute=0, second=0)
        today_end = today.replace(hour=23, minute=59, second=59)

        Asset = self.env['asset.asset']
        Room = self.env['meeting.room']
        Booking = self.env['meeting.booking']

        assets = Asset.search([])
        total_value = sum(assets.mapped('price'))

        for rec in self:
            rec.total_assets = len(assets)
            rec.available_assets = len(assets.filtered(lambda a: a.state == 'available'))
            rec.using_assets = len(assets.filtered(lambda a: a.state == 'using'))
            rec.repair_assets = len(assets.filtered(lambda a: a.state == 'repair'))
            rec.broken_assets = len(assets.filtered(lambda a: a.state == 'broken'))
            rec.total_asset_value = total_value

            rooms = Room.search([])
            rec.total_rooms = len(rooms)
            rec.available_rooms = len(rooms.filtered(lambda r: r.state == 'available'))
            rec.busy_rooms = len(rooms.filtered(lambda r: r.state == 'busy'))

            rec.total_bookings = Booking.search_count([])
            rec.bookings_today = Booking.search_count([
                ('start_datetime', '>=', today_start),
                ('start_datetime', '<=', today_end),
            ])
            rec.pending_bookings = Booking.search_count([('state', '=', 'confirm')])
            rec.approved_bookings = Booking.search_count([('state', '=', 'approved')])
            rec.done_bookings = Booking.search_count([('state', '=', 'done')])
            rec.cancelled_bookings = Booking.search_count([('state', '=', 'cancel')])

    def action_open_assets(self):
        return {'type': 'ir.actions.act_window', 'res_model': 'asset.asset', 'view_mode': 'tree,form', 'name': 'Tài sản'}

    def action_open_rooms(self):
        return {'type': 'ir.actions.act_window', 'res_model': 'meeting.room', 'view_mode': 'tree,form', 'name': 'Phòng họp'}

    def action_open_bookings(self):
        return {'type': 'ir.actions.act_window', 'res_model': 'meeting.booking', 'view_mode': 'tree,form', 'name': 'Đặt phòng'}

    def action_open_pending(self):
        return {'type': 'ir.actions.act_window', 'res_model': 'meeting.booking', 'view_mode': 'tree,form', 'name': 'Chờ duyệt', 'domain': [('state', '=', 'confirm')]}

    def action_open_bookings_today(self):
        today = fields.Datetime.now()
        today_start = today.replace(hour=0, minute=0, second=0)
        today_end = today.replace(hour=23, minute=59, second=59)
        return {'type': 'ir.actions.act_window', 'res_model': 'meeting.booking', 'view_mode': 'tree,form', 'name': 'Lịch hôm nay', 'domain': [('start_datetime', '>=', today_start), ('start_datetime', '<=', today_end)]}

    def action_open_available_assets(self):
        return {'type': 'ir.actions.act_window', 'res_model': 'asset.asset', 'view_mode': 'tree,form', 'name': 'Tài sản sẵn sàng', 'domain': [('state', '=', 'available')]}

    def action_open_using_assets(self):
        return {'type': 'ir.actions.act_window', 'res_model': 'asset.asset', 'view_mode': 'tree,form', 'name': 'Tài sản đang dùng', 'domain': [('state', '=', 'using')]}
