from openai import OpenAI
from prompt.settings import Api_key

client = OpenAI(api_key=Api_key)

# Set your OpenAI API key

def summarize_topic(topic):
    """Summarize a given topic."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes topics for study purposes."},
        {"role": "user", "content": f"Summarize the following topic in concise points: {topic}"}
    ]

    response = client.chat.completions.create(model="gpt-3.5-turbo",  # or "gpt-4" if available
    messages=messages,
    max_tokens=100)

    summary = response.choices[0].message.content.strip()
    return summary

def generate_questions(topic):
    """Generate practice questions for a given topic."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates multiple choice questions."},
        {"role": "user", "content": f"Generate five multiple choice questions for the following topic: {topic}"}
    ]

    response = client.chat.completions.create(model="gpt-4",  # or "gpt-3.5-turbo"
    messages=messages,
    max_tokens=200)

    questions = response.choices[0].message.content.strip()
    return questions

# def main():
#     print("Welcome to the AI-Powered Study Buddy!")

#     while True:
#         print("\nChoose an option:")
#         print("1. Summarize a topic")
#         print("2. Generate practice questions")
#         print("3. Exit")
#         choice = input("Enter your choice (1/2/3): ")

#         if choice == "1":
#             topic = input("\nEnter the topic you want to summarize: ")
#             summary = summarize_topic(topic)
#             print("\nSummary of the topic:")
#             print(summary)

#         elif choice == "2":
#             topic = input("\nEnter the topic you want practice questions for: ")
#             questions = generate_questions(topic)
#             print("\nGenerated Questions:")
#             print(questions)

#         elif choice == "3":
#             print("\nExiting the AI-Powered Study Buddy. Happy studying!")
#             break

#         else:
#             print("\nInvalid choice. Please choose again.")

# if _name_ == "_main_":
#     main()