from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from datetime import datetime, timedelta
import random

app = FastAPI(title="EcoWaste Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data store
USERS = {
    "hero": {
        "name": "Hero",
        "email": "hero@campus.edu",
        "state": "Karnataka",
        "total_points": 250,
        "rank": 5,
        "eco_contribution": "Good",
        "avatar": "🧑‍🎓",
        "joined": "2026-08-15"
    },
    "rahul": {
        "name": "Rahul",
        "email": "rahul@campus.edu",
        "state": "Karnataka",
        "total_points": 2450,
        "rank": 1,
        "eco_contribution": "Excellent",
        "avatar": "🧑‍💼",
        "joined": "2026-07-01"
    },
    "priya": {
        "name": "Priya",
        "email": "priya@campus.edu",
        "state": "Maharashtra",
        "total_points": 2180,
        "rank": 2,
        "eco_contribution": "Excellent",
        "avatar": "👩‍🎓",
        "joined": "2026-07-10"
    },
    "amit": {
        "name": "Amit",
        "email": "amit@campus.edu",
        "state": "Gujarat",
        "total_points": 1850,
        "rank": 3,
        "eco_contribution": "Very Good",
        "avatar": "🧑‍💻",
        "joined": "2026-07-20"
    },
    "sneha": {
        "name": "Sneha",
        "email": "sneha@campus.edu",
        "state": "Delhi",
        "total_points": 1720,
        "rank": 4,
        "eco_contribution": "Very Good",
        "avatar": "👩‍🔬",
        "joined": "2026-08-01"
    }
}

WASTE_CATEGORIES = {
    "biodegradable": {"name": "Biodegradable", "desc": "Food & organic waste", "points": 15, "icon": "🌱"},
    "plastic": {"name": "Plastic", "desc": "Plastic bottles & items", "points": 10, "icon": "🧴"},
    "paper": {"name": "Paper", "desc": "Paper & cardboard", "points": 5, "icon": "📄"},
    "ewaste": {"name": "E-Waste", "desc": "Electronic waste", "points": 50, "icon": "♻️"}
}

LEADERBOARD = [
    {"rank": 1, "name": "Rahul", "title": "Eco Champion", "points": 2450, "state": "Karnataka"},
    {"rank": 2, "name": "Priya", "title": "Green Warrior", "points": 2180, "state": "Maharashtra"},
    {"rank": 3, "name": "Amit", "title": "Eco Warrior", "points": 1850, "state": "Gujarat"},
    {"rank": 4, "name": "Sneha", "title": "Green Hero", "points": 1720, "state": "Delhi"},
    {"rank": 5, "name": "You", "title": "Keep going!", "points": 250, "state": "Karnataka"}
]

ACTIVITY_LOG = {
    "hero": [
        {"date": "2026-09-28", "action": "Scanned plastic bottle", "points": "+10", "category": "plastic"},
        {"date": "2026-09-27", "action": "Submitted paper", "points": "+5", "category": "paper"},
        {"date": "2026-09-26", "action": "Submitted e-waste", "points": "+50", "category": "ewaste"},
        {"date": "2026-09-25", "action": "Scanned food waste", "points": "+15", "category": "biodegradable"},
    ]
}

REWARDS = [
    {"id": 1, "name": "Campus Cafe Voucher", "points": 200, "desc": "$5 off your next meal", "redeemed": False},
    {"id": 2, "name": "Eco T-Shirt", "points": 500, "desc": "Limited edition green tee", "redeemed": False},
    {"id": 3, "name": "Reusable Bottle", "points": 150, "desc": "Stainless steel water bottle", "redeemed": True},
    {"id": 4, "name": "Movie Ticket", "points": 300, "desc": "Free campus theater ticket", "redeemed": False},
]

@app.get("/")
def home():
    return {"status": "Active", "system": "EcoWaste Backend"}

@app.get("/user/{username}")
def get_user(username: str):
    user = USERS.get(username.lower())
    if not user:
        return {"error": "User not found"}, 404
    return {"status": "success", "user": user}

@app.get("/profile/{username}")
def get_profile(username: str):
    user = USERS.get(username.lower())
    if not user:
        return {"error": "User not found"}, 404
    return {
        "status": "success",
        "profile": {
            **user,
            "stats": {
                "items_scanned": random.randint(10, 100),
                "co2_saved": round(random.uniform(5, 50), 1),
                "total_waste_kg": random.randint(20, 200)
            }
        }
    }

@app.get("/stats")
def get_stats():
    return {
        "status": "success",
        "metrics": {
            "total_items_scanned": 142,
            "total_eco_points_awarded": 1280,
            "co2_saved_kg": 45.5,
            "total_waste_kg": 320.5
        },
        "waste_breakdown": {
            "biodegradable": 45,
            "plastic": 52,
            "paper": 30,
            "ewaste": 15
        }
    }

@app.get("/leaderboard")
def get_leaderboard():
    return {"status": "success", "leaderboard": LEADERBOARD}

@app.get("/waste-categories")
def get_waste_categories():
    return {"status": "success", "categories": WASTE_CATEGORIES}

@app.get("/rewards/{username}")
def get_rewards(username: str):
    return {"status": "success", "rewards": REWARDS}

@app.post("/redeem-reward/{username}/{reward_id}")
def redeem_reward(username: str, reward_id: int):
    for reward in REWARDS:
        if reward["id"] == reward_id:
            reward["redeemed"] = True
            return {"status": "success", "message": f"Reward {reward['name']} redeemed!"}
    return {"status": "error", "message": "Reward not found"}, 404

@app.get("/activity/{username}")
def get_activity(username: str):
    activity = ACTIVITY_LOG.get(username.lower(), [])
    return {"status": "success", "activity": activity}

@app.post("/predict")
async def predict_waste(
    file: UploadFile = File(...),
    student_name: Optional[str] = Form("hero"),
    state: Optional[str] = Form("Karnataka"),
):
    filename = (file.filename or "").lower()

    if "plastic" in filename or "bottle" in filename or "cup" in filename:
        category = "plastic"
        eco_points = 10
    elif "paper" in filename or "book" in filename or "cardboard" in filename:
        category = "paper"
        eco_points = 5
    elif "battery" in filename or "circuit" in filename or "wire" in filename or "ewaste" in filename:
        category = "ewaste"
        eco_points = 50
    elif "biodegradable" in filename or "food" in filename or "organic" in filename:
        category = "biodegradable"
        eco_points = 15
    else:
        category = "plastic"
        eco_points = 10

    # Update user points
    username = student_name.lower().replace(" ", "")
    if username not in USERS:
        USERS[username] = {
            "name": student_name,
            "email": f"{username}@campus.edu",
            "state": state,
            "total_points": 0,
            "rank": len(USERS) + 1,
            "eco_contribution": "Good",
            "avatar": "🧑‍🎓",
            "joined": datetime.now().strftime("%Y-%m-%d")
        }
    
    USERS[username]["total_points"] += eco_points

    # Log activity
    if username not in ACTIVITY_LOG:
        ACTIVITY_LOG[username] = []
    
    waste_info = WASTE_CATEGORIES.get(category, {})
    ACTIVITY_LOG[username].insert(0, {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "action": f"Submitted {waste_info.get('name', 'waste')}",
        "points": f"+{eco_points}",
        "category": category
    })

    return {
        "status": "success",
        "waste_category": WASTE_CATEGORIES[category]["name"],
        "eco_reward_points": eco_points,
        "message": f"Great! {student_name} earned +{eco_points} points!"
    }

@app.get("/dashboard/{username}")
def get_dashboard(username: str):
    user = USERS.get(username.lower())
    if not user:
        return {"error": "User not found"}, 404
    
    return {
        "status": "success",
        "dashboard": {
            "user": user,
            "waste_categories": WASTE_CATEGORIES,
            "top_contributors": LEADERBOARD[:5],
            "stats": {
                "items_scanned": user["total_points"] // 10,
                "total_waste_kg": user["total_points"] // 5,
                "leaderboard_rank": user["rank"],
                "eco_contribution": user["eco_contribution"]
            }
        }
    }
