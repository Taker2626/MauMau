'''Moves card from From at position Pos to the pos2 position in To To'''
def Move_card(Master,From,pos,To,pos2):
    Master[To].insert(pos2,Master[From][pos])
    Master[From].pop(pos)
