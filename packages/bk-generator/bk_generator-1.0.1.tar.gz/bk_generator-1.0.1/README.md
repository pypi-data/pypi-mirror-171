# friendly-sniffle

Quickly and securely generate a username or a password from EFF Dicewords list.

## Installation

```bash
$ pip install bk-generator
```

## Usage

### python

```python
>>> import generate
>>> generate.generate_username(wordlist, include_numbers)
>>> generate.generate_passphrase(wordlist, num_words, separator, capitalize, include_numbers)
```

### cli

```bash
$ generate --help
usage: generate.py [-h] {passphrase,username} ...

Generate a username or passphrase.

options:
  -h, --help            show this help message and exit

commands:
  valid commands

  {passphrase,username}
                        command to run
```

```bash
$ generate username -h
usage: generate.py username [-h] [-w WORDLIST] [-C] [-i]

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist to use (default: eff_large_wordlist.txt)
  -C, --copy            Copy passphrase to clipboard
  -i, --include-numbers
                        Include numbers in passphrase
```

```bash
generate username
Fancy-Zebra
```

```bash
$ generate password -h
usage: generate.py passphrase [-h] [-w WORDLIST] [-C] [-i] [-n NUM_WORDS] [-c] [-s SEPARATOR | -xs]

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist to use (default: eff_large_wordlist.txt)
  -C, --copy            Copy passphrase to clipboard
  -i, --include-numbers
                        Include numbers in passphrase
  -n NUM_WORDS, --num-words NUM_WORDS
                        Number of words in passphrase (default: 3)
  -c, --capitalize      Capitalize the first letter of each word

Separator options:
  -s SEPARATOR, --separator SEPARATOR
                        Separator between words (default: -)
  -xs, --no-separator   Do not use a separator between words
```

```bash
$ generate password -C -i
Rejoice-Jigsaw-Exact14
```
