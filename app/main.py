from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")
#templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('templates')))

@app.get("/items", response_class=HTMLResponse)
async def read_item(request: Request):
    print('GET METHOD IS WORKING JOSE DANIEL')
    return templates.TemplateResponse("index.html", {"request": request})
    
# @app.get("/items")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# Mount Static Files
# app.mount("/", StaticFiles(directory="app/static", html = True), name="static")
# templates = Jinja2Templates(directory="templates")





#from app.inference import get_category, plot_category

# @app.post("/", response_class=HTMLResponse)
# async def read_item(request: Request, image_file: str):
    
#     if 'file' not in request.files:
#         print('File Not Uploaded')
#         return 'File Not Uploaded'

#     # Read file from upload
#     image_file = request.files['file']
#     # Get category of prediction
#     category = get_category(img=file)
#     # Plot the category
#     now = datetime.now()
#     current_time = now.strftime("%H-%M-%S")
#     plot_category(image_file, current_time)
#     # Render the result template
#     return templates.TemplateResponse("result.html", {"category": category, "current_time": current_time})




# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


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
