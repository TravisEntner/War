import random
emergencyWar = []
print("This is 2 player war card game! (14's are in place of Aces)")
cards = [
    2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8,
    8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13,
    13, 13, 13, 14, 14, 14, 14
]

deck = []
number=51
for i in range(26):
  index = random.randint(0, (number))
  firstCard = cards[index]
  deck.append(firstCard)
  number = number - 1
  cards.pop(index)
print("player1 your deck is " + str(cards))
print("Player 2 your deck is " + str(deck))
while True:
  if(cards == []) or (deck == []):
    break
  player1 = cards[0]
  player2 = deck[0]


  if str(player1) > str(player2):
    print("Player 1 wins!")
    print(str(player1) + ">" + str(player2))
    deck.remove(player2)
    cards.remove(player1)
    cards.append(player2)
    cards.append(player1)
  elif str(player2) > str(player1):
    print("Player 2 wins!")
    print(str(player2) + ">" + str(player1))
    cards.remove(player1)
    deck.remove(player2)
    deck.append(player1)
    deck.append(player2)
  tie = 10
  if str(player1) == str(player2):
    while tie>5:
      print("both cards were "+ str(player2) + " so its time for a war!")
      p1cards =[]
      p2cards=[]
      #add the cards player 1 will put up for war
      p1cards.append(cards[1])
      p1cards.append(cards[2]) 
      p1cards.append(player1)
      p1Save = player1
      cards.remove(cards[0])
      player1 = cards[2]
      p1cards.append(player1)
      #add the cards player 2 will put up for war 
      p2cards.append(player2)
      p2cards.append(deck[1])
      p2cards.append(deck[2])
      deck.remove(deck[0])
      p2Save = player2
      player2 = deck[2]
      p2cards.append(player2)

      print("Player 1's card is ", player1, " Player 2's card is ", player2)
      if player2 > player1:
        print("Player 2 won the war, and recived " + str(p1cards) + "!!")      
        deck.append(p2Save)
        del cards[0:3]
        for n in range(4):
          deck.append(p1cards[0])
          p1cards.remove(p1cards[0])
          deck.append(emergencyWar[0])


        
      if player1 > player2:
        print("Player 1 won the war, and recived " + str(p2cards) + "!!")      
        cards.append(p1Save)
        del deck[0:3]
        for n in range(4):
          cards.append(p2cards[0])
          p2cards.remove(p2cards[0])
          cards.append(emergencyWar[0])
      if player1 == player2:
        for n in range(4):
          emergencyWar.append(p1cards)
          emergencyWar.append(p2cards)
        
      if player1 != player2:
        tie=0
  emergencyWar=[]
      

  totalCards= len(cards) + len(deck)
      
  print("player one your have " + str(len(cards))+ " cards left")
  print("player two your have " + str(len(deck)) +" cards left")
  wait = input("press enter when ready")
