from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, orientation: str = "P", unit: str = "mm", format: str = "A4") -> None:
        super().__init__(orientation, unit, format)
        if orientation == "P":
            self._page_width = 210
            self._page_height = 297
        else:
            self._page_width = 297
            self._page_height = 210
    
    def create(self, name: str) -> None:
        self.output(f"{name}.pdf", "F")
    
    def draw_frame(self, margin: float = 5.0) -> None:
        # Safety checks
        if margin <= 0.0: return

        self.rect(margin, margin, self._page_width - 2 * margin, self._page_height - 2 * margin)
    
    def write_title(self, title: str) -> None:
        pass

    def place_image(self, image) -> None:
        #i_width, i_height = image.size()

        self.set_xy()
