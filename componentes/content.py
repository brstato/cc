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
                ),
            ),

            margin=ft.margin.all(20),
                
        )   