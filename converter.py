
import time
from datetime import datetime, timedelta


def conversion(value):
    result = ""
    for i in range(len(value)):
        if i % 4 == 0 and i != 0:
            result += ' '
        result += value[i]
    return result


def numericalConverter(IN,OP):
    try:
        num_of_bits = 4
        if OP == "Decimal to Binary":
            value = str(bin(int(IN,10)))[2:].zfill(num_of_bits)
        elif OP == "Decimal to Hex":
            value = str(hex(int(IN,10)))[2:].zfill(num_of_bits)
        elif OP == "Decimal to Oct":
            value = str(oct(int(IN,10)))[2:].zfill(num_of_bits)

        elif OP == "Binary to Decimal":
            value = str(int(IN,2))
        elif OP == "Binary to Hex":
            value = str(hex(int(IN,2)))[2:].zfill(num_of_bits)
        elif OP == "Binary to Oct":
            value = str(oct(int(IN,2)))[2:].zfill(num_of_bits)

        elif OP == "Hex to Decimal":
            value = str(int(IN,16))
        elif OP == "Hex to Binary":
            value = str(bin((int(IN,16))))[2:].zfill(num_of_bits)
        elif OP == "Hex to Oct":
            value = str(oct(int(IN,16)))[2:].zfill(num_of_bits)
        

        return conversion(value)
    except:
        return "Invalid Input"



def massConverter(IN, OP):
    try:
        IN = float(IN)
        if OP == "Kg to Gram":
            value = str(IN * 1000)
        if OP == "Gram to Kg":
            value = str(In * 0.001)
        if OP == "Kg to Pound":
            value = str(IN * 2.204623)

        if OP == "Pound to Kg":
            value = str(IN * 0.4535924)
        if OP == "Gram to Pound":
            value = str(IN * 0.002204623)
        return value
    except:
        return "Invalid Input"


def tempConverter(IN, OP):
    try:
        IN = float(IN)
        if OP == "°F to °C":
            value = str((IN - 32.00)/1.8000)
        if OP == "°C to °F":
            value = str(IN * 1.8000 + 32.00)
        if OP == "°C to K":
            value = str(273.15 + IN)
        if OP == "°F to K":
            value = str(254.9278 + IN)
        if OP == "K to °C":
            value = str(-273.15 + IN)
        if OP == "K to °F":
            value = str(-459.67 + IN)
        return value
    except:
        return "Invalid Input"




def lenConverter(IN, OP):
    try:
        IN = float(IN)
        if OP == "Feet to Inch":
            value = str(12 * IN)
        if OP == "Feet to CM":
            value = str(30.48 * IN)
        if OP == "Feet to Meter":
            value = str(0.3048 * IN)


        if OP == "Inch to Feet":
            value = str(0.08333333 * IN)
        if OP == "Inch to CM":
            value = str(2.54 * IN)
        if OP == "Inch to Meter":
            value = str(0.0254 * IN)

        if OP == "CM to Feet":
            value = str(0.0328084 * IN)    
        if OP == "CM to Inch":
            value = str(0.3937008 * IN)
        if OP == "CM to Meter":
            value = str(0.01 * IN)
        
        if OP == "Meter to Inch":
            value = str(39.37008 * IN)
        if OP == "Meter to Feet":
            value = str(3.28084 * IN)
        if OP == "Meter to CM":
            value = str(100 * IN)
        if OP == "Meter to KM":
            value = str(0.001 * IN)
        if OP == "Meter to Mile":
            value = str(0.0006213712 * IN)

        if OP == "KM to Mile":
            value = str(0.6213712 * IN)
        if OP == "Mile to KM":
            value = str(1.609344 * IN)
        
        
        return value
    except:
        return "Invalid Input"

def ageConverter(IN,OP):
    try:
        year = int(IN.split(',')[0])
        month = int(IN.split(',')[1])
        date = int(IN.split(',')[2])
        dob = datetime(year,month,date)
        new_date = datetime.today() - dob

        totalDays = int(new_date.days)
        totalMonths = int(new_date.days/30.4375)

        years = int(new_date.days/365.25)
        RD = new_date.days % 365.25
        months = int(RD/30.4375)
        days= int(RD % 30.4375)

        if OP == "Full Details":
            return str(years) +' years '+ str(months) +" months " + str(days)+ " days"
        elif OP == "Years":
            return str(years) + ' years'
        elif OP == "Month":
            return str(totalMonths) + ' months'
        elif OP == "Days":
            return str(totalDays) + ' days'
    except:
        return "Invalid Input"






