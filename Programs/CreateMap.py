from Vertex import Vertex
from Graph import Graph
from Algorithm import dijkstra

#Init graph
Map = Graph()

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
Map.add_vertex(A)
Map.add_vertex(B)
Map.add_vertex(C)
Map.add_vertex(D) 
Map.add_vertex(E)
Map.add_vertex(F)
Map.add_vertex(G)
Map.add_vertex(H)
Map.add_vertex(I)
Map.add_vertex(J)
Map.add_vertex(K)
Map.add_vertex(L)
Map.add_vertex(M)
Map.add_vertex(N)

#A Vertex
A.add_edge(B.value)
A.add_edge(D.value)
A.add_edge(E.value)
Map.add_edge(A,B)
Map.add_edge(A,D)
Map.add_edge(A,E)
A.add_building("Arthur's House","Top")
A.add_building("Trade Post","Bottom")

#B Vertex
B.add_edge(A.value)
B.add_edge(D.value)
B.add_edge(C.value)
B.add_edge(E.value)
Map.add_edge(B,A)
Map.add_edge(B,D)
Map.add_edge(B,C)
Map.add_edge(B,E)
B.add_building("Arthur's House","Left")
B.add_building("Dutch's House","Right")

#C Vertex
C.add_edge(B.value)
Map.add_edge(C,B)
C.add_building("Jared's House","Left")
C.add_building("Tom's House","Right")

#D Vertex
D.add_edge(A.value)
D.add_edge(B.value)
D.add_edge(F.value)
D.add_edge(E.value)
Map.add_edge(D,A)
Map.add_edge(D,B)
Map.add_edge(D,F)
Map.add_edge(D,E)
D.add_building("General Store","Bottom")
D.add_building("Dutch's House","Top")

#E Vertex
E.add_edge(A.value)
E.add_edge(D.value)
E.add_edge(B.value)
E.add_edge(N.value)
Map.add_edge(E,A)
Map.add_edge(E,D)
Map.add_edge(E,B)
Map.add_edge(E,N)
E.add_building("Trade Post","Left")
E.add_building("General Store","Right")

#F Vertex 
F.add_edge(D.value)
F.add_edge(G.value)
Map.add_edge(F,D)
Map.add_edge(F,G)
F.add_building("Sheriffs Office","Top")

#G Vertex
G.add_edge(F.value)
G.add_edge(H.value)
Map.add_edge(G,F)
Map.add_edge(G,H)
G.add_building("Courtyard","Top")
G.add_building("Town Bank","Bottom")

#H Vertex
H.add_edge(G.value)
H.add_edge(I.value)
H.add_edge(K.value)
Map.add_edge(H,G)
Map.add_edge(H,I)
Map.add_edge(H,K)
H.add_building("Town Hall","Bottom")


#I Vertex
I.add_edge(H.value)
I.add_edge(J.value)
Map.add_edge(I,J)
Map.add_edge(I,H)
I.add_building("Courtyard","Left")
I.add_building("Saloon","Right")

#J Vertex
J.add_edge(I.value)
Map.add_edge(J,I)
J.add_building("Horse Stable","Left")
J.add_building("Post Office","Top")
J.add_building("Graveyard","Right")


#K Vertex
K.add_edge(H.value)
K.add_edge(L.value)
Map.add_edge(K,H)
Map.add_edge(K,L)
K.add_building("Saloon","Top")
K.add_building("Micah's House","Bottom")

#L Vertex
L.add_edge(K.value)
L.add_edge(M.value)
Map.add_edge(L,M)
Map.add_edge(L,K)
L.add_building("Hotel","Top")
L.add_building("Emerald Ranch","Right")

#M Vertex
M.add_edge(L.value)
M.add_edge(N.value)
Map.add_edge(M,L)
Map.add_edge(M,N)
M.add_building("Army Recruitment","Top")

#N Vertex
N.add_edge(M.value)
N.add_edge(E.value)
Map.add_edge(N,M)
Map.add_edge(N,E)
N.add_building("Leviticus Cornwall Estate","Bottom")

print(dijkstra(Map,"Town Hall","Emerald Ranch"))