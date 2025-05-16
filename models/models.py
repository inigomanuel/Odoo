# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    lang = fields.Selection([
        ('en_US', 'English'),
        ('es_ES', 'Español'),
    ], string="Idioma")

class Subordinados(models.Model):
    _name = "prueba.subordinados"
    _description = "Tabla de Esclavos"

    name = fields.Char(string="Nombre",required=True)
    age = fields.Integer(string="Edad")
