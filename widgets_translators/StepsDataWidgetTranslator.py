from utils import Translator

class StepsDataWidgetTranslator(Translator):
    ###
    # Buttons
    ###

    __steps_button: dict = {
        "English": "Steps",
        "Portuguese": "Passos"
    }

    @property
    def steps_button(self): return self.translate(self.__steps_button)

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



    ###
    # Keywords
    ###

    __step_key: dict = {
        "English": "Step",
        "Portuguese": "Passo"
    }

    @property
    def step_key(self): return self.translate(self.__step_key)
