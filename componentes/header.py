import flet as ft

class Header(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.TextButton(
                        content=(
                            ft.Text(
                                value='Inicio',
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.GREY_300,
                            )
                        )                                                                   
                    ),
                    ft.Container(
                        expand=True,
                    ),
                    ft.TextButton(
                        content=(
                            ft.Text(
                                value='Sobre',
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.GREY_300,
                            )
                        )                                                                   
                    ),
                    ft.Text(value='|', color=ft.colors.GREY_300),
                    ft.TextButton(
                        content=(
                            ft.Text(
                                value='Profissionais',
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.GREY_300,
                            )
                        )                                                                   
                    ),                    

                    ft.Container(
                        ft.TextButton(
                            content=(
                                ft.Text(
                                    value='Contato',
                                    text_align=ft.TextAlign.CENTER,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLACK,                                            
                                )
                            )
                        ),
                        border=ft.border.all(width=1, color=ft.colors.WHITE),
                        border_radius=ft.border_radius.all(10),
                        bgcolor=ft.colors.GREY_300,
                        
                    ),
                    
                ],
            
            ),
            padding=ft.padding.symmetric(vertical=5, horizontal=10),
        )  