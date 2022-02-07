import json
from Application import Application

from utils import Window
from widgets.RecipeCard import RecipeCard

from pdf_generator import PDF, PortraitPDF

from windows_translators import BookWindowTranslator

class BookWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/BookWindow.ui", BookWindowTranslator())
    
    def setup(self) -> None:
        # Buttons
        self.buttonCreateRecipe.clicked.connect(self.create_recipe)
        self.buttonExport.clicked.connect(self.export_pdf)
        self.buttonClose.clicked.connect(self.exit)
    
    def setup_language(self) -> None:
        # Labels
        # TODO - The following 4 labels are updated on the show method... Find a way to update language here
        #self.labelBookName.setText()
        #self.labelAuthorName.setText()
        #self.labelDate.setText()
        #self.labelRecipesCounter.setText()
        self.labelFilters.setText(self._translator.filters_label)
        
        # Buttons
        self.buttonCreateRecipe.setText(self._translator.create_recipe_button)
        self.buttonExport.setText(self._translator.export_button)
        self.buttonClose.setText(self._translator.close_button)
    
    def create_recipe(self) -> None:
        Application.Windows.open("create_recipe")
    
    def export_pdf(self) -> None:        
        pdf = PortraitPDF()
        self.write_in_pdf(pdf)
        pdf.output(f"pdfs/{Application.Book.data().name}.pdf", "F")
    
    def write_in_pdf(self, pdf: PDF):
        pdf.add_page()
        
        pdf.set_font("Arial", "B", 40)
        pdf.set_y(100)
        pdf.multi_cell(0, 40, Application.Book.data().name, 0, "C")

        pdf.set_font("Arial", "B", 16)
        pdf.multi_cell(0, 10, f"{self._translator.book_author_key}: {Application.Book.data().author}", 0, "C")

        for index in range(self.scrollAreaWidgetContents.layout().count() - 1):
            self.scrollAreaWidgetContents.layout().itemAt(index).widget().write_in_pdf(pdf)
    
    def exit(self):
        Application.Windows.open("main")
        self.close()
    
    def refresh(self):
        self.clear_scroll_area()
        self.build_scroll_area()

    def show(self) -> None:
        self.labelBookName.setText(f"{self._translator.book_name_label}: {Application.Book.data().name}")
        self.labelAuthorName.setText(f"{self._translator.author_name_label}: {Application.Book.data().author}")
        self.labelRecipesCounter.setText(f"{self._translator.recipes_counter_label}: {len(Application.Book.data().recipies)}")
        self.labelDate.setText(f"{self._translator.date_label}: {Application.Book.data().date[2]}/{Application.Book.data().date[1]}/{Application.Book.data().date[0]}")
        super().show()
    
    def clear_scroll_area(self):
        for index in range(self.scrollAreaWidgetContents.layout().count() - 1)[::-1]:
            self.scrollAreaWidgetContents.layout().itemAt(index).widget().setParent(None)
    
    def build_scroll_area(self):
        spacer = self.scrollAreaWidgetContents.layout().takeAt(0)

        for recipe in Application.Book.data().recipies:
            self.scrollAreaWidgetContents.layout().addWidget(RecipeCard(recipe))
        
        self.scrollAreaWidgetContents.layout().addItem(spacer)

