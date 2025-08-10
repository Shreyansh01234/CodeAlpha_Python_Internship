# ----- Basic Chatbot -----
# Developed by: <Shreyansh pandey>
# Internship Project: CodeAlpha
# This is a simple rule-based chatbot that replies to user messages.

def show_intro():
    print("\n🤖 ChatBot Activated!")
    print("Type something and I'll try to reply. Type 'bye' to exit.\n")

def get_bot_reply(user_message):
    """Return chatbot's reply based on user input."""
    message = user_message.lower()

    if message in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif "your name" in message:
        return "I'm CodeAlphaBot, created for my internship project."
    elif "bye" in message:
        return "Goodbye! Have a great day."
    else:
        return "Hmm, I don't have a reply for that yet."

def run_chatbot():
    show_intro()
    while True:
        user_input = input("You: ").strip()
        reply = get_bot_reply(user_input)
        print("Bot:", reply)

        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    run_chatbot()
