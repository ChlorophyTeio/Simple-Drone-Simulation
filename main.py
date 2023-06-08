import tkinter as tk


class QuadcopterUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quadcopter Simulation")

        self.speed_labels = []
        self.thrust_labels = []

        # 创建标签用于显示旋翼转速和产生升力
        for i in range(4):
            speed_label = tk.Label(self.window, text=f"Rotor {i + 1} Speed: ")
            speed_label.grid(row=i, column=0, padx=10, pady=5)
            thrust_label = tk.Label(self.window, text=f"Rotor {i + 1} Thrust: ")
            thrust_label.grid(row=i, column=1, padx=10, pady=5)
            self.speed_labels.append(speed_label)
            self.thrust_labels.append(thrust_label)

        # 创建按钮用于控制无人机运动状态
        hover_button = tk.Button(self.window, text="Hover", command=self.hover)
        hover_button.grid(row=4, column=0, padx=10, pady=5)
        forward_button = tk.Button(self.window, text="Forward", command=self.forward)
        forward_button.grid(row=4, column=1, padx=10, pady=5)
        backward_button = tk.Button(self.window, text="Backward", command=self.backward)
        backward_button.grid(row=5, column=0, padx=10, pady=5)
        left_button = tk.Button(self.window, text="Left", command=self.left)
        left_button.grid(row=5, column=1, padx=10, pady=5)
        right_button = tk.Button(self.window, text="Right", command=self.right)
        right_button.grid(row=6, column=0, padx=10, pady=5)
        up_button = tk.Button(self.window, text="Up", command=self.up)
        up_button.grid(row=6, column=1, padx=10, pady=5)
        down_button = tk.Button(self.window, text="Down", command=self.down)
        down_button.grid(row=7, column=0, padx=10, pady=5)
        clockwise_button = tk.Button(self.window, text="Clockwise", command=self.clockwise)
        clockwise_button.grid(row=7, column=1, padx=10, pady=5)
        anticlockwise_button = tk.Button(self.window, text="Anti-clockwise", command=self.anticlockwise)
        anticlockwise_button.grid(row=8, column=0, padx=10, pady=5)

        self.window.mainloop()

    def update_ui(self, speeds, thrusts):
        # 更新界面上的旋翼转速和产生升力的数值
        for i in range(4):
            self.speed_labels[i].config(text=f"Rotor {i + 1} Speed: {speeds[i]}")
            self.thrust_labels[i].config(text=f"Rotor {i + 1} Thrust: {thrusts[i]}N")

    def hover(self):
        speeds = [4000, 4000, 4000, 4000]
        thrusts = [10, 10, 10, 10]
        self.update_ui(speeds, thrusts)

    def forward(self):
        speeds = [4100, 4100, 3900, 3900]
        thrusts = [10.5, 10.5, 9.5, 9.5]
        self.update_ui(speeds, thrusts)

    def backward(self):
        speeds = [3900, 3900, 4100, 4100]
        thrusts = [9.5, 9.5, 10.5, 10.5]
        self.update_ui(speeds, thrusts)

    def left(self):
        speeds = [3900, 4100, 4100, 3900]
        thrusts = [9.5, 10.5, 10.5, 9.5]
        self.update_ui(speeds, thrusts)

    def right(self):
        speeds = [4100, 3900, 3900, 4100]
        thrusts = [10.5, 9.5, 9.5, 10.5]
        self.update_ui(speeds, thrusts)

    def up(self):
        speeds = [4050, 4050, 4050, 4050]
        thrusts = [10.1, 10.1, 10.1, 10.1]
        self.update_ui(speeds, thrusts)

    def down(self):
        speeds = [3950, 3950, 3950, 3950]
        thrusts = [9.9, 9.9, 9.9, 9.9]
        self.update_ui(speeds, thrusts)

    def clockwise(self):
        speeds = [4050, 3950, 4050, 3950]
        thrusts = [10.1, 9.9, 10.1, 9.9]
        self.update_ui(speeds, thrusts)

    def anticlockwise(self):
        speeds = [3950, 4050, 3950, 4050]
        thrusts = [9.9, 10.1, 9.9, 10.1]
        self.update_ui(speeds, thrusts)


# 创建QuadcopterUI实例
ui = QuadcopterUI()
