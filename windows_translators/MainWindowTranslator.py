from utils import Translator

class MainWindowTranslator(Translator):
    ###
    # Labels
    ###

    __title_label: dict = {
        "English": "My Cooking Books",
        "Portuguese": "Os Meus Livros de Receitas"
    }

    @property
    def title_label(self): return self.translate(self.__title_label)

    __language_label: dict = {
        "English": "Language:",
        "Portuguese": "Idioma:"
    }

    @property
    def language_label(self): return self.translate(self.__language_label)



    ###
    # Buttons
    ###

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

    __options_button: dict = {
        "English": "More options",
        "Portuguese": "Mais opções"
    }

    @property
    def options_button(self): return self.translate(self.__options_button)



    ###
    # Dropbox LANGUAGE options
    ###

    __english_opt: dict = {
        "English": "English",
        "Portuguese": "Inglês"
    }

    __portuguese_opt: dict = {
        "English": "Portuguese",
        "Portuguese": "Português"
    }

    @property
    def language_dropbox(self): return [
        self.translate(self.__english_opt),
        self.translate(self.__portuguese_opt)
    ]
