from windows import Window

from .OptionalDataWidget import OptionalDataWidget
from .IngredientsDataWidget import IngredientsDataWidget
from .StepsDataWidget import StepsDataWidget

from pdf_generator import PDF

class ComponentDataWidget(Window):
    __is_collapsed: bool = True
    
    def __init__(self) -> None:
        #self._optional = OptionalDataWidget()
        self._ingredients = IngredientsDataWidget()
        self._steps = StepsDataWidget()
        super().__init__("widgets/designs/ComponentDataWidget.ui")
    
    def setup(self) -> None:
        # Modules
        #self.frameContents.layout().addWidget(self._optional)
        self.frameContents.layout().addWidget(self._ingredients)
        self.frameContents.layout().addWidget(self._steps)

        self.buttonHeader.clicked.connect(self.toggle_visibility)
        self.buttonDelete.setText("Del")
        self.buttonDelete.clicked.connect(self.delete)

        self.setup_view()
    
    def delete(self):
        self.setParent(None)
    
    def toggle_visibility(self):
        self.__is_collapsed = not self.__is_collapsed
        self.setup_view()
    
    def setup_view(self):
        if self.__is_collapsed: self.show_collapsed()
        else: self.show_expanded()
    
    def show_expanded(self):
        self.frameContents.setHidden(False)

    def show_collapsed(self):
        self.frameContents.setHidden(True)
    
    def open_data(self, data: dict) -> None:
        self.buttonHeader.setText(data["name"])

        self._ingredients.open_data(data)
        self._ingredients.enter_view_mode()
        self._steps.open_data(data)
        self._steps.enter_view_mode()
    
    def enter_edit_mode(self):
        self.buttonDelete.setHidden(False)

        # Modules
        self._ingredients.enter_edit_mode()
        self._steps.enter_edit_mode()

    def enter_view_mode(self):
        self.buttonDelete.setHidden(True)

        # Modules
        self._ingredients.enter_view_mode()
        self._steps.enter_view_mode()
    
    def get_input_data(self):
        data = {}
        #data.update(self._optional.get_input_data())
        data.update({"name": self.buttonHeader.text()})
        data.update(self._ingredients.get_input_data())
        data.update(self._steps.get_input_data())
        return data
    





    def write_in_pdf(self, pdf: PDF):
        pdf.set_font(pdf.font_family, "B", 14)

        pdf.cell(0, 8, f"{self.buttonHeader.text()}", 1, 1, "L")

        pdf.set_font(pdf.font_family, "", 12)

        self._ingredients.write_int_pdf_as_component(pdf)
        self._steps.write_int_pdf_as_component(pdf)

        pdf.ln(5)
