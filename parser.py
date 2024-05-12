class JSONParser:
    def __init__(self, data):
        self.data = data

    def parse(self):
        message = self.data.get('message', 'no message')
        return message


class JSONListParser:
    def __init__(self, students_list):
        self.student_list = [Student(i) for i in students_list]


class Student:
    def __init__(self, student_dictionaries):
        self.name = student_dictionaries["Name"]
        self.grade = student_dictionaries["Grade"]
        self.nationality = student_dictionaries["Nationality"]
        self.major = student_dictionaries["Major"]
        self.university = student_dictionaries["University"]
        self.student_id = student_dictionaries["Student_ID"]