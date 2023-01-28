# Currency conversion api
 A mid-market currency converter API using FastAPI
 
# Getting Started

 # Installation
 1. clone the repository
 
 `git clone https://github.com/balogvn/currency-conversion-api.git`
 
 2. Install the dependencies
 
 `pip install -r requirements.txt`
 
# Running the app
1. Start the application

`uvicorn shake:api --reload`

2. Open the API documentation
The API documentation will be available at http://localhost:8000/docs

You can test the endpoints using the interactive documentation provided by the Swagger UI.

# Usage
Make sure the server is running, and then you can use the endpoints by sending HTTP requests to the appropriate paths. You will need to provide a valid API key in the query parameter apiKey for all endpoints.

Endpoints:

/convert: Convert an amount from one currency to another.

/currencies: Get a list of all available currencies.

/history: Get a list of all previous conversions.

# Contact
Kayode Balogun - balogvn@gmail.com



