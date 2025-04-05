# 🧳 Travel Booking Saga Pattern - Microservices Simulation

This project simulates the **Saga Pattern** using four simple microservices communicating over HTTP via REST. The architecture follows a centralized orchestrator model to coordinate the distributed transactions.

Each service uses in-memory storage (Python lists or Node.js arrays), making it ideal for quick testing and learning environments.

---

## 🚀 Microservices Overview

| Service         | Port  | Description                              |
|-----------------|-------|------------------------------------------|
| flight_service  | 5001  | Simulates flight booking and cancellation |
| hotel_service   | 5002  | Simulates hotel booking (with possible failure) |
| car_service     | 5003  | Simulates car rental booking              |
| orchestrator    | 5000  | Coordinates the booking flow (Saga logic) |

---

## 🧱 Technologies Used

- Python + Flask (`flight_service`, `car_service`, `orchestrator`)
- Node.js + Express (`hotel_service`)
- Docker + Docker Compose

---

## 📦 How to Run It

```bash
git clone https://github.com/fredyunivalle/saga-reserva-viaje.git
cd saga-reserva-viaje
docker-compose up --build

```
## 📦  Test the Workflow
```bash
curl -X POST http://localhost:5000/book-trip -H "Content-Type: application/json" -d '{"user": "john_doe"}'
```
Each service will print logs in the console. If the hotel service fails randomly, the orchestrator will call the corresponding compensation routes.

## 🎓 Final Challenge for Students
Mission: Take this basic simulation and evolve it into a fault-tolerant, scalable, highly available system running in Kubernetes.

---

## 🧠 More Saga Use Case Ideas (Beyond Travel)

Don't limit yourself to travel-themed systems — microservices and the Saga pattern apply to many domains. Below are some real-world and imaginative scenarios to inspire your team:

### 💳 Fintech / Digital Banking
- **Use Case:** Opening a new bank account
- **Services:** Identity verification, credit check, account creation, card issuance
- **Compensation:** Revoke application, delete user data

### 🛍️ E-Commerce Checkout
- **Use Case:** Purchasing a product
- **Services:** Cart validation, payment processing, inventory update, order confirmation
- **Compensation:** Cancel payment, restock items, invalidate order

### 🏥 Hospital Management
- **Use Case:** Scheduling surgery
- **Services:** Book surgeon, reserve operating room, assign anesthesia team
- **Compensation:** Free up resources, notify cancellation

### 🎮 Online Gaming Matchmaking
- **Use Case:** Creating a multiplayer match
- **Services:** Lobby creation, player matching, server allocation
- **Compensation:** Close lobby, release server slots

### 🍕 Food Delivery
- **Use Case:** Ordering a meal
- **Services:** Create order, assign restaurant, dispatch rider, process payment
- **Compensation:** Cancel order, refund payment, notify customer

### 🎓 University Enrollment
- **Use Case:** Semester registration
- **Services:** Course eligibility check, enroll subjects, generate bill
- **Compensation:** Cancel enrollment, release class seats

### 📦 Logistics & Shipping
- **Use Case:** Fulfill a shipping order
- **Services:** Assign warehouse, prepare package, schedule pickup
- **Compensation:** Cancel shipment, restock inventory

---

### 🧙‍♀️ Magical or Cutesy (Imaginative) Scenarios

#### 🧙 Wizard School Enrollment
- **Services:** Wand validation, house assignment, owl delivery  
- **Compensation:** Revoke owl, undo house sorting

#### 🐉 Dragon Rider Training
- **Services:** Dragon match, training session, gear assignment  
- **Compensation:** Cancel training, return dragon

#### 💕 LoveSong Records
- **Services:** Write lyrics, compose music, record vocals, deliver digital file  
- **Compensation:** Emotional refund 💔, delete song

---

## 🧪 Lab Instructions (Team Project)

This is a **team lab**. You must collaborate to implement a full Saga-based microservices project.

- Each team member should build one microservice (e.g., flight, hotel, payment, etc.).
- Together, you will design and develop the **central orchestrator**.
  - Optionally, nominate a **tech lead** to coordinate the orchestrator logic.
- You can implement services in different languages (e.g., Python, Node.js, Java).
- Use Docker Compose for local testing, and Kubernetes for deployment in the final version.

> 💡 Be creative. Think like real engineers. Surprise your instructor with something useful, fun, or just totally unexpected!

