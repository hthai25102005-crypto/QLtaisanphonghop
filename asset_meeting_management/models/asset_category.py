from odoo import api, models, fields


class AssetCategory(models.Model):
    _name = "asset.category"
    _description = "Asset Category"
    _order = "name"

    name = fields.Char(
        string="Tên danh mục",
        required=True
    )

    code = fields.Char(
        string="Mã danh mục",
        required=True
    )

    description = fields.Text(
        string="Mô tả"
    )

    active = fields.Boolean(
        default=True
    )

    asset_ids = fields.One2many(
        "asset.asset",
        "category_id",
        string="Tài sản"
    )

    asset_count = fields.Integer(
        string="Số tài sản",
        compute="_compute_asset_count"
    )

    @api.depends('asset_ids')
    def _compute_asset_count(self):
        for rec in self:
            rec.asset_count = len(rec.asset_ids)

    _sql_constraints = [
    (
        "asset_category_code_unique",
        "unique(code)",
        "Mã danh mục đã tồn tại!"
    )
    ]        