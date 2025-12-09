# The provided code is a good starting point to improve 
# by applying all four OOP principles (encapsulation, abstraction, inheritance, and polymorphism), 
# but it has several issues that violate good OOP practices. Specifically, the code:
# # - Violates the Single Responsibility Principle (SRP) by mixing logic for writing, 
# # sharpening, checking ink, etc., within the Notebook class.
# 
# # - Doesn’t take advantage of polymorphism to simplify handling different types of writing objects.
# 
# # - The WriteObject class does not encapsulate its behavior and relies on the Notebook class
# # to know how to use different writing tools.
# 
# # - Abstraction is not well-implemented, as private methods like __sharpen and __refill_ink 
# # should be part of the writing tool objects themselves, not the Notebook.


class WriteObject():
    def __init__(self, type):
        self.type = type

class Notebook():
    def __init__(self, write_object):
        self.write_object = write_object
    
    def write(self, text):
        if self.write_object.type == "ball pen":
            self.__turn_on(self.write_object)
            return text
        elif self.write_object.type == "ink pen":
            if self.__has_enough_ink(self.write_object):
                return text
            else:
                self.__refill_ink(self.write_object)
                return text
        elif self.write_object.type == 'pencil':
            if self.__sharp_enough(self.write_object):
                return text
            else:
                self.__sharpen(self.write_object)
                return text
        else:
            raise Exception("need some write object to write")
            
    # private methods
    def __sharpen(write_object):
        # sharpen the pencil
        pass

    def __refill_ink(write_object):
        # refill ink
        pass

    def __sharp_enough(write_object):
        # check if pencil is sharp enough
        pass


    def __has_enough_ink(write_object):
        # check if ink pen it has enough ink
        pass

    def __turn_on(write_object):
        #press the top of the ball pen to turn it on
        pass

pencil = WriteObject('pencil')

notebook = Notebook(pencil)
notebook.write('hi my dear calendar')