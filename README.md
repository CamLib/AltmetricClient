# AltmetricClient

Retrieves and parses information from https://www.altmetric.com.

This is still a work in progress and hasn't made a usable first release yet. But we've started to use the issues list for ideas / requests for more features etc.

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

Then we'll use a data analysis / visualisation tool of some sort to load the lists back in and join them back together on the DOI. (Could do this with Qlik but fancy trying it with R / R Studio).

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

This has a couple of implications for testing (see below).

## Testing

The code is a little 'impure' in terms of testing, in that there are what some people might (probably correctly) call Integration Tests mashed in with Unit Tests. As a result, there are three directories with tests in.

All tests that are independent and can be run locally are in the 'tests' folder. This still contains some tests that might not be considered 'pure' Unit Tests, i.e. tests to read lists of DOIs in from CSVs (there's a files_in directory in the codebase, with a test file in it).

Then the other two test directories (tests_integration and tests_issues) contain some tests that call out to the Altmetric endpoint. As such, these should only be run one at a time, and very occasionally - like when a config change has been made, or if the endpoint changes.

Oddly enough, the tests_issues directory contains tests that map onto issues in the issues list. They're mostly included for a bit of history and documentation.

All three directories contain tests that rely upon a local resources (e.g. test CSVs loaded in from the files-in directory or written to files_out)... This means tests will fail in PyCharm unless the local 'working directory' for those tests has been set in the run config.

See [https://www.jetbrains.com/help/pycharm/run-debug-configuration.html](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html)...

... examples of the latter kind (i.e. tests that exercise third party resources) have been added to a seperate directory (tests_integration), though, so it's easier to exclude them from test runs. Otherwise, just by testing the code over and over, we'd be rather rudely hitting Altmetric's endpoint all the time.