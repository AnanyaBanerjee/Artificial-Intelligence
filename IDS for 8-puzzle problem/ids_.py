#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:56:59 2020

@author: ananyabanerjee

IDS to solve 8-puzzle problem
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


#function to perform DFS
def perform_DFS(inp,goal_arr):
    print("Performing DFS")
    dfs=[]
    #create a dictionary where key is key of LOP
    #and val is visited or not visited
    #initialize your all nodes as not visited or False
    DFS_vis=dict()
    for x in list(Lop.keys()):
        DFS_vis[x]=False
    
    level=0
    
    #
    node_name=str(level)+'s'+str(inp)
    dfs.append(node_name)
    child=dfs[len(dfs)-1]
    DFS_vis[child]=True
    l=inp
    #list of key val
    
    while(l!=goal_arr):
        #print("Updating stack", dfs)
        #print("level=", level)
        
        #print("child", child, "goal", goal_arr)
        
       
        children=Lop[child]
        
        if level<8:
            
            l, level=resolve(child)
            #update level
            level+=1
            #append only the non visited child
            for x in children:
                n_x_name=str(level)+'s'+str(x)
                #t = Lop[n_x_name]
                if DFS_vis[n_x_name]==False:
                    DFS_vis[n_x_name]=True
                    dfs.append(n_x_name)
                    flag=False
                    #print("your updates DFS_Vis is", DFS_vis[n_x_name], "for node", n_x_name) 
                    break
        
            
       # print("level:: ", level)
        
         
        
        #print("flag: ", flag)
        
        if flag==True:# or level == 8:    
            #print("popping child=", dfs[len(dfs)-1], "lEN is", len(dfs)-1, "dfs is", dfs)
            #pop that element
            dfs.pop()
            #reduce level
            
            
        
        child=dfs[len(dfs)-1]
        l, level=resolve(child)
        #print("Updating stack", dfs)
        flag=True
        
        if l==goal_arr:
            print("Hurray")
    
    #true only dfs
    list_dfs_val=list(DFS_vis.values())
    res = [i for i, val in enumerate(list_dfs_val) if val] 
    #print ("res is", res)
    dfs_our=[]
    list_dfs_keys=list(DFS_vis.keys())
    for x in res:
        dfs_our.append(list_dfs_keys[x])
    
    return dfs_our, level


#function to perfrom Iterative Deepening Seach
def perform_IDS(inp, LEV, goal_arr):
    ids=[]
    #generate level only when needed
    print("Performing IDS")
    #create a dictionary where key is key of LOP
    #and val is visited or not visited
    #initialize your all nodes as not visited or False
    IDS_vis=dict()
    for x in list(Lop.keys()):
        IDS_vis[x]=False
    
    level=0
    
    #
    node_name=str(level)+'s'+str(inp)
    ids.append(node_name)
    child=ids[len(ids)-1]
    IDS_vis[child]=True
    l=inp
    #list of key val
    
    while(l!=goal_arr):
       # print("Updating stack", ids)
        #print("level=", level)
        
       # print("child", child, "goal", goal_arr)
        
       
        children=Lop[child]
        
        if level<LEV:
            
            l, level=resolve(child)
            #update level
            level+=1
            #append only the non visited child
            for x in children:
                n_x_name=str(level)+'s'+str(x)
                #t = Lop[n_x_name]
                if IDS_vis[n_x_name]==False:
                    IDS_vis[n_x_name]=True
                    ids.append(n_x_name)
                    flag=False
                    break
        
            
        #print("level:: ", level)
        
         
        
        #print("flag: ", flag)
        
        if flag==True:# or level == 8:    
            #print("popping child=", dfs[len(dfs)-1], "lEN is", len(dfs)-1, "dfs is", dfs)
            #pop that element
            ids.pop()
            #reduce level
            
        if len(ids)==0:
            #true only dfs
            list_ids_val=list(IDS_vis.values())
            res = [i for i, val in enumerate(list_ids_val) if val] 
            #print ("res is", res)
            ids_our=[]
            list_ids_keys=list(IDS_vis.keys())
            for x in res:
                ids_our.append(list_ids_keys[x])
            
            return ids_our, ids, level, False
        
        child=ids[len(ids)-1]
        l, level=resolve(child)
        #print("Updating stack", ids)
        flag=True
        
        if l==goal_arr:
            print("Hurray")
            list_ids_val=list(IDS_vis.values())
            res = [i for i, val in enumerate(list_ids_val) if val] 
            #print ("res is", res)
            ids_our=[]
            list_ids_keys=list(IDS_vis.keys())
            for x in res:
                ids_our.append(list_ids_keys[x])
            
            return ids_our, ids, level, True
            
        
    list_ids_val=list(IDS_vis.values())
    res = [i for i, val in enumerate(list_ids_val) if val] 
    #print ("res is", res)
    ids_our=[]
    list_ids_keys=list(IDS_vis.keys())
    for x in res:
        ids_our.append(list_ids_keys[x])
    
    return ids_our, ids, level, False
    
 #function to perform IDS
def undergo_ids(inp, goal_arr):
    lev=1
    while lev!=10:
          IDS_vis,ids, moves_, decision=perform_IDS(inp, lev, goal_arr)
          lev+=1
          if decision==True:
              break
    return IDS_vis, ids, moves_, decision
       

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
    #type_of_algo='ids'
    print ("Type of Algorithm chosen are", type_of_algo)
    
    
    #creating search tree
    create_dictree(inp_arr)   

    
    if type_of_algo=='ids':
        IDS_vis, ids, moves_, decision=undergo_ids(inp_arr, goal_arr)
        generate_final_board(ids, goal_arr,inp_arr)
        print("Total Number of moves", moves_)
        print ("Total Enqueued", len(IDS_vis))
    
      
    
    else:
        print("Invalid Algorithm. Please try again!")
    

   
    
if __name__=="__main__":
    main()


