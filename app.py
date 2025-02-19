import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

load_dotenv()

reponame = os.getenv("REPO_TITLE", "File Browser by Dilan Gilluly")
filepath = os.getenv("REPO_PATH", "static")

app = FastAPI()
app.mount(f"/s", StaticFiles(directory=filepath), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def browse(request:Request, r_path:str=""):
    full_path = os.path.join(filepath, r_path)    
    if os.path.isdir(full_path):
        dir_list = os.listdir(full_path)
        dir_list.sort()
        contents = [(item, os.path.join(r_path, item), os.path.isfile(os.path.join(full_path, item))) for item in dir_list]
        return templates.TemplateResponse(request=request, name="browse.html", context={"reponame": reponame, "path": r_path, "contents": contents})
    else:
        return FileResponse(full_path)
