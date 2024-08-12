# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class Department(models.Model):
    _inherit = ['gdu.department']
    _description = 'Departamento de la persona'

    area_base_id = fields.Many2one('gdu.base.area', 'Área base', readonly=True)

