from utils import Translator

class RecipeWindowTranslator(Translator):
    ###
    # Labels
    ###

    __recipe_name_label: dict = {
        "English": "Recipe name",
        "Portuguese": "Nome da receita"
    }

    @property
    def recipe_name_label(self): return self.translate(self.__recipe_name_label)

    __confirm_label: dict = {
        "English": "Confirm",
        "Portuguese": "Confirmar"
    }

    @property
    def confirm_label(self): return self.translate(self.__confirm_label)



    ###
    # Buttons
    ###

    __update_button: dict = {
        "English": "Save",
        "Portuguese": "Gravar"
    }

    @property
    def update_button(self): return self.translate(self.__update_button)

    __cancel_button: dict = {
        "English": "Cancel",
        "Portuguese": "Cancelar"
    }

    @property
    def cancel_button(self): return self.translate(self.__cancel_button)

    __export_button: dict = {
        "English": "Export PDF",
        "Portuguese": "Exportar PDF"
    }

    @property
    def export_button(self): return self.translate(self.__export_button)

    __edit_button: dict = {
        "English": "Edit",
        "Portuguese": "Editar"
    }

    @property
    def edit_button(self): return self.translate(self.__edit_button)

    __close_button: dict = {
        "English": "Close",
        "Portuguese": "Fechar"
    }

    @property
    def close_button(self): return self.translate(self.__close_button)

    __delete_button: dict = {
        "English": "Delete",
        "Portuguese": "Apagar"
    }

    @property
    def delete_button(self): return self.translate(self.__delete_button)

    __yes_button: dict = {
        "English": "Yes",
        "Portuguese": "Sim"
    }

    @property
    def yes_button(self): return self.translate(self.__yes_button)

    __no_button: dict = {
        "English": "No",
        "Portuguese": "Não"
    }

    @property
    def no_button(self): return self.translate(self.__no_button)