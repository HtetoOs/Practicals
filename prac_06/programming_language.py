class ProgrammingLanguage:
    def __init__(self, field="", typing="", reflection="", year=""):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, first appeared in {}".format(str(self.field), str(self.typing),
                                                                             str(self.reflection),
                                                                             str(self.year))
