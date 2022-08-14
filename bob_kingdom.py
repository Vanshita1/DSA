def norm(waterList, checked, p):
    if p in checked:
        return waterList[p]

    checked.add(p)
    for conn_p in waterList[p]:
        waterList[p] = waterList[p].union(norm(waterList, checked, conn_p))

    checked.union(waterList)
    return waterList[p]

def waterPaths(waterList):
    crossed = set()
    for p in waterList:
        checked = set(crossed)
        norm(waterList, checked, p)
        crossed.add(p)

    for p in waterList:
        waterList[p].discard(p)
    return waterList

def getComp(landList, checked, p):
    global component
    if p in checked:
        return
    
    checked.add(p)
    component.add(p)
    for conn_p in landList[p]:
        getComp(landList, checked, conn_p)
    
def valComp(waterList):
    global component
    conn_by_water = set()
    for p in component:
        conn_by_water = conn_by_water.union(waterList[p])

    return len(component.intersection(conn_by_water)) == 0

def getList(N, edges):
    adjList = {}
    for p in range(1, N+1):
        adjList[p] = set() 
    
    for edge in edges:
        adjList[edge[0]].add(edge[1])
        adjList[edge[1]].add(edge[0])

    return adjList

component = set()
def solve(A, B, N, land, water):
    global component
    landList = getList(N, land)
    waterList = getList(N, water)
    waterList = waterPaths(waterList)
    checked = set()
    maxP = 0
    for p in range(1, N+1):
        component = set()
        if not p in checked:
            getComp(landList, checked, p)
            if len(component) > maxP and valComp(waterList):
                maxP = len(component)

    return maxP