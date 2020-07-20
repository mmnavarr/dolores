# Import dolors classes from package
from dolores import Dolores


def test_dolores():
  # TODO: Create an object of Mammals class & call a method of it
  dolores = Dolores("API_KEY_GOES_HERE", "davinci")

  # Call the GPT-3 API
  dolores.list_engines()

  # TODO: Call the rest

  pass