#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['spylls']):
    from spylls.hunspell import Dictionary

dictionary = Dictionary.from_files('en_US')

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    word = fdp.ConsumeRemainingString()
    dictionary.lookup(word)
    dictionary.suggest(word)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
