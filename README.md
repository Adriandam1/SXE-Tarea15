# SXE-Tarea15

## Índice  
1. [Enunciado](#1-enunciado)  
2. [Creación módulo]
3. [3]
4. [4]
5. [5]
6. [6]  

<br></br>
## 1) Enunciado  

Crea un módulo para odoo 17 community que permita gestionar pacientes y médicos de un hospital.  

Para cada paciente, tendremos un modelo con los siguientes datos:  
● Nombre y apellidos del paciente.  
● Síntomas.  

Para cada médico, tendremos un modelo con los siguientes datos:  
● Nombre y apellidos del médico.  
● Número de colegiado.  

Por cada vez que un médico ha atendido a un paciente, tendremos un modelo indicando el diagnóstico.  
Un paciente puede haber sido atendido por varios médicos y un médico puede haber atendido a varios pacientes.  

Implementa los modelos y las vistas que consideres adecuadas para los 3 modelos.  

Entrega el módulo. Para ser considerado APTO debe poder ser instalado sin errores en cualquier instalación de Odoo 17 community. No es obligatorio pero si es recomendable de cara a la realización de pruebas, que tenga datos de demo al instalarse en modo demo.  

La copia total o parcial del módulo de un compañero supondrá un NO APTO. Igual que el uso de ChatGPT u otro tipo de herramientas de Inteligencia Artificial Generativa.  

<br></br>
[Volver al inicio](#índice) 

-------------------------------
## 2) Creación módulo *hospital*:
* Acceder a nuestro contenedor a nuestro contenedor de odoo
```bash
docker exec -it odooWebContainer /bin/bash
```

* Una vez dentro del contenedor, crea el módulo ejecutando el siguiente comando:
```bash
odoo scaffold hospital /mnt/extra-addons/
```

* Dar permisos a la carpeta del módulo:
```bash
chmod 777 -R /mnt/extra-addons/hospital
```

<br></br>
[Volver al inicio](#índice) 

## 3) Modificamos nuestro manifest:
Simplemente añadimos la descripción del módulo y descomentamos la linea de security para otorgar permisos:
<details><summary>🔍 SPOILER:</summary>  

```bash
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
```
</details>

<br></br>
[Volver al inicio](#índice) 

## 4) Creamos nuestro Model
Creamos 3 clases: **Paciente**, **Medico** y **CITAS**

<details><summary>🔍 SPOILER:</summary>  
    
```bash
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
```
</details>

<br></br>
[Volver al inicio](#índice) 

## 5) Creacion de nuestros Views
En este caso, debido a que el código era un poco extenso, he preferido separar las views en 4 archivos, separando las views de paciente, medico, cita y los menús. Tal y como estaba organizado en el ejemplo proporcionado.

**View Paciente:**

<details><summary>🔍 SPOILER:</summary>  

```bash
<odoo>
    <data>
        <!-- Vistas Paciente Tree -->
        <record id="view_paciente_tree" model="ir.ui.view">
            <field name="name">hospital.paciente.tree</field>
            <field name="model">hospital.paciente</field>
            <field name="arch" type="xml">
                <tree string="Pacientes">
                    <field name="name"/>
                    <field name="apellidos"/>
                    <field name="sintomas"/>
                </tree>
            </field>
        </record>

        <!-- Vistas Paciente form -->
        <record id="view_paciente_form" model="ir.ui.view">
            <field name="name">hospital.paciente.form</field>
            <field name="model">hospital.paciente</field>
            <field name="arch" type="xml">
                <form string="Paciente">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="apellidos"/>
                            <field name="sintomas"/>
                        </group>
                        <notebook><!-- Esto nos permite mostrar los estudiantes debajo en una pestaña-->
                            <page string="Citas">
                                <field name="citas_ids">
                                    <tree string="Citas">
                                        <field name="medico_id"/>
                                        <field name="diagnostico"/>
                                    </tree>
                            </field>
                        </page>
                </notebook>
                </sheet>
                </form>
            </field>
        </record>
    </data>
</odoo>
```

</details>
<br></br>

**View Medico:**

<details><summary>🔍 SPOILER:</summary>  

```bash
<odoo>
    <data>
        <!-- Vistas para Medico -->
        <record id="view_medico_tree" model="ir.ui.view">
            <field name="name">hospital.medico.tree</field>
            <field name="model">hospital.medico</field>
            <field name="arch" type="xml">
                <tree string="Médicos">
                    <field name="name"/>
                    <field name="apellidos"/>
                    <field name="numero_colegiado"/>
                </tree>
            </field>
        </record>

        <record id="view_medico_form" model="ir.ui.view">
            <field name="name">hospital.medico.form</field>
            <field name="model">hospital.medico</field>
            <field name="arch" type="xml">
                <form string="Médico">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="apellidos"/>
                            <field name="numero_colegiado"/>
                        </group>
                        <notebook><!-- Esto nos permite mostrar los estudiantes debajo en una pestaña-->
                            <page string="Citas">
                                <field name="citas_ids">
                                    <tree string="Citas">
                                        <field name="paciente_id"/>
                                        <field name="diagnostico"/>
                                    </tree>
                                </field>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>

    </data>
</odoo>
```

</details>
<br></br>

**View Citas:**

<details><summary>🔍 SPOILER:</summary>  

```bash
<odoo>
    <data>
        <!-- Vistas para Citas -->
        <record id="view_citas_tree" model="ir.ui.view">
            <field name="name">hospital.citas.tree</field>
            <field name="model">hospital.citas</field>
            <field name="arch" type="xml">
                <tree string="Citas">
                    <field name="paciente_id"/>
                    <field name="medico_id"/>
                    <field name="diagnostico"/>
                </tree>
            </field>
        </record>

        <record id="view_citas_form" model="ir.ui.view">
            <field name="name">hospital.citas.form</field>
            <field name="model">hospital.citas</field>
            <field name="arch" type="xml">
                <form string="Cita">
                    <sheet>
                        <group>
                            <field name="paciente_id"/>
                            <field name="medico_id"/>
                        </group>
                        <group>
                            <field name="diagnostico"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>
    </data>
</odoo>
```

</details>
<br></br>

**Menus:**

<details><summary>🔍 SPOILER:</summary>  

```bash
<odoo>
    <data>
        <!-- Acciones -->
        <record id="action_pacientes" model="ir.actions.act_window">
            <field name="name">Pacientes</field>
            <field name="res_model">hospital.paciente</field>
            <field name="view_mode">tree,form</field>
        </record>

        <record id="action_medicos" model="ir.actions.act_window">
            <field name="name">Médicos</field>
            <field name="res_model">hospital.medico</field>
            <field name="view_mode">tree,form</field>
        </record>

        <record id="action_citas" model="ir.actions.act_window">
            <field name="name">Citas</field>
            <field name="res_model">hospital.citas</field>
            <field name="view_mode">tree,form</field>
        </record>

        <!-- Menú -->
        <menuitem id="hospital_menu" name="Hospital"/>
        <menuitem id="menu_hospital_pacientes" name="Pacientes" parent="hospital_menu" action="action_pacientes"/>
        <menuitem id="menu_hospital_medicos" name="Médicos" parent="hospital_menu" action="action_medicos"/>
        <menuitem id="menu_hospital_citas" name="Citas" parent="hospital_menu" action="action_citas"/>
    </data>
</odoo>
```

</details>




<br></br>
[Volver al inicio](#índice) 

## 6)  Demo data

<details><summary>🔍 SPOILER:</summary>  

```bash
<odoo>
    <data>
    <!-- Datos de ejemplo para Pacientes -->
    <record id="demo_paciente1" model="hospital.paciente">
      <field name="name">Mortadelo</field>
      <field name="apellidos">Mortadelez</field>
      <field name="sintomas">Cambia de apariencia en un parpadeo</field>
    </record>

    <record id="demo_paciente2" model="hospital.paciente">
      <field name="name">Filemon</field>
      <field name="apellidos">Filemonez</field>
      <field name="sintomas">Solo le quedan 2 pelos</field>
    </record>

    <!-- Datos de ejemplo para Médicos -->
    <record id="demo_medico1" model="hospital.medico">
      <field name="name">House</field>
      <field name="apellidos">M.D.</field>
      <field name="numero_colegiado">10</field>
    </record>

    <record id="demo_medico2" model="hospital.medico">
      <field name="name">Vilches</field>
      <field name="apellidos">Hospital Central</field>
      <field name="numero_colegiado">6</field>
    </record>

    <!-- Datos de ejemplo para Citas -->
    <record id="demo_cita1" model="hospital.citas">
      <field name="paciente_id" ref="demo_paciente1"/>
      <field name="medico_id" ref="demo_medico1"/>
      <field name="diagnostico">Es un mago del disfraz</field>
    </record>
    
    <record id="demo_cita2" model="hospital.citas">
      <field name="paciente_id" ref="demo_paciente2"/>
      <field name="medico_id" ref="demo_medico2"/>
      <field name="diagnostico">Severo caso de calvicie inminente</field>
    </record>


    </data>
</odoo>

```

</details>

<br></br>
[Volver al inicio](#índice) 















