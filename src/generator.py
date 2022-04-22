from random import randint
from utility.parsers.writer import XmlWriter

import names


class XmlGenerator:
    def __init__(self):
        pass
    
    
    @staticmethod
    def generate_xml_file(count_of_students):
        path = 'src/data.xml'
        data_dict = {}
        with open(path, 'w') as file:
            writer = XmlWriter(path)
            for _ in range(count_of_students):
                data_dict['name'] = names.get_full_name()
                data_dict['group'] = str(randint(100000, 999999))
                data_dict['semester 1'] = str(randint(1, 50))
                data_dict['semester 2'] = str(randint(1, 50))
                data_dict['semester 3'] = str(randint(1, 50))
                data_dict['semester 4'] = str(randint(1, 50))
                data_dict['semester 5'] = str(randint(1, 50))
                data_dict['semester 6'] = str(randint(1, 50))
                data_dict['semester 7'] = str(randint(1, 50))
                data_dict['semester 8'] = str(randint(1, 50))
                data_dict['semester 9'] = str(randint(1, 50))
                data_dict['semester 10'] = str(randint(1, 50))
                
                writer.create_xml_student(data_dict)
        writer.create_xml_file()

def main():
    XmlGenerator.generate_xml_file(100)
    
if __name__ == "__main__":
    main()
                