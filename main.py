from tkinter import *
from random import shuffle
from random import randint
from json import loads
class game():
    def __init__(self):
        self.formatted_cards = []
    def read_files(self):
        try:
            file = open("deck.json", encoding="utf-8")
            self.read_file = loads(file.read())
            self.cards = {}
            self.cards = self.read_file['cards']
            print(self.cards)
            #for item in self.cards:
             #   print(item)
            self.deck = self.read_file['deck']
            self.values = self.read_file['values']
            for item in self.cards:
                self.formatted_cards.append(PhotoImage(file = self.cards[item]))
            #for item in self.deck:
             #   print(item)
            #for item in self.values:
            #    print(item)
            #for item in self.cards:
            #    print(item)
            return self.deck, self.formatted_cards, self.values
        except FileNotFoundError:
            print("Missing File 'deck.json'")
            quit()



class gui:
    def  __init__(self, parent):
        self.formatted_cards = []
        self.layout_gui(parent)
        self.deck = []
        self.card_reference = {}
        self.evens = False
        self.runs = True
        self.current_card = None
        self.hands = [[],[],[],[]]
        self.cards, self.deck, self.values = game.read_files(self)
        #self.run_game(parent)
    
    def layout_gui(self, parent):
        f1 = Frame(parent)
        f1.grid(row = 1, column = 1)
        f2 = Frame(parent)
        f2.grid(row = 2, column = 1)
        f3 = Frame(parent)
        f3.grid(row = 1, column = 2)
    def play_card(self, card):
        print(card)
        PhotoImage(self.f1, Image = "asd")
    def shuffle_deck(self):
        shuffle(self.deck[0])
        x = 0
        for i in range(4):
            to_remove = randint(0,len(self.deck[0])-1)
            self.deck[0].pop(to_remove)
        for i in range(len(self.deck[0])):
            if x == 4:
                x = 0
            self.hands[x].append(self.deck[0][0])
            self.deck[0].pop(0)
            x += 1
            print(self.hands[0])
            print(self.hands[1])
            print(self.hands[2])
            print(self.hands[3])
            print(self.deck)
    def ai(self):
        if self.evens == False and self.runs == False:
            print()
    def check_card(self):
        pass
    def display_hand(self):
        pass
    def print_deck(self):
        i = 0
        x = 0
        z = 0
        for item in self.cards:
            print(item)
            i += 1
        for item in self.deck:
            print(item)
            x += 1
        for item in self.values:
            print(item)
            z += 1
        print(F"{i},{x},{z}")
    def show_hands(self):
        print(self.hands[0], len(self.hands[0]))
        print(self.hands[1], len(self.hands[1]))
        print(self.hands[2], len(self.hands[2]))
        print(self.hands[3], len(self.hands[3]))
    


if __name__ == '__main__':
    root = Tk()
    asd = gui(root)
    root.geometry("960x540")
    root.resizable(False, False)
    root.mainloop()
