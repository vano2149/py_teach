"""
parrot.py file!
"""

prompt = "\n Tell me somthing, and I will repead it back to you: "
prompt += "\n Enter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)
    print(message)


