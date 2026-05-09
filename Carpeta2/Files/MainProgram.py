import json
import csv
import configparser
import xml.etree.ElementTree as ET
import yaml

# -------------------------------
# Clase FileManager
# -------------------------------
class FileManager:
    def read_entire_file(self, path, mode):
        with open(path, mode, encoding="utf-8") as reader:
            print(reader.read())

    def get_file_lines(self, path, mode):
        with open(path, mode, encoding="utf-8") as reader:
            return reader.readlines()

    def read_line_by_line(self, path, mode):
        with open(path, mode, encoding="utf-8") as reader:
            line = reader.readline()
            while line != '':
                print(line, end='')
                line = reader.readline()

    def write_text(self, path, text):
        with open(path, 'w', encoding="utf-8") as file:
            file.write(text)

# -------------------------------
# Clase Student
# -------------------------------
class Student:
    def __init__(self, name, email, exam, note, grade, group, shift):
        self.name = name
        self.email = email
        self.exam = exam
        self.note = note
        self.grade = grade
        self.group = group
        self.shift = shift

# -------------------------------
# Clase MainProgram
# -------------------------------
class MainProgram:

    def obj_dict(self, obj):
        return obj.__dict__

    def object_to_xml(self, obj):
        root = ET.Element(obj.__class__.__name__)
        for key, value in self.obj_dict(obj).items():
            ET.SubElement(root, key).text = str(value)
        print(ET.tostring(root, encoding='unicode'))

    def object_to_json(self, obj):
        json_pretty = json.dumps(obj, default=self.obj_dict, indent=4, ensure_ascii=False)
        print(json_pretty)

    # -------------------------------
    # Crear dataset desde TXT
    # -------------------------------
    def create_dataset(self, path):
        students = []
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()[1:]  # saltar encabezado
            for line in lines:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 7:
                    # El archivo tiene columnas: Name | email | exa | calif | grado | grupo | turno |
                    name, email, exam, note, grade, group, shift = parts[:7]
                    grade = grade if grade else "N/A"
                    group = group if group else "N/A"
                    shift = shift if shift else "N/A"
                    exam = int(exam) if exam.isdigit() else 0
                    note = int(note) if note.isdigit() else 0
                    student = Student(name, email, exam, note, grade, group, shift)
                    students.append(student)

        # Ordenar por apellido (última palabra del nombre)
        students.sort(key=lambda s: s.name.split()[-1])
        return students

    # -------------------------------
    # Métodos para crear archivos
    # -------------------------------
    def create_csv(self, students):
        with open("students.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "email", "exam", "note", "grade", "group", "shift"])
            for s in students:
                writer.writerow([s.name, s.email, s.exam, s.note, s.grade, s.group, s.shift])
        print("Archivo students.csv creado")

    def create_ini(self, students):
        config = configparser.ConfigParser()
        for i, s in enumerate(students, start=1):
            section = f"student_{i}"
            config[section] = {
                "name": s.name,
                "email": s.email,
                "exam": str(s.exam),
                "note": str(s.note),
                "grade": str(s.grade),
                "group": s.group,
                "shift": s.shift
            }
        with open("students.ini", "w", encoding="utf-8") as file:
            config.write(file)
        print("Archivo students.ini creado")

    def create_yaml(self, students):
        data = {"students": [self.obj_dict(s) for s in students]}
        with open("students.yaml", "w", encoding="utf-8") as file:
            yaml.dump(data, file, allow_unicode=True)
        print("Archivo students.yaml creado")

    def create_xml(self, students):
        root = ET.Element("students")
        for s in students:
            student_elem = ET.SubElement(root, "student")
            for key, value in self.obj_dict(s).items():
                ET.SubElement(student_elem, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write("students.xml", encoding="utf-8", xml_declaration=True)
        print("Archivo students.xml creado")

    def create_json(self, students):
        data = {"students": [self.obj_dict(s) for s in students]}
        with open("students.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Archivo students.json creado")

# -------------------------------
# Ejecución principal
# -------------------------------
if __name__ == "__main__":
    main = MainProgram()

    # Crear dataset desde el archivo TXT
    student_list = main.create_dataset("2-J_mit.txt")

    # Exportar en todos los formatos
    main.create_csv(student_list)
    main.create_ini(student_list)
    main.create_yaml(student_list)
    main.create_xml(student_list)
    main.create_json(student_list)


