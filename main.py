from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
#pdf.add_page()
df = pd.read_csv("topics.csv")


def draw_line(start, end, lag =10):
    x1 = 10
    x2 = 200
    for i in range(start, end, lag):
        pdf.line(x1, i, x2, i)

def main():
    for index, raw in df.iterrows():
        pdf.add_page()
        pdf.set_font(family="Arial", size=20)
        pdf.cell(w=0, h=12, txt=raw["Topic"], align='L', ln=1, border=0)
        pdf.line(10, 20, 200, 20)

        # adding footers
        pdf.ln(260)
        pdf.set_font(family="Arial", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=raw["Topic"], align='R')

        draw_line(20, 280)
        num_pages = int(raw["Pages"])
        for i in range(1, num_pages):
            pdf.add_page()
            # adding footers
            pdf.ln(270)
            pdf.set_font(family="Arial", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=raw["Topic"], align='R')
            draw_line(20, 280)
    pdf.output("Output.pdf")


if __name__ == "__main__":
    main()
