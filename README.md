#Eco - track
# 🌱Eco Track

"EcoWaste" is a smart, lightweight web application designed to monitor, track, and manage campus waste while promoting sustainability through gamification.

## 🌿 About the Project

EcoWaste aims to empower campuses and students to measure their environmental impact. By collecting and analyzing data on recycling behavior and resource efficiency, this project aligns with modern smart-campus initiatives focused on sustainability, community engagement, and eco-friendly decision-making.

## 🚀 Features

* **Dashboard:** Real-time statistics tracking total points, waste tracked, campus ranking, and personal eco-contribution levels.
* **Waste Submission:** Upload photos or use live camera integration coupled with an intelligent waste type selector.
* **Smart Classification:** Backend-powered simulation that analyzes images and classifies waste categories automatically.
* **My Points:** Detailed breakdown of eco-points earned per individual waste type and category.
* **Live Leaderboard:** State-wise and campus-wide rankings of top eco-warriors.
* **Rewards System:** Redeem accumulated points for exciting perks like cafeteria discount vouchers, eco-friendly t-shirts, and movie tickets.
* **My Activity:** Complete, timestamped history of all past user waste submissions.
* **User Profile:** Personal stats, membership information, dorm block data, and overall environmental impact tracking.
* **Backend Architecture:** Powered by a Python backend (`main.py` and the `backend/` directory) to handle server logic, data routing, and point allocations.
* **Interactive Web Interface:** Clean and responsive single-file user interface (`frontend.html`) featuring live leaderboards, challenge dashboards, and a rewards store.


## 📂 Project Structure

```text
EcoWaste/
├── backend/
│   └── logic.py        # Backend processing, business logic, and in-memory DB
├── frontend.html       # Interactive frontend user interface
├── main.py             # Application entry point and server runner
└── README.md           # Project Documentation
