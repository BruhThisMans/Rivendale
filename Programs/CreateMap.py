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
A.add_edge(B.value)
A.add_edge(D.value)
A.add_edge(E.value)
A.add_building("Arthur's House","Top")
A.add_building("Trade Post","Bottom")

#B Vertex
B.add_edge(A.value)
B.add_edge(D.value)
B.add_edge(C.value)
B.add_edge(E.value)
B.add_building("Arthur's House","Left")
B.add_building("Dutch's House","Right")

#C Vertex
C.add_edge(B.value)
C.add_building("Jared's House","Left")
C.add_building("Tom's House","Right")

#D Vertex
D.add_edge(A.value)
D.add_edge(D.value)
D.add_edge(F.value)
D.add_edge(E.value)
D.add_building("General Store","Bottom")
D.add_building("Dutch's House","Top")

#E Vertex
E.add_edge(A.value)
E.add_edge(D.value)
E.add_edge(B.value)
E.add_edge(N.value)
E.add_building("Trade Post","Left")
E.add_building("General Store","Right")

#F Vertex 
F.add_edge(D.value)
F.add_edge(G.value)
F.add_building("Sheriffs Office","Top")

#G Vertex
G.add_edge(F.value)
G.add_edge(H.value)
G.add_building("Courtyard","Top")
G.add_building("Town Bank","Bottom")

#H Vertex
H.add_edge(G.value)
H.add_edge(I.value)
H.add_edge(K.value)
H.add_building("Town Hall","Bottom")


#I Vertex
I.add_edge(H.value)
I.add_edge(J.value)
I.add_building("Courtyard","Left")
I.add_building("Saloon","Right")

#J Vertex
J.add_edge(I.value)
J.add_building("Horse Stable","Left")
J.add_building("Post Office","Top")
J.add_building("Graveyard","Right")


#K Vertex
K.add_edge(H.value)
K.add_edge(L.value)
K.add_building("Saloon","Top")
K.add_building("Micah's House","Bottom")

#L Vertex
L.add_edge(K.value)
L.add_edge(M.value)
L.add_building("Hotel","Top")
L.add_building("Emerald Ranch","Right")

#M Vertex
M.add_edge(L.value)
M.add_edge(N.value)
M.add_building("Army Recruitment","Top")

#N Vertex
N.add_edge(M.value)
N.add_edge(E.value)
N.add_building("Leviticus Cornwall Estate","Bottom")
