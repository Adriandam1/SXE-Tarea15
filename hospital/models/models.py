# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class soporte(models.Model):
#     _name = 'soporte.soporte'
#     _description = 'soporte.soporte'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente del hospital'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    sintomas = fields.Text(string='Síntomas')
    citas_ids = fields.One2many('hospital.citas', 'paciente_id', string='Citas')

class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Médico del hospital'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    numero_colegiado = fields.Integer(string="Número de Colegiado", required=True)
    citas_ids = fields.One2many('hospital.citas', 'medico_id', string='Citas')

#Por cada vez que un médico ha atendido a un paciente, tendremos un modelo indicando el diagnóstico.
#Un paciente puede haber sido atendido por varios médicos y un médico puede haber atendido a varios pacientes.

class Citas(models.Model):
    _name = 'hospital.citas'
    _description = 'Cita de atención médica'

    paciente_id = fields.Many2one('hospital.paciente', string='Paciente', required=True)
    medico_id = fields.Many2one('hospital.medico', string='Médico', required=True)
    diagnostico = fields.Text(string='Diagnóstico', required=True)