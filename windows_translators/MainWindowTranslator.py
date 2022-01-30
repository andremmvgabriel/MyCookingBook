from utils import Translator

class MainWindowTranslator(Translator):
    __title_label: dict = {
        "English": "My Cooking Books",
        "Portuguese": "Os Meus Livros de Receitas"
    }

    @property
    def title_label(self): return self.translate(self.__title_label)

    __open_button: dict = {
        "English": "Open",
        "Portuguese": "Abrir"
    }

    @property
    def open_button(self): return self.translate(self.__open_button)

    __create_button: dict = {
        "English": "Create new book",
        "Portuguese": "Criar um novo livro"
    }

    @property
    def create_button(self): return self.translate(self.__create_button)

    __import_button: dict = {
        "English": "Import book",
        "Portuguese": "Importar livro"
    }

    @property
    def import_button(self): return self.translate(self.__import_button)
