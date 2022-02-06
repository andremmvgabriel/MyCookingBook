from utils import Translator

class BookWindowTranslator(Translator):
    ###
    # Labels
    ###

    __book_name_label: dict = {
        "English": "Book",
        "Portuguese": "Livro"
    }

    @property
    def book_name_label(self): return self.translate(self.__book_name_label)

    __author_name_label: dict = {
        "English": "Author",
        "Portuguese": "Autor"
    }

    @property
    def author_name_label(self): return self.translate(self.__author_name_label)

    __date_label: dict = {
        "English": "Created in",
        "Portuguese": "Criado a"
    }

    @property
    def date_label(self): return self.translate(self.__date_label)

    __recipes_counter_label: dict = {
        "English": "Number of recipes",
        "Portuguese": "Número de receitas"
    }

    @property
    def recipes_counter_label(self): return self.translate(self.__recipes_counter_label)

    __filters_label: dict = {
        "English": "Filters",
        "Portuguese": "Filtros"
    }

    @property
    def filters_label(self): return self.translate(self.__filters_label)



    ###
    # Buttons
    ###

    __create_recipe_button: dict = {
        "English": "Add new recipe",
        "Portuguese": "Adicionar nova receita"
    }

    @property
    def create_recipe_button(self): return self.translate(self.__create_recipe_button)

    __close_button: dict = {
        "English": "Close",
        "Portuguese": "Fechar"
    }

    @property
    def close_button(self): return self.translate(self.__close_button)
