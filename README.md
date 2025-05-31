# 20th Century Video Games

> *Conservamos la historia del videojuego, pieza a pieza.*

---

## 🎯 Visión

**20th Century Video Games** es un museo digital de código abierto dedicado a catalogar y preservar consolas, ordenadores, juegos físicos y juegos de mesa editados entre 1970-Actualidad. Nuestro objetivo es ofrecer una referencia fiable con fotografías en alta resolución, precios de mercado, documentación escaneada y contexto histórico para cada pieza de la colección.

## 🛠️ Tecnologías principales

| Capa       | Herramientas                                                           |
| ---------- | ---------------------------------------------------------------------- |
| Backend    | **Django 5.2** · PostgreSQL / SQLite · Django REST Framework (roadmap) |
| Front‑end  | **Bootstrap 5** + crispy‑bootstrap5 · HTMX · Alpine.js                 |
| Dev Ops    | Docker · Gunicorn · Nginx · GitHub Actions CI/CD                       |
| Multimedia | sorl‑thumbnail · Pillow‑SIMD                                           |

## ✨ Funcionalidades (MVP)

* Catálogo de **consolas**, **ordenadores**, **videojuegos físicos** y **juegos de mesa**.
* Soporte a múltiples **fotos** por artículo, con miniaturas WebP y carga perezosa.
* Atributos de coleccionista: edición, región (PAL/NTSC), estado, precios histórico/mercado.
* Buscador y filtros avanzados (django‑filter).
* Línea temporal interactiva de hitos del videojuego.
* Panel de administración completo para CRUD.

## 🚀 Demo

> *Próximamente*: deploy automático a `20thcenturyvideogames.com`.

## 🏁 Primeros pasos

```bash
# 1. Clona el repositorio
$ git clone https://github.com/danimap27/20thCenturyVideoGames.git
$ cd 20th-century-video-games

# 2. Crea y activa entorno virtual
$ python -m venv .venv
$ source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Instala dependencias
$ pip install -r requirements.txt

# 4. Aplica migraciones y carga datos de ejemplo
$ python manage.py migrate
$ python manage.py loaddata sample_fixture.json

# 5. Crea superusuario y arranca el servidor
$ python manage.py createsuperuser
$ python manage.py runserver
```

Accede a [http://127.0.0.1:8000](http://127.0.0.1:8000) y explora la colección.

## 🗂️ Estructura básica del proyecto

```
.
├── catalog/            # Modelos, vistas y urls de coleccionables
├── mediafiles/         # App de fotos y documentos
├── museum/             # Configuración global Django (settings, urls, wsgi)
├── docker/             # Dockerfile, nginx, gunicorn
├── docs/               # Documentación adicional y auditoría de la web original
└── ...
```

## 🛣️ Roadmap

Consulta el tablero de [GitHub Projects](https://github.com/users/danimap27/projects/5) para ver el progreso y las *issues* activas.

## 🤝 Contribuir

1. Abre una *issue* para proponer cambio o reportar bug.
2. Haz un **fork** y crea una rama descriptiva: `feat/añadir-timeline`.
3. Asegúrate de que `pytest` pasa localmente y cubre tu código.
4. Envía un **Pull Request**.

## 📝 Licencia

Publicado bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más información.

## 🙌 Créditos y agradecimientos

Proyecto inspirado en la web original *20thCenturyVideoGames.com* (2004‑2024). Agradecemos a todos los coleccionistas y colaboradores que mantienen vivo el legado retro‑gamer.
