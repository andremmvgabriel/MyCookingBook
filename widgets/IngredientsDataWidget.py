from windows import Window

from pdf_generator import PDF

from widgets_translators import IngredientsDataWidgetTranslator

class IngredientsDataWidget(Window):
    __is_collapsed: bool = False

    def __init__(self) -> None:
        super().__init__("widgets/designs/IngredientsDataWidget.ui", IngredientsDataWidgetTranslator())
    
    def setup(self) -> None:
        # Buttons
        self.buttonIngredients.clicked.connect(self.toggle_visibility)
        self.buttonAddIngredient.clicked.connect(self.add_ingredient)
        self.buttonRemoveIngredient.clicked.connect(self.remove_ingredient)

        self.buttonAddIngredient.setEnabled(False)
        self.buttonRemoveIngredient.setEnabled(False)

        # Entries
        self.entryIngredient.textChanged.connect(self.ingredient_text_changed)
        self.entryIngredient.returnPressed.connect(self.ingredient_return_key_pressed)
        self.listIngredients.currentItemChanged.connect(self.ingredient_selected)

        self.setup_view()
    
    def setup_language(self) -> None:
        # Buttons
        self.buttonIngredients.setText(self._translator.ingredients_button)
        self.buttonAddIngredient.setText(self._translator.add_button)
        self.buttonRemoveIngredient.setText(self._translator.remove_button)

    def ingredient_text_changed(self):
        # Get text
        text = self.entryIngredient.text()

        # Checks button visibility
        if len(text) < 3: self.buttonAddIngredient.setEnabled(False)
        else: self.buttonAddIngredient.setEnabled(True)
    
    def ingredient_return_key_pressed(self):
        # Get text
        text = self.entryIngredient.text()

        # Checks button visibility
        if len(text) >= 3: self.add_ingredient()
    
    def ingredient_selected(self):
        self.buttonRemoveIngredient.setEnabled(True)
    
    def toggle_visibility(self):
        self.__is_collapsed = not self.__is_collapsed
        self.setup_view()

    def add_ingredient(self):
        text = self.entryIngredient.text()
        text = text.capitalize()
        n_item = self.listIngredients.count()
        text = f"{n_item+1}) {text}"
        self.entryIngredient.setText("")
        self.listIngredients.addItem(text)

    def remove_ingredient(self):
        # Gets the item from the list
        row = self.listIngredients.currentRow()
        item = self.listIngredients.takeItem(row)

        # Clears the selection
        self.listIngredients.clearSelection()
        self.listIngredients.setCurrentRow(999)

        # Updates the ingredients numbers
        for index in range(self.listIngredients.count()):
            text = self.listIngredients.item(index).text()
            _, ingredient = text.split(") ")
            text = f"{index + 1}) {ingredient}"
            self.listIngredients.item(index).setText(text)

        # Deactivates once again the remove button
        self.buttonRemoveIngredient.setEnabled(False)
    
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
        for index in range(len(data["ingredients"])):
            self.listIngredients.addItem(f"{index + 1}) {data['ingredients'][index]}")
    
    def enter_edit_mode(self):
        self.frameEdit.setHidden(False)

    def enter_view_mode(self):
        self.frameEdit.setHidden(True)
    
    def get_input_data(self):
        ingredients_list = []
        # Updates the ingredients numbers
        for index in range(self.listIngredients.count()):
            text = self.listIngredients.item(index).text()
            _, ingredient = text.split(") ")
            ingredients_list.append(ingredient)

        return { "ingredients": ingredients_list }
    
    def clear(self):
        for index in range(self.listIngredients.count())[::-1]:
            self.listIngredients.takeItem(index)
    





    def write_in_pdf(self, pdf: PDF):
        pdf.set_font(pdf.font_family, "B", 16)

        pdf.cell(0, 10, "I. Ingredients:", 1, 1, "L")

        pdf.set_font(pdf.font_family, "", 12)

        for index in range(self.listIngredients.count()):
            pdf.ln(2)
            text = self.listIngredients.item(index).text()
            pdf.multi_cell(0, 5, text, 1)

        pdf.ln(5)
    
    def write_int_pdf_as_component(self, pdf: PDF):
        pdf.cell(0, 10, "Ingredients:", 1, 1, "C")
        pdf.set_font(pdf.font_family, "", 12)

        for index in range(self.listIngredients.count()):
            pdf.ln(2)
            text = self.listIngredients.item(index).text()
            pdf.multi_cell(0, 5, text, 1)
        
        pdf.ln(5)
