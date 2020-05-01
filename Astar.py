from tkinter import *
from math import inf,sqrt
import heapq
from time import sleep
def start_end():
    check=False
    root = Tk()
    l1=Label(root,text="start (x,y)",width=10)
    e1=Entry(root,width=20)
    l2=Label(root,text="end (x,y)")
    e2=Entry(root,width=20)
    e1_txt=None
    e2_txt=None
    def my_click():
        nonlocal e1_txt
        nonlocal e2_txt
        e1_txt=e1.get()
        e2_txt=e2.get()
        root.destroy()
    submit=Button(root,text='Submit',width=20,command=lambda:my_click())
    l1.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    submit.grid(row=2,column=0,columnspan=2)
    root.mainloop()
    return [e1_txt,e2_txt]
strt_end=start_end()
strt=list(map(lambda string:int(string),strt_end[0].split(',')))
end=list(map(lambda string:int(string),strt_end[1].split(',')))
rows=25
columns=50
btns = [[None for i in range(columns)] for j in range(rows)]
root=Tk()
def darken(i,j):
    if(not((i==strt[0] and j==strt[1])or(i==end[0] and j==end[1]))):
        btns[i][j].configure(bg='black')
for i in range(rows):
    for j in range(columns):
        btns[i][j]=Button(root, bg='white',width=1,padx=5,command=lambda c=i,d=j:darken(c,d))
        btns[i][j].grid(row=i,column=j)
        if((i==strt[0] and j==strt[1])or(i==end[0] and j==end[1])):
            btns[i][j].configure(bg='yellow')
def heuristic(i,j):
    return (abs(i-end[0])+abs(j-end[1]))
def darken1(event):
    widget=event.widget.winfo_containing(event.x_root, event.y_root)
    if widget:
        widget.configure(bg='black')
def onKeyPress(event):
    if event.char==' ':
        distances={}
        previous={}
        visited=[]
        heap_dict={}
        pq=[]
        ended=None
        for i in range(rows):
            for j in range(columns):
                previous[f'[{i},{j}]']=None
                if(i==strt[0] and j==strt[1]):
                    distances[f'[{i},{j}]']=0
                    heap_dict[f'[{i},{j}]']=heuristic(i,j)
                    heapq.heappush(pq,heap_dict[f'[{i},{j}]'])
                else:
                    distances[f'[{i},{j}]']=inf
        while(len(pq)>0):
            current=list(heap_dict.keys())[list(heap_dict.values()).index(heapq.heappop(pq))]
            del heap_dict[current]
            i_j=list(map(lambda st:int(st),current.strip('][').split(',')))
            i=i_j[0]
            j=i_j[1]
            btns[i][j]['bg']='tomato'
            if(current==f'[{end[0]},{end[1]}]'):
                ended=current
                break
            if j+1<columns:
                node=f'[{i},{j+1}]'
                if (btns[i][j+1].cget('bg')=='white')or(btns[i][j+1].cget('bg')=='yellow') or (btns[i][j+1].cget('bg')=='green' and distances[current]+1<distances[node]):     
                    if btns[i][j+1].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i,j+1)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i][j+1]['bg']='green'
            if(i+1<rows):
                node=f'[{i+1},{j}]'
                if ((btns[i+1][j].cget('bg')=='white')or(btns[i+1][j].cget('bg')=='yellow') or (btns[i+1][j].cget('bg')=='green' and distances[current]+1<distances[node])):
                    if btns[i+1][j].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i+1,j)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i+1][j]['bg']='green'
            if(j-1>=0):
                node=f'[{i},{j-1}]'
                if ((btns[i][j-1].cget('bg')=='white')or(btns[i][j-1].cget('bg')=='yellow') or (btns[i][j-1].cget('bg')=='green' and distances[current]+1<distances[node])):    
                    if btns[i][j-1].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i,j-1)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i][j-1]['bg']='green'
            if(i-1>=0):
                node=f'[{i-1},{j}]'
                if ((btns[i-1][j].cget('bg')=='white')or(btns[i-1][j].cget('bg')=='yellow') or (btns[i-1][j].cget('bg')=='green' and distances[current]+1<distances[node])):
                    if btns[i-1][j].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i-1,j)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i-1][j]['bg']='green'



            if(i-1>=0 and j+1<columns):
                node=f'[{i-1},{j+1}]'
                if ((btns[i-1][j+1].cget('bg')=='white')or(btns[i-1][j+1].cget('bg')=='yellow') or (btns[i-1][j+1].cget('bg')=='green' and distances[current]+1.4<distances[node])):
                    if btns[i-1][j+1].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1.4
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i-1,j+1)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i-1][j+1]['bg']='green'
            if(i+1<rows and j+1<columns):
                node=f'[{i+1},{j+1}]'
                if ((btns[i+1][j+1].cget('bg')=='white')or(btns[i+1][j+1].cget('bg')=='yellow') or (btns[i+1][j+1].cget('bg')=='green' and distances[current]+1.4<distances[node])):
                    if btns[i+1][j+1].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1.4
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i+1,j+1)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i+1][j+1]['bg']='green'
            if(i+1<rows and j-1>=0):
                node=f'[{i+1},{j-1}]'
                if((btns[i+1][j-1].cget('bg')=='white')or(btns[i+1][j-1].cget('bg')=='yellow') or (btns[i+1][j-1].cget('bg')=='green' and distances[current]+1.4<distances[node])):
                    if btns[i+1][j-1].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1.4
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i+1,j-1)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i+1][j-1]['bg']='green'
            if(i-1>=0 and j-1>=0):
                node=f'[{i-1},{j-1}]'
                if ((btns[i-1][j-1].cget('bg')=='white')or(btns[i-1][j-1].cget('bg')=='yellow') or (btns[i-1][j-1].cget('bg')=='green' and distances[current]+1.4<distances[node])):
                    if btns[i-1][j-1].cget('bg')=='green':
                        pq.remove(heap_dict[node])
                    distances[node]=distances[current]+1.4    
                    previous[node]=current
                    heap_dict[node]=distances[node]+heuristic(i-1,j-1)
                    heapq.heappush(pq,heap_dict[node])
                    btns[i-1][j-1]['bg']='green'
            root.update()
            sleep(0.03)
        while(not ended==None):
            stored=ended
            ended=list(map(lambda st:int(st),ended.strip('][').split(',')))
            btns[ended[0]][ended[1]]['bg']='red3'
            ended=previous[stored]
            root.update()
            sleep(0.1)
        root.unbind('<KeyPress>')
root.bind('<B1-Motion>',darken1)
root.bind('<KeyPress>', onKeyPress)
root.mainloop()

