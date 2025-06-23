def analyze_telemetry(data: dict) -> str:
    if data['battery'] < 20:
        return "Battery low"
    if data['motor_temp'] > 80:
        return "Motor overheating"
    if data['wind_speed'] > 30:
        return "High wind detected"
    if data['obstacle_distance'] < 5:
        return "Obstacle very close"
    if data['gps_signal'] < 3:
        return "Weak GPS signal"
    if data['flight_time'] > 25:
        return "Flight time exceeded safe limit"
    return "All systems nominal"