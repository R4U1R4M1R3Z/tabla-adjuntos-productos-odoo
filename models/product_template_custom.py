# -*- coding:utf-8 -*-
from odoo import api, fields, models

class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    attachment_ids = fields.Many2many('product.attachment', string='Adjuntos')
    

class ProductAttachment(models.Model):
    _name = 'product.attachment'
    
    attachment = fields.Binary(string='Adjunto')
    attachment_filename = fields.Char(string='Nombre del adjunto')
    date = fields.Datetime(string='Fecha', default=fields.Datetime.now)
