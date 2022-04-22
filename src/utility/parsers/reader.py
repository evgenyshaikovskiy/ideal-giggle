import xml.sax as sax


class XmlReader(sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.table_data = []
        self.student_data = []
        self.parser = sax.make_parser()
        
    
    def startElement(self, name, attrs):
        self.current = name
        if name == 'student':
            pass
        
    
    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'group':
            self.group = content
        elif self.current == '1':
            self.semester_1 = content
        elif self.current == '2':
            self.semester_2 = content
        elif self.current == '3':
            self.semester_3 = content
        elif self.current == '4':
            self.semester_4 = content
        elif self.current == '5':
            self.semester_5 = content
        elif self.current == '6':
            self.semester_6 = content
        elif self.current == '7':
            self.semester_7 = content
        elif self.current == '8':
            self.semester_8 = content
        elif self.current == '9':
            self.semester_9 = content
        elif self.current == '10':
            self.semester_10 = content
            
    
    def endElement(self, name):
        if self.current == 'name':
            selt.student_data.append(self.name)
        elif self.current == 'group':
            selt.student_data.append(self.group)
        elif self.current == '1':
            selt.student_data.append(self.semester_1)
        elif self.current == '2':
            selt.student_data.append(self.semester_2)
        elif self.current == '3':
            selt.student_data.append(self.semester_3)
        elif self.current == '4':
            selt.student_data.append(self.semester_4)
        elif self.current == '5':
            selt.student_data.append(self.semester_5)
        elif self.current == '6':
            selt.student_data.append(self.semester_6)
        elif self.current == '7':
            selt.student_data.append(self.semester_7)
        elif self.current == '8':
            selt.student_data.append(self.semester_8)
        elif self.current == '9':
            selt.student_data.append(self.semester_9)
        elif self.current == '10':
            selt.student_data.append(self.semester_10)
            
        if len(self.student_data) == 12:
            self.table_data.append(tuple(self.student_data))
            self.student_data = []
            
        self.current = ''

