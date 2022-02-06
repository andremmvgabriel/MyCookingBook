from utils import Translator

class ComponentDataWidgetTranslator(Translator):
    ###
    # Buttons
    ###

    __delete_button: dict = {
        "English": "Del",
        "Portuguese": "Del"
    }

    @property
    def delete_button(self): return self.translate(self.__delete_button)
