import openai

openai.api_key = 'sk-proj-amPMC8Hap-tr-UxBhmLUiLER9K7yTyhnGT48C9nvmUpMI4M-mKUsqDKPF1sF_e4TkDFr94WaEsT3BlbkFJYZv0iLhqMhTwGJmWx6aipNetSm6_-pdPoj_MMvgcOtuptlkUF7Fd5uLHa_nB-AG_BTFk-aRP8AH'

def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    response = openai.ChatCompletion.create(
        messages=[message],
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_gpt_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
