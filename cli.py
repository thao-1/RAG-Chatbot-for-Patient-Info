import argparse
from chatbot import MedicalChatbot

def main():
    parser = argparse.ArgumentParser(description="Medical Chatbot CLI")
    parser.add_argument("--question", "-q", type=str, help="Question to ask the chatbot")
    args = parser.parse_args()
    
    bot = MedicalChatbot()
    
    if args.question:
        response = bot.ask(args.question)
        print(f"Answer: {response['answer']}\n")
        print(f"Sources: {', '.join(response['sources'])}")
    else:
        print("Interactive mode. Type 'exit' to quit.")
        while True:
            question = input("\nQuestion: ")
            if question.lower() in ["exit", "quit", "q"]:
                break
            response = bot.ask(question)
            print(f"Answer: {response['answer']}\n")
            print(f"Sources: {', '.join(response['sources'])}")

if __name__ == "__main__":
    main()