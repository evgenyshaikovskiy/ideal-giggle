import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class DialogContent(BoxLayout):
    pass


class InputDialogContent(BoxLayout):
    pass


class FilterDialogContent(BoxLayout):
    pass


class DeleteDialogContent(BoxLayout):
    pass


class UploadDialogContent(BoxLayout):
    pass


class SaveDialogContent(BoxLayout):
    pass


class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs['title'],
            type='custom',
            content_cls=kwargs['content_cls'],
            buttons=[
                MDFlatButton(text='OK', theme_text_color='Custom', on_release=self.close),
            ],
        )
        self.mode = kwargs['mode']
        self.model = kwargs['model']
        
    def close(self, obj):
        self.dismiss()
        self.model.close_dialog()
        

class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title='Fill new student data:',
            content_cls=InputDialogContent(),
            mode='input',
            model=kwargs['model'],
        )
    
    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(
            [
                self.content_cls.ids.input_name.text,
                self.content_cls.ids.input_group.text,
                self.content_cls.ids.input_1_semester.txt,
                self.content_cls.ids.input_2_semester.txt,
                self.content_cls.ids.input_3_semester.txt,
                self.content_cls.ids.input_4_semester.txt,
                self.content_cls.ids.input_5_semester.txt,
                self.content_cls.ids.input_6_semester.txt,
                self.content_cls.ids.input_7_semester.txt,
                self.content_cls.ids.input_8_semester.txt,
                self.content_cls.ids.input_9_semester.txt,
                self.content_cls.ids.input_10_semester.txt,
            ]
        )


class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Filter students: ",
                content_cls=FilterDialogContent(),
                mode="filter",
                model=kwargs["model"],
        )


    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(
            [
                self.content_cls.ids.filter_name.text,
                self.content_cls.ids.filter_group.text,
                self.content_cls.ids.filter_count.txt,
            ]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Delete students: ",
                content_cls=DeleteDialogContent(),
                mode="delete",
                model=kwargs["model"],
        )

    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(
            [
                self.content_cls.ids.delete_name.text,
                self.content_cls.ids.delete_group.text,
                self.content_cls.ids.delete_count.txt,
            ]
        )


class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Saving: ",
                content_cls=SaveDialogContent(),
                mode="save",
                model=kwargs["model"],
        )


    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(self.content_cls.ids.save_path.text)
        

class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Upload: ",
                content_cls=UploadDialogContent(),
                mode="upload",
                model=kwargs["model"],
        )


    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(self.content_cls.ids.upload_path.text)
        

Builder.load_file('/home/evgeny/source/repos/ideal-giggle/src/utility/windows/windows.kv')
