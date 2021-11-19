#backend of all program
import time 
from tkinter import*
import requests
import json

class Inputs:

    def Take_inputs(self, answer):
        i = 0
        if answer == ('yes' or 'Yes'):
            i=1
        else: i=0
        return(i)

class OperatingInputs:
    
    def DecisionOnPassing(self, checked_input):
        if checked_input==1:
            i=1
           #print('decision made')
        else: 
            i=0
            print('negative')
        return(i)

def Forecast(): #returns a list = [current temperature, 'feels like', humidity]
    #list for temperatures and pressure
    info_weather = [] 
    
    #getting current temperature in valkeakoski
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Valkeakoski&appid=64e7550aa2f530d893c8f2cb4c323f95")
    
    #filtering information with "main" citeria
    response_json= response.json()['main']
   
    #appending information to the list
    for d in response_json:
        if d == 'temp':
            result= round(response_json[d]-273, 2)
            info_weather.append(result)
        if d == 'feels_like':
            result= round(response_json[d]-273, 2)
            info_weather.append(result)
        if d == 'humidity':
            info_weather.append(response_json[d])
    print(info_weather)
    
class OperatingOutputs:

    def PassToDevice(self, input_operator):
        if input_operator==1:
            heater =1 
        else: heater=0 
        print('heater=', heater)   
        return(heater)

def OnButtonPress(): 
    question = Inputs() #creating an instance of Inputs class
    K = question.Take_inputs(input('Do u want me hot, daddy?')) #returning the result of Take_inputs with our answer into K

    decision = OperatingInputs() #instance
    D = decision.DecisionOnPassing(K) #result of DecisionOnPassing with K given

    heating = OperatingOutputs()
    heating.PassToDevice(D)


def ProcessingTime():
    t = time.localtime()
    string_time = time.asctime(t)
    only_time = string_time[11:19]
    hour = int(string_time[11:13])
    minutes = int(string_time[14:16])
    seconds = int(string_time[17:19])
    print(hour, minutes, seconds)

def main():
    Forecast()
    OnButtonPress()    
    ProcessingTime()
   
    

if __name__=='__main__':
    main()
     


