from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hola Mundo!')
pdf.cell(40, 10, 'Hola Mundo!',1,1)
pdf.output('tuto1.pdf', 'F')