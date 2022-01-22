from windows import Window

from .ComponentDataWidget import ComponentDataWidget

class ComponentsDataWidget(Window):
    __is_collapsed: bool = False

    def __init__(self) -> None:
        super().__init__("widgets/designs/ComponentsDataWidget.ui")
    
    def setup(self):
        # Buttons
        self.buttonComponents.setText("Componentes")
        self.buttonComponents.clicked.connect(self.toggle_visibility)
        self.buttonAdd.setText("Adicionar")
        self.buttonAdd.clicked.connect(self.add_component)

        self.buttonAdd.setEnabled(False)

        # Entries
        self.entryComponent.textChanged.connect(self.text_changed)
        self.entryComponent.returnPressed.connect(self.return_key_pressed)

        self.setup_view()
    
    def text_changed(self):
        # Get text
        text = self.entryComponent.text()

        # Checks button visibility
        if len(text) < 3: self.buttonAdd.setEnabled(False)
        else: self.buttonAdd.setEnabled(True)
    
    def return_key_pressed(self):
        # Get text
        text = self.entryComponent.text()

        # Checks button visibility
        if len(text) >= 3: self.add_component()
    
    def add_component(self):
        # Get text
        text = self.entryComponent.text()
        text = text.capitalize()
        self.entryComponent.setText("")

        spacer = self.scrollComponentsLayout.layout().takeAt(self.scrollComponentsLayout.layout().count()-1)
        component = ComponentDataWidget()
        component.buttonHeader.setText(text)
        self.scrollComponentsLayout.layout().addWidget(component)
        self.scrollComponentsLayout.layout().addItem(spacer)
        self.setup_view()        

    def toggle_visibility(self):
        self.__is_collapsed = not self.__is_collapsed
        self.setup_view()

    def setup_view(self):
        if self.__is_collapsed: self.show_collapsed()
        else: self.show_expanded()
    
    def show_expanded(self):
        self.frameControl.setHidden(False)
        self.frameSpacer.setHidden(False)
        if self.scrollComponentsLayout.layout().count() > 1:
            self.frameComponents.setHidden(False)

    def show_collapsed(self):
        self.frameControl.setHidden(True)
        self.frameSpacer.setHidden(True)
        self.frameComponents.setHidden(True)
    
    def open_data(self, data: dict) -> None:
        # Clears
        self.clear()
        
        spacer = self.scrollComponentsLayout.layout().takeAt(0)

        # Writes
        for component_data in data["components"]:
            component = ComponentDataWidget()
            component.open_data(component_data)
            component.enter_view_mode()
            self.scrollComponentsLayout.layout().addWidget(component)
        
        self.scrollComponentsLayout.layout().addItem(spacer)
    
    def enter_edit_mode(self):
        self.frameControl.setHidden(False)

        for index in range(self.scrollComponentsLayout.layout().count() - 1):
            self.scrollComponentsLayout.layout().itemAt(index).widget().enter_edit_mode()

    def enter_view_mode(self):
        self.frameControl.setHidden(True)

        for index in range(self.scrollComponentsLayout.layout().count() - 1):
            self.scrollComponentsLayout.layout().itemAt(index).widget().enter_view_mode()
    
    def get_input_data(self):
        return { "components": [self.scrollComponentsLayout.layout().itemAt(index).widget().get_input_data() for index in range(self.scrollComponentsLayout.layout().count() - 1)] }
    
    def clear(self):
        spacer = self.scrollComponentsLayout.layout().takeAt(self.scrollComponentsLayout.layout().count()-1)

        for index in range(self.scrollComponentsLayout.layout().count())[::-1]:
            self.scrollComponentsLayout.layout().takeAt(index).widget().setParent(None)
        
        self.scrollComponentsLayout.layout().addItem(spacer)
