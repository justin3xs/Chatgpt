from openai import OpenAI
client = OpenAI(api_key="sk-proj-LRONcgBoEz7DthHFty3AT3BlbkFJoV0Jr1QkOjxHQVE7FHg4")
class ChatGPT:

    def __init__(self, api_key = "sk-proj-LRONcgBoEz7DthHFty3AT3BlbkFJoV0Jr1QkOjxHQVE7FHg4"):
        self.openai = client
        self.openai.api_key = api_key
        self.messages = []

    def send_request(self, prompt, max_tokens=1000, temperature=1.00):
        try:
            self.messages.append({'role': 'user', 'content': prompt})
            print("bad")

            response = self.openai.chat.completions.create(
                model='gpt-4o',
                max_tokens=max_tokens,
                temperature=temperature,
                messages=self.messages
            )
            print("bad")
            self.messages.append({'role': 'assistant', 'content': response.choices[0].message.content})
            return {'usage': response['usage']['total_tokens'], 'content': response.choices[0].message.content}
        except Exception as e:
            print("we got a problem")
            return {'error': str(e)}