# PZ.O3 Remonty dróg

**Projekt na Podstawy Sztucznej Inteligencji**

## Treść projektu

Dany jest graf opisujący sieć drogową w danym kraju, w którym krawędzie mają wagi wskazujące na przepustowość dróg (maksymalną liczbę pojazdów, które mogą przejechać odcinkiem w jednostce czasu). “Remont” połączenia drogowego polega na modyfikacji jego wagi, co obarczone jest pewnym kosztem. Należy opracować metodę pozwalającą na optymalizację kosztów remontów tak, aby maksymalnie poprawić przepustowość sieci drogowej przy zachowaniu danego budżetu. Przepustowość rozumiana jest jako średnia liczba pojazdów, która jest w stanie przejechać między dwoma miastami w kraju.<br><br>
Dane wejściowe:
* plik z grafem (węzły *v<sub>1</sub>, v<sub>2</sub>, …*; krawędzie *e<sub>1</sub>, e<sub>2</sub>*, …) opisującym mapę drogową (waga *w<sub>i</sub>* krawędzi *e<sub>i</sub>* to przepustowość połączenia),
* lista kosztów *k<sub>1</sub>, k<sub>2</sub>, …,* gdzie *k<sub>i</sub>* to koszt remontu *e<sub>i</sub>*,
* maksymalny budżet *C*,<br>

Dane wyjściowe: lista krawędzi do wyremontowania, przepustowość przed i po remoncie.

[Strona projektów](https://pzawistowski.github.io/PSZT19Z)


## Some documentation

### Main
#### How to use Graph and Weights objects
You need to create an object of class Graph and an object of class Weights.<br>
Then you need to of course load graph and weights from files.
Then you obligatory need to set weights to graph - it's not going to work with none weights. You can call function: graph.setWeights( weights.getList(), [] )<br>
Now you can do whatever you want<br><br>

### Graph
It stores whole graph with vertices which can be cities or not, edges and weights
* *_graph* - table of edges and weights \[ vertex1, vertex2, weight \]
* *_size* - quantity of edges
* *_vertices* - list of vertices and if they are or they are not cities<br><br>

**loadFromFile( fileName )**<br>
Function loads graph from file
* *fileName* - name of file with graph *(string)*
File format:<br>
v<sub>0</sub> v<sub>1</sub> v<sub>2</sub> v<sub>3</sub> ...<br> - separated with space
c<sub>0</sub> c<sub>1</sub> c<sub>2</sub> c<sub>3</sub> ...<br> - separated with space
e<sub>i0</sub> e<sub>j0</sub><br> - separated with tab
e<sub>i1</sub> e<sub>j1</sub><br>
e<sub>i2</sub> e<sub>j2</sub> ...<br><br>
where c<sub>i</sub> is type of bool and says if vertex is a city or not

**setWeights( weights, modifiesEdgesIndexes )**<br>
Function sets new weights to graph
* *weights* - table of weights and costs \[ weightBefore, weightAfter, cost \]. It should be oject of class *weights*
* *modifiesEdgesIndexes* - list of edge's indexes which need to be modified. Edge's index can be given by function *getEdgeIndex*<br><br>

**getEdgeIndex( vertex1, vertex2 )**<br>
Function return edge's index based on 2 vertices
* *vertex1, vertex2* - vertices of edge which index function will return
* *return* - index of given edge or -1 if edge doesn't exist<br><br>

**maxFlow( begin, end )**<br>
Function counts maximum flow of graph for pair of vertex *( begin, end )*
* *begin, end* - vertices - between them function will count maximum flow
* *return* - maximum flow<br><br>

### Weights
Stores list of weights and costs<br><br>

**loadFromFile( fileName )**<br>
Function loads weights and costs from file
* *fileName* - name of file with weights and costs *(string)*
Line in file format:<br>
weightBefore weightAfter cost - must be separated with tab

**getList()**<br>
Function returns list of weights and costs
*return* - list of weights and costs
