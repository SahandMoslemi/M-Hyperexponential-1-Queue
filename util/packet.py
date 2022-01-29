class PacketClass:
    def __init__(self, mu_value):
        self.mu_value = mu_value
        self.packets_arrived_numbers = 0
        self.packets_served_numbers = 0
        

class Packet:
    def __init__(self, arrival_time, packet_class):
        self.arrival_time = arrival_time
        self.packet_class = packet_class