# -*- coding: utf-8 -*-
# Copyright (C) 2019-present  Technaureus Info Solutions(<http://www.technaureus.com/>).

from odoo import models, fields


class ProcessStatuses(models.Model):
    _name = "process.statuses"
    _order = "sequence"

    name = fields.Char(string='Name')
    sequence = fields.Integer('Sequence', default=10)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    process_status_id = fields.Many2one('process.statuses', string='Process Status')
