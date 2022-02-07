from utils import Window

from pdf_generator import PDF

from widgets_translators import StepsDataWidgetTranslator

class StepsDataWidget(Window):
    __is_collapsed: bool = False

    def __init__(self) -> None:
        super().__init__("widgets/designs/StepsDataWidget.ui", StepsDataWidgetTranslator())
    
    def setup(self) -> None:
        # Buttons
        self.buttonSteps.clicked.connect(self.toggle_visibility)
        self.buttonAdd.clicked.connect(self.add)
        self.buttonRemove.clicked.connect(self.remove)

        self.buttonAdd.setEnabled(False)
        self.buttonRemove.setEnabled(False)

        # Entries
        self.entryStep.textChanged.connect(self.text_changed)
        self.entryStep.returnPressed.connect(self.return_key_pressed)
        self.listSteps.currentItemChanged.connect(self.step_selected)

        self.setup_view()
    
    def setup_language(self):
        self.buttonSteps.setText(self._translator.steps_button)
        self.buttonAdd.setText(self._translator.add_button)
        self.buttonRemove.setText(self._translator.remove_button)

    def text_changed(self):
        # Get text
        text = self.entryStep.text()

        # Checks button visibility
        if len(text) < 3: self.buttonAdd.setEnabled(False)
        else: self.buttonAdd.setEnabled(True)
    
    def return_key_pressed(self):
        # Get text
        text = self.entryStep.text()

        # Checks button visibility
        if len(text) >= 3: self.add()
    
    def step_selected(self):
        self.buttonRemove.setEnabled(True)
    
    def toggle_visibility(self):
        self.__is_collapsed = not self.__is_collapsed
        self.setup_view()

    def add(self):
        text = self.entryStep.text()
        text = text.capitalize()
        n_step = self.listSteps.count()
        text = f"{self._translator.step_key} {n_step+1}: {text}"
        self.entryStep.setText("")
        self.listSteps.addItem(text)

    def remove(self):
        # Gets the item from the list
        row = self.listSteps.currentRow()
        item = self.listSteps.takeItem(row)

        # Clears the selection
        self.listSteps.clearSelection()
        self.listSteps.setCurrentRow(999)

        # Updates the ingredients numbers
        for index in range(self.listSteps.count()):
            text = self.listSteps.item(index).text()
            _, step = text.split(": ")
            text = f"{self._translator.step_key} {index + 1}: {step}"
            self.listSteps.item(index).setText(text)

        # Deactivates once again the remove button
        self.buttonRemove.setEnabled(False)
    
    def setup_view(self):
        if self.__is_collapsed: self.show_collapsed()
        else: self.show_expanded()
    
    def show_expanded(self):
        self.frameContent.setHidden(False)

    def show_collapsed(self):
        self.frameContent.setHidden(True)
    
    def open_data(self, data: dict) -> None:
        # Clears
        self.clear()
        
        # Writes
        for index in range(len(data["steps"])):
            self.listSteps.addItem(f"{self._translator.step_key} {index + 1}: {data['steps'][index]}")
    
    def enter_edit_mode(self):
        self.frameEdit.setHidden(False)

    def enter_view_mode(self):
        self.frameEdit.setHidden(True)
    
    def get_input_data(self):
        steps_list = []

        # Updates the ingredients numbers
        for index in range(self.listSteps.count()):
            text = self.listSteps.item(index).text()
            _, step = text.split(": ")
            steps_list.append(step)
        
        return { "steps": steps_list }
    
    def clear(self):
        for index in range(self.listSteps.count())[::-1]:
            self.listSteps.takeItem(index)
    






    def write_in_pdf(self, pdf: PDF):
        pdf.set_font(pdf.font_family, "B", 16)

        pdf.cell(0, 10, "II. Steps:", 0, 1, "L")

        pdf.set_font(pdf.font_family, "", 12)
        
        for index in range(self.listSteps.count()):
            pdf.ln(2)
            text = self.listSteps.item(index).text()
            pdf.multi_cell(0, 5, text, 0)

        pdf.ln(15)
    
    def write_in_pdf_as_component(self, pdf: PDF):
        if self.listSteps.count() == 0: return 

        pdf.cell(0, 10, "Steps:", 0, 1, "C")
        pdf.set_font(pdf.font_family, "", 12)

        for index in range(self.listSteps.count()):
            pdf.ln(2)
            text = self.listSteps.item(index).text()
            pdf.multi_cell(0, 5, text, 0)
        
        pdf.ln(5)
