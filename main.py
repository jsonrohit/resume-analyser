import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI()

url = "https://example.com"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

text = soup.get_text(" ", strip=True)

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {
            "role": "system",
            "content": "Extract structured information from webpages."
        },
        {
            "role": "user",
            "content": f"""
Extract the following information from this webpage:

- title
- company
- location
- salary
- experience

Return JSON only.

WEBPAGE:
{text}
"""
        }
    ]
)

print(response.choices[0].message.content)