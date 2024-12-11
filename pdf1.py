from fpdf import FPDF

with open("summary_transformer.txt", "r", encoding="utf-8") as f:
    text = f.read()


pdf = FPDF()


pdf.add_page()


pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)


pdf.multi_cell(0, 10, text)


pdf_output_path = "summary_transformerfinal.pdf"
pdf.output(pdf_output_path)  

print(f"PDF saved to {pdf_output_path}")

