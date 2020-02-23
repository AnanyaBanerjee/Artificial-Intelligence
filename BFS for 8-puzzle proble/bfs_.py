#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:56:18 2020

@author: ananyabanerjee

BFS to solve 8-puzzle problem
"""

from functools import reduce
import ast 
import sys
from collections import deque

##pp.pprint("hi")
#res = ast.literal_eval(ini_list)
#Goal Config
#goal_arr=[1,2,3,4,5,6,7,8,0]

#Input Config
#inp_arr=[0,1,3,4,2,5,7,8,6]

#Storing Level by Level Board Config
L=[]

#dictionary to signify index as key and type of board position as val
di=dict()
di[0]='corner_left_up'
di[1]='up_middle'
di[2]='corner_right_up'
di[3]='left_middle'
di[4]='middle'
di[5]='right_middle'
di[6]='corner_left_down'
di[7]='down_middle'
di[8]='corner_right__down'

#Dictionary containing the tree
"""
Trying to create a dictionary
whose key=['level_number'+'s'+'node val or parent']
and val=list of children
"""
Lop=dict()


#function to decide which moves to make 
def decide_spaces(inp_arr):
    #we need to move from inp_arr to goal_arr
    can_move=[] #possible list of moves
    
    #Step 1: identify where is blank or 0
    #This gives an idea about which initial config to choose
    ind_of_blank=inp_arr.index(0)
    
    #Check if its middle, then initialize can_move list containing indexes
    if ind_of_blank==4:
        can_move=[1,3,7,5]
        
    #check if its corner
    #corner_left_up ! corner=0  
    if ind_of_blank==0:
        can_move=[1,3]
        
    #corner_left_down ! corner=6
    if ind_of_blank==6:
        can_move=[3,7]
            
    #corner_right_up ! corner=2 
    if ind_of_blank==2:
        can_move=[1,5]
            
    #corner_right__down ! corner=8 
    if ind_of_blank==8:
        can_move=[7,5]
    
    #check if its side middle
    # up_middle ! up_middle=1
    if ind_of_blank==1:
        can_move=[0,2,4]
    
    # left_middle ! left_middle=3
    if ind_of_blank==3:
        can_move=[0,4,6]
        
    # right_middle ! right_middle=5
    if ind_of_blank==5:
        can_move=[2,4,8]
    
    # down_middle ! down_middle=7  
    if ind_of_blank==7:
        can_move=[4,6,8]
                 
    return can_move 

#function to take can_move and move spaces in the board arr
def move_spaces(inp_arr, can_move):
    #find where is 0 or blank
    ind_of_blank=inp_arr.index(0)
    
    #make a list of possible board configurations
    l=[]
    
    for x in can_move:
        #copy list inp_arr
        inp1=inp_arr.copy()
        temp=inp1[ind_of_blank]
        inp1[ind_of_blank]=inp1[x]
        inp1[x]=temp
        l.append(inp1)
        print (inp1)
        
    return l

    
#function to check of the goal is the one of the generated ones
def check_goal(seq, goal_arr):
    if goal_arr==seq:
        return True
    else:
        return False


#function to resolve level and node val from key
#key=[lev+s+nodeval]
def resolve(key):
    #print ("resolving key", key)
    node_val=ast.literal_eval(key[2:])
    level=int(key[0])
    return node_val, level

#function to create a tree
"""
Trying to create a dictionary
whose key=['level_number'+'s'+'node val or parent']
and val=list of children
"""
def create_dictree(inp):
    lev=0
    can_move=decide_spaces(inp)
    board_config=move_spaces(inp, can_move)
    #print("board config", board_config, "lev", lev, "inp", inp)
    Lop[str(lev)+'s'+str(inp)]=board_config
    #print ("BG is", board_config)
    lev+=1
    bg2=[]
    while(lev!=10):
        for x in board_config:
            can_move1=decide_spaces(x)
            board_config1=move_spaces(x, can_move1)
            bg2=bg2+board_config1
            #print ("BG1 is", board_config1)
            Lop[str(lev)+'s'+str(x)]=board_config1
       
        board_config=bg2
        bg2=[]
            
        lev+=1
        
#function to display board config arr
def print_board(arr, goal_arr, inp_arr):
    #print ("before is", arr)
        
    a1=arr[0:3]
    a2=arr[3:6]
    a3=arr[6:9]
   
    if arr==inp_arr:
        print (" ", a1[0], " ", a1[1], " ", a1[2], " ", "Input State")
   
    elif arr==goal_arr:
       print (" ", a1[0], " ", a1[1], " ", a1[2], " ", "(Goal State)")
    
    else:
       print (" ", a1[0], " ", a1[1], " ", a1[2])
        
    print ("\n")
    
    print (" ", a2[0], " ", a2[1], " ", a2[2])
        
        
    print ("\n")
    
    print (" ", a3[0], " ", a3[1], " ", a3[2])
        
        
    print ("\n")
    
    print ("-----------------")

#function to print all board config in given stack or queue
def print_queue(queue, goal_arr, inp_arr):
    
    #print ("queue is", queue, "and", queue[0], "then", queue[0][0])
    if len(queue)==1:
        print_board(queue[0], goal_arr, inp_arr,)
        return
    else:
        for x in queue:
            print_board(x)
     
#function to reach the goal_arr in the found level
def reach_goal(lev, moves, goal_arr):
    ind=lev.index(goal_arr)
    for i in range(ind+1):
        print_board(lev[i])
        moves+=1
    
    return moves

#function to generate final board for ids
def generate_final_board(IDS_vis, goal_arr, inp_arr):
    for x in IDS_vis:
        node, l=resolve(x)
        print_board(node, goal_arr, inp_arr)
    return


#function to conduct bfs using tree
def bfs(inp, goal_arr):
    print("Performing BFS")
    bfs=deque()
    #create a dictionary where key is key of LOP
    #and val is visited or not visited
    #initialize your all nodes as not visited or False
    BFS_vis=dict()
    for x in list(Lop.keys()):
        BFS_vis[x]=False
    
    level=0
    #anc is a list of visited nodes
    choose=[]
    anc=dict()
    #
    node_name=str(level)+'s'+str(inp)
    bfs.append(node_name)
    child=bfs[len(bfs)-1]
    BFS_vis[child]=True
    l=inp
    choose.append(l)
    anc[child]=[]    
    #list of key val
    
    while(level<=9 or l!=goal_arr):
        #print("bfs is", bfs) 
        #if bfs is empty then exit
        if len(bfs)==0:
            break
        
        #child
        child=bfs[0]
        #print("child", child)
        #pop left parent before adding children
        bfs.popleft()
        
        children=Lop[child]
        
        #level+=1
        for x in children:
            
            #level+=1
            l, level=resolve(child)
            level+=1
            n_x_name=str(level)+'s'+str(x)
            anc[n_x_name]=anc[child]+[child]
            #print ("x is", x, "name is", n_x_name)
            #l, level=resolve(n_x_name)
            #print("level", level, "l is", l)
            
            if BFS_vis[n_x_name]==False:
               bfs.append(n_x_name)
               BFS_vis[n_x_name]=True
        
            if x==goal_arr:
               print("Hurray")
               anc[n_x_name]=anc[n_x_name]+[str(level)+'s'+str(goal_arr)]
               #true only dfs
               list_bfs_val=list(BFS_vis.values())
               res = [i for i, val in enumerate(list_bfs_val) if val] 
               #print ("res is", res)
               bfs_our=[]
               list_bfs_keys=list(BFS_vis.keys())
               for x in res:
                   bfs_our.append(list_bfs_keys[x])
                
               return bfs_our, level, anc, n_x_name
           #break
       
        
           
    #true only dfs
    list_bfs_val=list(BFS_vis.values())
    res = [i for i, val in enumerate(list_bfs_val) if val] 
    #print ("res is", res)
    bfs_our=[]
    list_bfs_keys=list(BFS_vis.keys())
    for x in res:
        bfs_our.append(list_bfs_keys[x])
    
    return bfs_our, level, anc, n_x_name
 
            

def main():
    
    #- bfs : For running the Breadth-first search algorithm
    #- ids : For running the Iterative deepening search algorithm
    #- astar1 : For running the A* algorithm with heuristic 1.
    #- astar2 : For running the A* algorithm with heuristic 2.
    
    #taking input board config
    inp_arr=input("Enter the input state config")
    inp_arr=inp_arr.split()
    inp_arr=[int(i) for i in inp_arr]
    #taking goal board config
    goal_arr=input("Enter the goal state")
    goal_arr=goal_arr.split()
    goal_arr=[int(i) for i in goal_arr]
   
    #type_of_algo=input("Enter the algo you want to use")
    type_of_algo=sys.argv[1]
    #type_of_algo='bfs'
    print ("Type of Algorithm chosen are", type_of_algo)
    
    
    #creating search tree
    create_dictree(inp_arr)   

    
    if type_of_algo=='bfs':
        bfs_our, level, choose, x=bfs(inp_arr, goal_arr)
        generate_final_board(choose[x], goal_arr, inp_arr)
        print("Total Number of moves", level)
        print ("Total Enqueued", len(bfs_our))

    
    else:
        print("Invalid Algorithm. Please try again!")
    

   
    
if __name__=="__main__":
    main()


