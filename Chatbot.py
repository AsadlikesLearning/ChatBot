import re
import random


class RuleBot:
    negative_responses = ("no", "nah", "nope", "not a chance", "sorry")
    exit_commands = ("exit", "quit", "goodbye", "bye")
    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "Are you someone from CodeAlpha?",
        "Are you a robot?",
        "Are you a human?",
        "Are you a machine?"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_codeAlpha_intent': r'.*codeAlpha.*'
        }

    def greet(self):
        self.name = input("What's your name?\n")
        will_help = input(
            f"Hi {self.name}, I am Asad's Bot, here to learn about your goals on Earth, will you help me?\n")
        if will_help.lower() in self.negative_responses:
            print("Ok, have a nice day. Why no help me, me sad.")
            return
        self.chat()

    def make_exit(self, reply):
        if reply.lower() in self.exit_commands:
            print("Ok, have a nice day. Why no help me, me sad.")
            return True
        return False

    def chat(self):
        print(random.choice(self.random_questions))
        while True:
            reply = input().lower()
            if self.make_exit(reply):
                break
            response = self.match_reply(reply)
            print(response)

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            if re.match(value, reply, re.IGNORECASE):
                if key == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif key == 'answer_why_intent':
                    return self.answer_why_intent()
                elif key == 'about_codeAlpha_intent':
                    return self.about_codeAlpha_intent()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "My planet is Uranus. 🌌",
            "I am from Uranus, the capital of Joe Mama. 😄"
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in hostility and to destroy you all! 😈",
            "I hear your momma is quite unique! 😂"
        )
        return random.choice(responses)

    def about_codeAlpha_intent(self):
        responses = (
            "CodeAlpha is a fantastic platform for learners to grow.",
            "I'm doing an internship at CodeAlpha, and it's been a great experience!"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Can you tell me more?",
            "I'm not sure I understand. Could you elaborate?",
            "I don't quite get that. Could you explain further?"
        )
        return random.choice(responses)


if __name__ == "__main__":
    AlienBot = RuleBot()
    AlienBot.greet()
