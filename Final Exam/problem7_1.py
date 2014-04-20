def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    if atMe.myName() < newFrob.myName():
        if atMe.getAfter()==None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            changeFrob = atMe.getAfter()
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(changeFrob)
            changeFrob.setBefore(newFrob)
    else:
        if atMe.getBefore()==None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            changeFrob = atMe.getBefore()
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore(changeFrob)
            changeFrob.setAfter(newFrob)

