from Vertex import Vertex
from Graph import Graph

#Init vertex
A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
F = Vertex("F")
G = Vertex("G")
H = Vertex("H")
I = Vertex("I")
J = Vertex("J")
K = Vertex("K")
L = Vertex("L")
M = Vertex("M")
N = Vertex("N")

#A Vertex
A.add_edge("B")
A.add_edge("D")
A.add_edge("E")
A.add_building("Arthur's House","Top")
A.add_building("Trade Post","Bottom")

#B Vertex
B.add_edge(A)
B.add_edge(D)
B.add_edge(C)
B.add_edge(E)
B.add_building("Arthur's House","Left")
B.add_building("Dutch's House","Right")

#C Vertex
C.add_edge(B)
C.add_building("Jared's House","Left")
C.add_building("Tom's House","Right")

#D Vertex
D.add_edge(A)
D.add_edge(D)
D.add_edge(F)
D.add_edge(E)
D.add_building("General Store","Bottom")
D.add_building("Dutch's House","Top")

#E Vertex
E.add_edge(A)
E.add_edge(D)
E.add_edge(B)
E.add_edge(N)
E.add_building("Trade Post","Left")
E.add_building("General Store","Right")

#F Vertex 
F.add_edge(D)
F.add_edge(G)
F.add_building("Sheriffs Office","Top")

#G Vertex
G.add_edge(F)
G.add_edge(H)
G.add_building("Courtyard","Top")
G.add_building("Town Bank","Bottom")

#H Vertex
H.add_edge(G)
H.add_edge(I)
H.add_edge(K)
H.add_building("Town Hall","Bottom")


#I Vertex
I.add_edge(H)
I.add_edge(J)
I.add_building("Courtyard","Left")
I.add_building("Saloon","Right")

#J Vertex
J.add_edge(I)
J.add_building("Horse Stable","Left")
J.add_building("Post Office","Top")
J.add_building("Graveyard","Right")


#K Vertex
K.add_edge(H)
K.add_edge(L)
K.add_building("Saloon","Top")
K.add_building("Micah's House","Bottom")

#L Vertex
L.add_edge(K)
L.add_edge(M)
L.add_building("Hotel","Top")
L.add_building("Emerald Ranch","Right")

#M Vertex
M.add_edge(L)
M.add_edge(N)
M.add_building("Army Recruitment","Top")

#N Vertex
N.add_edge(M)
N.add_edge(E)
N.add_building("Leviticus Cornwall Estate","Bottom")
