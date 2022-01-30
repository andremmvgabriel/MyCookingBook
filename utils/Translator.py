from Application import Application

class Translator:
    def translate(self, target: dict) -> str:
        return target[Application.language]
