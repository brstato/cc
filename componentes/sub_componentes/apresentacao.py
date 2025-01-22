import flet as ft
from componentes.sub_componentes.profissionais import Profissionais
from componentes.sub_componentes.depoimentos import Depoimentos
from componentes.sub_componentes.carousel import Carousel

class Apresentacao(ft.UserControl):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(self,**kwargs)
        self.page = page
        
    
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                col={'xs': 12, 'sm': 6, 'md': 6, 'lg': 6},
                                content=
                                    ft.Image(
                                        src='Logo.webp',
                                    ),   
                                
                                alignment=ft.alignment.center_right,
                                
                            ),                            
                            ft.Column(

                                col={'xs': 12, 'sm': 6, 'md': 6, 'lg': 6},
                                controls=[
                                    ft.ResponsiveRow(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value='Bruno Tattoo',
                                                size=50,
                                                style=ft.TextThemeStyle.BODY_LARGE,
                                                color=ft.colors.GREY_300,
                                                text_align=ft.TextAlign.CENTER,
                                                # expand=True,
                                            ),
                                        ],
                                    ),
                                        
                                    ft.ResponsiveRow(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value='Tatuador Profissional',
                                                size=25,
                                                style=ft.TextThemeStyle.BODY_MEDIUM,
                                                color=ft.colors.GREY_300,
                                                text_align=ft.TextAlign.CENTER,
                                                # expand=True,
                                            ),
                                        ],
                                    ),     
                                    ft.ResponsiveRow(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value='Tatuador com mais de 10 anos de experiência, '+ 
                                                'especializado e premiado no estilo e preto e cinza.',
                                                size=12.5,
                                                style=ft.TextThemeStyle.BODY_SMALL,
                                                color=ft.colors.GREY_300,
                                                text_align=ft.TextAlign.CENTER,
                                                # expand=True,
                                            ),  
                                        ],
                                    ),                                                       
                                    
                                ],
                                expand=True,                      
                            ),
                        ]
                    ), 
                    ft.Divider(),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value='Depoimentos',
                                color=ft.colors.GREY_300,
                                text_align=ft.TextAlign.CENTER,                                
                            ),
                        ],
                    ),
                    Carousel(
                        controls=[
                            Depoimentos('depoimento.webp'),
                            Depoimentos('depoimento.webp'),
                            Depoimentos('depoimento.webp'),
                            Depoimentos('depoimento.webp'),
                            Depoimentos('depoimento.webp'),
                            Depoimentos('depoimento.webp'),
                        ],
                    ),
                    ft.Divider(),
                    ft.ResponsiveRow(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value='Profissionais',
                                color=ft.colors.GREY_300,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],    
                    ),
                    
                    Carousel(
                        controls=[
                            Profissionais(
                                page=self.page,
                                Nome='Bruno Tattoo',
                                insta='',
                                url_insta='https://www.instagram.com/brunoribeiro.tatuador/',
                                bio='Tatuador Profissional',
                                image='eu.jpg',
                            ),
                            Profissionais(
                                page=self.page,
                                Nome='Bruno Tattoo',
                                insta='',
                                url_insta='https://www.instagram.com/brunotattoo/',
                                bio='Tatuador Profissional',
                                image='eu.jpg',
                            ),
                            Profissionais(
                                page=self.page,
                                Nome='Bruno Tattoo',
                                insta='',
                                url_insta='https://www.instagram.com/brunotattoo/',
                                bio='Tatuador Profissional',
                                image='eu.jpg',
                            ),
                            Profissionais(
                                page=self.page,
                                Nome='Bruno Tattoo',
                                insta='',
                                url_insta='https://www.instagram.com/brunotattoo/',
                                bio='Tatuador Profissional',
                                image='eu.jpg',
                            ),
                            Profissionais(
                                page=self.page,
                                Nome='Bruno Tattoo',
                                insta='',
                                url_insta='https://www.instagram.com/brunotattoo/',
                                bio='Tatuador Profissional',
                                image='eu.jpg',
                            ),
                                                                                                                                            
                       ],
                    ),
                    ft.Divider(),
                ],
            ), 
        )