# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:31:56 2024

@author: ASHNER_NOVILLA
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class EMIRequest(BaseModel):
    amount: float  # Principal loan amount
    duration: int  # Loan tenure in months
    rate: float  # Annual interest rate as a fraction (e.g., 0.1 for 10%)
    down_payment: float = 0  # Optional down payment, default is 0

def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    monthly_rate = rate / 12  # Convert annual rate to monthly rate
    emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** duration) / \
          (((1 + monthly_rate) ** duration) - 1)
    return round(emi, 2)

@app.post("/emi")
def calculate_emi(request: EMIRequest):
    emi = loan_emi(request.amount, request.duration, request.rate, request.down_payment)
    return {"EMI": emi}
