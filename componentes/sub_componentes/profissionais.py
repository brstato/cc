import flet as ft


class Profissionais(ft.UserControl):
    def __init__(self, Nome: str = '', insta: str = '', url_insta: str = '',  bio: str = '', image: str = 'default.jpg',  **kwargs):
        super().__init__(**kwargs)
        self.nome = Nome
        self.bio = bio
        self.image = image
        self.insta = insta
        self.url_insta = url_insta

    def build(self):
        return ft.Container(
            content=ft.Stack(
                controls=[                   
                    ft.Container(
                        
                        content=ft.Column(

                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                ft.Text(
                                    value=self.nome,
                                    theme_style=ft.TextThemeStyle.BODY_LARGE,
                                    color=ft.colors.WHITE,
                                ),
                                ft.Text(
                                    value=self.bio,
                                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                    color=ft.colors.WHITE,
                                    text_align=ft.alignment.center_left,
                                ),   
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                        content=ft.TextButton(
                                            content=ft.Text(
                                                value='Portifólio',
                                                color=ft.colors.WHITE,
                                            ),
                                            url=self.url_insta,
                                        ),
                                        border=ft.border.all(width=0.5, color=ft.colors.GREY_300),
                                        border_radius=ft.border_radius.all(20),
                                        expand=True,
                                    ),
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                        content=ft.TextButton(
                                            content=ft.Text(
                                                value='Instagram',
                                                color=ft.colors.WHITE,
                                            ),
                                            url=self.url_insta,
                                        ),
                                        border=ft.border.all(width=0.5, color=ft.colors.GREY_300),
                                        border_radius=ft.border_radius.all(20),
                                        expand=True,
                                    ),
                                    ],
                                ),                                   
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                        content=ft.TextButton(
                                            content=ft.Text(
                                                value='Whatsapp',
                                                color=ft.colors.WHITE,
                                            ),
                                        ),
                                        border=ft.border.all(width=0.5, color=ft.colors.GREY_300),
                                        border_radius=ft.border_radius.all(20),
                                        expand=True,
                                    ),
                                    ],
                                ),   
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                        content=ft.TextButton(
                                            content=ft.Text(
                                                value='Agenda',
                                                color=ft.colors.BLACK,
                                                weight=ft.FontWeight.BOLD,
                                                size=18,
                                            ),
                                        ),
                                        border=ft.border.all(width=0.5, color=ft.colors.GREY_300),
                                        border_radius=ft.border_radius.all(20),
                                        expand=True,
                                        bgcolor=ft.colors.GREY_300,
                                    ),
                                    ],
                                ),                                                                                                                    
                            ],
                            
                        ),

                        border=ft.border.all(width=0.5, color=ft.colors.GREY_300),
                        border_radius=ft.border_radius.all(20),
                        bgcolor=ft.colors.WHITE10,
                        blur=10,
                        padding=ft.padding.only(top=100, left=10, right=10, bottom=10),
                        width=180,  
                        height=360,                      
                    ),
                    ft.Container(
                        height=100,
                        width = 100,
                        border=ft.border.all(width=0.5, color=ft.colors.GREY_300),
                        offset=ft.Offset(x=-0.2, y=-0.2),
                        border_radius=ft.border_radius.all(20),
                        image_src=self.image,
                        image_fit=ft.ImageFit.COVER,
                        image_repeat=ft.ImageRepeat.NO_REPEAT,
                        shadow=ft.BoxShadow(
                            blur_radius=40,
                            color=ft.colors.BLACK,
                            offset=ft.Offset(x=10, y=10), 
                        ),
                    ),  
                    ft.Container(
                        height=70,
                        width=70,
                        image_src='Logo.webp',
                        offset=ft.Offset(x=1.4, y=0.15),
                        image_repeat=ft.ImageRepeat.NO_REPEAT,
                    ),               
                ],
            ),
            margin=ft.margin.only(top=20, left=20),

        )