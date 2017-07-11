# AltmetricClient

Retrieves and parses information from https://www.altmetric.com.

Produced for a piece of research into the impact of Open Research on public policy.

##Pseudocode (for the minimal viable version)

1. Read in a set of DOIs [http://www.doi.org/](http://www.doi.org/) in a CSV
2. For each DOI.
    1. Call the Altmetric API
    2. Retrieve some JSON (Handle errors!)
    3. Write the JSON to a local object.
    4. Write out the fields we need (tbd) to another CSV
3. End

Use the issues list for ideas / requests for more features.

##Branches

To keep things simple, everything is being pushed to master until the first 'release'. Then once we're actually using the tool in anger, we'll branch to dev and then start adding new features to that.

##Dependencies

1. Tests are in [PyTest](https://docs.pytest.org/en/latest/).
2. REST / JSON handled using [requests](http://docs.python-requests.org/en/master/).
3. And we'll probably use the built-in [Python Config Parser](https://docs.python.org/3/library/configparser.html) to keep our Altmetrics key secret!

The code was written with PyCharm but we'll at least try to GitIgnore all the project management cruft. We also built this from the get-go with GitHub's default Python ignore file.