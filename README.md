# HW Week 2: Building an AI Agent with 2 Tools

This project is for Bootcamp Week 2. It demonstrates a simple AI agent that analyzes drone telemetry and recommends safe contingency or maintenance actions in real-time.

## Features

- **Telemetry Analyzer Tool:** Checks drone telemetry data (battery, motor temperature, wind speed, obstacle distance, GPS signal, flight time, etc.) and reports system status.
- **Contingency Recommender Tool:** Suggests safe actions based on the analyzed status (e.g., return to base, land immediately, continue mission).

## How to Use

1. Clone the repository or download the code.
2. Make sure you have Python 3 installed.
3. In your terminal, navigate to the project directory:
   ```
   cd my-project
   ```
4. Run the agent:
   ```
   python main.py
   ```
5. When prompted, type:
   - `analyze telemetry` to get a status report.
   - `recommend action` to get a status and a recommended action.
   - `exit` or `quit` to stop the program.

## Project Structure

C:\Users\Justin\my-project
│
├── main.py
├── agent.py
├── .gitignore
├── README.md
└── tools\
    ├── __init__.py
    ├── telemetry.py
    └── contingency.py

## Example
Ask the drone agent: analyze telemetry
Status: Battery low
Ask the drone agent: recommend action
Status: Battery low
Recommended Action: Return to base immediately.

## Notes

- The telemetry data is currently simulated in the code. You can expand it to accept user input or real drone data.
- Do **not** commit your `.env` file or any secrets to the repository.

---

Feel free to expand this README with more details about your logic, scenarios, or anything else you want to highlight!