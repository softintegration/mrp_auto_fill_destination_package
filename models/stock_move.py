# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.osv import expression


class StockMove(models.Model):
    _inherit = "stock.move"

    auto_fill_package = fields.Boolean(compute='_compute_auto_fill_package')

    @api.depends('product_id','raw_material_production_id')
    def _compute_auto_fill_package(self):
        for each in self:
            each.auto_fill_package = each.managed_by_package and each.raw_material_production_id

