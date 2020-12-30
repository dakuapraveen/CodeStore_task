import streamlit as st
import random
page_bg_img = '''
<style>
body {
background-image: url("https://cdn.hipwallpaper.com/i/91/18/5r6VAc.jpg")
'''
st.markdown(page_bg_img, unsafe_allow_html=True)



st.markdown("<h1 style='text-align: left; color: blue;'>CODESTORE ASSIGNMENT</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; color: green;'>DECK OF CARDS</h1>", unsafe_allow_html=True)
import random


class Card(object):
   def init(self, suit, val):
      self.suit = suit
      self.value = val

   def unicode(self):
      return self.show()

   def str(self):
      return self.show()

   def repr(self):
      return self.show()

   def show(self):
      if self.value == 1:
         val = "Ace"
      elif self.value == 11:
         val = "Jack"
      elif self.value == 12:
         val = "Queen"
      elif self.value == 13:
         val = "King"
      else:
         val = self.value

      return "{} of {}".format(val, self.suit)


class Deck(object):
   def init(self):
      self.cards = []
      self.build()

   def show(self):
      for card in self.cards:
         st.title(card.show())

   def build(self):
      self.cards = []
      for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
         for val in range(1, 14):
            self.cards.append(Card(suit, val))

   def shuffle(self, num=1):
      length = len(self.cards)
      for _ in range(num):

         for i in range(length - 1, 0, -1):

            randi = random.randint(0, i)
            if i == randi:
               continue
            self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]

   def deal(self):
      return self.cards.pop()


class Player(object):
   def init(self, name):
      self.name = name
      self.hand = []

   def sayHello(self):
      #st.title("Hi! My name is {}".format(self.name))
      st.markdown("<h1 style='text-align: left; color: red;'>Hello! My name is Praveen</h1>", unsafe_allow_html=True)
      return self

   def draw(self, deck, num=1):
      for _ in range(num):
         card = deck.deal()
         if card:
            self.hand.append(card)
         else:
            return False
      return True

   def showHand(self):
      if st.button("Choose Random Card"):
         st.title("{}'s hand: "
                  "{}".format(self.name, self.hand))
      return self

   def discard(self):
      return self.hand.pop()


myDeck = Deck()
myDeck.shuffle()

bob = Player("Praveen")
bob.sayHello()
bob.draw(myDeck, 1)
bob.showHand()
