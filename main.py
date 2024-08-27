from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from PIL import Image

app = FastAPI()

templates = Jinja2Templates(directory="templete")

# Load the dataset
df = pd.read_csv('CarPrice.csv')

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/compare", response_class=HTMLResponse)
async def compare(request: Request, car_name1: str, car_name2: str):
    car1 = df[df['CarName'].str.contains(car_name1, case=False, na=False)]
    car2 = df[df['CarName'].str.contains(car_name2, case=False, na=False)]

    if car1.empty or car2.empty:
        return templates.TemplateResponse("index.html", {"request": request, "error": "One or both car names not found."})

    car1 = car1.iloc[0]
    car2 = car2.iloc[0]

    features = ['price', 'enginesize', 'horsepower', 'citympg', 'highwaympg', 'cylindernumber']
    
    fig, axes = plt.subplots(nrows=1, ncols=len(features), figsize=(20, 5))
    axes = axes.flatten()

    for i, feature in enumerate(features):
        ax = axes[i]
        ax.bar(['Car 1', 'Car 2'], [car1[feature], car2[feature]])
        ax.set_ylabel(feature)
        ax.set_title(f'{feature.capitalize()} Comparison')

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return templates.TemplateResponse("index.html", {"request": request, "img_str": img_str})
