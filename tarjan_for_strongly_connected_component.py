def add_link(from_id,to_id):
    global link_seq,Ver,Next,Head
    link_seq+=1
    Ver[link_seq]=to_id
    Next[link_seq]=Head.get(from_id, 0)
    Head[from_id]=link_seq

def tarjan(from_node_id):
    global connected_set,stack,dfn,low,seq_num,cnt
    seq_num+=1

    dfn[from_node_id]=seq_num
    low[from_node_id]=seq_num
    stack.append(from_node_id)

    #all links start from this node id 
    i=Head.get(from_node_id, 0)
    while (i):
        to_node_id=Ver[i]
        if to_node_id not in dfn:
            tarjan(to_node_id)
            low[from_node_id]=min([low[from_node_id],low[to_node_id]])
        elif to_node_id in stack:
            low[from_node_id]=min([low[from_node_id],dfn[to_node_id]])
        i=Next[i]

    if(dfn[from_node_id]==low[from_node_id]):
        cnt+=1
        while(stack[-1]!=from_node_id):
            connected_set[cnt].append(stack.pop())
        connected_set[cnt].append(stack.pop())

if __name__=="__main__":
    _MAX_NUM_LINKS=100
    #list
    Ver=[0]*_MAX_NUM_LINKS
    Next=[0]*_MAX_NUM_LINKS
    stack=list()
    connected_set=[[] for i in range(_MAX_NUM_LINKS*2)]
    
    #dict
    Head=dict()
    dfn=dict()
    low=dict()

    link_seq=1
    seq_num=0
    cnt=0

    fp = open('data_input.txt')
    node_set=set()
    for line in fp:
        from_node,to_node=line.strip().split(",")
        node_set.add(from_node)
        node_set.add(to_node)
        add_link(from_node,to_node)
    fp.close()

    for node in node_set:
        if node not in dfn:
            tarjan(node)

    for i in range(1,cnt+1):
        print("The {}th connected set is{} ".format(i,str(connected_set[i])[1:-1].replace(","," ")))
        
    
            
            
            
            
    
