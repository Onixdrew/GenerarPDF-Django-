from fpdf import FPDF
import locale


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo-sena-naranja-png-2022.png', 10, 8, 30)
        
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(50)
        # Title
        self.cell(70, 10, 'Reporte Productos', 0, 0, 'C')
        # Line break
        self.ln(40)
    
    def footer(self):
         # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        self.cell(0,10,"Ejemplo reporte productos",0,0,'L')
        self.cell(30)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'L')
    
    
    def generarTabla(self,encabezado,datos):
        # agrega el signo de pesos al valor
        locale.setlocale(locale.LC_MONETARY,'es_CO.UTF-8')
        
        self.set_font('Arial','B',14)
        columnas=[20,50,50]
        for i in range(len(encabezado)):
            pdf.cell(columnas[i], 15, encabezado[i],1,0,'C')

        self.ln()
        for i in datos:
            pdf.cell(columnas[0], 15, str(i['Código']
                                          
                                          ),1,0,'C')
            pdf.cell(columnas[1], 15, i['Producto'],1,0,'C')
            pdf.cell(columnas[2], 15, str(locale.currency(i['Precio'], grouping=True)),1,1,'R')
  
  
    
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
encabezado=['Código','Producto','Precio']
datos=[
    {"Código":10,"Producto":"Televisor","Precio":2500000},
    {"Código":20,"Producto":"Computador","Precio":4500000},
    {"Código":10,"Producto":"Zapatos","Precio":380000},
]
    

pdf.generarTabla(encabezado,datos)
pdf.output('Reporte.pdf', 'F')