from cisc106 import assertEqual
animalWeights = {}
Animals = ['Lion', 'Cat', 'Dog', 'Cow', 'Snake', 'Person', 'Pig', 'Bird', 'Wombat', 'Hamster']
Weights = [420, 9, 70, 2400, 250, 137, 770, 10, 88, 0.5]
def make_pairs(alist, blist):
    """
    Pairs alist and blist into a dictionary, alist and blist must have an equal amount of elements.
    """
    if not alist:
        return animalWeights
    else:
        animalWeights[alist[0]] = blist[0] 
        return make_pairs(alist[1:], blist[1:])
        
assertEqual(make_pairs([2], [3]), {2:3})