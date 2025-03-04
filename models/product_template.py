# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'


    website_ids = fields.Many2many('website', string="Websites")

    def action_mass_update_product(self):
        action = self.env["ir.actions.actions"]._for_xml_id("bi_product_multi_website.action_mass_update_product_website")
        action['context'] = self.env.context
        return action