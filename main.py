from agent import agent

if __name__ == "__main__":
    while True:
        user_input = input("Ask the drone agent: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print(agent(user_input))