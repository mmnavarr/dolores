import json
import requests

# #                                             #   #
#   Dolores - abstraction module over openai's API  #
# #                                             #   #


# Defile module-scoped variables
engine = ""
api_key = ""
headers = {}


# Initialize module
def initialize(_api_key, _engine="davinci"):
  global api_key, engine, headers

  if _api_key:
    api_key = _api_key
    engine = _engine
  else:
    print("No API Key provided. Initialization failed.")
    return

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {_api_key}"
  }

# Get module-scoped values
def get_globals():
  global api_key, engine, headers

  return api_key, engine, headers

# Change engine setting
def set_engine(_engine):
  global engine
  engine = _engine

# List Engines GET
# Lists the currently available engines, and provides basic information about each option such as the owner and availability.
def list_engines():
  global headers

  url = "https://api.openai.com/v1/engines"
  response = requests.get(url, headers=headers)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()

# Retrieve Engine GET
# Retrieves an engine instance, providing basic information about the engine such as the owner and availability.
def retrieve_engine():
  global engine, headers

  url = f"https://api.openai.com/v1/engines/{engine}"
  response = requests.get(url, headers=headers)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()

# Create Completion POST
# Returns new text as well as, if requested, the probabilities over each alternative token at each position.
def create_completion(prompt, max_tokens=5, temperature=1, top_p=1, n=1):
  global engine, headers

  # Create payload for API Request
  payload = {
    "prompt": prompt,
    "max_tokens": max_tokens,
    "temperature": temperature,
    "top_p": top_p,
    "n": n
  }

  url = f"https://api.openai.com/v1/engines/{engine}/completions"
  response = requests.post(url, headers=headers, json=payload)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()

# Search POST
# Perform a semantic search over a list of documents.
def search(payload):
  global engine, headers

  url = f"https://api.openai.com/v1/engines/{engine}/search"
  response = requests.post(url, headers=headers, json=payload)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()
