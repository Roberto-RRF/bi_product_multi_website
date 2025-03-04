# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class Website(models.Model):

    _inherit = "website"

    def sale_product_domain(self):
        current_website_id = self.env['website'].sudo().get_current_website().id
        return [("sale_ok", "=", True),'|',('website_ids', 'in',current_website_id),('website_ids', '=',False)]