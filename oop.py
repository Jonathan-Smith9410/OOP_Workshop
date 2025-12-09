# Completing exercise in mix of psuedocode and copy/paste from oop_bad_code.py


class WriteObject():
    def __init__(self, type):
        self.type = type

"""
Should the first function for each of the write objects be part of def __init__(self,)?
"""

"""
If so, should those with if statements evaluating to False automatically call following function?
"""

"""
Is passing the argument the correct way of setting the type?
"""

class BallPen(WriteObject("ball pen")):
    def __turn_on(write_object):
        #press the top of the ball pen to turn it on
        pass

class InkPen(WriteObject("ink pen")):
    def __has_enough_ink(write_object):
        # check if ink pen it has enough ink
        pass
    def __refill_ink(write_object):
        # refill ink
        pass

class Pencil(WriteObject("pencil")):
    def __sharp_enough(write_object):
        # check if pencil is sharp enough
        pass
    def __sharpen(write_object):
        # sharpen the pencil
        pass

"""
If so, then should Notebook look something like this?
"""


class Notebook():
    def __init__(self, write_object):
        self.write_object = write_object
    
    def write(self, text):
        if self.write_object.type == "ball pen" or "ink pen" or "pencil":
            return text
        else:
            raise Exception("need some write object to write")