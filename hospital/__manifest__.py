# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "módulo para odoo 17 community que permita gestionar pacientes y médicos de un hospital.",

    'description': """
Este módulo nos permitirá gestionar pacientes y médicos en un hospital

Para cada paciente, tendremos un modelo con los siguientes datos:
● Nombre y apellidos del paciente.
● Síntomas.

Para cada médico, tendremos un modelo con los siguientes datos:
● Nombre y apellidos del médico.
● Número de colegiado.

Por cada vez que un médico ha atendido a un paciente, tendremos un modelo indicando el diagnóstico.
Un paciente puede haber sido atendido por varios médicos y un médico puede haber atendido a varios pacientes.


    """,

    'author': "Adrián Abeijón Carbajo",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/hospital.xml'
        #'views/views.xml',
        'views/citas.xml',
        "views/paciente.xml",
        "views/medico.xml",
        "views/menu.xml",
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

