from utils import Translator

class CreateBookWindowTranslator(Translator):
    ###
    # Labels
    ###

    __required_info_label: dict = {
        "English": "Required info",
        "Portuguese": "Informação necessária"
    }

    @property
    def required_info_label(self): return self.translate(self.__required_info_label)

    __title_label: dict = {
        "English": "Title",
        "Portuguese": "Título"
    }

    @property
    def title_label(self): return self.translate(self.__title_label)

    __author_label: dict = {
        "English": "Author",
        "Portuguese": "Autor"
    }

    @property
    def author_label(self): return self.translate(self.__author_label)



    ###
    # Buttons
    ###

    __create_button: dict = {
        "English": "Create",
        "Portuguese": "Criar"
    }

    @property
    def create_button(self): return self.translate(self.__create_button)

    __cancel_button: dict = {
        "English": "Cancel",
        "Portuguese": "Cancelar"
    }

    @property
    def cancel_button(self): return self.translate(self.__cancel_button)
