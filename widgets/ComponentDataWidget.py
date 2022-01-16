from windows import Window

from .OptionalDataWidget import OptionalDataWidget
from .IngredientsDataWidget import IngredientsDataWidget
from .StepsDataWidget import StepsDataWidget

class ComponentDataWidget(Window):
    __is_collapsed: bool = True
    
    def __init__(self) -> None:
        #self._optional = OptionalDataWidget()
        self._ingredients = IngredientsDataWidget()
        self._steps = StepsDataWidget()
        super().__init__("widgets/designs/ComponentDataWidget.ui")
    
    def setup(self) -> None:
        # Modules
        #self.frameContents.layout().addWidget(self._optional)
        self.frameContents.layout().addWidget(self._ingredients)
        self.frameContents.layout().addWidget(self._steps)

        self.buttonHeader.clicked.connect(self.toggle_visibility)
        self.buttonDelete.setText("Del")
        self.buttonDelete.clicked.connect(self.delete)

        self.setup_view()
    
    def delete(self):
        self.setParent(None)
    
    def toggle_visibility(self):
        self.__is_collapsed = not self.__is_collapsed
        self.setup_view()
    
    def setup_view(self):
        if self.__is_collapsed: self.show_collapsed()
        else: self.show_expanded()
    
    def show_expanded(self):
        self.frameContents.setHidden(False)

    def show_collapsed(self):
        self.frameContents.setHidden(True)
    
    def get_input_data(self):
        data = {}
        #data.update(self._optional.get_input_data())
        data.update(self._ingredients.get_input_data())
        data.update(self._steps.get_input_data())
        return data