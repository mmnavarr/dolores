import dolores

# Arrange, Act, Assert

def test_dolores(api_key, engine):
  print("Testing Dolores Module ..")

  # Initialize dolores module
  dolores.initialize(api_key, engine)


  # Get module-scoped globals & validate them
  dolores_api_key, dolores_engine, dolores_headers = dolores.get_globals()
  assert(dolores_api_key == api_key)
  assert(dolores_engine == engine)
  assert(dolores_headers["Content-Type"] == "application/json")
  assert(dolores_headers["Authorization"] == f"Bearer {dolores_api_key}")


  # Make API to get list of engine
  engines_response = dolores.list_engines()

  # Assert current module engine exists in response
  assert(any(engine["id"] == dolores_engine for engine in engines_response["data"]))


  # Make API to set a new engine and subsequently retrieve the engine
  dolores_engine = "ada"
  dolores.set_engine(dolores_engine)
  engine_response = dolores.retrieve_engine()

   # Assert current module engine matches retrieved engine
  assert(engine_response["id"] == dolores_engine)


  # Make API to complete test prompt
  completion_response = dolores.create_completion("Once upon a time", 5, 1, 1, 1)
  assert(type(completion_response) is dict)
  assert(type(completion_response["id"]) is str)
  assert(type(completion_response["choices"]) is list)
  assert(type(completion_response["choices"][0]["text"]) is str)