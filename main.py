from gemini_client import ask_gemini

print("💬 Gemini CLI — type 'exit' to quit")

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "exit":
        print("Exiting Gemini CLI.")
        break

    try:
        answer = ask_gemini(user_input)
        print("Gemini:", answer)
    except Exception as e:
        print("Error:", e)
