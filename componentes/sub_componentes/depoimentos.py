import flet as ft

class Depoimentos(ft.UserControl):
    def __init__(self, depoimento: str = '', **kwargs):
        super().__init__(**kwargs)
        self.depoimento = depoimento

    def build(self):
        return ft.Container(
            height=150,
            width=300,
            # image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_src=self.depoimento

        )    