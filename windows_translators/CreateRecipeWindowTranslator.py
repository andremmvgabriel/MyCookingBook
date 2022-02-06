from utils import Translator

class CreateRecipeWindowTranslator(Translator):
    ###
    # Labels
    ###

    __recipe_name_label: dict = {
        "English": "Recipe name",
        "Portuguese": "Nome da receita"
    }

    @property
    def recipe_name_label(self): return self.translate(self.__recipe_name_label)



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



    ###
    # Line Edits
    ###

    __name_placeholder_entry: dict = {
        "English": "Write recipe name here",
        "Portuguese": "Escreve o nome da receita aqui"
    }

    @property
    def name_placeholder_entry(self): return self.translate(self.__name_placeholder_entry)
