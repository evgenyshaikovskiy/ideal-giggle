from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from contoller.controller import ControllerComponent
from model.model import ModelComponent

from kivy.core.window import Window
from kivy.metrics import dp


class TableApplication(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5,'center_y': 0.54},
            size_hint={0.9, 0.8},
            use_pagination=True,
            rows_num=13,
            column_data=[
                ('Full name', dp(30)),
                ('Group', dp(20)),
                ('1', dp(10)),
                ('2', dp(10)),
                ('3', dp(10)),
                ('4', dp(10)),
                ('5', dp(10)),
                ('6', dp(10)),
                ('7', dp(10)),
                ('8', dp(10)),
                ('9', dp(10)),
                ('10', dp(10)),
                ('Total', dp(15)),
            ],
        )
        self.model = ModelComponent(table=self.table)
        self.controller = ControllerComponent(self.model)
        
    def build(self):
        Window.size = (1280, 800)
        return self.controller.get_screen()
    

TableApplication().run()

