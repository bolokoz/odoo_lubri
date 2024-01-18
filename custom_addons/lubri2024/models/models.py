# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class lubri2024(models.Model):
#     _name = 'lubri2024.lubri2024'
#     _description = 'lubri2024.lubri2024'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
