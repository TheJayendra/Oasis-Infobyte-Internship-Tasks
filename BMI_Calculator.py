from pywebio.input import *
from pywebio.output import *

class calculation:
 
    def BMIcalculator(self, Height, Mass):

        BMI = (Mass)/(Height*Height)
 
        
        for t1, t2 in [(16, 'severely underweight'),
                       (18.5, 'underweight'),
                       (25, 'normal'), (30, 'overweight'),
                       (35, 'moderately obese')]:
 
            if BMI <= t1:
                put_text('Your BMI is', BMI, 'and the person is :', t2)
                break
 
 

Height = input("Please enter height in meters(m)", type=FLOAT)
 

Mass = input("Please enter Mass/Weight in Kilograms(Kg)", type=FLOAT)
 
obj = calculation()
obj.BMIcalculator(Height, Mass)