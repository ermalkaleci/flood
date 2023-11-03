from __future__ import annotations
from random import randint
from flood.cli import cli_run
from flood.generators.object_generators.block_generators import generate_block_numbers

import os
import random
import flood

MIN_BLOCK_NUMBER = int(os.environ.get('MIN_BLOCK_NUMBER', 0))

assert os.environ.get('MAX_BLOCK_NUMBER') is not None, 'MAX_BLOCK_NUMBER env variable must be set'
MAX_BLOCK_NUMBER = int(os.environ.get('MAX_BLOCK_NUMBER'))

# make sure JSON-RPC requests id is within u64::MAX
def _randint(start, end):
    """Custom randint with max end u64::MAX
    """
    return randint(start, min(18_446_744_073_709_551_615, end))

# make sure block numbers are within MIN_BLOCK_NUMBER and MAX_BLOCK_NUMBER
# flood test are hardcoded with blocks from ethereum mainnet
def _generate_block_numbers(
    n: int,
    start_block: int,
    end_block: int,
    *,
    replace: bool = False,
    sort: bool = False,
    random_seed: flood.spec.RandomSeed | None = None,
    network: str | None = None
):
    """Custom generate_block_numbers with min/max block numbers
    """
    return generate_block_numbers(
        n=n,
        start_block=min(MIN_BLOCK_NUMBER, start_block),
        end_block=min(MAX_BLOCK_NUMBER, end_block),
        replace=replace,
        sort=sort,
        random_seed=random_seed,
        network=network
    )

random.randint = _randint
flood.generators.object_generators.block_generators.generate_block_numbers = _generate_block_numbers


if __name__ == '__main__':
    cli_run.run_cli()
