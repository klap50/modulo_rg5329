# rg5329 impuesto ARGENTINA

# Módulo Odoo: rg5329_klap

## 📌 Descripción

Este módulo implementa la percepción impositiva RG 5329 dispuesta por la AFIP en Argentina, con el objetivo de aplicar automáticamente un **3% adicional** sobre ciertos productos alcanzados, **solo en casos en los que la factura de ventas supere los $3000 en impuestos**.

---

## 🧾 ¿Qué hace este módulo?

- Crea un nuevo **grupo de impuestos** llamado **"Percepciones RG 5329"**.
- Crea un nuevo **impuesto de ventas** llamado **"Percepción RG 5329 - PAIS 3%"**, que aparece como seleccionable en productos.
- Agrega un **checkbox en los productos** para indicar si deben estar sujetos a esta percepción.
- Aplica automáticamente el impuesto RG 5329 en facturas de **ventas** si:
  - El producto tiene el checkbox activado, **y**
  - El total de impuestos de la factura supera los **$3000 ARS**.

---

## 🧠 Lógica automática

Durante la carga de líneas de factura:

- Se evalúa si el total de impuestos de la factura supera $3000.
- Si la condición se cumple:
  - Se agrega automáticamente el impuesto del 3% a las líneas que tienen el producto marcado con el campo “Aplicar Percepción RG 5329”.
- Si no se cumple:
  - Se remueve automáticamente dicho impuesto si estaba aplicado.

---

## ✅ Requisitos

- Odoo 15 o superior
- Módulo `account` instalado (dependencia base de contabilidad)

---

## 🚀 Instalación

1. Copiar la carpeta `rg5329_tax_module` al directorio de addons de tu instancia Odoo.
2. Reiniciar el servidor de Odoo.
3. Activar el modo desarrollador.
4. Ir a **Apps**, actualizar la lista de aplicaciones.
5. Buscar e instalar **rg5329_klap**.

---

## 🧪 Cómo probarlo

1. Ir a **Productos > Productos**.
2. Editar un producto y tildar el checkbox “Aplicar Percepción RG 5329”.
3. Crear una **factura de cliente** (venta) con productos seleccionados.
4. Si el total de impuestos supera los $3000, se agregará automáticamente el impuesto “Percepción RG 5329 - PAIS 3%” a la línea correspondiente.

---

## 🔒 Licencia

Licencia: LGPL-3

---

## 👤 Autor

- **Nombre**: Klap / FwCorp  
- **Sitio Web**: [https://fwcorp.com.ar](https://fwcorp.com.ar)  
- **Año**: 2025

---

Para el culo roto de Mieli que mete impuesto en donde puede para intentar rescatar su corrida bancaria y lo unico que logro fue una corrida en su cola.
