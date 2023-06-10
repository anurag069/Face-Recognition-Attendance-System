from chatbot import openai

# Set up the OpenAI API key
openai.api_key = "<your_api_key>"

# Define the prompt for the chatbot
prompt = "User: Hello, can you help me with my computer?\nAI:"

# Get the response from the chatbot
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.7,
)

# Print the chatbot's response
print(response.choices[0].text.strip())
