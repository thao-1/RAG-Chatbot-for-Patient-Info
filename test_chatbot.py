from chatbot import MedicalChatbot

def test_chatbot():
    try:
        bot = MedicalChatbot()
        response = bot.ask("What are common side effects of ibuprofen?")
        print("Test response:", response["answer"])
        print("Sources:", response["sources"])
        return True
    except Exception as e:
        print(f"Error testing chatbot: {e}")
        return False

if __name__ == "__main__":
    print("Testing chatbot...")
    success = test_chatbot()
    print(f"Test {'succeeded' if success else 'failed'}")