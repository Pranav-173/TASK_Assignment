# Programming for Problem Solving – Task Assignment

**Student:** D. Pranav Kumar 


**Roll No:** 25951A6677


**Branch:** CSE(AIML) - B


**Course:** Programming for Problem Solving Laboratory (ACSE07)  

---

## Task 12 – Daily Water Intake Tracker

### Description:
A Python program that tracks daily water consumption and determines whether a user is **Under-hydrated**, **Adequately Hydrated**, or **Over-hydrated** based on recommended intake levels.

### Constraints:
- Water intake range: 0 to 5 liters per day  
- Recommended intake: 2 liters per day  
- Numeric input only  
- Console-based application  
- No permanent data storage  

### Classification Rules:
| Status              | Condition              |
|---------------------|-----------------------|
| Under-hydrated      | intake < 2 liters     |
| Adequately Hydrated | intake = 2 liters     |
| Over-hydrated       | intake > 2 liters     |

---

## Task 14 – Smart Traffic Signal Timer Advisor

### Description:
A Python program that analyzes the number of vehicles waiting at a traffic signal and determines the traffic density as **Low**, **Medium**, or **High**. Based on this analysis, the system suggests an appropriate green signal duration and provides basic traffic guidance to drivers.

### Constraints:
- Number of vehicles range: 0 to 100  
- Green signal timing is an estimate (not real-time control)  
- Console-based application  
- Fixed rule-based logic  
- No sensor or live data integration  

### Traffic Classification Rules:
| Traffic Density | Vehicle Count Range |
|----------------|-------------------|
| Low            | 0 – 10            |
| Medium         | 11 – 30           |
| High           | 31 – 100          |

---

## Task 45 – Movie Theatre Seat Booking System

### Description:
A Python-based simulation of a movie theatre booking system that manages seat reservations using the **First-Come, First-Served (FCFS)** approach. Customers request a number of seats, and the system processes each request in order of arrival. If enough seats are available, the booking is confirmed; otherwise, it is rejected. The system tracks seat availability, total customers served, and rejected bookings.

### Core Concepts Used:
- Queue (`collections.deque`)  
- Simulation-based programming  
- Resource allocation  
- First-Come, First-Served (FCFS) scheduling  

### Constraints:
- Total seats > 0  
- Requested seats > 0  
- Requests processed in arrival order  
- Only one booking counter is available  
- No dictionaries are used  
- Only lists, tuples, and queues are allowed  
