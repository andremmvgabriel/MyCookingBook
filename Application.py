import sys
import json
import logging

from pathlib import Path
from datetime import datetime

from PyQt5 import QtWidgets

from data_structures import BookData
from data_structures.RecipeData import RecipeData

class BookSaveError(Exception): ...
class BookInvalidDataError(Exception): ...
class Application:
    __books_path: str = Path.cwd() / "books"

    class Book:
        __book_data: BookData = BookData()
        __is_open: bool = False

        @classmethod
        def is_open(cls) -> bool: return cls.__is_open

        @classmethod
        def data(cls) -> BookData: return cls.__book_data

        @classmethod
        def open(cls, book_name: str) -> None:
            try:
                path_to_book = Path(Application.get_books_path()) / (book_name + ".json")
                with open(path_to_book, "r") as file:
                    cls.__book_data.unwrap(json.load(file))
                    cls.__is_open = True
            except FileNotFoundError:
                cls.__is_open = False
                logging.warning("Could not find the book to open.")
        
        @classmethod
        def save(cls):
            if not cls.__is_open: return
            if not cls.__book_data.valid: raise BookInvalidDataError
            try:
                path_to_book = Path(Application.get_books_path()) / (cls.__book_data.name + ".json")
                with open(path_to_book, "w") as file:
                    json.dump(cls.__book_data.wrap(), file, indent=4)
            except FileNotFoundError:
                logging.warning("Could not find the book to save.")

        @classmethod
        def close(cls):
            cls.__is_open = False

        @classmethod
        def create(cls, book_data: BookData) -> None:
            if cls.__is_open: raise BookSaveError
            try:
                cls.__is_open = True
                cls.__book_data = book_data
                cls.__book_data.date = datetime.now().timetuple()
                cls.save()
                cls.close()
            except BookInvalidDataError:
                raise BookSaveError
        
        @classmethod
        def add_recipe(cls, recipe_data: RecipeData) -> None:
            if not cls.__is_open: return
            for tag in recipe_data.tags:
                if tag not in cls.__book_data.tags:
                    cls.__book_data.tags.append(tag)
            cls.__book_data.recipies.append(recipe_data)
            cls.save()
        
        @classmethod
        def delete_recipe(cls, recipe_data: RecipeData) -> None:
            if not cls.__is_open: return
            cls.__book_data.recipies.remove(recipe_data)
            cls.save()

    class Windows:
        __windows: dict = dict()

        @classmethod
        def setup(cls) -> None:
            logging.debug("Setting up the multiple windows of the application.")

            # Local imports to create each window
            from windows import MainWindow
            from windows import CreateBookWindow
            from windows import BookWindow
            from windows import CreateRecipeWindow
            from windows import RecipeWindow

            # Windows creation
            cls.__windows["main"] = MainWindow()
            cls.__windows["create_book"] = CreateBookWindow()
            cls.__windows["book"] = BookWindow()
            cls.__windows["create_recipe"] = CreateRecipeWindow()
            cls.__windows["recipe"] = RecipeWindow()

            logging.debug("Windows setup completed.")
        
        @classmethod
        def open(cls, tag: str) -> None:
            cls.refresh(tag)
            logging.debug(f"Open window: {tag}.")
            cls.__windows[tag].show()
        
        @classmethod
        def refresh(cls, tag: str) -> None:
            logging.debug(f"Refreshing window: {tag}.")
            cls.__windows[tag].refresh()
        
        @classmethod
        def close(cls, tag: str) -> None:
            logging.debug(f"Closing window: {tag}.")
            cls.__windows[tag].close()

        @classmethod
        def get(cls, tag: str):
            return cls.__windows[tag]

    @classmethod
    def start(cls) -> None:
        logging.info("Starting application: My Cooking Book")

        # Creates the needed directories
        Path(cls.__books_path).mkdir(exist_ok=True)

        app = QtWidgets.QApplication(sys.argv)
        
        cls.Windows.setup()
        cls.Windows.open("main")

        app.exec_()

        logging.info("Closed application.")
    
    @classmethod
    def get_books_path(cls) -> str: return cls.__books_path

    @classmethod
    def set_books_path(cls, path: str) -> None: cls.__books_path = path
