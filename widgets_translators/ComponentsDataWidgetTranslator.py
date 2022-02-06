from utils import Translator

class ComponentsDataWidgetTranslator(Translator):
    ###
    # Buttons
    ###

    __components_button: dict = {
        "English": "Components",
        "Portuguese": "Componentes"
    }

    @property
    def components_button(self): return self.translate(self.__components_button)

    __add_button: dict = {
        "English": "Add",
        "Portuguese": "Adicionar"
    }

    @property
    def add_button(self): return self.translate(self.__add_button)
