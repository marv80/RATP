# RATP
Transport App Project using RATP Api and data 

#NavEco project 

After deciding on our project, the next step that came naturally was the choice of the method that we wanted to implement and how to use it in order to solve it.

To be able to solve the problem, we actually have to know our problem and what we can be able to implement in the time that we have.(like Sun-Tzu has said in the art of war : “If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle.”) and that’s the way we’re going to process during this project.


First of all, the context:
The RATP has recently made a step forward to embrace the Open Data world.
We’re going to use the data in order to have a new public transport application which will push people to use public transports over car.

 The open data philosophy consists in the availability and liberty to use all data for everyone.
It’s based on the same alignment as the open-source, a more collaborative and a possibility of innovation for everyone.
All stations and time schedule are now available in the GTFS format (General Transit Feed Specification) , a format created by google which allows the storage and usage of the transport data.  
https://developers.google.com/transit/gtfs/reference/?hl=fr

The paradigm that we chose is an eco-responsible / cultural one. On top of the different transportation and multi-modal transport management, our application will propose different services like velib' and interesting pedestrian walks in Paris. It will also indicate the different places were you can buy tickets. 


The main problem that we are currently facing is a classical one in the algorithm world; the shortest path algorithm.
An algorithm that has for goal to calculate the shortest way between two given points places.
We chosed to start by practicing the algorithm on 2 sets of data :

-        A set composed by ourselves with the same format as the RATP data but with only 5 simple lines that we can associate to  an oriented graph. 

-        Another set of data which is composed of some metro, train and bus lines to be sure that the algorithm is able to give us the best answer according to the Multi-modal aspect of the problem.

This problem of the shortest path was first addressed by ……….. and the most popular one the Djikstra algorithm.
Both of them use the graph theory where :
-        A place is a node
-        A road is a vertices

-        The different vertices are weighted; they include a number which correspond to the length of the chosen road.
We started by  studying both of those algorithm
After those complete studies we decided to implement them
  The next step that we chose to have and we went throw their most advanced iteration.
Our application won’t be base don Djikstra algorithm . We will use the RAPTOR one.
BONUS, Since we’re going to implement a non-graph-based algorithm, we will try to implement if we do have enough time an iteration of Djikstra’s with the velib stations.
