from email.message import Message


def parse_header(line):
    message = Message()
    message['content-type'] = line
    main_value = message.get_content_type()
    params = {}

    for key, value in message.get_params()[1:]:
        params[key] = value

    return main_value, params
