import flet as ft
from typing import List
import asyncio

def async_handler(coro):  
    def wrapper(e):
        asyncio.create_task(coro(e)) 
    return wrapper   

class Carousel(ft.UserControl):
    def __init__(self, controls: List[ft.Control], **kwargs):
        super().__init__(**kwargs)
        self.controls = controls
        self.carousel = None

    async def mover(self, e, Delta: int = 0):
        if self.carousel:
            await self.carousel.scroll_to_async(
                delta = Delta,
                duration = 300,
                curve = ft.AnimationCurve.DECELERATE
            )    
            self.carousel.update_async()        

    def build(self):
        self.carousel = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            controls=self.controls,
        )
        return ft.Column(
            controls=[
                self.carousel,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD_ARROW_LEFT,
                            on_click=async_handler(lambda e: self.mover(e, -100)),
                        ),
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT,
                            on_click=async_handler(lambda e: self.mover(e, 100)),
                        )
                    ],
                ),
            ]
        )