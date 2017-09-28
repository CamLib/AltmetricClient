# AltmetricClient

Retrieves and parses information from https://www.altmetric.com.

Produced for a piece of research into the impact of Open Research on public policy.

## Pseudocode (for the minimal viable version)

1. Read in a set of DOIs [http://www.doi.org/](http://www.doi.org/) in a CSV
2. For each DOI.
    1. Call the Altmetric API
    2. Retrieve some JSON (Handle errors!)
    3. Write the JSON to a local object.
    4. Write out the fields we need into three lists:
        1. The master list containing core Altmetric data such as citation info, counts and demographics.
        2. A 'mentions' list.
        3. An 'authors' list (which will have a composite key of doc DOI with author id of some sort - details to be sorted out as and when).
3. End

N.b.: Altmetric's terminology feels a bit twisted... Blog posts, documentation etc tend to speak of 'mentions', but the API calls them 'posts'. Hmmm...

The primary key we can use to bind all this data back together again when we analyse it will be the document DOI (which we use to retrieve the JSON in the first place).

Then we'll use a data analysis / visualisation tool of some sort to load the lists back in and join them back together on the DOI. (Could do this with Qlik but fancy trying it with R / R Studio.

Use the issues list for ideas / requests for more features.

## Configuration

The AlmetricClient needs a configuration file called config.ini to be created in the root folder. It should contain the following information used to connect to Altmetric's API.

    [api.altmetric.com]
    APIBaseURI = http://api.altmetric.com
    APIVersion = v1
    APIBaseCommand = fetch
    APIRequestedItemIdType = doi
    APIKey = <<PUT YOUR ALTMETRIC KEY HERE>>

You need the http:// in the URL, but you don't need to put any forward slashes in the other values - the URLBuilder class does that for you.

(All fields correct at time of going to press... See [https://api.altmetric.com/](https://api.altmetric.com/) for further details).

## Branches

To keep things simple, everything is being pushed to master until the first 'release'. Then once we're actually using the tool in anger, we'll branch to dev and then start adding new features to that.

## Dependencies

1. Tests are in [PyTest](https://docs.pytest.org/en/latest/).
2. REST / JSON handled using [requests](http://docs.python-requests.org/en/master/).
3. The built-in [Python Config Parser](https://docs.python.org/3/library/configparser.html), which we've used to keep our Altmetrics key secret! (Never push the config.ini - keep a reference to it in .gitignore...

The code was written with PyCharm but we'll at least try to GitIgnore all the project management cruft. We also built this from the get-go with GitHub's default Python ignore file.