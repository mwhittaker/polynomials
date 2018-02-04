#! /usr/bin/env bash

set -euo pipefail

main() {
    pylint polynomial.py --errors-only
}

main "$@"
