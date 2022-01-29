import random
from util.queue import Queue
from util.packet import Packet
from util.config import LARGE_NUMBER
from util.util import exponential_random


class Simulator:
    def __init__(self, end_time, packet_classes, average_lambda):
        self.end_time = end_time
        self.packet_classes = packet_classes
        self.average_lambda = average_lambda
        self.buffer = Queue()

    def run(self):
        time = 0
        next_arrival_time = time + exponential_random(1/self.average_lambda)
        next_departure_time = LARGE_NUMBER
        self.total_delay = 0
        
        while time <= self.end_time:
            time = min(next_arrival_time, next_departure_time)

            if time == next_arrival_time:
                arrived_packet = self.buffer.insert(Packet(time, random.choice(self.packet_classes)))
                arrived_packet.packet_class.packets_arrived_numbers += 1
                next_arrival_time = time + exponential_random(1/self.average_lambda)

                if next_departure_time == LARGE_NUMBER:
                    next_departure_time = time + exponential_random(1/self.buffer.first_item.packet_class.mu_value)

            if time == next_departure_time:
                last_served_packet = self.buffer.delete()
            
                packet_delay = time - last_served_packet.arrival_time
                last_served_packet.packet_class.packets_served_numbers += 1
                self.total_delay += packet_delay

                if self.buffer.is_empty(): 
                    next_departure_time = LARGE_NUMBER

                else:
                    next_departure_time = time + exponential_random(1/self.buffer.first_item.packet_class.mu_value)

    @property
    def simulated_average_packet_delay(self):
        total_packets_arrived_number = 0
        
        for packet_class in self.packet_classes:
            total_packets_arrived_number += packet_class.packets_arrived_numbers

        return self.total_delay / total_packets_arrived_number

    @property
    def analytical_average_packet_delay(self):
        n = len(self.packet_classes)
        sigma_inverse_mu = 0
        sigma_inverse_mu_square = 0
        
        for packet_class in self.packet_classes:
            sigma_inverse_mu += 1 / packet_class.mu_value
            sigma_inverse_mu_square += 1 / (packet_class.mu_value ** 2)

        average = (1 / n) * sigma_inverse_mu
        second_moment = (2 / n) * sigma_inverse_mu_square
        w = ((self.average_lambda * second_moment) / (2 * (1 - (self.average_lambda * average)))) + average

        return w

