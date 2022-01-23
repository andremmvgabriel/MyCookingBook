from pdf_generator import PortraitPDF

if __name__ == "__main__":
    pdf = PortraitPDF()
    pdf.add_page()
    pdf.draw_frame()
    pdf.cell()
    pdf.create("test")
