# Clase 2

## Descripción general

- Instalar Python desde la web oficial.
- Marcar la casilla "Add Python to PATH" y luego instalar.

En VS Code:

- Ir a extensiones (`Ctrl + Shift + X`).
- Buscar Python.
- Instalar la extensión oficial de Microsoft.

Luego, crear una aplicación de prueba de Python en un repositorio de prueba y probar un "Hola Mundo".

- Instalar Git desde la web oficial.
- Realizar por única vez la configuración global.

Luego se crea el entorno virtual, se instalan y registran las dependencias y se activa el entorno virtual.

Ver si se instaló la librería de Python para manejar el tráfico HTTP de web y APIs:

```bash
pip show requests
```

Si te informa que `Package not found: requests`, se instala con:

```bash
pip install requests
```

## Comandos utilizados en esta clase

## Configurar el entorno virtual

Escribir en terminal:

```bash
python -c "import sys; print(sys.executable)"
```

```bash
py -m venv .venv
```

```bash
.venv\Scripts\activate
```

Para desactivarlo:

```bash
deactivate
```

```bash
python -c "import sys; print(sys.executable)"
```

## Instalar dependencias

```bash
pip install requests
```

```bash
pip list
```

## Para guardar requirements

```bash
pip freeze > requirements.txt
```

Para reconstruir el entorno en otra máquina con el requirements:

```bash
pip install -r requirements.txt
```

## Crear .gitignore

```gitignore
.venv
__pycache__/
```

## Comandos para crear una rama local

```bash
git init
```

```bash
git status
```

Esto sirve para ver en qué rama estamos parados. Lo lógico es que esté en `main`.

Si dice `master`, entonces se debe renombrar la rama local:

```bash
git branch -M "Nombre nuevo de rama"
```

```bash
git add .
```

```bash
git commit -m "Primer commit"
```
