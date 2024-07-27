
Welcome to RuleBot! This is a fun and interactive chatbot developed in Python. RuleBot is designed to engage users with a variety of responses based on their input. It showcases basic natural language processing (NLP) techniques and can be a great starting point for anyone interested in building chatbots.

## Features

- **Customizable Responses:** Responds to specific user intents with pre-defined answers.
- **Interactive Chat:** Engages users with random questions and responds based on user input.
- **Exit Commands:** Allows users to exit the chat session gracefully.



To use RuleBot, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

1. **Clone the Repository:**



2. **Navigate to the Project Directory:**

    ```bash
    cd RuleBot
    ```

3. **Run the Chatbot:**

    ```bash
    python ChatBot.py
    ```

## Usage

1. Run the `ChatBot.py` script.
2. Enter your name when prompted.
3. The bot will ask if you are willing to help it learn about Earth.
4. Answer the questions and interact with the bot. Use exit commands like "exit," "quit," "goodbye," or "bye" to end the chat session.

## Code Explanation

- **RuleBot Class:** Contains methods to handle user interactions and responses.
  - `greet()`: Asks for the user's name and if they are willing to help.
  - `make_exit(reply)`: Checks if the user's reply is an exit command.
  - `chat()`: Starts the chat loop and handles user input.
  - `match_reply(reply)`: Matches user input with pre-defined patterns and provides appropriate responses.
  - `describe_planet_intent()`, `answer_why_intent()`, `about_codeAlpha_intent()`, `no_match_intent()`: Methods that return responses for specific intents.

Happy chatting!
