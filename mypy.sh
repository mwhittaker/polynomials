#! /usr/bin/env bash

set -euo pipefail

main() {
    mypy polynomial.py --ignore-missing-imports
}

main "$@"
