import ollama

MODEL = "llama3.2:1b"  # small model that runs on most computers

# This is your AI's personality. Change it however you like!
history = [
    {
        "role": "system",
        "content": "You are Matis, a friendly helper for my Scratch games "
                   "and drawing projects. Keep answers short and simple.",
    }
]

print("Chat with Matis! Type 'quit' to stop.")

while True:
    text = input("You: ")
    if text.lower() == "quit":
        break
    history.append({"role": "user", "content": text})
    reply = ollama.chat(model=MODEL, messages=history)
    answer = reply["message"]["content"]
    history.append({"role": "assistant", "content": answer})
    print("Matis:", answer)
