from utils import Translator

class OptionalDataWidgetTranslator(Translator):
    ###
    # Labels
    ###

    __author_label: dict = {
        "English": "Author",
        "Portuguese": "Autor"
    }

    @property
    def author_label(self): return self.translate(self.__author_label)

    __tags_label: dict = {
        "English": "Tags",
        "Portuguese": "Tags"
    }

    @property
    def tags_label(self): return self.translate(self.__tags_label)

    __description_label: dict = {
        "English": "Description",
        "Portuguese": "Descrição"
    }

    @property
    def description_label(self): return self.translate(self.__description_label)



    ###
    # Buttons
    ###

    __optional_button: dict = {
        "English": "Optional",
        "Portuguese": "Opcional"
    }

    @property
    def optional_button(self): return self.translate(self.__optional_button)

    __add_tag_button: dict = {
        "English": "Add",
        "Portuguese": "Adicionar"
    }

    @property
    def add_tag_button(self): return self.translate(self.__add_tag_button)

    __remove_tag_button: dict = {
        "English": "Remove",
        "Portuguese": "Remover"
    }

    @property
    def remove_tag_button(self): return self.translate(self.__remove_tag_button)

    __select_image_button: dict = {
        "English": "Select image",
        "Portuguese": "Selecionar imagem"
    }

    @property
    def select_image_button(self): return self.translate(self.__select_image_button)
