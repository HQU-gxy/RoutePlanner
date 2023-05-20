from models import Node, Connection
from math import sqrt
# Add the Nodes and Connections
nodesPlaces = [Node('许东亮纪念楼', (378, 528),True), Node('土木楼', (373, 404),True),
               Node('美术学院', (480, 203),True), Node('永亮楼', (510, 253),True),
               Node('菲华楼', (656, 173),True), Node('生物医学学院', (876, 350),True),
               Node('陈嘉庚纪念堂', (524, 537),True), Node('文学院', (647, 812),True),
               Node('旅游学院', (818, 570),True), Node('数学科学学院', (167, 561),True),
               Node('工学院', (345, 783),True), Node('侨总图书馆', (835, 93),True)]

nodePaths = [Node('a2', (895, 97)), Node('a3', (614, 172)),
             Node('a4', (502, 191)), Node('a5', (498, 242)),
             Node('a6', (606, 228)), Node('a7', (717, 228)),
             Node('a8', (752, 226)), Node('a9', (894, 222)),
             Node('a10', (937, 221)), Node('a11', (742, 353)),
             Node('a12', (430, 431)), Node('a13', (711, 404)),
             Node('a14', (856, 406)), Node('a15', (912, 406)),
             Node('a16', (592, 447)), Node('a17', (700, 448)),
             Node('a18', (209, 550)), Node('a19', (426, 527)),
             Node('a20', (425, 555)), Node('a21', (523, 555)),
             Node('a22', (586, 558)), Node('a23', (231, 644)),
             Node('a24', (424, 617)), Node('a25', (469, 623)),
             Node('a26', (546, 625)), Node('a27', (584, 622)),
             Node('a28', (809, 634)), Node('a29', (906, 634)),
             Node('a30', (462, 770)), Node('a31', (536, 769)),
             Node('a32', (541, 804)), Node('a33', (462, 277))]

'''
a18 a23
a23 a24
a24 a20
10b a18
a20 a19
11c a30
a30 a25
a25 a24
a25 a26
a26 a27
a20 a21
a21 7a
1a a19
a12 2b
a12 a19
a33 a12
a33 a5
a5 4b
3a a4
a4 a5
a5 a6
a6 a3
a3 5a
a22 a21
a22 a27
a26 a31
a31 a30
a31 a32
a32 8b
a22 a16
a16 a6
a6 a7
a7 a8
a8 a11
a11 a13
a13 a17
a16 a17
a13 a14
a14 a15
a27 a28
a28 9a
a28 a29
a29 a15
a15 a10
12d a2
a2 a9
a9 a10
a9 a8
6b a14
'''
connectionsPos = [
    (nodePaths[16], nodePaths[21]), (nodePaths[21], nodePaths[22]),
    (nodePaths[22], nodePaths[18]), (nodesPlaces[9], nodePaths[16]),
    (nodePaths[18], nodePaths[17]), (nodesPlaces[10], nodePaths[28]),
    (nodePaths[28], nodePaths[23]), (nodePaths[23], nodePaths[22]),
    (nodePaths[23], nodePaths[24]), (nodePaths[24], nodePaths[25]),
    (nodePaths[18], nodePaths[19]), (nodePaths[19], nodesPlaces[6]),
    (nodesPlaces[0], nodePaths[17]), (nodePaths[10], nodesPlaces[1]),
    (nodePaths[10], nodePaths[17]), (nodePaths[31], nodePaths[10]),
    (nodePaths[31], nodePaths[3]), (nodePaths[3], nodesPlaces[3]),
    (nodesPlaces[2], nodePaths[2]), (nodePaths[2], nodePaths[3]),
    (nodePaths[3], nodePaths[4]), (nodePaths[4], nodePaths[1]),
    (nodePaths[1], nodesPlaces[4]), (nodePaths[20], nodePaths[19]),
    (nodePaths[20], nodePaths[25]), (nodePaths[24], nodePaths[29]),
    (nodePaths[29], nodePaths[28]), (nodePaths[29], nodePaths[30]),
    (nodePaths[30], nodesPlaces[7]), (nodePaths[20], nodePaths[14]),
    (nodePaths[14], nodePaths[4]), (nodePaths[4], nodePaths[5]),
    (nodePaths[5], nodePaths[6]), (nodePaths[6], nodePaths[9]),
    (nodePaths[9], nodePaths[11]), (nodePaths[11], nodePaths[15]),
    (nodePaths[14], nodePaths[15]), (nodePaths[11], nodePaths[12]),
    (nodePaths[12], nodePaths[13]), (nodePaths[25], nodePaths[26]),
    (nodePaths[25], nodePaths[26]), (nodePaths[26], nodesPlaces[8]),
    (nodePaths[26], nodePaths[27]), (nodePaths[27], nodePaths[13]),
    (nodePaths[13], nodePaths[8]), (nodesPlaces[11], nodePaths[0]),
    (nodePaths[0], nodePaths[7]), (nodePaths[7], nodePaths[8]),
    (nodePaths[7], nodePaths[6]), (nodesPlaces[5], nodePaths[13])]


# 2.2px/m
connections = []

for cp in connectionsPos:
    weight = int(sqrt(((cp[0].pos[0] - cp[1].pos[0]) **
                      2 + (cp[0].pos[1] - cp[1].pos[1])**2))/2.2)
    connections.append(Connection(cp, weight, (0, 100, 100)))
