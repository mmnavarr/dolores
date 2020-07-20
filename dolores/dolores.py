import json
import requests

# Dolores - abstraction layer over openai's API
class Dolores:

  # Constructor
  def __init__(self, api_key, engine="davinci"):
    self.engine = engine
    self.headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
      }

  # Change engine setting
  def set_engine(self, engine):
    self.engine = engine

  # List Engines GET
  # Lists the currently available engines, and provides basic information about each option such as the owner and availability.
  def list_engines(self):
    url = "https://api.openai.com/v1/engines"
    response = requests.get(url, headers=self.headers)

    return response.text

  # Retrieve Engine GET
  # Retrieves an engine instance, providing basic information about the engine such as the owner and availability.
  def retrieve_engine(self):
    url = f"https://api.openai.com/v1/engines/{self.engine}"
    response = requests.get(url, headers=self.headers)

    return response.text

  # Create Completion POST
  # Create a completion. This is the main endpoint of the API.
  # Returns new text as well as, if requested, the probabilities over each alternative token at each position.
  def create_completion(self, payload):
    url = f"https://api.openai.com/v1/engines/{self.engine}/completions"
    response = requests.post(url, headers=self.headers, data=payload)

    return response.text

  # Search POST
  # Perform a semantic search over a list of documents.
  def search(self, payload):
    url = f"https://api.openai.com/v1/engines/{self.engine}/search"
    response = requests.post(url, headers=self.headers, data=str(payload))

    return response.text

  # Test function to confirm it works
  def test_create_completion(self):
    payload = {
      "prompt": "Once upon a time",
      "max_tokens": 5,
      "temperature": 1,
      "top_p": 1,
      "n": 1
    }

    self.create_completion(payload)



"""
Example completion request payload
{
  "prompt": "Once upon a time",
  "max_tokens": 5,
  "temperature": 1,
  "top_p": 1,
  "n": 1,
  "stream": false,
  "logprobs": null,
  "stop": "\n"
}
"""