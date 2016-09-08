from unicodedata import east_asian_width

from slackbot.bot import respond_to


def _message_length(message):
    """
    メッセージの長さを返す
    """
    length = 0
    for char in message:
        width = east_asian_width(char)
        if width == 'W':
            length += 2
        elif width == 'Na':
            length += 1

    return length

@respond_to('^suddendeath$')
@respond_to('^suddendeath\s+(.*)')
def suddendeath(message, words='突然の死'):
    """
    突然の死のメッセージを返す
    """
    if words == 'help':
        return

    length = _message_length(words)

    header = '＿' + '人' * (length // 2 + 2) + '＿'
    footer = '￣' + 'Y^' * (length // 2) + 'Y￣'
    middle = "＞　" + words + "　＜"

    message.send("\n".join([header, middle, footer]))

@respond_to('^suddendeath\s+help')
def suddendeath_help(message):
    message.send('''- `$suddendeath`: 突然の死のメッセージを返す
- `$suddendeath words`: words を使って突然の死のメッセージを返す
''')
