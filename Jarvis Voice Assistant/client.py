from openai import OpenAI


# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="Your OpenAI API key"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in professional tasks like Alexa and Google"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)