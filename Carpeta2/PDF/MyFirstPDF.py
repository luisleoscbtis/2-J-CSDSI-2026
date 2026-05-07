import itertools
import json
from statistics import mean
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

class MyFirstPDF:

    def grouper(self, iterable, n):
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args)

    def export_to_pdf(self, data):
        c = canvas.Canvas("grilla-alumnos.pdf", pagesize=LETTER)
        w, h = LETTER
        max_rows_per_page = 45
        # Márgenes
        x_offset = 50
        y_offset = 50
        # Espaciado entre filas
        padding = 15
        
        xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
        
        for rows in self.grouper(data, max_rows_per_page):
            rows = tuple(filter(bool, rows))
            c.grid(xlist, ylist[:len(rows) + 1])
            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    c.drawString(x + 2, y - padding + 3, str(cell))
            c.showPage()
        
        c.save()

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

data = [("NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROM.", "ESTADO")]

for s in students:
    notas = [int(s["exam"]), int(s["note"]), int(s["grade"])]
    promedio = round(mean(notas), 2)
    estado = "Aprobado" if promedio >= 4 else "Desaprobado"
    data.append((s["name"], *notas, promedio, estado))

my_pdf = MyFirstPDF()
my_pdf.export_to_pdf(data)

my_pdf.export_to_pdf(data)
print("PDF generado correctamente")

