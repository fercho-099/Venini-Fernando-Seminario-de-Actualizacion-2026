# App Streamlit mínima

## Descripción general

- Se creó una cuenta en Render, una plataforma similar a Hugging Face para desplegar proyectos Gradio y otros.
- Se configuró el puerto en `demo.launch`.
- Render permite que la app siga funcionando aunque la PC esté apagada.

Usando otros frameworks:

- Se creó un proyecto con Streamlit, un framework similar a Gradio, pero llamado Streamlit.
- Se creó una cuenta en Streamlit.

Este proyecto es una aplicación mínima creada con Streamlit, un framework para desarrollar y desplegar aplicaciones web de Python de forma sencilla, similar a Gradio pero orientado a dashboards e interfaces interactivas.

## Requisitos

- Python 3.11 o superior
- Entorno virtual

## Crear el entorno virtual

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá en el navegador por defecto.
