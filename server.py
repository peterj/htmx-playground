from fastapi import FastAPI, Response, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/contact/{id}", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "contact": {
        "id": "1",
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@doe.com"
    }, "title": "Edit Contact"}

    return templates.TemplateResponse("edit.html", context)


@app.put("/contact/{id}", response_class=HTMLResponse)
# content: str = Form(...)
async def update_contact(request: Request, id: int, firstName: Annotated[str, Form()], lastName: Annotated[str, Form()], email: Annotated[str, Form()]):
    context = {"request": request, "contact": {
        "id": id,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,

    },
        "title": "Contact Updated"}
    return templates.TemplateResponse("item.html", context)


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    context = {
        "request": request,
        "contact": {
            "id": "1",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john@doe.com"
        },
        "title": "Home Page"
    }
    return templates.TemplateResponse("index.html", context)
