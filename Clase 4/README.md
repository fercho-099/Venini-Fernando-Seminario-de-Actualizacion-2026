# Clase 4

## Descripción general

Si anteriormente no se hizo la implementación de Gradio, se realiza la adaptación del código a Gradio para deployarla luego en Hugging Face.

- Se creó una cuenta de Hugging Face y un nuevo space.
- Se realizó el token de seguridad en Hugging Face.
- Se lo vinculó, al igual que GitHub, con un alias diferente, a Hugging Face.
- Se resolvieron conflictos de `README.md` entre el repositorio local y Hugging Face.
- Se deployó la app desde Hugging Face.
- Se hizo uso de `gradio.Blocks` en el repositorio local.

## Deploy en Hugging Face

El proyecto de la clase 3 lo vamos a deployar en Hugging Face. Para eso:

- Crear cuenta de Hugging Face
- Clickear en tu perfil y luego "New space"
- Completar el nombre del space, la licencia y seleccionar Gradio
- Abajo seleccionar CPU básico y visibilidad pública

Luego vamos a crear un token que nos permite vincular el repositorio local con el space:

- Icono de perfil
- Settings
- Access Tokens
- Create new token
- Seleccionar permiso de escritura
- Copiar y guardar el token en un notepad porque, si no, se debe eliminar y crear uno nuevo

Para conectar el repositorio desde nuestro IDE:

```bash
git remote add space <url del space>
```

Modificar a mano el archivo `README.md` del Hugging Face que hace por defecto y agregar la información que se encuentra en el `README.md` de esta carpeta.

```bash
git push space main
```

---
title: Seminario Actualizacion
emoji: 📊
colorFrom: red
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
