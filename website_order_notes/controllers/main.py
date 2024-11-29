# -*- coding: utf-8 -*-
#################################################################################
#
# Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>:wink:
# See LICENSE file for full copyright and licensing details.
#################################################################################

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
import datetime

class website_sale(WebsiteSale):

    @http.route(['/website/order/notes'], type='json', auth="public", website=True)
    def order_notes(self, notes='', desire_date=False, **post):
        order = request.website.sale_get_order()
        if desire_date:
            cust_desire_date=datetime.datetime.strptime(desire_date,'%Y-%m-%d')
        else:
            cust_desire_date=desire_date
        order.sudo().write(
            {
            'wk_notes': notes,
            'wk_desire_date': cust_desire_date,
            })
        return True
