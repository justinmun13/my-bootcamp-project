from tools.telemetry import analyze_telemetry
from tools.contingency import recommend_action

def agent(query: str) -> str:
    # Simulated telemetry data
    telemetry = {
        "battery": 15,         # percent
        "motor_temp": 85,      # Celsius
        "altitude": 120,       # meters
        "gps": "37.7749,-122.4194"
    }
    if "analyze" in query:
        status = analyze_telemetry(telemetry)
        return f"Status: {status}"
    elif "recommend" in query:
        status = analyze_telemetry(telemetry)
        action = recommend_action(status)
        return f"Status: {status}\nRecommended Action: {action}"
    else:
        return "Try 'analyze telemetry' or 'recommend action'."