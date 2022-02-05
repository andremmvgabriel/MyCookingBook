from utils import Translator

class OptionsWindowTranslator(Translator):
    ###
    # Labels
    ###

    __pdfs_label: dict = {
        "English": "PDFs directory",
        "Portuguese": "Directoria para os PDFs gerados"
    }

    @property
    def pdfs_label(self): return self.translate(self.__pdfs_label)

    __books_label: dict = {
        "English": "Books directory",
        "Portuguese": "Directoria para os livros gerados"
    }

    @property
    def books_label(self): return self.translate(self.__books_label)



    ###
    # Buttons
    ###

    __pdfs_button: dict = {
        "English": "Select folder",
        "Portuguese": "Selecionar pasta"
    }

    @property
    def pdfs_button(self): return self.translate(self.__pdfs_button)

    __books_button: dict = {
        "English": "Select folder",
        "Portuguese": "Selecionar pasta"
    }

    @property
    def books_button(self): return self.translate(self.__books_button)

    __save_button: dict = {
        "English": "Save",
        "Portuguese": "Gravar"
    }

    @property
    def save_button(self): return self.translate(self.__save_button)

    __cancel_button: dict = {
        "English": "Cancel",
        "Portuguese": "Cancelar"
    }

    @property
    def cancel_button(self): return self.translate(self.__cancel_button)



    ###
    # Search Directory Windows
    ###

    __pdfs_select_dir: dict = {
        "English": "Select directory to save PDFs",
        "Portuguese": "Selectionar diretoria para gravar PDFs"
    }

    @property
    def pdfs_select_dir(self): return self.translate(self.__pdfs_select_dir)

    __books_select_dir: dict = {
        "English": "Select directory to save Books",
        "Portuguese": "Selectionar diretoria para gravar livros"
    }

    @property
    def books_select_dir(self): return self.translate(self.__books_select_dir)
