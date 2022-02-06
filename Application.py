import os
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
    language: str
    pdfs_path: str
    books_path: str
    temporary_path: str = Path.cwd() / "temp"

    __app = QtWidgets.QApplication(sys.argv)

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
                path_to_book = Path(Application.books_path) / (book_name + ".json")
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
                path_to_book = Path(Application.books_path) / (cls.__book_data.name + ".json")
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
            from windows import OptionsWindow
            from windows import CreateBookWindow
            from windows import BookWindow
            from windows import CreateRecipeWindow
            from windows import RecipeWindow

            # Windows creation
            cls.__windows["main"] = MainWindow()
            cls.__windows["options"] = OptionsWindow()
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
        def setup_language(cls, tag: str) -> None:
            logging.debug(f"Setting language in window: {tag}.")
            cls.__windows[tag].setup_language()

        @classmethod
        def get(cls, tag: str):
            return cls.__windows[tag]
        
        @classmethod
        def as_list(cls):
            return cls.__windows.keys()
    
    @classmethod
    def _create_default_configurations(cls):        
        cls.language = "English"
        cls.pdfs_path = str(Path.cwd() / "pdfs")
        cls.books_path = str(Path.cwd() / "books")
        cls._save_configurations()
    
    @classmethod
    def _load_configurations(cls):
        logging.debug("Loading app configurations...")
        if not os.path.exists("configuration.json"):
            logging.debug("Configuration file missing. Creating default one.")
            cls._create_default_configurations()
        
        try:
            with open("configuration.json", "r") as file:
                data = json.load(file)
                cls.language = data["language"]
                cls.pdfs_path = data["save_pdfs_directory"] 
                cls.books_path = data["save_books_directory"]
        except KeyError:
            logging.error("Configuration is missing a parameter. Fix the issue or delete the current configuration file (a default one will be created).")
        
        logging.debug("Configurations loaded.")
    
    @classmethod
    def _save_configurations(cls):
        with open("configuration.json", "w") as file:
            json.dump({
                "language": cls.language,
                "save_pdfs_directory": cls.pdfs_path,
                "save_books_directory": cls.books_path
            }, file, indent=4)
    
    @classmethod
    def _setup_directories(cls):
        logging.debug("Setting up the app directories.")
        Path(cls.pdfs_path).mkdir(exist_ok=True)
        Path(cls.books_path).mkdir(exist_ok=True)
        Path(cls.temporary_path).mkdir(exist_ok=True)
    
    @classmethod
    def setup_language(cls):
        logging.debug("Setting up the windows language.")
        for window in cls.Windows.as_list():
            try: # TODO - REMOVE LATER
                cls.Windows.setup_language(window)
            except Exception:
                pass
    
    @classmethod
    def _setup(cls):
        cls._load_configurations()
        cls._setup_directories()
        cls.Windows.setup()
        cls.setup_language()
    
    @classmethod
    def _init(cls):
        cls.Windows.open("main")
        cls.__app.exec_()

    @classmethod
    def start(cls) -> None:
        logging.info("Starting application: My Cooking Book")
        cls._setup()
        cls._init()
        logging.info("Closed application.")
