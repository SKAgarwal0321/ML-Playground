resp = {
    "hellow": "Hi there, how are you",
    "how are you" : "I'm just a bot, but I'm doing great!",
    "bye" : "Good bye, Have a nice day"
}

while True:
    user_input = input("You: ")
    if user_input=="bye":
        print("bot: Good bye, Have a nice day")
        break