import flet as ft
import os
import flet_fastapi
from flet_fastapi import FletApp
from contextlib import asynccontextmanager
from fastapi import FastAPI 
# import requests
# import asyncio
from concurrent.futures import ThreadPoolExecutor
from componentes.header import Header
from componentes.content import Content

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)  
    

@app.get('/loja/{id}')
async def get_user(id: int = 0):
    return {f'Loja {id}'}       

async def main(page: ft.Page):

    header = Header()
    content = Content()

    layout = ft.Container(
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                header,
                content,
                
            ]
        ),
        image_src='fundo.webp',
        image_fit=ft.ImageFit.COVER,
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        expand=True,
        bgcolor=ft.colors.GREY_900,
    )

    await page.add_async(layout)  
    await page.update_async()

assets_path = os.path.join(os.path.dirname(__name__), "assets")    


app.mount(path='/', app=flet_fastapi.app(main, assets_dir='C:\\Users\\brsta\\OneDrive\\Documentos\\cc\\assets', web_renderer='canvaskit'))