BGP_MSG_OPEN = 1
BGP_MSG_UPDATE = 2
BGP_MSG_NOTIFICATION = 3
BGP_MSG_KEEPALIVE = 4
BGP_MSG_ROUTE_REFRESH = 5

class Bgp:

    def __init__(self,bgp):
        self.bgp=bgp
        self.type=bgp[36:38] # bgp_type_message
    def check_validity(self):
