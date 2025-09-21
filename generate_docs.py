#!/usr/bin/env python3
"""NT Documentation Generator - Main CLI entry point."""

import argparse
import time
from pathlib import Path

from ntdoc_gen import config
from ntdoc_gen.generator import generate_docs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="phnt include path", required=True)
    parser.add_argument("-c", "--commit", help="phnt commit")
    parser.add_argument("-m", "--msdn-docs-path")
    parser.add_argument("-i", "--ids-pattern",
                        help="generate only the ids matching the regex pattern, "
                             "useful for testing to quickly generate a subset of the docs")
    args = parser.parse_args()

    phnt_include_path = Path(args.path)

    if args.commit is not None:
        config.PHNT_REPOSITORY_COMMIT = args.commit

    msdn_docs_path = Path(args.msdn_docs_path) if args.msdn_docs_path else None

    start = time.time()

    generate_docs(phnt_include_path, msdn_docs_path, args.ids_pattern)

    end = time.time()
    print(f'Finished in {end - start:.2f}s')


if __name__ == '__main__':
    main()
