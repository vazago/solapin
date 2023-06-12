# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 


class solapin(models.Model): 
    _name = 'ej.solapin'

    name = fields.Char(string='nombre y apellido')
    foto = fields.Image(string='Imagen')
    departament = fields.Selection(
        string='Departamento',
        selection=[('profesor_invitado', 'Profesor Invitado'),
                   ('intercambio', 'Intercambio academico'),
                   ('estancia_postdoctoral', 'Estancia Postdoctoral'),
                   ('estancia_investigacion', 'Estancia de Investigación'),
                   ('curso_corto', 'Curso Corto'),
                   ('evento_congreso', 'Evento o Congreso'),
                   ('red_tematica', 'Red Temática'),
                   ('proyecto_investigacion', 'Proyecto de Investigación'),
                   ('opta_beca', 'Opta por Beca'),
                   ('otros', 'Otros'),
                   ], required=False, )
    cargo = fields.Selection(
        string='Cargo',
        selection=[('trabajador', 'TRABAJADOR'),
                   ('estudiante', 'ESTUDIANTE'),
                   ('cuadro', 'CUADRO'),
                   ('estancia_investigacion', 'Estancia de Investigación'),
                   ('curso_corto', 'Curso Corto'),
                   ('evento_congreso', 'Evento o Congreso'),
                   ('red_tematica', 'Red Temática'),
                   ('proyecto_investigacion', 'Proyecto de Investigación'),
                   ('opta_beca', 'Opta por Beca'),
                   ('otros', 'Otros'),
                   ], required=False, )
    ci= fields.Integer(string='carnet identidad')

