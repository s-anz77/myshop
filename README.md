# MyShop

A small shop demonstration built as a Vue frontend backed by a Django REST Framework API. The frontend displays a product catalogue, keeps a shopping basket in browser local storage, and submits orders to the API. The project does not connect to an online payment system; orders are a simulation.

**Live frontend:** [anzore-shop.up.railway.app](https://anzore-shop.up.railway.app/)

**Live API:** [anzore-shop-api.up.railway.app](https://anzore-shop-api.up.railway.app/)

## Features

- Load and display products from the API.
- Add products to a basket, remove them, and clear the basket; basket contents persist in browser local storage.
- Submit an order with customer name, email, phone number, selected items, and total.
- Edit product details through the frontend's product edit form.
- Browse the frontend's home, items, order, shipping, and about views.

## Tech stack

- Backend: Python 3.15, Django 6.1, Django REST Framework, SQLite
- Frontend: Node.js 22.18+ or 24.12+, Vue 3, Vue Router, Axios, Vite
- WhiteNoise and Gunicorn for backend deployment

## Prerequisites

- Python 3.15 and pip
- Node.js `^22.18.0 || >=24.12.0` and npm

## Backend setup

From the repository root, create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
$env:SECRET_KEY = "replace-with-a-local-secret"
```

macOS/Linux:

```bash
source .venv/bin/activate
export SECRET_KEY="replace-with-a-local-secret"
```

Install dependencies, create the local database, and start Django:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The backend requires `SECRET_KEY` at startup. The checked-in settings also restrict `ALLOWED_HOSTS` and CORS origins to the deployed API and frontend domains, so local browser access from a different origin may require updating those settings.

## Frontend setup

In a second terminal:

```bash
cd public
npm install
npm run dev
```

Vite prints the local address when the development server starts. To create a production build, run `npm run build` from `public/`.

The frontend currently requests the API at `https://anzore-shop-api.up.railway.app`; this URL is set in the Vue source. The backend's API routes are `/api/items/`, `/api/order/`, and `/api/edit/<slug>/`.

## Project structure

- `main/` — product and order models, serializers, API views, and routes.
- `myshop/` — Django settings and root URL configuration.
- `public/src/` — Vue application, views, and components.
- `public/package.json` — frontend dependencies and Vite scripts.
- `manage.py` — Django management commands.

