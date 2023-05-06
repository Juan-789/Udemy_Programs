import Art as a
import Data as d
import random as r
#get the first comparison
#get the second one
#+1 if right
#keep score at welcome
points = 0
winning_streak = True
def random_selectorA():     #choose random person A
    person1= d.data[r.randint(0,49)]
    print (f"Compare A: {person1.get('name')}, a {person1.get('description')}, from {person1.get('country')}")
    return person1.get('follower_count')        #return the followers count
    
def random_selectorB():         #choose random person B
    global personBIndex
    personBIndex = d.data[r.randint(0,49)]
    print (f"Against B: {personBIndex.get('name')}, a {personBIndex.get('description')}, from {personBIndex.get('country')}")
    return personBIndex.get('follower_count')        #return the followers count

def determinator(A,B,C):
    if (A>B and C=="A") or (B>A and C=="B"):       #evaluates the biggest
        global points
        points+=1
        print(a.logo)
        print( f"You're right! Current Score: {points}.")
        if A>B:
            return A
        elif B>A:
            return B
    else:
        global winning_streak
        winning_streak = False      #break while loop
        print( f"Sorry that's wrong. Final Score {points}")

def start():        #starting game
    print (a.logo)  #prints logo
    personA = random_selectorA()      #chooses random person
    print(a.vs)
    global personB
    personB = random_selectorB()
    choice = input("Who has more followers? Type 'A' or 'B': ")
    determinator(personA,personB,choice)


#create new var to store last winner than compare to new person
start()

while winning_streak:       #the game after the first round
    print (f"Compare A: {personBIndex.get('name')}, a {personBIndex.get('description')}, from {personBIndex.get('country')}")
    print(a.vs)
    newPersonB = random_selectorB()
    choice = input("Who has more followers? Type 'A' or 'B': ")
    determinator(personB, newPersonB, choice)        #the last personB becomes compareA, and the new person is always the against B
