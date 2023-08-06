# Fenerbahce

fenerbahce is a command line tool to fetch information past and future games of Fenerbahçe's Professional Football Team

Currently, only the last and the next game information can be shown. In the future I will integrate live scores, and pip packaging.

## Installation

Install with pip:

```pip install fenerbahce```


## Commands

`fenerbahce next` -> Fetches next match information

`fenerbahce last` -> Fetches last match information

## Dependencies

fenerbahce depends on the following packages:

- BeautifulSoup4
- lxml
- click
- requests
- pytest
- coverage.py

## Running locally

The project is built by using poetry and Python3. So to be able to run this project locally, make sure you have a running Python3 instance and a working poetry distribution.

In order to run the project locally, after cloning the repository, use the command:

```
poetry run fenerbahce
```

Commands described above can also be executed, but with little caveats:

`poetry run fenerbahce next` -> Fetches next match information

`poetry run fenerbahce last` -> Fetches last match information

## Testing

To run tests, run the command:
```
poetry run pytest
```

To calculate coverage, run these commands consecutively:
```
poetry run coverage run -m pytest
poetry run coverage report
```

Alternatively, an HTML report can also be generated:
```
poetry run coverage run -m pytest
poetry run coverage html
```