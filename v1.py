from tkinter import *
from random import shuffle
import json
class game():
    def __init__(self):
        print("Game Class")
        self.deck = []
        self.card_reference = {}
        self.evens = False
        self.runs = True
        self.current_card = None
        self.hands = [[],[],[],[]]
    def play_card(self, card):
        pass
    def read_files(self):
        try:
            file = open("deck.json", encoding="utf-8")
            self.read_file = json.loads(file.read())
            self.cards = self.read_file['cards']
            self.deck = self.read_file['deck']
            self.values = self.read_file['values']
        except FileNotFoundError:
            print("Missing File 'deck.json'")


class gui:
    def  __init__(self, parent):
        game()

if __name__ == '__main__':
    root = Tk()
    asd = gui(root)
    root.mainloop()
    
