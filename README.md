# Django REST API Project - Contacts API

## Overview

This project is a Django-based REST API that allows users to create, read, update, and delete (CRUD) Contact entries stored in a PostgreSQL database.

It was built to learn and practice Django fundamentals including:
- Setting up a Django project and app
- Connecting Django to a PostgreSQL database
- Running migrations to create database tables
- Building Django Admin functionality
- Building RESTful API endpoints using Django REST Framework
- Organizing project structure across apps, models, serializers, views, and URLs

---

## Project Structure

> Overview of important folders and files:

- **contacts_api/**
  - `admin.py` - Registers the Contact model with Django Admin.
  - `models.py` - Defines the Contact model with fields (name, age).
  - `serializers.py` - Converts Contact model instances into JSON for the API.
  - `views.py` - Handles listing, creating, retrieving, updating, and deleting contacts.
  - `urls.py` - Routes API endpoints `/api/contacts` and `/api/contacts/<id>`.
- **django_rest_api/**
  - `settings.py` - Project settings (database setup, installed apps).
  - `urls.py` - Project-level routing; includes contacts_api routes.
- **manage.py** - Django's command-line utility.
- **README.md** - This project documentation file.

---

## Technologies Used

- **Python 3.11**
- **Django 5.2**
- **Django REST Framework**
- **PostgreSQL 16**
- **psycopg2-binary** (Postgres adapter for Django)

---

## Major Concepts Practiced

- **Virtual Environments** (`ga-env`)  
  Used to isolate project dependencies.

- **PostgreSQL Database Setup**  
  Created a database `django_api`, connected it via Django settings.

- **Migrations**  
  Used `makemigrations` and `migrate` to automatically build SQL tables from models.

- **Django Admin Panel**  
  Created a superuser account and registered the Contact model for admin management.

- **REST API Development**  
  Built API endpoints using Django REST Framework's `generics` class-based views and serializers.

- **Project Structure Best Practices**  
  Organized functionality into apps, views, serializers, models, and modular URLs.

---

## API Endpoints

| Method | URL | Description |
|:---|:---|:---|
| GET | `/api/contacts` | List all contacts |
| POST | `/api/contacts` | Create a new contact |
| GET | `/api/contacts/<id>` | Retrieve a single contact |
| PUT | `/api/contacts/<id>` | Update a contact |
| DELETE | `/api/contacts/<id>` | Delete a contact |

---

