from tkinter import *
from random import shuffle
from random import randint
from json import loads
class data():
    def __init__(self):
        self.formatted_cards = []
    def read_files(self):
        try:
            file = open("deck.json", encoding="utf-8")
            self.read_file = loads(file.read())
            self.cards = {}
            self.cards = self.read_file['cards']
            self.cards2 = self.read_file['cards2']
            self.deck = self.read_file['deck']
            self.values = self.read_file['values']
            #print(x)
            return self.deck, self.cards, self.values, self.cards2
        except FileNotFoundError:
            print("Missing File 'deck.json'")
            quit()

class gui:
    def  __init__(self, parent):
        self.layout_gui(parent)
        self.deck = []
        self.hands = [[],[],[],[]]
        self.asd = "spadeking.gif"
        self.deck, self.cards, self.values, self.cards2 = data.read_files(self)
        self.image = PhotoImage(file = self.asd)
        self.imageLabel = Label(self.f1, image = self.image, height = 150, width = 200, padx = 20, text = "text" )
        self.imageLabel.pack()
        self.deal_hands()
        print(self.hands)
        self.display_hand()
    def layout_gui(self, parent):
        self.f1 = Frame(parent)
        self.f1.grid(row = 1, column = 1)
        self.f2 = Frame(parent)
        self.f2.grid(row = 2, column = 1)
        self.f3 = Frame(parent)
        self.f3.grid(row = 1, column = 2)
    def deal_hands(self):
        i = 0
        print(self.deck)
        for x in range(len(self.deck)):
            if i == 4:
                i = 0
            self.hands[i].append(self.deck[x])
            i += 1
            print(i)
    def display_hand(self):
        i = 0
        for item in self.hands[0]:
            print(item)
            self.image = PhotoImage(file = self.cards[self.deck[self.deck.index(item)]])
            self.imageLabel2 = Label(self.f2, image = self.image, height = 150, width = 200, padx = 20,)
            self.imageLabel2.grid(row = 0, column = i)
            i += 1




if __name__ == '__main__':
    root = Tk()
    asd = gui(root)
    root.geometry("960x540")
    root.resizable(False, False)
    root.mainloop()
