from utils import Translator

class IngredientsDataWidgetTranslator(Translator):
    ###
    # Buttons
    ###

    __ingredients_button: dict = {
        "English": "Ingredients",
        "Portuguese": "Ingredientes"
    }

    @property
    def ingredients_button(self): return self.translate(self.__ingredients_button)

    __add_button: dict = {
        "English": "Add",
        "Portuguese": "Adicionar"
    }

    @property
    def add_button(self): return self.translate(self.__add_button)

    __remove_button: dict = {
        "English": "Remove",
        "Portuguese": "Remover"
    }

    @property
    def remove_button(self): return self.translate(self.__remove_button)
