import flet as ft
from componentes.sub_componentes.apresentacao import Apresentacao

class Content(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Container(
            content=ft.Container(
                content=ft.Column(
                    
                    controls=[
                        Apresentacao(),
                    ],
                    # scroll=ft.ScrollMode.ALWAYS,
                ),
                # border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                # border_radius=ft.border_radius.all(20),
                # blur=10,                               
                # bgcolor=ft.Colors.WHITE10,   
            ),

            margin=ft.margin.all(20),
                
        )   