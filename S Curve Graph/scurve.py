#Name: Ethan Rackleff
###Description: This application is meant to help the user decide whether or not a stock is a good investment
###based off an s-curve which uses multiple variables where 3 of them have to be predicted
#Citations: https://stats.areppim.com/glossaire/scurve_def.htm ,



import math #to do simple calculations
import matplotlib.pyplot as plt #for creating the s-cruve graph
import numpy as np #to use e, natural logirithm, and arange

greeting = input("Hey, what's your name?") #just to greet user
greeting2 = input("Okay,are you ready to make some money? (yes or no)") #fun intro
if greeting2 in ['y', 'Y', 'yes', 'Yes', 'YES']: #if the user types some type of "yes" the program will function
    print("Well let's get started then...")

    name = input("What is the name of your stock?")#name of your stock (it can be the symbol or name)
    tstart = input("Start time (year)") #the year the stock was founded or the product was put into production
    tend = input("End time (year)") #the year you want to predict to
    vstart = input("Value at the start") #value at the start (IPO or number of ____ bought)
    saturation = input("Value at peak or plateau") #the maximum value or amount of whatever stock or product (you or an expert needs to predict these through previous related stocks)
    growth = input("What is your growth time?") #calculate the growth time by applying Monte Carlo to the distribution of the residuals from the least squares or have an expert do it for you
    mid = input("What is going to be the midpoint of your graph?") #calculated based off historic data and trial and error or an expert
###from here to the next triple hashtag it is just turning the inputs into floats, so they can be put into the s-curve formula
    tstart = float(tstart)
    tend = float(tend)
    vstart = float(vstart)
    saturation = float(saturation)
    growth = float(growth)
    mid = float(mid)
###
    t = np.arange(tstart, tend, 1) #sets up the x coordinate, so for every y coordinate the year will go up one

    y = saturation/(1 + np.e**(((-1*(np.log(81)))/growth)*(t-mid))) #the s-curve formula that will create the final graph

    print(t) #shows exact values for user of the year
    print(y) #shows exact values of the growth per year for user

    plt.figure(1) #creates graph
    plt.subplot(211) #puts it on a subplot for the potential of multiple graphs (when I set up webscraping)
    plt.plot(t,y,'rs') #plots the graph... t is the year and y is the growth
    plt.title(name) #displays the name of the stock the user inputed
    plt.axis([tstart, tend, 0, saturation]) #sets up where the axeses stop and start
    plt.ylabel('Growth') #labels the y axis as growth
    plt.xlabel('Years') #labels the x axis as years
    plt.show() #displays the graph

elif greeting2 in ['n','N','no','No','NO']: #if the user did not say they were ready to make some money this message displays
    print("Well maybe this application isn't for you")
else: #if they said neither no or yes this message will display
    print("I don't think that was one of the choices")
