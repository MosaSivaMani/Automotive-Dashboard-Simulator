import tkinter as tk
import random
import math
import time
from tkinter import ttk

class AutoDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Automotive Dashboard")
        self.root.geometry("800x400")
        self.root.configure(bg="#222222")
        
        # Initialize variables
        self.speed = 0
        self.fuel_level = 100
        self.rpm = 0
        self.engine_temp = 50
        self.left_indicator = False
        self.right_indicator = False
        self.hazard_lights = False
        self.high_beam = False
        self.low_fuel = False
        self.check_engine = False
        self.indicator_state = False
        self.indicator_counter = 0
        
        self.setup_ui()
        self.update_dashboard()
    
    def setup_ui(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg="#222222")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Speedometer frame
        self.speed_frame = tk.Frame(self.main_frame, bg="#222222")
        self.speed_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Speedometer canvas
        self.speed_canvas = tk.Canvas(self.speed_frame, width=300, height=300, 
                                     bg="#222222", highlightthickness=0)
        self.speed_canvas.pack(pady=10)
        
        # RPM frame
        self.rpm_frame = tk.Frame(self.main_frame, bg="#222222")
        self.rpm_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # RPM canvas
        self.rpm_canvas = tk.Canvas(self.rpm_frame, width=300, height=300, 
                                   bg="#222222", highlightthickness=0)
        self.rpm_canvas.pack(pady=10)
        
        # Indicators frame
        self.indicators_frame = tk.Frame(self.main_frame, bg="#222222")
        self.indicators_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
        # Left indicator
        self.left_ind_btn = tk.Button(self.indicators_frame, text="◀", font=("Arial", 16),
                                     bg="#333333", fg="#555555", width=3, height=1,
                                     command=self.toggle_left_indicator)
        self.left_ind_btn.pack(side=tk.LEFT, padx=10)
        
        # Hazard lights
        self.hazard_btn = tk.Button(self.indicators_frame, text="⚠", font=("Arial", 16),
                                   bg="#333333", fg="#555555", width=3, height=1,
                                   command=self.toggle_hazard)
        self.hazard_btn.pack(side=tk.LEFT, padx=10)
        
        # High beam
        self.high_beam_btn = tk.Button(self.indicators_frame, text="⊙", font=("Arial", 16),
                                      bg="#333333", fg="#555555", width=3, height=1,
                                      command=self.toggle_high_beam)
        self.high_beam_btn.pack(side=tk.LEFT, padx=10)
        
        # Check engine
        self.check_engine_btn = tk.Button(self.indicators_frame, text="⚙", font=("Arial", 16),
                                         bg="#333333", fg="#555555", width=3, height=1,
                                         command=self.toggle_check_engine)
        self.check_engine_btn.pack(side=tk.LEFT, padx=10)
        
        # Fuel level
        self.fuel_frame = tk.Frame(self.indicators_frame, bg="#222222")
        self.fuel_frame.pack(side=tk.LEFT, padx=20)
        
        self.fuel_label = tk.Label(self.fuel_frame, text="Fuel", font=("Arial", 12),
                                  bg="#222222", fg="white")
        self.fuel_label.pack()
        
        self.fuel_bar = ttk.Progressbar(self.fuel_frame, orient=tk.HORIZONTAL, 
                                       length=100, mode='determinate')
        self.fuel_bar.pack(pady=5)
        
        # Temperature
        self.temp_frame = tk.Frame(self.indicators_frame, bg="#222222")
        self.temp_frame.pack(side=tk.LEFT, padx=20)
        
        self.temp_label = tk.Label(self.temp_frame, text="Temp", font=("Arial", 12),
                                  bg="#222222", fg="white")
        self.temp_label.pack()
        
        self.temp_bar = ttk.Progressbar(self.temp_frame, orient=tk.HORIZONTAL, 
                                       length=100, mode='determinate')
        self.temp_bar.pack(pady=5)
        
        # Right indicator
        self.right_ind_btn = tk.Button(self.indicators_frame, text="▶", font=("Arial", 16),
                                      bg="#333333", fg="#555555", width=3, height=1,
                                      command=self.toggle_right_indicator)
        self.right_ind_btn.pack(side=tk.RIGHT, padx=10)
        
        # Control buttons
        self.control_frame = tk.Frame(self.root, bg="#222222")
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
        self.accel_btn = tk.Button(self.control_frame, text="Accelerate", 
                                  command=self.accelerate)
        self.accel_btn.pack(side=tk.LEFT, padx=10)
        
        self.brake_btn = tk.Button(self.control_frame, text="Brake", 
                                  command=self.brake)
        self.brake_btn.pack(side=tk.LEFT, padx=10)
        
        self.refuel_btn = tk.Button(self.control_frame, text="Refuel", 
                                   command=self.refuel)
        self.refuel_btn.pack(side=tk.RIGHT, padx=10)
    
    def draw_speedometer(self):
        # Clear canvas
        self.speed_canvas.delete("all")
        
        # Draw speedometer arc
        self.speed_canvas.create_arc(50, 50, 250, 250, start=140, extent=260,
                                    style="arc", outline="white", width=2)
        
        # Draw speed markings
        for i in range(0, 220, 20):
            angle = 140 + (i / 220) * 260
            radian = math.radians(angle)
            x1 = 150 + 90 * math.cos(radian)
            y1 = 150 + 90 * math.sin(radian)
            x2 = 150 + 100 * math.cos(radian)
            y2 = 150 + 100 * math.sin(radian)
            self.speed_canvas.create_line(x1, y1, x2, y2, fill="white")
            
            # Add speed numbers
            x3 = 150 + 75 * math.cos(radian)
            y3 = 150 + 75 * math.sin(radian)
            self.speed_canvas.create_text(x3, y3, text=str(i), fill="white")
        
        # Draw needle
        angle = 140 + (self.speed / 220) * 260
        radian = math.radians(angle)
        x = 150 + 90 * math.cos(radian)
        y = 150 + 90 * math.sin(radian)
        self.speed_canvas.create_line(150, 150, x, y, fill="red", width=2)
        
        # Draw center circle
        self.speed_canvas.create_oval(145, 145, 155, 155, fill="red", outline="")
        
        # Display speed text
        self.speed_canvas.create_text(150, 200, text=f"{int(self.speed)} km/h", 
                                     fill="white", font=("Arial", 14, "bold"))
    
    def draw_rpm_gauge(self):
        # Clear canvas
        self.rpm_canvas.delete("all")
        
        # Draw RPM arc
        self.rpm_canvas.create_arc(50, 50, 250, 250, start=140, extent=260,
                                  style="arc", outline="white", width=2)
        
        # Draw RPM markings
        for i in range(0, 8000, 1000):
            angle = 140 + (i / 8000) * 260
            radian = math.radians(angle)
            x1 = 150 + 90 * math.cos(radian)
            y1 = 150 + 90 * math.sin(radian)
            x2 = 150 + 100 * math.cos(radian)
            y2 = 150 + 100 * math.sin(radian)
            self.rpm_canvas.create_line(x1, y1, x2, y2, fill="white")
            
            # Add RPM numbers
            x3 = 150 + 75 * math.cos(radian)
            y3 = 150 + 75 * math.sin(radian)
            self.rpm_canvas.create_text(x3, y3, text=str(i//1000), fill="white")
        
        # Draw red zone
        self.rpm_canvas.create_arc(50, 50, 250, 250, start=140 + (6000 / 8000) * 260, 
                                  extent=(8000 - 6000) / 8000 * 260,
                                  style="arc", outline="red", width=4)
        
        # Draw needle
        angle = 140 + (self.rpm / 8000) * 260
        radian = math.radians(angle)
        x = 150 + 90 * math.cos(radian)
        y = 150 + 90 * math.sin(radian)
        self.rpm_canvas.create_line(150, 150, x, y, fill="red", width=2)
        
        # Draw center circle
        self.rpm_canvas.create_oval(145, 145, 155, 155, fill="red", outline="")
        
        # Display RPM text
        self.rpm_canvas.create_text(150, 200, text=f"{int(self.rpm)} RPM", 
                                   fill="white", font=("Arial", 14, "bold"))
    
    def update_indicators(self):
        # Update indicator state (blinking effect)
        self.indicator_counter += 1
        if self.indicator_counter >= 5:
            self.indicator_state = not self.indicator_state
            self.indicator_counter = 0
        
        # Update left indicator
        if self.left_indicator or self.hazard_lights:
            if self.indicator_state:
                self.left_ind_btn.config(fg="green")
            else:
                self.left_ind_btn.config(fg="#555555")
        else:
            self.left_ind_btn.config(fg="#555555")
        
        # Update right indicator
        if self.right_indicator or self.hazard_lights:
            if self.indicator_state:
                self.right_ind_btn.config(fg="green")
            else:
                self.right_ind_btn.config(fg="#555555")
        else:
            self.right_ind_btn.config(fg="#555555")
        
        # Update hazard lights
        if self.hazard_lights:
            if self.indicator_state:
                self.hazard_btn.config(fg="yellow")
            else:
                self.hazard_btn.config(fg="#555555")
        else:
            self.hazard_btn.config(fg="#555555")
        
        # Update high beam
        if self.high_beam:
            self.high_beam_btn.config(fg="blue")
        else:
            self.high_beam_btn.config(fg="#555555")
        
        # Update check engine
        if self.check_engine:
            self.check_engine_btn.config(fg="orange")
        else:
            self.check_engine_btn.config(fg="#555555")
        
        # Update fuel bar
        self.fuel_bar['value'] = self.fuel_level
        if self.fuel_level < 20:
            self.fuel_label.config(fg="red")
        else:
            self.fuel_label.config(fg="white")
        
        # Update temperature bar
        self.temp_bar['value'] = self.engine_temp
        if self.engine_temp > 80:
            self.temp_label.config(fg="red")
        else:
            self.temp_label.config(fg="white")
    
    def toggle_left_indicator(self):
        if not self.hazard_lights:
            self.left_indicator = not self.left_indicator
            if self.left_indicator:
                self.right_indicator = False
    
    def toggle_right_indicator(self):
        if not self.hazard_lights:
            self.right_indicator = not self.right_indicator
            if self.right_indicator:
                self.left_indicator = False
    
    def toggle_hazard(self):
        self.hazard_lights = not self.hazard_lights
        if self.hazard_lights:
            self.left_indicator = False
            self.right_indicator = False
    
    def toggle_high_beam(self):
        self.high_beam = not self.high_beam
    
    def toggle_check_engine(self):
        self.check_engine = not self.check_engine
    
    def accelerate(self):
        if self.speed < 220:
            self.speed += 10
        if self.rpm < 8000:
            self.rpm += 500
        if self.fuel_level > 0:
            self.fuel_level -= 1
        if self.engine_temp < 100:
            self.engine_temp += 2
    
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
        if self.rpm > 0:
            self.rpm -= 500
        if self.engine_temp > 50:
            self.engine_temp -= 1
    
    def refuel(self):
        self.fuel_level = 100
    
    def update_dashboard(self):
        # Simulate some random fluctuations
        if self.speed > 0:
            self.speed += random.uniform(-2, 2)
            self.speed = max(0, min(220, self.speed))
            
            self.rpm += random.uniform(-100, 100)
            self.rpm = max(0, min(8000, self.rpm))
            
            self.fuel_level -= random.uniform(0, 0.1)
            self.fuel_level = max(0, min(100, self.fuel_level))
            
            self.engine_temp += random.uniform(-0.5, 0.5)
            self.engine_temp = max(50, min(100, self.engine_temp))
        
        # Update UI elements
        self.draw_speedometer()
        self.draw_rpm_gauge()
        self.update_indicators()
        
        # Schedule next update
        self.root.after(100, self.update_dashboard)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoDashboard(root)
    root.mainloop()