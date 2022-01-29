from simulation.simulator import Simulator
from util.packet import PacketClass
from plotting.plotter import TwoFunctionPlotter, ThreeFunctionPlotter


def main():
    lambda_values_1 = [value / 10 for value in range(50, 130, 3)]
    mu_values = [14, 20, 26]
    
    simulated_average_packet_delay_values_1 = []
    analytical_average_packet_delay_values_1 = []

    for lambda_value in lambda_values_1:
        packet_classes = []
        
        for mu_value in mu_values:
            packet_classes.append(PacketClass(mu_value = mu_value))

        simulation = Simulator(end_time=20000, average_lambda=lambda_value, packet_classes=packet_classes)
        simulation.run()

        simulated_average_packet_delay_values_1.append(simulation.simulated_average_packet_delay)
        analytical_average_packet_delay_values_1.append(simulation.analytical_average_packet_delay)

    plotter_1 = TwoFunctionPlotter(
        lambda_values_1, 
        simulated_average_packet_delay_values_1,
        'Simulation',
        analytical_average_packet_delay_values_1, 
        'Analysis',
        'Lambda Value', 'Delay'
        )
    plotter_1.plot()

if __name__ == '__main__':
    main()