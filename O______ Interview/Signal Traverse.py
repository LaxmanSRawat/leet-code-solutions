

class Network():
    def __init__(self):
        self.graph = {}

    def add_satellite(self, sat_id):
        self.graph[sat_id] = []
        
    
    def add_relationship(self, sat_id1, sat_id2):
        if sat_id1 in self.graph and sat_id2 in self.graph:
            self.graph[sat_id1].append(sat_id2)
            self.graph[sat_id1].sort()
            self.graph[sat_id2].append(sat_id1)
            self.graph[sat_id2].sort()
            print(self.graph)
        else:
            print("Error - sat id doesn't exists")
    
    def network_test(self,listSats):
        if len(listSats):
            visitedSats = {}
            for sat in listSats:
                if sat not in visitedSats:
                    visitedSats[sat] = 0
                else:
                    print("Error Message sent twice")
            
            while(len(listSats)):
                sat = listSats[0]
                
                for connected_sat in self.graph[sat]:
                    if connected_sat not in visitedSats or (visitedSats[connected_sat] > visitedSats[sat] + 10):
                        visitedSats[sat] +=10
                        visitedSats[connected_sat] = visitedSats[sat] 
                        listSats.append(connected_sat)
                
                listSats.pop(0)

            
            print(visitedSats)

network = Network()
network.add_satellite(1)
network.add_satellite(2)
network.add_satellite(3)
network.add_satellite(4)
network.add_satellite(5)
network.add_satellite(6)
network.add_relationship(1,2)
network.add_relationship(2,3)
network.add_relationship(3,4)
network.add_relationship(4,5)
network.add_relationship(5,6)
network.add_relationship(1,4)
network.network_test([3,4])


