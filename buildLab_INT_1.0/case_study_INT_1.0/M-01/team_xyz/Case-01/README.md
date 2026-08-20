Case Study 01 — Logistics Delivery & Route Optimization System
Case type: Product/technical outcome | Status: Draft
Contributors and Roles
Team Lead: Rohit Pandey
Delivery Owner: Rohit Pandey
Quality & Documentation Owner: Tejas G.C, Srijana Bohara
Problem 1 — Efficient Dynamic Route Planning & Traffic Adaptation
Problem Statement: In e-commerce logistics, delivering packages involves deciding vehicle routes under constantly changing real-world conditions like traffic jams, road closures, and varied delivery locations. A route that appears shortest by distance on a map may take significantly longer due to congestion. The system must dynamically select optimal routes and recalculate paths when real-time conditions change instead of treating deliveries as isolated, static trips.
Impact
•	Database: Requires storing order details, real-time location vectors, route histories, driver assignments, and delivery status logs.
•	Users (Customers & Couriers): Couriers experience delays and increased transit times without traffic awareness; customers suffer from unpredictable delivery windows and lack of transparency.
•	System: Manual route decisions do not scale. Without dynamic routing, the system cannot optimize multiple concurrent deliveries, leading to higher operational costs and inefficient resource utilization.
Engineering Solutions (Tech Stack Used)
Control / Component	Technology	Why
Network Representation	Graph Models (Nodes & Edges)	Maps intersections as nodes and roads as edges with cost attributes (distance/travel time).
Core Pathfinding	Dijkstra’s Algorithm	Finds the lowest-cost path through the network when road costs are non-negative.
Directed Path Search	A* (A-Star) Algorithm	Uses g(n) (cost traveled) and h(n) (heuristic estimate to goal) to prioritize efficient search.
Live Traffic Integration	Traffic Data API & GPS Services	Converts real-time traffic congestion into dynamic edge costs.
Dynamic Re-routing	Route Engine Trigger	Recalculates the remaining path mid-transit if traffic conditions spike the original path cost.
References
•	Dijkstra, E. W. (1959). A Note on Two Problems in Connection with Graphs.
•	Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths.
•	Google Maps Traffic Documentation & OpenStreetMap Data
Problem 2 — Real-Time Delivery Tracking & Customer Transparency
Problem Statement: Once a package is in transit, lack of real-time visibility creates uncertainty for both the delivery operation and the customer. Systems must continuously track courier locations, process updates, and push status changes instantly without requiring continuous manual page refreshes.
Impact
•	Database: High write volume required to log continuous GPS coordinates, route events, and historical delivery logs.
•	Users: Customers experience anxiety and higher support inquiries if delivery states (Dispatched, Out for Delivery, Delivered) are delayed or inaccurate.
•	System: Traditional polling mechanisms overload backend servers when handling thousands of active delivery tracking requests simultaneously.
Engineering Solutions (Tech Stack Used)
Component	Technology	Why
Courier & Tracking UI	React	Reusable component-based interface for courier dashboards and live customer tracking.
Backend API	Python + Django / REST API	Serves endpoints for managing orders, courier assignments, and delivery events.
Data Persistence	PostgreSQL	Reliably stores structured entities including orders, drivers, routes, and status history.
Location Services	Map / GPS Service	Supplies vehicle coordinates to update location markers on the interactive map UI.
Real-Time Updates	WebSockets	Pushes instant location and status alerts directly to customer interfaces without polling.
Customer Alerts	Notification Service	Sends critical state changes (e.g., 'Out for Delivery', 'Delivered') to mobile/email channels.
System Flow: Courier App GPS Ping → WebSockets / Django REST API → PostgreSQL Event Log → Route Engine Evaluation → Customer Tracking UI + Notification Service
References
•	OpenStreetMap Routing API Documentation
•	Google Maps Help - Traffic & Real-Time Tracking
Context and Constraints
Product stage: Design/case-study stage — system architecture and core routing algorithms defined; not yet deployed to production.
Constraints
•	Heuristic Accuracy: Heuristics (h) used in A* must remain optimistic/admissible to guarantee that pathfinding does not overlook optimal routes.
•	Cost Metric Normalization: Graph edge costs must combine distance and real-time travel time dynamically.
•	Network Limits: Frequent re-routing calls must be time-boxed or event-triggered to avoid server strain on the Route Engine.
•	Privacy & Scope: Real-world logistics public data does not reveal internal private architecture; design is modeled as an open engineering framework.
Assumptions
•	Delivery vehicles are equipped with GPS-enabled mobile apps capable of streaming coordinates.
•	External traffic APIs or historical speed data are accessible to update road edge weights.
•	Road networks can be mapped accurately into graph nodes and weighted edges.
Risks
•	Stale Traffic Data: Outdated traffic feeds may lead the algorithm to route vehicles into unexpected delays.
•	Frequent Re-routing Oscillations: Rapidly changing edge costs could cause the system to flip endlessly between two alternative routes.
•	Connection Dropouts: Lost mobile connection on courier devices will temporarily interrupt real-time tracking feeds.
Approach
Chosen approach: Dynamic Graph-Based Routing with Real-Time Traffic Ingestion
•	1. Graph Representation: Structure the road network into nodes (intersections/destinations) and edges (roads).
•	2. Algorithmic Route Calculation: Execute Dijkstra's algorithm for global minimum path evaluation or A* algorithm with distance heuristics for rapid target-focused routing.
•	3. Real-Time Data Ingestion: Collect vehicle coordinates and live traffic conditions via GPS and traffic APIs.
•	4. Dynamic Cost Adjustment: Convert dynamic traffic delays into updated edge weights.
•	5. Event-Driven Re-routing: Recalculate routes mid-transit if live edge weights make an alternative path significantly faster.
•	6. Full-Stack Event Pipeline: Stream progress updates through React UI, Django REST API, WebSockets, and PostgreSQL storage to inform both couriers and end customers in real time.
Alternative considered: A static map-based routing approach calculating paths strictly by geographical distance prior to dispatch. This was rejected because static paths ignore traffic jams and road delays, resulting in inaccurate ETA estimates, delivery delays, and higher fuel costs.
Evidence
•	https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
•	https://en.wikipedia.org/wiki/A*_search_algorithm
•	https://www.openstreetmap.org/
•	https://support.google.com/maps/
What Changed
•	Defined a two-fold engineering system: Dynamic Pathfinding (Dijkstra/A*) and Real-Time Event Tracking/Notification.
•	Established a scalable technology stack: React (UI), Django REST API (Backend), PostgreSQL (Persistence), WebSockets (Real-time events), and GPS/Traffic APIs (Routing inputs).
•	Shifted route evaluation from static distance metrics to dynamic travel-time cost models.
Result and Lessons
What improved: Established an integrated, end-to-end model connecting order assignment, pathfinding algorithms, live traffic feedback, and real-time customer transparency.
What did not work / open questions: No production benchmarks yet; testing is needed to determine the exact travel time delta threshold required before triggering automated mid-transit re-routing to prevent route bouncing.
What the team will do differently
•	Implement threshold checks (e.g., minimum 5-minute savings) before issuing mid-trip re-route commands.
•	Integrate open graph standards like OpenStreetMap early for consistent network modeling.
•	Build offline map caching into courier mobile applications to gracefully handle lost network connectivity.


