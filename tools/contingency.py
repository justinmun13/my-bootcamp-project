def recommend_action(status: str) -> str:
    if status == "Battery low":
        return "Return to base immediately."
    if status == "Motor overheating":
        return "Land immediately and inspect motors."
    if status == "High wind detected":
        return "Descend to lower altitude and return to base."
    if status == "Obstacle very close":
        return "Stop and hover. Await manual control."
    if status == "Weak GPS signal":
        return "Ascend to improve signal or return to last known safe location."
    if status == "Flight time exceeded safe limit":
        return "Return to base to avoid battery depletion."
    return "Continue mission."