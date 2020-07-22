# Dolores 🤖⚡

Dolores is an python package that provides direct access to GPT-3 via dolores class instance. Instantiate dolores with your API key to create dolores with the proper configurations required to make requests to the OpenAI API.


## Installation (PyPi Package)
```
$ pip install dolores
```

## Usage
Either do so in the python interpreter or in a python file.

```
from dolores import Dolores

# dolores.initialize("<your_api_key_goes_here>", "<engine_name_goes_here>")
# dolores.initialize"<XXX-YYY-ZZZ>", "davinci")
```

From there you may not call openai's API directly via the accessible methods in the Dolores class instance. The following out call the list engines API call. Each API call has an associated method call that can be used to call the API.


### List Engines GET
Lists the currently available engines, and provides basic information about each option such as the owner and availability.
```
dolores.list_engines()
```

### Retrieve Engine GET
Retrieves an engine instance, providing basic information about the engine such as the owner and availability.
```
dolores.retrieve_engine()
```

### Changing Engines
After instantiating the Dolores class, subsequent class to the Open AI API will be made under the same engine selection. In order to change the engine used for the API call there is an exposed method.


```
dolores.set_engine("davinci")
```

Note: Validation against the existing engine types is in consideration for future versions.

### Create Completion POST (!important)
Create a completion. This is the main endpoint of the API. Returns new text as well as, if requested, the probabilities over each alternative token at each position.
```
# dolores.create_completion(prompt, max_tokens=5, temperature=1, top_p=1, n=1):
dolores.create_completion("Is the JavaScript programming language better than python?")
```

#### Request Payload Schema

| Name        	| In   	| Type              	| Required 	| Description                                                                                                                                                                                                                                                                                                	|
|-------------	|------	|-------------------	|----------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| engine      	| body 	| string            	| true     	| The engine ID                                                                                                                                                                                                                                                                                              	|
| prompt      	| body 	| (see description) 	| false    	| One or more prompts to generate from. Can be a string, list of strings, a list of integers (i.e. a single prompt encoded as tokens), or list of lists of integers (i.e. many prompts encoded as integers).                                                                                                 	|
| max_tokens  	| body 	| integer           	| false    	| How many tokens to complete to. Can return fewer if a stop sequence is hit.                                                                                                                                                                                                                                	|
| temperature 	| body 	| number            	| false    	| What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend using this or top_p but not both.                                                        	|
| top_p       	| body 	| number            	| false    	| An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend using this or temperature but not both. 	|
| n        	| body 	| integer                   	| false    	| How many choices to create for each prompt.                                                                                                                                                                                                                                                                   	|
| stream   	| body 	| boolean                   	| false    	| Whether to stream back partial progress. If set, tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message.                                                                                                                          	|
| logprobs 	| body 	| integer                   	| false    	| Include the log probabilites on the logprobs most likely tokens. So for example, if logprobs is 10, the API will return a list of the 10 most likely tokens. If logprobs is supplied, the API will always return the logprob of the sampled token, so there may be up to logprobs+1 elements in the response. 	|
| stop     	| body 	| string or list of strings 	| false    	| One or more sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.                                                                                                                                                                                	|


## Internal Contributor Notes (Dev Only)
### Testing
Using pytest to test the dolores module can be done by executing the following in the root of the project:
```
pytest tests/test_dolores.py --api_key "<api_key_goes_here" --engine "davinci"
```

### Generating Distribution Archives
In order to update the package, a new distribution must be made for the package. These are archives that are uploaded to the Package Index and can be installed by pip.

Make sure you have the latest versions of `setuptools` and `wheel` installed:

```
$ python3 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:

```
$ python3 setup.py sdist bdist_wheel
```

Note: Do not forget to update the version number in the setup.py file depending on the update.


### Uploading Distribution Archives to PyPi ([Link](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives]))

Make sure you have the latest `twine` package installed:
```
$ python3 -m pip install --user --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:
```
$ python3 -m twine upload --repository pypi dist/*
```
