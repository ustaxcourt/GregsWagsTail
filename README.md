# Wagtail Blog Site

A basic blog built with Wagtail CMS.

## Setup

Activate the virtual environment:
```bash
source venv/bin/activate
```

Run migrations:
```bash
python manage.py migrate
```

Start the server:
```bash
python manage.py runserver
```

Admin login: http://localhost:8000/admin/
- Username: admin
- Password: admin123

## What's Included

- Home page
- Blog with posts, authors, and tags
- Image galleries for blog posts
- Search functionality
- Author profiles

## Usage

After logging in, you can:
- Create blog posts under a BlogIndexPage
- Add authors as snippets
- Tag posts for organization
- Upload images to posts

## Tech

- Python 3.12
- Django 5.1
- Wagtail 6.3
