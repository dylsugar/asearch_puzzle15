import math
import os
import sys
import time
from queue import PriorityQueue

class Board:
    def __init__(self,tiles):
        self.size = int(math.sqrt(len(tiles)))
        self.tiles = tiles

    def execute_action(self,action):
        new_tiles = self.tiles[:]
        empty_index = new_tiles.index('0')
        if action=='L':
            if empty_index%self.size>0:
                new_tiles[empty_index-1],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index-1]
        if action=='R':
            if empty_index%self.size < (self.size-1):
                new_tiles[empty_index+1],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index+1]  
        if action=='U':
            if empty_index - self.size >= 0:
                new_tiles[empty_index-self.size],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index-self.size]  
        if action=='D':
            if empty_index + self.size < self.size*self.size:
                new_tiles[empty_index+self.size],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index+self.size] 
        return Board(new_tiles)

    
class Node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self):
        return str(self.state.tiles)

    def __eq__(self,other):
        return self.state.tiles == other.state.tiles

    def __hash__(self):
        return hash(self.state)
    

def get_children(parent_node):
    children = []
    actions = ['L','R','U','D']
    for action in actions:
        child_state = parent_node.state.execute_action(action)
        child_node = Node(child_state,parent_node,action)
        children.append(child_node)
    return children


def gcalc(node):
    '''G-value Calculation: finds the cost of current state from original state'''
    count=0
    while node.parent is not None:
        node = node.parent
        count+=1
    return count


def hamming(tiles):
    '''Hamming Heuristic: Counts number of misplaced tiles per different state'''
    distance = 0
    goaltiles = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']
    for i in goaltiles:
        if goaltiles.index(i) - tiles.index(i) != 0 and i != 0:
            distance += 1
    return distance



def manhattan_calculate(tiles):
    '''Manhattan Heuristic: counts number of squares from desired location/per tile'''
    count = 0 
    for i in range(0,15):
        index = tiles.index(str(i+1)) #because range starts at 0
        count+=(abs((i/4)-(index/4))+ abs((i%4)-(index%4))) # %4 is the column and /4 is the row
    return count


def find_path(node):
    '''Returns path back to input node or source node'''
    path = []
    while(node.parent is not None):
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path


def goal_test():
        return ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']


def astar(src,target,heuristic):
    '''A* Search Algorithm'''
    start_time = time.time()
    openlist = list()
    count = 0
    closedlist = dict()
    openlist.append(src)
    closedlist[src.state] = src
    while openlist:
        minim = []
        holder = []
        for x in openlist: 
            if heuristic == 0:
                minim.append(hamming(x.state.tiles) + gcalc(x)) #This is the F = h + g
            elif heuristic == 1:
                minim.append(manhattan_calculate(x.state.tiles) + gcalc(x))
            holder.append(x)
        m = min(minim) #finds minimum F value
        src = holder[minim.index(m)]

        if src.state.tiles == target:#solution found!
            end_time = time.time()
            print("\n\nFound Solution!")
            print("Moves: " + str(' '.join(find_path(src))))
            print("Number of Nodes expanded: " + str(count))
            print("Time Taken: " + str(round((end_time-start_time),3)))
            print("Memory Used: " + str(sys.getsizeof(closedlist)+sys.getsizeof(openlist)) + " kb")
            break
        
        openlist.pop(openlist.index(src))
        for child in get_children(src):
            count+=1
            s = child.state
            if s not in closedlist or gcalc(child) < gcalc(closedlist[s]):
                closedlist[s] = child
                openlist.append(child)




def main(argv):
    heuristic = input("Enter Heuristic either 'H' or 'M' (H is Hamming and M is Manhattan): ")
    if heuristic == 'H':
        heuristic = 0
    elif heuristic == 'M':
        heuristic = 1

    max_depth = 10
    root = Node(Board(argv),None,None)
    astar(root,goal_test(),heuristic)
    openlist = []
    openlist.append(root)
    
if __name__=="__main__":
    main(sys.argv[1:])
