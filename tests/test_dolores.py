import dolores

# Arrange, Act, Assert

def test_dolores(api_key, engine):
  print("Testing Dolores Module ..")

  # Initialize dolores module
  dolores.initialize(api_key, engine)


  # Get module-scoped globals
  dolores_api_key, dolores_engine, dolores_headers = dolores.get_globals()

  # Assert
  assert(dolores_api_key == api_key)
  assert(dolores_engine == engine)
  # TODO: Assert header

  engines_json = dolores.list_engines()

  breakpoint()

  assert(any(engine.id == dolores_engine for engine in engines_json.data))

  # TODO: Call the rest

  pass





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