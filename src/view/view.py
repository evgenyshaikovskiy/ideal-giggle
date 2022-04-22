import os

import utility.windows.windows as window
from utility.abstractions.observer import Observer

# kivy dependencies
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# kivyMD dependencies
from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar


class ViewComponent(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
        # subscribe view component to model as observer
        self.model.subscribe(self)
        self.screen = Screen()
    
    
    def open_dialog(self, window_type: str):
        if window_type == 'input':
            self.dialog = window.InputWindow(model=self.model)
        elif window_type == 'filter':
            self.dialog = window.FilterWindow(model=self.model)
        elif window_type == 'delete':
            self.dialog = window.DeleteWindow(model=self.model)
        elif window_type == 'save':
            self.dialog = window.SaveWindow(model=self.model)
        elif window_type == 'upload':
            self.dialog = window.UploadWindow(model=self.model)
            
        self.dialog.open()
        self.controller.dialog(window_type, self.dialog)
    
    
    def close_dialog(self, dialog_data: list=[]):
        if self.dialog.mode == 'input':
            self.controller.input_student(dialog_data)
        elif self.dialog.mode == 'filter':
            self.controller.filter_students(dialog_data)
        elif self.dialog.mode == 'delete':
            deleted = self.controller.delete_students(dialog_data)
            Snackbar(text=f'{deleted} students are deleted.').open()
        elif self.dialog.mode == 'upload':
            self.controller.upload_from_file(dialog_data)
        elif self.dialog.mode == 'save':
            self.controller.save_in_file(dialog_data)
        
        self.dialog = None
        
    
    def on_model_change(self, data):
        self.close_dialog(data)


    def refresh(self):
        self.controller.refresh()
        
        
    def build(self):
        self.add_widget(self.model.table)
        return self
    
    
Builder.load_file(os.path.join(os.path.dirname(__file__), "view.kv"))       