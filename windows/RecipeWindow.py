from datetime import datetime

from Application import Application
from data_structures.RecipeData import RecipeData
from pdf_generator.PortraitPDF import PortraitPDF
from .Window import Window
from widgets.OptionalDataWidget import OptionalDataWidget
from widgets.ComponentsDataWidget import ComponentsDataWidget
from widgets.IngredientsDataWidget import IngredientsDataWidget
from widgets.StepsDataWidget import StepsDataWidget

from windows_translators import RecipeWindowTranslator

class RecipeWindow(Window):
    _recipe: RecipeData = None

    def __init__(self) -> None:
        self._optional = OptionalDataWidget()
        self._ingredients = IngredientsDataWidget()
        self._steps = StepsDataWidget()
        self._components = ComponentsDataWidget()
        super().__init__("windows/designs/RecipeWindow.ui", RecipeWindowTranslator())
    
    def setup(self) -> None:
        # Modules
        self.leftSide.addWidget(self._optional)
        self.leftSide.addWidget(self._ingredients)
        self.leftSide.addWidget(self._steps)
        self.rightSide.addWidget(self._components)

        # Buttons
        self.buttonUpdate.clicked.connect(self.update_recipe)
        self.buttonCancel.clicked.connect(self.cancel_update)
        self.buttonExport.clicked.connect(self.export_pdf)
        self.buttonEdit.clicked.connect(self.enter_edit_mode)
        self.buttonClose.clicked.connect(self.close_window)
        self.buttonDelete.clicked.connect(self.delete_recipe)
        self.buttonYes.clicked.connect(self.confirm_delete)
        self.buttonNo.clicked.connect(self.cancel_delete)

        # Frames
        self.frameDelete.setHidden(True)
        self.frameMainOptions.setHidden(False)
        self.frameEditOptions.setHidden(True)
    
    def setup_language(self) -> None:
        # Labels
        self.labelRecipeName.setText(f"{self._translator.recipe_name_label}:")
        self.labelConfirm.setText(self._translator.confirm_label)

        # Buttons
        self.buttonUpdate.setText(self._translator.update_button)
        self.buttonCancel.setText(self._translator.cancel_button)
        self.buttonExport.setText(self._translator.export_button)
        self.buttonEdit.setText(self._translator.edit_button)
        self.buttonClose.setText(self._translator.close_button)
        self.buttonDelete.setText(self._translator.delete_button)
        self.buttonYes.setText(self._translator.yes_button)
        self.buttonNo.setText(self._translator.no_button)

        # Modules
        self._optional.setup_language()
        self._ingredients.setup_language()
        self._steps.setup_language()
        self._components.setup_language()
    
    def open_recipe(self, recipe: RecipeData):
        self._recipe = recipe
        self.open_data(self._recipe.wrap())
    
    def open_data(self, data: dict) -> None:
        self.entryName.setText(data["name"])
        self._optional.open_data(data)
        self._optional.enter_view_mode()
        self._ingredients.open_data(data)
        self._ingredients.enter_view_mode()
        self._steps.open_data(data)
        self._steps.enter_view_mode()
        self._components.open_data(data)
        self._components.enter_view_mode()
    
    def update_recipe(self):
        # Frames
        self.frameDelete.setHidden(True)
        self.frameMainOptions.setHidden(True)
        self.frameEditOptions.setHidden(False)

        # Data
        self._recipe.unwrap(self.get_input_data())
        Application.Book.save()
        self.enter_view_mode()
    
    def cancel_update(self):
        # Frames
        self.enter_view_mode()

        # Data
        self.open_data(self._recipe.wrap())
    
    def delete_recipe(self):
        # Frames
        self.frameDelete.setHidden(False)
    
    def confirm_delete(self):
        Application.Book.delete_recipe(self._recipe)
        Application.Windows.open("book")
        self.close()

    def cancel_delete(self):
        # Frames
        self.frameDelete.setHidden(True)
        self.frameMainOptions.setHidden(False)
        self.frameEditOptions.setHidden(True)
    
    def export_pdf(self):
        pdf = PortraitPDF()
        pdf.set_font("Arial", "B", 24)
        pdf.add_page()
        pdf.cell(0, 10, f"{self.entryName.text()}", 1, 1, "C")
        pdf.ln(5)
        self._optional.write_in_pdf(pdf)
        self._ingredients.write_in_pdf(pdf)
        self._steps.write_in_pdf(pdf)
        self._components.write_in_pdf(pdf)
        pdf.output(f"pdfs/{self.entryName.text()}.pdf", "F")
    
    # def write_in_pdf


    def close_window(self):
        Application.Windows.open("book")
        self.close()

    def get_input_data(self):
        data = {}
        data.update({
            "name": self.entryName.text(),
            "date": datetime.now().timetuple()
        })
        data.update(self._optional.get_input_data())
        data.update(self._ingredients.get_input_data())
        data.update(self._steps.get_input_data())
        data.update(self._components.get_input_data())

        return data
    
    def enter_edit_mode(self):
        # Frames
        self.frameDelete.setHidden(True)
        self.frameMainOptions.setHidden(True)
        self.frameEditOptions.setHidden(False)

        # Entries
        self.entryName.setReadOnly(False)

        # Modules
        self._optional.enter_edit_mode()
        self._ingredients.enter_edit_mode()
        self._steps.enter_edit_mode()
        self._components.enter_edit_mode()

    def enter_view_mode(self):
        # Frames
        self.frameDelete.setHidden(True)
        self.frameMainOptions.setHidden(False)
        self.frameEditOptions.setHidden(True)

        # Entries
        self.entryName.setReadOnly(True)

        # Modules
        self._optional.enter_view_mode()
        self._ingredients.enter_view_mode()
        self._steps.enter_view_mode()
        self._components.enter_view_mode()
    
    def show(self) -> None:
        self.enter_view_mode()
        self.showMaximized()
