html_parser 1.0

Process html page, extract sequence of charcter and count top occurences.

Assumption:
Not valid character (letter) acts as separator. Eg:<br />
This is test -> [This, is, test]<br />
This%is&test -> [This, is, test]<br />
This@is&nbsp;test -> [This, is, test]<br />

It supports Latin like languages

Run script from root directory:
pip install -r src/requirements.txt
PYTHONPATH=src python main.py

Run tests:
pip install -r tests/requirements.txt
pytest tests

