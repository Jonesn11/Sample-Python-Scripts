#! python3
#import modules
import pprint

#Initialize a dictionary
ratings_dict = {} 

#Declare a function with parameters string, and votes
#Make votes int arguments and Calculate a score using the string and votes, with a digit specifier 
#Take the string and put it in the dictionary as a key and the score as the value

def item_score(name, pos, neg):
    '''function that takes in a string and takes in positive and negative votes, and gives you a rating of that
#one in a dictionary'''
    p = int(pos)
    n = int(neg)
    score = (p-n)/(p+n)
    score = ("%.2f" % float(score))
    ratings_dict[name] = score
    pass

def run_rater():
    '''function that keeps getting input from the user, and passes the input as arguments into earlier
#function until the user says stop'''
    x = 0
    while x != 'n':
        while True:
            name = input('Enter the item name:\n>> ')
            if name.isdigit():
                print("You did not enter a valid item name")
                continue
            else:
                break
        pos = input('Enter the positive votes:\n>> ')
        neg = input('Enter the negative votes:\n>> ')
        score = item_score(name,pos,neg)
        while True:
            x = input('If you are done rating items, enter "n". To continue, enter "y":\n>> ').lower()
            if x not in ['y','n']:
                print('You did not enter one of the two options: "y" or "n"')
                continue
            else:
                break
        
    pprint.pprint(ratings_dict)     

#Execute
run_rater()    


 



