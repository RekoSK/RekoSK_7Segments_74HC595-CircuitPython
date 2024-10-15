# **RekoSK 7 Segments 74HC595 library for CircuitPython**
A circuitpython library which was inspired by my arduino library, which makes working with 7 segments and 74HC595 (shift registers) easy.
## **What does it feature?**
* Printing any decimal number (even negative ones)
* Clearing the display
* *Coming (really) soon* - Printing text string
* Animations for every functiom
* Printing out segments
* Support for any lenght of display

## **How to use?**
After downloading, move the library to the `lib` folder on your circuit python device and import the library into the code (or just the class, how i like to do it):

```python
from RekoSK_7Segments_74HC595 import RekoSK_7Segments_74HC595 as ss
```

After that you need to initialize the 7 segment:
```python
My7Segment: ss = ss(input, clk, latch, numberOfDigits, negatedInput, DefaultDelay)
```

Now, you can use all the functions. The most useful one is `printINT()`, which will print any number (even negative ones):
```python
My7Segment.printINT(value, animation)
```
**For more info and help, you can check tutorials!**

#### If you like this project and you want to support it, please give me a star ;).