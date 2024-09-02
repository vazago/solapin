# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gdu_base_area(models.Model):
    _name = 'gdu.base.area'

    name= fields.Char('Área base', readonly=True)
    sigla=fields.Char('Sigla',  readonly=True)
    centro = fields.Char(string='Centro')
    departamentos_ids = fields.One2many('gdu.department', 'area_base_id', 'Departamentos')
    partners_ids = fields.One2many('res.partner','area_base_id', string='Personas')

    rango_inicial = fields.Char('Rango inicial')
    rango_final = fields.Char('Rango final')

    user_id = fields.Many2one('res.users', string='Jefe de Área')