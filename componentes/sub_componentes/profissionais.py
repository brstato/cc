import flet as ft
import asyncio 

overlay_largeview = None


class Profissionais(ft.UserControl):
    def __init__(self, page: ft.Page, Nome: str = '', insta: str = '', url_insta: str = '',  bio: str = '', image: str = 'default.jpg',  **kwargs):
        super().__init__(self, **kwargs)
        self.nome = Nome
        self.bio = bio
        self.image = image
        self.insta = insta
        self.url_insta = url_insta
        self.page = page
        self.profissionais = None
        self.overlay_largeview = None
        self.overlay_portifolio = None


    async def close_largeview(self, e):   
        self.page.overlay.remove(self.overlay_largeview)      
        await self.page.update_async()            

    async def show_largeview(self, e):  
        self.overlay_largeview = ft.Column(
            controls=[                
                        ft.Stack(
                            controls=[
                                ft.Container(
                                    bgcolor=ft.colors.BLACK,
                                    expand=True,
                                    opacity=0.8,
                                ),                              

                                ft.Container(
                                    image_src = 'eu.jpg',
                                    expand=True,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.CLOSE,
                                            icon_color=ft.colors.GREY_300,
                                            on_click=self.close_largeview,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                ),                      
                            ],
                            expand=True,
                        ),
                    # ],
                    # expand=True,
                    # scroll = ft.ScrollMode.AUTO,
                # ),
            ],
            expand=True,
            # scroll=ft.ScrollMode.AUTO,
        )
        self.page.overlay.append(self.overlay_largeview)       
        await self.page.update_async()                 

    async def close_portifolio(self, e):
        self.page.overlay.remove(self.overlay_portifolio)
        await self.page.update_async()    

    async def show_portifolio(self, e):
        images=['eu.jpg','eu.jpg','eu.jpg','eu.jpg','eu.jpg','eu.jpg','eu.jpg']
        
        self.overlay_portifolio = ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[   
               
                ft.Stack(
                    controls=[
                        ft.Container(                             
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            expand=True,
                            opacity=0.8,
                        ), 
                        ft.Container(
                            content=ft.GridView(
                            expand=True,
                            spacing=10,
                            run_spacing=10,
                            
                            max_extent=500,
                            controls=[
                                ft.Container(
                                    image_src=image, 
                                    image_fit=ft.ImageFit.COVER,
                                    on_click=self.show_largeview,
                                ) for image in images

                            ]
                            ),
                            margin=ft.margin.all(50),
                        ),  
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.CLOSE,
                                    icon_color=ft.colors.GREY_300,
                                    on_click=self.close_portifolio,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),                                                 
                    ],
                    expand=True,
                    # scroll=ft.ScrollMode.AUTO,
                ),              
                                
            ],
        )

        self.page.overlay.append(self.overlay_portifolio)
        await self.page.update_async()          
 

    def build(self):   
        self.profissionais = ft.Container(
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
                                            # url=self.url_insta,
                                            on_click=lambda e: asyncio.create_task(self.show_portifolio(e)),
                    

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
        return self.profissionais