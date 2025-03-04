# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class MassUpdateProduct(models.TransientModel):
    _name = 'mass.update.product'
    _description = 'Mass Update Product'

    website_ids = fields.Many2many('website', string="Websites")

    def update_mass_product(self):
        if 'active_ids' in self._context:
            product_template_ids = self.env['product.template'].browse(self._context.get('active_ids'))
            for product in product_template_ids:
                product.website_ids = self.website_ids