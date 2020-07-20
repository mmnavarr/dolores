# Dolores

## Dolores is an python package that provides direct access to GPT-3 via dolores class instance. Instantiate dolores with your API key to create dolores with the proper configurations required to make requests to the OpenAI API.


## Prerequisites for Running Locally
```
$ pip install json
```
```
$ pip install requests
```

## How to run the package locally


Open up the python interpreter in the root of the project and execute the following:

```
$ from dolores import Dolores
$ dolores = Dolores("<your_api_key_goes_here>", "<open_ai_engine_goes_here>")
```

From there you may not call openai's API directly via the accessible methods in the Dolores class instance. The following out call the list engines API call. Each API call has an associated method call that can be used to call the API.

```
dolores.list_engines()
```


## Changing Engines
After instantiating the Dolores class, subsequent class to the Open AI API will be made under the same engine selection. In order to change the engine used for the API call there is an exposed method.

```
dolores.set_engine("<new_engine_type>")
```

Note: Validation against the existing engine types is in consideration for future versions.

## Internal Contributor Notes (Dev Only)
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

This command should output a lot of text and once completed should generate two files in the dist directory:

```
dist/
    dolores-0.1.0-py3-none-any.whl
    dolores-0.1.0.tar.gz
```

Note: Do not forget to update the version number in the setup.py file depending on the update.

### Uploading Distribution Archives to PyPi ([Link](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives]))
