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


<h2> Response </h2>

