#Eco - track
# 🌱Eco Track

"Ecotrack" is a smart, lightweight web application designed to monitor, track, and manage campus waste while promoting sustainability through gamification.

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
## 🔄 System Architecture & Working Flow

EcoTrack operates on a modern client-server architecture, connecting a responsive single-page frontend interface with a high-performance FastAPI Python backend. 

### 1. Initialization & Data Synchronization (GET Flow)
* *Application Load:* When the user opens the application (frontend_CAMERA_FIXED.html), the client triggers an asynchronous window.onload script[span_0](start_span)[span_0](end_span).
* *API Requests:* JavaScript fires parallel fetch() requests to FastAPI backend endpoints (/dashboard/{username}, /leaderboard, /rewards/{username}, and /waste-categories)[span_1](start_span)[span_1](end_span).
* *UI Hydration:* The backend queries its in-memory data structures, returns the payload in JSON format, and dynamically populates the user dashboard, metrics, and state-wise leaderboard[span_2](start_span)[span_2](end_span).

### 2. Live Media Capture & Processing Flow
* *Camera Access:* Users can capture waste items in real-time by activating the browser's native navigator.mediaDevices.getUserMedia API, which streams the feed into an HTML5 <video> element[span_3](start_span)[span_3](end_span).
* *Snapshot Conversion:* Upon clicking "Capture Photo", an invisible HTML5 <canvas> element captures the current video frame and converts it into a compressed JPEG image Blob[span_4](start_span)[span_4](end_span).

### 3. Submission & Smart Classification (POST Flow)
* *Payload Packaging:* The frontend packages the captured image Blob (or an uploaded file) along with metadata (student_name, state, and wasteTypeSelect) into a multipart FormData object[span_5](start_span)[span_5](end_span).
* *Server-Side Routing:* The data is sent via a POST request to the FastAPI /predict endpoint[span_6](start_span)[span_6](end_span).
* *Classification Logic:* The backend reads the incoming filename, categorizes the waste item (e.g., Plastic, Paper, E-Waste, Biodegradable), and calculates corresponding eco-points (ranging from 5 to 50 points).

### 4. Real-Time State Update & Logging
* *Score Increment:* The backend automatically updates the specific user's total score (total_points) and dynamically adjusts their rank on the leaderboard.
* *Activity Tracking:* The action is logged into the user's personal ACTIVITY_LOG array with a timestamp[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span).
* *UI Refresh:* FastAPI returns a success confirmation JSON response, instantly triggering frontend functions (loadDashboard() and loadActivity()) to reflect the updated points and stats live on the dashboard[span_9](start_span)[span_9](end_span).
*

## 📂 Project Structure

```text
EcoWaste/
├── backend/
│   └── logic.py        # Backend processing, business logic, and in-memory DB
├── frontend.html       # Interactive frontend user interface
├── main.py             # Application entry point and server runner
└── README.md           # Project Documentation
