# -*- coding: utf-8 -*-
from odoo import models, fields


class TmCategory(models.Model):
    _name = 'tm.category'
    _description = 'Time Management Category'
    _order = 'sequence, name'

    name = fields.Char(string='Category Name', required=True, translate=True)
    code = fields.Char(string='Code', size=10)
    sequence = fields.Integer(string='Sequence', default=10)
    color = fields.Integer(string='Color')
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Category name must be unique!'),
        ('code_uniq', 'unique(code)', 'Category code must be unique!'),
    ]
