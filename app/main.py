from typing import Optional
from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

import os
from random import randint

from fastapi.responses import FileResponse
import uuid

from app.inference import get_category, plot_category
from datetime import datetime


# -----------------------------------------------------------------------------------------------------------------
# FAST API APPLICATION

app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# Instantiate Jinja2Templates to be able to render HTML files
templates = Jinja2Templates(directory="app/templates")


# -----------------------------------------------------------------------------------------------------------------
 # GET AND POST METHODS

# GET method to render index.html
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #print('GET METHOD IS WORKING JOSE DANIEL')
    return templates.TemplateResponse("index.html", {"request": request})

# POST method to retreive image from the form located in index.html and render it to result.html.
@app.post("/result")
async def create_file(request: Request, file: UploadFile = File(...), ):
    
    
    #file.filename = f"{uuid.uuid4()}"
    contents = await file.read()  # <-- Important!

    IMAGEDIR = "app/static/test_images/"
     # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    
     # get a random file from the image directory
    #files = os.listdir(IMAGEDIR)
    #random_index = randint(0, len(files) - 1)
    #path = f"{IMAGEDIR}{files[random_index]}"
    #response = FileResponse(path)              # FileResponse expects a path and It will render the image.
    

    path = f"{IMAGEDIR}{file.filename}" 
    category = get_category(img=path)
 
    return templates.TemplateResponse("result.html", {"request": request, "category":category, "current_time":file.filename,})


# -----------------------------------------------------------------------------------------------------------------
# SIMPLE INTRO FASTAPI

# @app.get("/items")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
# -----------------------------------------------------------------------------------------------------------------






# @app.get('/', methods=['GET', 'POST'])
# def rock_paper_scissor():
#     # Write the GET Method to get the index file
#     if request.method == 'GET':
#         return render_template('index.html')
#     # Write the POST Method to post the results file
#     if request.method == 'POST':
#         print(request.files)
#         if 'file' not in request.files:
#             print('File Not Uploaded')
#             return
#         # Read file from upload
#         file = request.files['file']
#         # Get category of prediction
#         category = get_category(img=file)
#         # Plot the category
#         now = datetime.now()
#         current_time = now.strftime("%H-%M-%S")
#         plot_category(file, current_time)
#         # Render the result template
#         return render_template('result.html', category=category, current_time=current_time)
