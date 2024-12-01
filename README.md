# FastAPI EMI Calculator

A simple API for calculating Equated Monthly Installments (EMI) for loans, built using FastAPI.

## Features

- Calculate EMI based on principal amount, interest rate, loan duration, and optional down payment.
- Fast and efficient API.
- Easily deployable on platforms like Render or Heroku.

## API Endpoints

### `POST /emi`

**Request Body**:
  ```json
  {
    "amount": float,       // Principal loan amount
    "duration": int,       // Loan tenure in months
    "rate": float,         // Annual interest rate as a fraction (e.g., 0.1 for 10%)
    "down_payment": float  // Optional down payment, default is 0
  }
  ```

## Response
  ```
  {
    "EMI": float  // Monthly EMI amount
  }
  ```

## Example Request
  ```
  {
  curl -X POST "http://localhost:8000/emi" \
  -H "Content-Type: application/json" \
  -d '{"amount": 100000, "duration": 12, "rate": 0.1, "down_payment": 20000}'
  
  }
  ```

## Example Response
```
  {
    "EMI": 7118.15
  }
```

## Running the Application

### Prerequisites
    - Python 3.9 or higher
    - pip for managing Python packages

### Installation
    1. Clone the repository:
      ``` 
      {
        git clone https://github.com/yourusername/fastapi-emi-calculator.git
        cd fastapi-emi-calculator
      }
      ```
    2. Install dependencies:
      ```
      {
        pip install -r requirements.txt
      }
      ```
    3. Run the application:
    ```
    {
      uvicorn main:app --reload
    }
    ```
    4. Access the API documentation:
      - Swagger UI: http://127.0.0.1:8000/docs
      - ReDoc: http://127.0.0.1:8000/redoc

## Deployment

###  Render
      - Add a render.yaml file with the following content:

      ```
      {
      services:
        - type: web
          name: fastapi-emi-calculator
          env: python
          buildCommand: ""
          startCommand: uvicorn main:app --host 0.0.0.0 --port 8000
      }
      ```
