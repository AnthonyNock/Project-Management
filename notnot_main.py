from json import loads
from tkinter import *
from random import shuffle

class gui:
    def __init__(self, parent):
        # Define variables and canvas
        self.canvas = Canvas(root, width = 960, height = 540)
        self.canvas.pack()
        self.hands = [[],[],[],[]]
        self.current_displayed_hand = []
        # Read file
        file = open("deck.json", encoding="utf-8")
        self.read_file = loads(file.read())
        self.cards = self.read_file['cards2']
        self.deck = self.read_file['deck']
        self.values = self.read_file['values']
        self.path = self.cards[0]
        self.shuffleddeck = self.deck
        self.play_card(parent, self.cards[9])
        self.shuffle_deck()
        self.deal_hands()
        self.display_hand()

    def play_card(self,parent, card):
        self.image = PhotoImage(file = card)
        self.canvas.create_image(60,90, image = self.image)
        self.current_card = self.image
        #l1 = Label(parent, image = self.image)
        #l1.grid(row = 0, column=0)
    
    def deal_hands(self):
        i = 0
        for x in range(len(self.shuffleddeck)):
            if i == 4:
                i = 0
            self.hands[i].append(self.shuffleddeck[x])
            i += 1
    
    def shuffle_deck(self):
        shuffle(self.shuffleddeck)
        self.shuffleddeck = self.shuffleddeck[4:]
    
    def card_clicked(self, card):
        print(card)
    
    def display_hand(self):
        i = 0
        x = 60
        add_amount = 960/len(self.hands[0])
        for item in self.hands[0]:
            print(item)
            index_number = None
            self.image = PhotoImage(file = self.cards[self.deck.index(item)])
            self.canvas.create_image(x,500, image = self.image)
            button = Button(self.canvas, image = self.image)
            button.place(x, 500)
            button.bind('<Button-1>', self.card_clicked(item))
            self.current_displayed_hand.append(self.image)
            #self.imageLabel2 = Label(parent, image = self.image, height = 150, width = 200, padx = 20,)
            #self.imageLabel2.grid(row = 1, column = i)
            i += i
            x += add_amount
    

if __name__ == "__main__":
    root = Tk()
    asd = gui(root)
    root.geometry("960x540")
    #root.resizable(False, False)
    root.mainloop()