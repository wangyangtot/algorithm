import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

def main():
    edge = {}
    reversedEdge = {}
    vertex = []
    reversedVertex = []

    with open('scc.txt', 'r') as f:
        for line in f:
            tem = line.strip()
            a, b = tem.split(' ')
            if a not in vertex:
                vertex.append(a)
                tem = []
                tem.append(b)
                edge[a] = tem
            else:
                edge[a].append(b)

            if b not in reversedVertex:
                reversedVertex.append(b)
                rtem = []
                rtem.append(a)
                reversedEdge[b] = rtem
            else:
                reversedEdge[b].append(a)

    for i in reversedVertex:
        if i not in vertex:
            vertex.append(i)

    print edge
    print reversedEdge

    # print reversedVertex
    # print vertex


    def initFlag():
        flag = {}
        for i in vertex:
            flag[i] = False  # faise present having not been traveled
        return flag

    def DFS(edge, flag, vertexi, stack):
        flag[vertexi] = True
        if vertexi in edge.keys():
            m = len(edge[vertexi])
            i = 0
            # print vertexi
            while i < m and (flag[edge[vertexi][i]] == True):
                # print edge[vertexi][i]
                i = i + 1
                # print i,'not finish'
            if i != m:
                # print i
                # print edge[vertexi][i]
                stack.append(vertexi)
                # print stack
                DFS(edge, flag, edge[vertexi][i], stack)
                # print stack
            else:
                stack.append(vertexi)
                # print "finish "
        else:
            stack.append(vertexi)

    '''
    flag = initFlag()
    print flag
    stack = []
    DFS(edge,flag,'1',stack)
    print stack
  
    '''

    def FinishTimeOrdering(vertex, edge):
        flag = initFlag()
        stack = []
        i = 0
        finishTime = []
        while len(vertex) != len(finishTime):
            if vertex[i] not in finishTime:
                stack.append(vertex[i])
                while len(stack) != 0:
                    tem = stack.pop()
                    # print tem
                    # print flag[tem]
                    DFS(edge, flag, tem, stack)
                    # print stack
                    stem = stack.pop()
                    finishTime.append(stem)
            else:
                i = i + 1
        return finishTime

    finish = FinishTimeOrdering(vertex, edge)
    print finish
    finishTime = finish[::-1]
    print finishTime

    def findcomponent(reversedEdge, flag, leader, stack, component):
        DFS(reversedEdge, flag, leader, stack)
        print stack
        tem = stack.pop()
        component.append(tem)

        # print tem
        if len(stack) != 0:
            tem = stack.pop()
            findcomponent(reversedEdge, flag, tem, stack, component)
        return len(component)

    def cout(reversedEdge, finishTime):
        flag = initFlag()
        m = len(finishTime)
        nums = []
        total = 0
        while m != total:
            stack = []
            component = []
            i = 0
            while flag[finishTime[i]] == True:
                i = i + 1
            num = findcomponent(reversedEdge, flag, finishTime[i], stack, component)
            print num
            nums.append(num)
            total += num
        return nums

    couts = cout(reversedEdge, finishTime)
    sortcout = sorted(couts)
    print sortcout[:5]
thread = threading.Thread(target=main)
thread.start()




