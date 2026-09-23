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

## Posibles errores que fueron solucionados

Al crear un nuevo repositorio, el entorno virtual quedó "atado" a otra carpeta, por lo que es necesario reinstalar el entorno virtual en el nuevo repositorio.

- Ir a la carpeta donde están los archivos de nuestra app.
- Instalar el entorno virtual:

```powershell
python -m venv .venv
```

- Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

- Instalar dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para hacer funcionar la app en modo local ejecutamos:

```powershell
streamlit run app.py
```

Desde nuestro VS Code, en la consola, nos da una URL local y ahí podemos ver la aplicación.

**La url de streamlit en cloud es: https://appprueba-526jbeljq2zxduhvpzyxxp.streamlit.app/**
