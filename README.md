# 🚦 Smart Traffic Signal AI
**Meta PyTorch OpenEnv Hackathon – Round 1 Submission**

## 👥 Team Details
This project was developed as part of the **Meta PyTorch OpenEnv Hackathon Round 1**.

**Team Name:** Smart Innovators  
**Project Type:** AI / Reinforcement Learning Simulation  
**Category:** Smart Traffic Optimization  

---

## 📌 Project Overview
This project is an AI-based traffic signal simulation built as a Reinforcement Learning environment.

The system simulates a **4-way road junction**:
- North
- South
- East
- West

The AI agent analyzes traffic density and decides which road should receive the green signal in order to reduce congestion and improve traffic flow.

---

## 🎯 Objective
The objective of this project is to **reduce traffic congestion and waiting time** by using AI-based decision making to optimize traffic signal flow.

This system aims to:
- improve traffic movement
- reduce vehicle waiting time
- prioritize emergency vehicles
- dynamically adapt to changing traffic conditions

---

## ❗ Problem Statement
Traditional traffic lights operate on fixed timers, which can cause unnecessary waiting and traffic jams.

Our project solves this by creating an intelligent traffic signal controller that:
- reduces waiting time
- prioritizes high traffic roads
- handles emergency vehicles
- dynamically adapts to new traffic

---

## ⚙️ How It Works
1. The environment generates random traffic on 4 roads.
2. The AI selects the road with the highest traffic.
3. The signal turns green for that road.
4. Traffic on that road decreases.
5. New vehicles arrive randomly.
6. Rewards and penalties are calculated.

---

## 🏆 Reward Logic
- **+10** → correct road selected
- **-3** → wrong road selected
- **-10** → emergency vehicle ignored
- additional penalty for high waiting traffic

---

## 🛠️ Tech Stack
- Python
- NumPy
- Google Colab
- Reinforcement Learning Logic

---

## 🚀 Demo
The project is implemented and tested successfully in **Google Colab**.

The simulation demonstrates:
- dynamic traffic generation
- smart green signal selection
- congestion reduction
- emergency handling

---

## 🔥 Future Improvements
- real-time traffic prediction
- timer optimization
- ambulance priority system
- deep RL model integration
- city-scale traffic simulation

---

## 🏁 Conclusion
This project provides a smart AI-based traffic signal simulation that helps optimize urban traffic flow using Reinforcement Learning concepts.

It is designed as a scalable foundation for future smart city traffic systems.
