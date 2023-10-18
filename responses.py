def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "Life is cat!"

    if "x.com" in p_message:
        link_suffix = p_message[13:]
        return "https://vxtwitter.com" + link_suffix


    return None