import random

greetings = ["hi", "hello", "hey"]
greeting_responses = [
    "Hello there!",
    "Hi! Nice to meet you.",
    "Hey! How can I help you?"
]

how_are_you_inputs = ["how are you", "how are you doing"]
how_are_you_responses = [
    "I'm fine, thanks!",
    "Doing great! What about you?",
    "I'm just a bot, but I'm feeling awesome!"
]

thanks_inputs = ["thanks", "thank you"]
thanks_responses = [
    "You're welcome!",
    "No problem!",
    "Glad I could help!"
]

def show_help():
    print("\nYou can try typing:")
    print("- hello")
    print("- how are you")
    print("- thanks")
    print("- bye")
    print("- help\n")

def chatbot():
    print("===================================")
    print("      🤖 Welcome to Chatbot       ")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit the chatbot.")
    print("===================================\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in greetings:
            print("Chatbot:", random.choice(greeting_responses))

        elif user_input in how_are_you_inputs:
            print("Chatbot:", random.choice(how_are_you_responses))

        elif user_input in thanks_inputs:
            print("Chatbot:", random.choice(thanks_responses))

        elif user_input == "help":
            show_help()

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break

        elif user_input == "":
            print("Chatbot: Please type something.")

        else:
            print("Chatbot: Sorry, I don't understand that.")
            print("Chatbot: Type 'help' to see what I can understand.")

chatbot()
