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

assets_path = os.path.join(os.path.dirname(__name__), "assets")  
absolute_path = os.path.abspath(assets_path) 

async def main(page: ft.Page):

    header = Header()
    content = Content(page)

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

# if __name__ == '__main__':
#         ft.app(target=main, assets_dir=absolute_path)
app.mount(path='/', app=flet_fastapi.app(main, assets_dir=absolute_path, web_renderer='canvaskit'))