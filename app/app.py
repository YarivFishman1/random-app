from fastapi import FastAPI, Query
import math
from typing import List

app = FastAPI()


@app.get('/welcome')
async def welcome(name: str):
    return f'Welcome {name}'


@app.get('/factorial')
async def factorial(number: int):
    return math.factorial(number)


@app.get('/sort')
async def sort(numbers: List[int] = Query(None)):
    numbers.sort()
    return numbers
