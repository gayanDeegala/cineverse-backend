# cineverse-backend

## API Server

### Run the live server:
`uvicorn main:app --reload`

### Check it
Open your browser at http://127.0.0.1:8000

### Interactive API docs
Go to http://127.0.0.1:8000/docs.

Alternative
Go to http://127.0.0.1:8000/redoc

### OpenAPI and JSON Schema
You can see it directly at: http://127.0.0.1:8000/openapi.json

## Database

## Create mysql-server
To install MySQL, run the following command from a terminal prompt:
`sudo apt install mysql-server`

quick check: `sudo service mysql status`

start the server: `sudo service mysql restart`