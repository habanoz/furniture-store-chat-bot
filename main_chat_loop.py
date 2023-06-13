from chat import Chat

def start_chat_loop():
    chat = Chat()
    message = input("Merhaba\n")

    while True:
        reply = chat.predict(message)
        input(reply)


if __name__ == '__main__':
    start_chat_loop()
