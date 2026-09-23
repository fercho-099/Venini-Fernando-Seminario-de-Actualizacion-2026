# Clase 3

## Descripción general

- Se creó una cuenta y repositorio en GitHub.
- Se vinculó el repositorio local con nuestra cuenta de GitHub.

## Conectar repositorio local con GitHub

Se debe crear un repositorio nuevo a través de "New" en GitHub y:

- No Add Readme
- No Add .gitignore (de esta manera no habrá conflicto con el README y .gitignore del repositorio local)

Una vez creado el repositorio de GitHub, este queda vacío:

```bash
git remote add origin <url>
```

La `url` es la del repositorio de GitHub que creamos.

```bash
git push origin main
```

o

```bash
git push -u origin main
```

Esto asocia la rama local `main` con la del remoto y, luego, cada vez que hagas cambios, basta con:

```bash
git push
```

Así queda configurado `main` local con `main` remoto.
