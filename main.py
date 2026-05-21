from agent import SportsAgent

def main():
    print("\n" + "*"*40)
    print("* SPORTS ANALYSIS ASSISTANT       *")
    print("*"*40 + "\n")
    
    agent = SportsAgent()
    
    while True:
        print("-" * 40)
        user_input = input("Enter a football team name (or type 'exit'): ")
        
        if user_input.lower() == 'exit':
            print("\nShutting down the AI Agent. Goodbye!")
            break
            
        if not user_input.strip():
            print("Invalid input. Please enter a valid team name.")
            continue
            
        result = agent.analyze_team(user_input)
        print(result)

if __name__ == "__main__":
    main()