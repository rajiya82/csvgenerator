from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv("topics.csv")

for index, raw in df.iterrows():
    pdf.add_page()
    pdf.set_font(family = "Arial", size=12)
    pdf.cell(w=0, h=12, txt=raw["Topic"], align='L', ln=1, border=0)
    pdf.line(10, 20, 200, 20)
pdf.output("Output.pdf")