import json
from Application import Application

from .Window import Window
from widgets.RecipeCard import RecipeCard

class BookWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/BookWindow.ui")
    
    def setup(self) -> None:
        # Buttons
        self.buttonCreateRecipe.clicked.connect(self.create_recipe)
    
    def create_recipe(self) -> None:
        Application.Windows.open("create_recipe")
    
    def refresh(self):
        self.clear_scroll_area()
        self.build_scroll_area()

    def show(self) -> None:
        self.labelBookName.setText(f"Livro: {Application.Book.data().name}")
        self.labelAuthorName.setText(f"Autor: {Application.Book.data().author}")
        self.labelRecipesCounter.setText(f"Contém {len(Application.Book.data().recipies)} receitas.")
        self.labelDate.setText(f"Criado a: {Application.Book.data().date[2]}/{Application.Book.data().date[1]}/{Application.Book.data().date[0]}")
        super().show()
    
    def clear_scroll_area(self):
        for index in range(self.scrollAreaWidgetContents.layout().count() - 1)[::-1]:
            self.scrollAreaWidgetContents.layout().itemAt(index).widget().setParent(None)
    
    def build_scroll_area(self):
        spacer = self.scrollAreaWidgetContents.layout().takeAt(0)

        for recipe in Application.Book.data().recipies:
            self.scrollAreaWidgetContents.layout().addWidget(RecipeCard(recipe))
        
        self.scrollAreaWidgetContents.layout().addItem(spacer)

