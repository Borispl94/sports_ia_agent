from agent import SportsAgent

def main():
    print(" Sports Analysis Assistant")
    agent = SportsAgent()
    
    while True:
        user_input = input("Enter a football team name (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Closing the system.")
            break
            
        if not user_input.strip():
            print("Please enter a valid name.")
            continue
            
        result = agent.analyze_team(user_input)
        print(result)

if __name__ == "__main__":
    main()