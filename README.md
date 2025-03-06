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
        'views/views.xml',
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

## 4) Model


<br></br>
[Volver al inicio](#índice) 

## 5) Views


<br></br>
[Volver al inicio](#índice) 

## 6)  


<br></br>
[Volver al inicio](#índice) 















