from googletrans import Translator
import random

translator = Translator()
def translate_to_korean(text):
    translation = translator.translate(text, dest='ko')
    return translation.text

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

first_message = """Hello, I am Marvin, the simple robot.
You can end this conversation at any time by typing '잘가'
After typing each answer, press 'enter'
How are you today?"""

first_message = translate_to_korean(first_message)
print(first_message)


while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input== "잘가":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = translate_to_korean(random.choices(random_responses)[0])
    print(response)

goodbye_message = "It was nice talking to you, goodbye!"
goodbye_message = translate_to_korean(goodbye_message)
print(goodbye_message)
