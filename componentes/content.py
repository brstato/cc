import flet as ft
from componentes.sub_componentes.apresentacao import Apresentacao

class Content(ft.UserControl):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(self, **kwargs)
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Container(
                content=ft.Column(
                    
                    controls=[
                        Apresentacao(self.page),
                    ],
                ),
            ),

            margin=ft.margin.all(20),
                
        )   