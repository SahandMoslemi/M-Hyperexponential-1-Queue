from matplotlib import pyplot as plotter


class TwoFunctionPlotter:
    def __init__(self, x_values, y_values_1, function_label_1, y_values_2, function_label_2, x_label, y_label):
        self.x_values = x_values
        self.y_values_1 = y_values_1
        self.function_label_1 = function_label_1
        self.y_values_2 = y_values_2
        self.function_label_2 = function_label_2
        self.x_label = x_label
        self.y_label = y_label

    def plot(self):
        plotter.plot(self.x_values, self.y_values_1, marker='o', label=self.function_label_1)
        plotter.plot(self.x_values, self.y_values_2, marker='^', label=self.function_label_2)
        plotter.xlabel(self.x_label)
        plotter.ylabel(self.y_label)
        plotter.legend()
        plotter.show()


class ThreeFunctionPlotter:
    def __init__(self, x_values, y_values_1, function_label_1, y_values_2, function_label_2, y_values_3, function_label_3, x_label, y_label):
        self.x_values = x_values
        self.y_values_1 = y_values_1
        self.function_label_1 = function_label_1
        self.y_values_2 = y_values_2
        self.function_label_2 = function_label_2
        self.y_values_3 = y_values_3
        self.function_label_3 = function_label_3
        self.x_label = x_label
        self.y_label = y_label

    def plot(self):
        plotter.plot(self.x_values, self.y_values_1, marker='o', label=self.function_label_1)
        plotter.plot(self.x_values, self.y_values_2, marker='^', label=self.function_label_2)
        plotter.plot(self.x_values, self.y_values_3, marker='>', label=self.function_label_3)
        plotter.xlabel(self.x_label)
        plotter.ylabel(self.y_label)
        plotter.legend()
        plotter.show()