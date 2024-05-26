def get_int(message):
    if message.isdigit():
        message = int(message)
        return message
    else:
        print("Not Digit")