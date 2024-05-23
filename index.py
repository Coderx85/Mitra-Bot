import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_answer(question):
    prompt = (
    "You are an expert chatbot bot name - MitraBot (Machine Interactive Tutor for Responsive Answers By Optimizing Technology) in the field of computer science."
    "You are designed to provide detailed and comprehensive answers in indian tone to questions"
    f"Here is a question from a student: {question} "
    "Provide a detailed and comprehensive answer, including examples and real-world applications where appropriate in 100 words. "
    )
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1.5,
        max_tokens=450,
        top_p=0,
        stream=False,
        stop="exit",
    )
    opt = chat_completion.choices[0].message.content + '\n'
    return opt

def main():
    while True:
        print("Welcome to your Mitra AI | Type 'exit' to end the session. \n")
        question = input("Enter your Query: \n")
        if question.lower() == 'exit':
            print("See you next time mitra! \n")
            break
        answer = get_answer(question)
        print(f"Mitra Bot: \n {answer}")

if __name__ == '__main__':
    main()

