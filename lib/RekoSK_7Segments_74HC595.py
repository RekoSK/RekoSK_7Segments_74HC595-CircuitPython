"""A circuitpython library for connecting 74HC595s to 7segments easily"""


import board
import digitalio
from time import sleep

class RekoSK_7Segments_74HC595:
    
    
    def __init__(self, _input, _clk, _latch, numberOfDigits: int, negatedInput: bool, defDelay: float = 0.025) -> None:
        self.__input = digitalio.DigitalInOut(_input)
        self.__clk = digitalio.DigitalInOut(_clk)
        self.__latch = digitalio.DigitalInOut(_latch)
        self.defDelay = defDelay
        
        
        self.__input.direction = digitalio.Direction.OUTPUT
        self.__clk.direction = digitalio.Direction.OUTPUT
        self.__latch.direction = digitalio.Direction.OUTPUT

        self.numberOfDigits = numberOfDigits
        self.negatedInput = negatedInput
    
    def __Show(self):
        self.__latch.value = True
        self.__latch.value = False
    
    def SegmentPrint(self, status: bool, visible: bool):
        #if self.negatedInput:
            #status = not status

        self.__input.value = status
        self.__clk.value = True
        self.__clk.value = False

        if visible:
            self.__Show()
            sleep(self.defDelay)
            
    def Clear(self, anim: bool = False):
        for i in range((8 * self.numberOfDigits)):
            self.SegmentPrint(False, anim)
    
    def Create1(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)
        
        for i in range(4):
            self.SegmentPrint(False, anim)

        for i in range(2):
            self.SegmentPrint(True, anim)

        
        self.SegmentPrint(False, anim)
            
    def Create2(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        self.SegmentPrint(True, anim)
        self.SegmentPrint(False, anim)
        self.SegmentPrint(True, anim)
        self.SegmentPrint(True, anim)
        self.SegmentPrint(False, anim)
        self.SegmentPrint(True, anim)
        self.SegmentPrint(True, anim)

    
    def Create3(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        self.SegmentPrint(True, anim)
        self.SegmentPrint(False, anim)
        self.SegmentPrint(False, anim)

        for i in range(4):
            self.SegmentPrint(True, anim)
    
    def Create4(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        self.SegmentPrint(True, anim)
        self.SegmentPrint(True, anim)
        self.SegmentPrint(False, anim)
        self.SegmentPrint(False, anim)
        self.SegmentPrint(True, anim)
        self.SegmentPrint(True, anim)
        self.SegmentPrint(False, anim)

    def Create5(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        self.SegmentPrint(True, anim)
        self.SegmentPrint(True, anim)
        
        self.SegmentPrint(False, anim)
        
        self.SegmentPrint(True, anim)
        self.SegmentPrint(True, anim)
        self.SegmentPrint(False, anim)
        self.SegmentPrint(True, anim)


    def Create6(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)
        
        for i in range(5):
            self.SegmentPrint(True, anim)
        
        self.SegmentPrint(False, anim)
        self.SegmentPrint(True, anim)


    def Create7(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        for i in range(4):
            self.SegmentPrint(False, anim)
        
        for i in range(3):
            self.SegmentPrint(True, anim)


    def Create8(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        for i in range(7):
            self.SegmentPrint(True, anim)


    def Create9(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        self.SegmentPrint(True, anim)
        self.SegmentPrint(True, anim)
        
        self.SegmentPrint(False, anim)
        
        for i in range(4):
            self.SegmentPrint(True, anim)


    def Create0(self, dot: bool, anim: bool = False):
        self.SegmentPrint(dot, anim)

        self.SegmentPrint(False, anim)

        for i in range(6):
            self.SegmentPrint(True, anim)


    def CreateMinus(self, anim: bool = False):
        self.SegmentPrint(False, anim)
        self.SegmentPrint(True, anim)
        
        for i in range(6):
            self.SegmentPrint(False, anim)


    def CreateBlank(self, anim: bool = False):
        for i in range(8):
            self.SegmentPrint(False, anim)
            
    def __IntLogic(self, num: int, anim: bool):
        # Dictionary mapping numbers to corresponding functions
        create_methods = {
            0: self.Create0,
            1: self.Create1,
            2: self.Create2,
            3: self.Create3,
            4: self.Create4,
            5: self.Create5,
            6: self.Create6,
            7: self.Create7,
            8: self.Create8,
            9: self.Create9
        } 

        # Call the appropriate function, default to CreateBlank if number is not 0-9
        if num in create_methods:
            create_methods[num](False, anim)
        else:
            self.CreateBlank(anim)
            
    def printINT(self, value: int, anim: bool = False):
        """if value == 0:
            self.Create0(False, anim)
            if not anim:
                self.__Show()
            return"""
        
        absval = abs(value)
        lenghtINT = len(str(value))

        
        if lenghtINT > self.numberOfDigits:
            raise ValueError("Lenght of value needs to be the same or smaller than lenght of numberOfDigits defined at __init__.\r\nMinus sign counts into lenght of value too.")
        
        
        
        lenghtINT = len(str(absval))
        for i in range(lenghtINT):
            if i != 0:
                x = int((absval / (i * 10)) % 10)
            else:
                x = int((absval) % 10)
            
            self.__IntLogic(x, anim)
            
        blanks:int = len(str(self.numberOfDigits)) - lenghtINT
        

        for i in range(blanks + 1):
            print("Creating blank")
            self.CreateBlank(anim)
            
        if absval != value:
            self.CreateMinus(anim)
        
        
        
        
        if not anim:
            self.__Show()
    
    def Clear(self, anim:bool = False):
        for i in range(8 * self.numberOfDigits):
            self.SegmentPrint(False, anim)
        
        if not anim:
            self.__Show()