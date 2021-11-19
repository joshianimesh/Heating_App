#backend of all program
import time 
from tkinter import*
import requests
import json

class Inputs:

    def Take_input_manual(self, answer): #function to turn on manually without time control
        i = 0
        if answer == ('yes' or 'Yes'):
            i=1
        else: i=0
        return(i)

    def Take_input_time(self, tim): #probably implementation of time setting mode (not finished)
        res=0
        while (cur!= tim) or (cur>tim):
            cur = GetCurTime()
            time.sleep(10)
            res = 1
        return(res)

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

def ManualTurnOn(): 
    question = Inputs() #creating an instance of Inputs class
    K = question.Take_input_manual(input('Do u want me hot, daddy?')) #returning the result of Take_inputs with our answer into K

    decision = OperatingInputs() #instance
    D = decision.DecisionOnPassing(K) #result of DecisionOnPassing with K given

    heating = OperatingOutputs()
    heating.PassToDevice(D)


def GetCurTime():
    time=[]
    t = time.localtime() #current time
    string_time = time.asctime(t) #converting current time to the string 

    time.append(int(string_time[11:13])) #current hour in integer
    time.append(int(string_time[14:16])) #current minute in int
    time.append(int(string_time[17:19]))
    return(time)
    
def ManualPutTime():
    reply = []
    set_tim = int(input('When im gonna sleep, daddy?'))
    reply.append(set_tim)
    return(reply)

def main():
    Forecast()
    #ManualTurnOn()    
    GetCurTime()
    
    

if __name__=='__main__':
    main()
     


