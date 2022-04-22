from view.view import ViewComponent


class ControllerComponent:
    def __init__(self, model):
        self.model = model
        self.view = ViewComponent(controller=self, model=self.model)
        
    
    def refresh(self):
        self.model.refresh_students()
        

    def get_screen(self):
        return self.view.build()
    
    
    def dialog(self, window_type, dialog):
        self.model.open_dialog(window_type, dialog)
        
        
    def input_student(self, data):
        self.model.add_new_student(row=data)
    
    
    def filter_students(self, data):
        self.model.filter_students(filters=data)
        
    
    def delete_students(self, data):
        deleted = self.model.delete_students(filters=data)
        return deleted
    
    
    def upload_from_file(self, data):
        self.model.read_data(path=data)
        
    
    def save_in_file(self, data):
        self.model.write_data_to_file(path=data)