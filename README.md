# Flask-RESTful and React Application

## Project Overview

This project is an application built with Flask-RESTful for the backend and React for the frontend. It is designed to manage episodes, guests, and their appearances on a show. The application provides a RESTful API.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Features

- Create, Read, Update, and Delete (CRUD) operations for episodes, guests, and appearances.
- Rate guest appearances in episodes.
- Responsive frontend built with React.
- RESTful API built with Flask-RESTful.
- Environment variable configuration for easy setup.

## Technologies

- **Backend**: Flask, Flask-RESTful, SQLAlchemy
- **Database**: SQLAlchemy (for development), PostgreSQL (for production)
- **Deployment**: Render.com
- **Environment**: Python 3.x, Node.js

## Installation

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nathanchepkonga/late-show-challenge.git
   cd backend

2. **Create a virtual environment:**

   ```bash
   python -m venv venv

3. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

5. **Create a .env file in the backend folder:**
   ```bash
   DATABASE_URL=sqlite:///database.db  

6. **Run database migrations**
   ```bash
   flask db upgrade


 ### Start the backend server
   ```bash
   cd backend
   Python app.py




