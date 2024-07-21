
class Server:
    def __init__(self,name):
        self,name = name
        self.active_connections = 0

    def connect(self):
        self.active_connections += 1
    
    def disConnect(self):
        if self.active_connections > 0:
            self.active_connections -= 1

class LoadBalancer:
    def __init__(self,servers):
        self.servers = servers
    
    def get_least_loaded_server(self):
        return min(self.servers, key=lambda serv: serv.active_connections)
        

    def handle_requests(self):
        server = self.get_least_loaded_server()
        server.connect()
    
    def close_connection(self,server_name):
        for server in self.servers:
            if server.name == server_name:
                server.disconnect()
        

#Execution Begins here
# Instantiating 3 Instances of 
servers = [Server("Server A"), Server("Server B"), Server("Server C")]
lb = LoadBalancer(servers)

for _ in range(10):
    lb.handle_request()

lb.close_connection("Server A")
lb.close_connection("Server B")
lb.close_connection("Server C")
