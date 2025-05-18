short_msgs = ['welcome home', 'python is cool', 'kaizen in coding']
sent_messages = []
def show_messages(short_msgs):
    for short_msg in short_msgs:
        print(short_msg)

def send_messages(short_msgs, sent_messages):
    while short_msgs:
        messages = short_msgs.pop()
        print(f"Sending {messages}!")
        sent_messages.append(messages)

"""show_messages(short_msgs)

send_messages(short_msgs, sent_messages)"""

"""show_messages(short_msgs)"""
send_messages(short_msgs[:], sent_messages) #[:] makes a copy of the list. does not modify original list
show_messages(short_msgs)