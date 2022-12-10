# this program will check if a certain index is below a threshold. Good tool for
# keeping track of cheap funds/ETFs

from marketIndexScraper import getMarketIndex
from tkinter import *
import sys

# layout for GUI class
class stockGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Index change list")
        self.master.geometry("350x800")

        self.addMarketIndicesEntries()

    # check if change is positive or negative, and give distint color
    def checkChangeValue(self, changeValue):
        if changeValue >= 0:
            return "green"
        else:
            return "red"


    # adds entries for each market index
    def addMarketIndicesEntries(self):
        master = self.master

        header1Label = Label(master, text="Market index", font=('Arial', 12, 'bold'))
        header1Label.grid(row=0, column=0,pady=2)

        header2Label = Label(master, text="Change (%)", font=('Arial', 12, 'bold'))
        header2Label.grid(row=0, column=1, pady=2)

        for i in range(len(marketIndex)):
            for j in range(len(marketIndex[0])):

                if j == 0:
                    text = marketIndex[i][j]
                    textColor = "black"
                    width = 30
                else:
                    text = str(marketIndex[i][j]) + "%"
                    changeValue = marketIndex[i][j]
                    textColor = self.checkChangeValue(changeValue)
                    width = 10

                # add every market index in a grid
                self.e = Entry(master, width=width, fg=textColor, font=('Arial', 10, 'normal'))
                self.e.grid(row=i+1, column=j, sticky="w")
                self.e.insert(END, text)

# define marketIndex list
marketIndex = getMarketIndex()

# checks if conditions are met, and runs the program if so
def checkIfConditionsAreMet():
    whatToCheck = sys.argv[1]
    operator = sys.argv[2]
    threshold = float(sys.argv[3])

    minVal = 20
    maxVal = -20
    sum = 0
    for j in range(len(marketIndex)):
        value = float(marketIndex[j][1][:-1])
        marketIndex[j][1] = value
        sum += value

        if value < minVal:
            minVal = value

        if value > maxVal:
            maxVal = value

    # exit program if conditions are not met
    if whatToCheck == "sum":
        if operator == "gt":
            if sum <= threshold:
                exit()
        elif operator == "lt":
            if sum >= threshold:
                exit()
    elif whatToCheck == "value":
        if operator == "gt":
            if maxVal <= threshold:
                exit()
        elif operator == "lt":
            if minVal >= threshold:
                exit()

    # sort marketIndex list by second element in every sublist
    marketIndex.sort(key=lambda x: x[1])

    runProgram()

# runs the GUI
def runProgram():
    root = Tk()
    myGUI = stockGUI(root)
    root.mainloop()


checkIfConditionsAreMet()









