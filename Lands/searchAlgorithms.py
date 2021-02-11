from . models import stands

def searchStand(searchValue):
    #all unpurchased objects
    standsAll = stands.objects.filter(purchased=False)
    #filtered dictinary
    standsSearched = []
    #linear search
    for stand in standsAll:
        if searchValue in stand.address:
            standsSearched.append(stand)
    
    #return search result in form of dictionary
    return {"stands" : standsSearched}