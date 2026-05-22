from agent import SportsAgent

def main():
    agent = SportsAgent()
    print("Welcome to the Sports AI Agent. Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter a football team name: ").strip()
        
        if user_input.lower() == 'exit':
            break
            
        if user_input:
            result = agent.run(user_input)
            print(result)

if __name__ == "__main__":
    main()