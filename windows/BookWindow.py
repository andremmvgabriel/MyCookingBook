import json
from Application import Application

from .Window import Window
from widgets.RecipeCard import RecipeCard

from windows_translators import BookWindowTranslator

class BookWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/BookWindow.ui", BookWindowTranslator())
    
    def close(self) -> bool:
        Application.Windows.open("main")
        return super().close()
    
    def setup(self) -> None:
        # Buttons
        self.buttonCreateRecipe.clicked.connect(self.create_recipe)
        self.buttonClose.clicked.connect(self.close)
    
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
        self.buttonClose.setText(self._translator.close_button)
    
    def create_recipe(self) -> None:
        Application.Windows.open("create_recipe")
    
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

