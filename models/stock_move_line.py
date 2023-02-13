# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.osv import expression


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    auto_fill_package = fields.Boolean(compute='_compute_auto_fill_package')

    @api.depends('product_id','move_id')
    def _compute_auto_fill_package(self):
        for each in self:
            each.auto_fill_package = each.managed_by_package and each.move_id and each.move_id.raw_material_production_id


    @api.onchange('package_id','auto_fill_package')
    def _onchange_package_id(self):
        if self.package_id and self.auto_fill_package:
            self.update({'result_package_id': self.package_id})

