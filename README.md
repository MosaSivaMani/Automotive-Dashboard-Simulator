# 🚗 Automotive Dashboard Simulator

This project is a **graphical simulation of a car dashboard** using **Python and Tkinter**. It mimics basic functionalities of a real car dashboard, including a **speedometer**, **RPM gauge**, **fuel and temperature indicators**, and **dashboard warning lights**.   

It’s ideal for educational use, basic GUI projects, or simulation concepts for embedded/automotive systems.

---





## 🔧 Features

- 📈 **Speedometer & RPM Gauge**: Analog-style dials with animated needles.
- ⛽ **Fuel Bar**: Displays current fuel level; decreases with acceleration.
- 🌡️ **Engine Temperature Bar**: Shows increasing temp with engine use.
- 🚨 **Warning Lights**:
  - Left and Right Blinkers (Indicators)
  - Hazard Lights
  - High Beam Light
  - Check Engine Light
- 🕹️ **Interactive Buttons**:
  - Accelerate: Increases speed, RPM, and engine heat.
  - Brake: Slows down the car and cools the engine.
  - Refuel: Refills the fuel tank.
  - Toggle lights and indicators.

---

## 📦 Requirements

- **Python 3.x**
- **Tkinter** (Standard with most Python distributions)

No extra packages are required.

---

## 📁 Folder Structure

```

automotive-dashboard-simulator/
│
├── dashboard.py            # Main application file
├── assets/                 # (Optional) For storing custom icons/images
├── README.md               # Project documentation
└── LICENSE                 # License file (optional)

````

---

## ▶️ How to Run

1. Clone or download the repository.

```bash
git clone [https://github.com/MosaSivaMani/Automotive-Dashboard-Simulator.git](https://github.com/MosaSivaMani/Automotive-Dashboard-Simulator)
cd Automotive-Dashboard-Simulator
````

2. Run the main Python file:

```bash
python dashboard.py
```

> The GUI window will open showing the dashboard simulator.

---

## 🕹️ Controls

| Button        | Function                                                        |
| ------------- | --------------------------------------------------------------- |
| 🚀 Accelerate | Increases speed, RPM, and temperature; fuel decreases gradually |
| 🛑 Brake      | Reduces speed, RPM, and temperature                             |
| ⛽ Refuel      | Refills the fuel tank to maximum                                |
| 🔁 Indicators | Left, Right, and Hazard blinkers blink when toggled             |
| 💡 Lights     | High Beam and Check Engine indicators toggle on click           |

All components update in real time based on the state of the vehicle.

---

## 📚 Learning Objectives

This project helps you understand:

* GUI layout and canvas drawing with **Tkinter**
* Simulating analog instruments using arcs and lines
* Event-driven programming in Python
* Basic state management in GUI applications

---

## 📸 Screenshot
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e51641c6-9d06-4ba9-8d20-a76b859986ca" />


---

## 🧠 Future Enhancements (Ideas)

* Add gear shifting (automatic or manual)
* Use real-time threading to simulate time-based updates
* Add digital odometer and trip meter
* Use sound effects (e.g., engine hum, indicator click)
* Connect to hardware for real input (e.g., via Arduino)

---

## 📝 License

This project is provided **for educational purposes only**.

You may modify and distribute it freely under the terms of the [MIT License](LICENSE).

---


