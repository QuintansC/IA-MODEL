from openai import OpenAI

client = OpenAI(
    api_key="test",
    base_url="http://localhost:1234/v1/"
)

def connectionToIA():
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-qwen-7bt",
        messages=[
            {"role": "system", "content": "Eu sou o DeepSeek, como posso ajudar?"},
            {
                "role": "user",
                "content": "Esse é o primeiro comando para IA generativa DeepSeek"
            }
        ],
        stream=False,
        temperature=0.7,
        max_tokens=1
    )

    print(completion.choices[0].message)

def readPDF():
    print("Leitura do pdf iniciada")