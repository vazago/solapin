# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
import logging, qrcode, base64

from io import BytesIO
_logger = logging.getLogger(__name__)
class Partner(models.Model):
    _inherit = ['res.partner']

    # def onchange_name(self, cr, uid, ids, given_name, context=None):
    #     if given_name:
    #         return {'value': {'given_name': given_name.title()}}
    #     return {'value': {}}
    # no_trabajador = fields.Char(related='trabajador_id.no_trabajador', string='Número de nómina:', readonly='True')
    categoria_ocupacional = fields.Char(related='trabajador_id.categoria_ocupacional', string='Categoría Ocupacional')
    investigador = fields.Boolean(related='trabajador_id.investigador', string='¿Investigador?')
    funcionario = fields.Boolean('¿Funcionario?', store=True)
    work_position_id = fields.Many2one(comodel_name='gdu.work_position',
                                string='Cargo')
    given_name = fields.Char(string='Nombre')
    last_name = fields.Char(string='Apellidos')

    # @api.onchange('given_name')
    # def _ini_mayus(self):
    #     self.given_name = self.given_name.title() if self.given_name else False
    #     self.last_name = self.last_name.title() if self.last_name else False

    siglas = fields.Selection(
        string='Siglas',
        selection=[('dinf', 'Dirección Informatización'),
                   ('drejam', 'DRE Julio Antonio Mella'),
                   ('dream', 'DRE Antonio Maceo'),
                   ('contrucciones', 'Fac. Construcciones'),
                   ('fcne', 'FCNE'),
                   ('cum_tf', 'CUM Tercer Frente'),
                   ('cum_ps', 'CUM Palma Soriano'),
                   ('cum_c', 'CUM Contramaestra'),
                   ('cum_sm', 'CUM Songo la Maya'),
                   ('cum_sl', 'CUM San Luis'),
                   ('cum_sf', 'CUM Segundo Frente'),
                   ('cum_tf', 'CUM Tercer Frente'),
                   ('cum_sjam', 'CUM Julio Antonio Mella'),
                   ('cum_g', 'CUM Guamá'),
                   ('cebi', 'CEBI'),
                   ('cnea', 'CNEA'),
                   ('cbm', 'CBM'),
                   ('rectorado', 'Rectorado'),
                   ('sg', 'Secretaría General'),
                   ('pd', 'Puesto de Dirección'),
                   ('gdr', 'Grup. Despacho del Rector'),
                   ('dge', 'DGE'),
                   ('drh', 'DRH'),
                   ('deco', 'DECO'),
                   ('dgas', 'DGAS'),
                   ('dl', 'Dir. Logística'),
                   ('dim', 'Dir. Inversiones y Mantenimiento'),
                   ('dt', 'Dir. de Transporte'),
                   ('dp', 'Dep. Poligráfico'),
                   ('dsjam', 'Dir. Sede Julio Antonio Mella'),
                   ('dsam', 'Dir. Sede Antonio Maceo'),
                   ('gaue', 'Grup. Ahorro y Uso de Energía'),
                   ('dgre', 'DGRE'),
                   ('daloj', 'Dir. Alojamiento'),
                   ('dcuadros', 'Dir. Cuadros'),
                   ('ddssam', 'DDS Sede Antonio Maceo'),
                   ('ddssjam', 'DDS Julio Antonio Mella'),
                   ('dopec', 'DOPEC'),
                   ('deu', 'Dir. Extensión Universitaria'),
                   ('dfp', 'Dir. Formación de Pregrado'),
                   ('dhml', 'Dir. Historia y Marxismo-Leninismo'),
                   ('dict', 'DICT'),
                   ('dep', 'Dir. Educación de Postgrado'),
                   ('dcti', 'Dir. Ciencias Tecnología e Innovación'),
                   ('dri', 'DRI'),
                   ('dci', 'Dir. Comunicación Institucional'),
                   ('digd', 'Dir. Información y Gestión Documental'),
                   ('dpsc', 'Dir. Preparación y Superación de Cuadros'),
                   ('djuridico', 'Departamento Jurídico'),
                   ('dauditoria', 'Departamento de Auditoría'),
                   ('dend', 'Dep. de Evento (No Docente)'),
                   ('dprotocolo', 'Departamento de Protocolo'),
                   ('dem', 'Dep. Enseñanza Militar'),
                   ('dtyc', 'Dep. Transferencia y Comercialización'),
                   ('dhpu', 'Dep. Historia y Patrimonio Universitario'),
                   ('fitib', 'FITIB'),
                   ('fsc', 'FSC'),
                   ('fh', 'Facultad Humanidades'),
                   ('FLE', 'Facultad Lenguas Extranjeras'),
                   ('FCEE', 'FCEE'),
                   ('Fie', 'Facultad Ingeniería Eléctrica'),
                   ('foc', 'Facultad de Construcciones'),
                   ('fimi', 'Fac. Ingeniería Mecánica e Industrial'),
                   ('fiqa', 'Fac. Ingeniería Química y Agronomía'),
                   ('fcf', 'Fac. Cultura Física'),
                   ('fce', 'Fac. Ciencias de la Educación'),
                   ('gdr', 'Grup. Despacho del Rector'),
                   ],compute='_compute_category_siglas')

    # @api.depends('area_base_id')
    @api.depends('siglas')
    def _compute_category_siglas(self):
        for record in self:
            if record.area_base_id.name == 'FACULTAD DE CIENCIAS NATURALES Y EXACTAS':
                record.siglas = 'fcne'
            elif record.area_base_id.name == 'GRUPO DE DESPACHO DEL RECTOR':
                record.siglas = 'gdr'
            elif record.area_base_id.name == 'FACULTAD DE CIENCIAS DE LA EDUCACIÓN':
                record.siglas = 'fce'
            elif record.area_base_id.name == 'DIRECCIÓN DE INFORMATIZACIÓN':
                record.siglas = 'dinf'
            elif record.area_base_id.name == 'FACULTAD DE CULTURA FÍSICA':
                record.siglas = 'fcf'
            elif record.area_base_id.name == 'FACULTAD DE INGENIERÍA QUÍMICA Y AGRONOMÍA':
                record.siglas = 'fiqa'
            elif record.area_base_id.name == 'FACULTAD DE INGENIERÍA MECÁNICA E INDUSTRIAL':
                record.siglas = 'fimi'
            elif record.area_base_id.name == 'FACULTAD DE CONSTRUCCIONES':
                record.siglas = 'foc'
            elif record.area_base_id.name == 'FACULTAD DE INGENIERÍA ELÉCTRICA':
                record.siglas = 'Fie'
            elif record.area_base_id.name == 'FACULTAD DE CIENCIAS ECONÓMICAS Y EMPRESARIALES':
                record.siglas = 'FCEE'
            elif record.area_base_id.name == 'FACULTAD DE LENGUAS EXTRANJERAS':
                record.siglas = 'FLE'
            elif record.area_base_id.name == 'FACULTAD DE HUMANIDADES':
                record.siglas = 'fh'
            elif record.area_base_id.name == 'FACULTAD DE CIENCIAS SOCIALES':
                record.siglas = 'fsc'
            elif record.area_base_id.name == 'FAC DE INGENIERIA EN TELECOMUNICACIONES INFORMATICA Y BIOMEDICA':
                record.siglas = 'fitib'
            elif record.area_base_id.name == 'DEPARTAMENTO DE HISTORIA Y PATRIMONIO UNIVERSITARIO':
                record.siglas = 'dhpu'
            elif record.area_base_id.name == 'DEPARTAMENTO DE TRANSFERENCIA Y COMERCIALIZACIÓN':
                record.siglas = 'dtyc'
            elif record.area_base_id.name == 'DEPARTAMENTO DE ENSEÑANZA MILITAR':
                record.siglas = 'dem'
            elif record.area_base_id.name == 'DEPARTAMENTO DE PROTOCOLO':
                record.siglas = 'dprotocolo'
            elif record.area_base_id.name == 'DEPARTAMENTO DE EVENTO(DEPARTAMENTO NO DOCENTE)':
                record.siglas = 'dend'
            elif record.area_base_id.name == 'DEPARTAMENTO DE AUDITORÍA':
                record.siglas = 'dauditoria'
            elif record.area_base_id.name == 'DEPARTAMENTO JURÍDICO':
                record.siglas = 'djuridico'
            elif record.area_base_id.name == 'DIRECCIÓN DE PREPARACIÓN Y SUPERACIÓN DE CUADROS':
                record.siglas = 'dpsc'
            elif record.area_base_id.name == 'DIRECCIOÓN DE INFORMACIÓN Y GESTIÓN DOCUMENTAL':
                record.siglas = 'digd'
            elif record.area_base_id.name == 'DIRECCIÓN DE COMUNICACIÓN INSTITUCIONAL':
                record.siglas = 'dci'
            elif record.area_base_id.name == 'DIRECCIÓN DE RELACIONES INTERNACIONALES':
                record.siglas = 'dri'
            elif record.area_base_id.name == 'DIRECCIÓN DE CIENCIAS TECNOLOGÍA E INNOVACIÓN':
                record.siglas = 'dcti'
            elif record.area_base_id.name == 'DIRECCIÓN DE EDUCACIÓN DE POSTGRADO':
                record.siglas = 'dep'
            elif record.area_base_id.name == 'DIRECCIÓN DE INFORMACIÓN CIENTÍFICO TÉCNICO':
                record.siglas = 'dict'
            elif record.area_base_id.name == 'DIRECCIÓN DE HISTORIA Y MARXISMO-LENINISMO':
                record.siglas = 'dhml'
            elif record.area_base_id.name == 'DIRECCIÓN DE FORMACIÓN DE PREGRADO':
                record.siglas = 'dfp'
            elif record.area_base_id.name == 'DIRECCIÓN DE EXTENSIÓN UNIVERSITARIA':
                record.siglas = 'deu'
            elif record.area_base_id.name == 'DIRECCIÓN DE ORGANIZACIÓN PLANIFICACIÓN EVALUACIÓN Y CALIDAD':
                record.siglas = 'dopec'
            elif record.area_base_id.name == 'DIRECCIÓN DE DEFENSA Y SEGURIDAD SEDE JULIO ANTONIO MELLA':
                record.siglas = 'ddssjam'
            elif record.area_base_id.name == 'DIRECCIÓN DE DEFENSA Y SEGURIDAD SEDE ANTONIO MACEO':
                record.siglas = 'ddssam'
            elif record.area_base_id.name == 'DIRECCIÓN DE CUADROS':
                record.siglas = 'dcuadros'
            elif record.area_base_id.name == 'DIRECCIÓN DE ALOJAMIENTO':
                record.siglas = 'daloj'
            elif record.area_base_id.name == 'DIRECCIÓN GENERAL DE RESIDENCIAS ESTUDIANTILES':
                record.siglas = 'dgre'
            elif record.area_base_id.name == 'GRUPO DE AHORRO Y USO DE ENERGÍA':
                record.siglas = 'gaue'
            elif record.area_base_id.name == 'DIRECCIÓN DE SEDE ANTONIO MACEO':
                record.siglas = 'dsam'
            elif record.area_base_id.name == 'DIRECCIÓN DE SEDE JULIO ANTONIO MELLA':
                record.siglas = 'dsjam'
            elif record.area_base_id.name == 'DEPARTAMENTO POLIGRÁFICO':
                record.siglas = 'dp'
            elif record.area_base_id.name == 'DIRECCIÓN DE TRANSPORTE':
                record.siglas = 'dt'
            elif record.area_base_id.name == 'DIRECCIÓN DE INVERSIONES Y MANTENIMIENTO':
                record.siglas = 'dim'
            elif record.area_base_id.name == 'DIRECCIÓN DE LOGÍSTICA':
                record.siglas = 'dl'
            elif record.area_base_id.name == 'DIRECCIÓN GENERAL DE ADMINISTRACIÓN Y SERVICIOS':
                record.siglas = 'dgas'
            elif record.area_base_id.name == 'DIRECCIÓN ECONÓMICA':
                record.siglas = 'deco'
            elif record.area_base_id.name == 'DIRECCIÓN DE RECURSOS HUMANOS':
                record.siglas = 'drh'
            elif record.area_base_id.name == 'DIRECCIÓN GENERAL ECONÓMICA':
                record.siglas = 'dge'
            elif record.area_base_id.name == 'PUESTO DE DIRECCION':
                record.siglas = 'pd'
            elif record.area_base_id.name == 'SECRETARÍA GENERAL':
                record.siglas = 'sg'
            elif record.area_base_id.name == 'RECTORADO':
                record.siglas = 'rectorado'
            elif record.area_base_id.name == 'CBM':
                record.siglas = 'cbm'
            elif record.area_base_id.name == 'CNEA':
                record.siglas = 'cnea'
            elif record.area_base_id.name == 'CENTRO DE ESTUDIO DE BIOTECNOLOGIA INDUSTRIAL':
                record.siglas = 'cebi'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL GUAMÁ':
                record.siglas = 'cum_g'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL JULIO ANTONIO MELLA':
                record.siglas = 'cum_sjam'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL TERCER FRENTE':
                record.siglas = 'cum_tf'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL SEGUNDO FRENTE':
                record.siglas = 'cum_sf'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL SAN LUIS':
                record.siglas = 'cum_sl'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL SONGO LA MAYA':
                record.siglas = 'cum_sm'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL CONTRAMAESTRE':
                record.siglas = 'cum_c'
            elif record.area_base_id.name == 'CENTRO UNIVERSITARIO MUNICIPAL PALMA SORIANO':
                record.siglas = 'cum_ps'
            elif record.area_base_id.name == 'FACULTAD DE CONSTRUCCIONES':
                record.siglas = 'contrucciones'
            elif record.area_base_id.name == 'DIRECCIÓN DE RESIDENCIA ESTUDIANTIL SEDE ANTONIO MACEO':
                record.siglas = 'dream'
            elif record.area_base_id.name == 'DIRECCIÓN DE RESIDENCIA ESTUDIANTIL SEDE JULIO ANTONIO MELLA':
                record.siglas = 'drejam'
            else:
                record.siglas = False

    categorias = fields.Selection(
        string='Categorías',
        selection=[('cuadro', 'Cuadro'),
                   ('funcionario', 'Funcionario'),
                   ('investigador', 'Investigador'),
                   ('profesor', 'Profesor'),
                   ('trabajador', 'Trabajador'),
                   ('estudiante', 'Estudiante'),
                   ],compute='_compute_category_ocupational')

    @api.depends('work_position_id')
    def _compute_category_ocupational(self):
        for record in self:
            print(record.work_position_id.name)

            if record.categoria_ocupacional == 'Cuadros Intermedio':
                record.categorias = 'cuadro'
            elif record.categoria_ocupacional == 'dro Ejecutivo':
                record.categorias = 'cuadro'
            elif record.categoria_ocupacional == 'Administrativos':
                record.categorias = 'cuadro'
            elif record.categoria_ocupacional == 'Cuadros Dir. Sup':
                record.categorias = 'cuadro'
            elif record.categoria_ocupacional == 'Cuadro directivo':
                record.categorias = 'cuadro'
            elif record.categoria_ocupacional == 'Cuadro':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'DIRECTOR':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'DECANO':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'RECTOR':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'VICEDECANO':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'JEFE DE DEPARTAMENTO DOCENTE':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'DIRECTOR DE CENTRO DE ESTUDIO':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'DIRECTOR UNIVERSITARIO MUNICIPAL':
                record.categorias = 'cuadro'
            elif record.work_position_id.name == 'JEFE DE DEPARTAMENTO':
                record.categorias = 'cuadro'
            elif record.funcionario == True:
                record.categorias = 'funcionario'
            elif record.investigador == True:
                record.categorias = 'investigador'
            elif record.is_professor == True:
                record.categorias = 'profesor'
            elif record.is_work == True:
                record.categorias = 'trabajador'
            elif record.is_student == True:
                record.categorias = 'estudiante'
            else:
                record.categorias = False

    qr_code = fields.Binary('QRcode', compute="_generate_qr")

    @api.depends('qr_code')
    def _generate_qr(self):
        "method to generate QR code"
        for rec in self:
            if qrcode and base64:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=50,
                    border=3,
                )
                qr.add_data("Nombre : ")
                qr.add_data(rec.given_name)
                qr.add_data(", Apellidos : ")
                qr.add_data(rec.last_name)
                qr.add_data(", CI: ")
                qr.add_data(rec.carne_id)
                # qr.add_data(", Nomina : ")
                # qr.add_data(rec.no_trabajador)
                qr.add_data(", Categorias : ")
                qr.add_data(rec.categorias)
                qr.add_data(", Cargo : ")
                qr.add_data(rec.work_position_id.name)
                qr.add_data(", Area Base : ")
                qr.add_data(rec.area_base_id.name)
                qr.make(fit=True)
                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                rec.update({'qr_code': qr_image})