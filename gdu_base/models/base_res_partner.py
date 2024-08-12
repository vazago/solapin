# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)
class Partner(models.Model):
    _inherit = ['res.partner']
    area_base_id = fields.Many2one(related='department_id.area_base_id', string='Área base', readonly=True, store=True)