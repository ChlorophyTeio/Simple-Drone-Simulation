import tkinter as tk
from PIL import Image, ImageTk


class QuadcopterUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quadcopter Simulation")

        # 加载图像
        image = Image.open(r"src\image.jpg")  # 替换为您自己的图像文件路径
        image = image.resize((300, 151))
        self.photo = ImageTk.PhotoImage(image)

        # 创建标签用于显示图像
        image_label = tk.Label(self.window, image=self.photo)
        image_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        self.speed_labels = []
        self.thrust_labels = []
        self.speed_change_labels = []
        self.thrust_change_labels = []

        # 创建标签用于显示旋翼转速和产生升力
        for i in range(4):
            speed_label = tk.Label(self.window, text=f"Rotor {i + 1} Speed: ")
            speed_label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="E")
            thrust_label = tk.Label(self.window, text=f"Rotor {i + 1} Thrust: ")
            thrust_label.grid(row=i + 1, column=1, padx=10, pady=5, sticky="E")
            speed_change_label = tk.Label(self.window, text="Speed Change: ")
            speed_change_label.grid(row=i + 1, column=2, padx=10, pady=5, sticky="E")
            thrust_change_label = tk.Label(self.window, text="Thrust Change: ")
            thrust_change_label.grid(row=i + 1, column=3, padx=10, pady=5, sticky="E")
            self.speed_labels.append(speed_label)
            self.thrust_labels.append(thrust_label)
            self.speed_change_labels.append(speed_change_label)
            self.thrust_change_labels.append(thrust_change_label)

        # 创建按钮用于控制无人机运动状态
        hover_button = tk.Button(self.window, text="Hover", command=self.hover)
        hover_button.grid(row=5, column=0, padx=10, pady=5)
        forward_button = tk.Button(self.window, text="Forward", command=self.forward)
        forward_button.grid(row=5, column=1, padx=10, pady=5)
        backward_button = tk.Button(self.window, text="Backward", command=self.backward)
        backward_button.grid(row=6, column=0, padx=10, pady=5)
        left_button = tk.Button(self.window, text="Left", command=self.left)
        left_button.grid(row=6, column=1, padx=10, pady=5)
        right_button = tk.Button(self.window, text="Right", command=self.right)
        right_button.grid(row=7, column=0, padx=10, pady=5)
        up_button = tk.Button(self.window, text="Up", command=self.up)
        up_button.grid(row=7, column=1, padx=10, pady=5)
        down_button = tk.Button(self.window, text="Down", command=self.down)
        down_button.grid(row=8, column=0, padx=10, pady=5)
        clockwise_button = tk.Button(self.window, text="Clockwise", command=self.clockwise)
        clockwise_button.grid(row=8, column=1, padx=10, pady=5)
        anticlockwise_button = tk.Button(self.window, text="Anti-clockwise", command=self.anticlockwise)
        anticlockwise_button.grid(row=9, column=0, padx=10, pady=5)
        land_button = tk.Button(self.window, text="Land", command=self.land)
        land_button.grid(row=9, column=1, padx=10, pady=5)

        self.window.mainloop()

    def update_ui(self, speeds, thrusts, speed_changes, thrust_changes):
        # 更新界面上的旋翼转速和产生升力的数值以及变化量
        for i in range(4):
            self.speed_labels[i].config(text=f"Rotor {i + 1} Speed: {speeds[i]}")
            self.thrust_labels[i].config(text=f"Rotor {i + 1} Thrust: {thrusts[i]}N")
            self.speed_change_labels[i].config(text=f"Speed Change: {speed_changes[i]}")
            self.thrust_change_labels[i].config(text=f"Thrust Change: {thrust_changes[i]}N")

    def hover(self):
        speeds = [4000, 4000, 4000, 4000]
        thrusts = [10, 10, 10, 10]
        speed_changes = [0, 0, 0, 0]
        thrust_changes = [0, 0, 0, 0]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def forward(self):
        speeds = [4100, 4100, 3900, 3900]
        thrusts = [10.5, 10.5, 9.5, 9.5]
        speed_changes = [100, 100, -100, -100]
        thrust_changes = [0.5, 0.5, -0.5, -0.5]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def backward(self):
        speeds = [3900, 3900, 4100, 4100]
        thrusts = [9.5, 9.5, 10.5, 10.5]
        speed_changes = [-100, -100, 100, 100]
        thrust_changes = [-0.5, -0.5, 0.5, 0.5]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def left(self):
        speeds = [3900, 4100, 4100, 3900]
        thrusts = [9.5, 10.5, 10.5, 9.5]
        speed_changes = [-100, 100, 100, -100]
        thrust_changes = [-0.5, 0.5, 0.5, -0.5]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def right(self):
        speeds = [4100, 3900, 3900, 4100]
        thrusts = [10.5, 9.5, 9.5, 10.5]
        speed_changes = [100, -100, -100, 100]
        thrust_changes = [0.5, -0.5, -0.5, 0.5]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def up(self):
        speeds = [4050, 4050, 4050, 4050]
        thrusts = [10.1, 10.1, 10.1, 10.1]
        speed_changes = [50, 50, 50, 50]
        thrust_changes = [0.1, 0.1, 0.1, 0.1]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def down(self):
        speeds = [3950, 3950, 3950, 3950]
        thrusts = [9.9, 9.9, 9.9, 9.9]
        speed_changes = [-50, -50, -50, -50]
        thrust_changes = [-0.1, -0.1, -0.1, -0.1]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def clockwise(self):
        speeds = [4050, 3950, 4050, 3950]
        thrusts = [10.1, 9.9, 10.1, 9.9]
        speed_changes = [50, -50, 50, -50]
        thrust_changes = [0.1, -0.1, 0.1, -0.1]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def anticlockwise(self):
        speeds = [3950, 4050, 3950, 4050]
        thrusts = [9.9, 10.1, 9.9, 10.1]
        speed_changes = [-50, 50, -50, 50]
        thrust_changes = [-0.1, 0.1, -0.1, 0.1]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)

    def land(self):
        speeds = [0, 0, 0, 0]
        thrusts = [0, 0, 0, 0]
        speed_changes = [0, 0, 0, 0]
        thrust_changes = [0, 0, 0, 0]
        self.update_ui(speeds, thrusts, speed_changes, thrust_changes)


# 创建QuadcopterUI实例
ui = QuadcopterUI()
