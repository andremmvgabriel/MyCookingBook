from .PDF import PDF

class PortraitPDF(PDF):
    def __init__(self) -> None:
        super().__init__("P", "mm", "A4")
