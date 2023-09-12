# Pokémon API

## Overview
A FastAPI-powered RESTful API for querying Pokémon data.

## Features
- Asynchronous SQLAlchemy for database operations
- Pydantic models for serialization
- Customizable logging configuration, including SQLAlchemy query logging

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- PostgreSQL database (with credentials)

### Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/jeevandhakal/pokemon.git
   cd pokemon
2. Create a virtual environment (recommended):
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the project dependencies:
   ```shell
   pip install -r requirements.txt
4. Create a PostgreSQL database and update the database URL in `.env`:
   ```shell
   DATABASE_URL=postgresql+asyncpg://username:password@localhost/database_name
   DEBUG=True
5. Run the Uvicorn server:
   ```shell
   make serve
6. Access the API at `http://localhost:8000/docs` for interactive documentation.

## Usage

### List Pokémon
- **GET** `/pokemons/`
  - Retrieve a list of Pokémon.
  - Query parameters:
    - `limit` (int, optional): Limit the number of results.
    - `offset` (int, optional): Offset the results.
    - `type` (string, optional): Filter Pokémon by type.
    - `name` (string, optional): Filter Pokémon by name.

### Example API Request
- Use `curl` to make a request with query parameters:

#### List Pokémon (with filtering)
```shell
curl -X GET "http://localhost:8000/pokemons/?limit=10&offset=0&type=electric&name=pikachu"

