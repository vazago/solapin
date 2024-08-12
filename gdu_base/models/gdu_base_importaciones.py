# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from lxml.html.clean import word_break
from odoo import api, fields, models
from odoo import exceptions
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo import tools, _
from odoo.modules.module import get_module_resource

import logging
import suds
from suds.client import Client
from datetime import datetime, date, timedelta
import requests,json
from requests import auth
from suds.cache import NoCache
import ssl
#import ldap

from ldap3 import ALL, ALL_ATTRIBUTES, Connection, MODIFY_ADD, MODIFY_DELETE, MODIFY_REPLACE, Server, SUBTREE

_logger = logging.getLogger(__name__)
class gdu_base_importaciones(models.TransientModel):
    _name = 'gdu.base.importaciones'
    _description = 'Importaciones basicas para el GDU'

    def asignar_area_a_los_departamentos(self):
        areas_base_ids=self.env['gdu.base.area'].search([])
        for area in areas_base_ids:
            self.env['gdu.department'].search([('center','=',area.centro), ('code','>=',area.rango_inicial), ('code','<=',area.rango_final)]).write({'area_base_id':area.id})

    def borrar_areas(self):
        areas_gestor_list = self.env['gdu.base.area'].search([])
        cccc = areas_gestor_list.unlink()