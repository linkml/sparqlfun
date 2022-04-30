import os
import pprint

from linkml_runtime.dumpers import yaml_dumper

from sparqlfun.model import ResultSet

ROOT = os.path.abspath(os.path.dirname(__file__))
INPUT_DIR = os.path.join(ROOT, 'input')
OUTPUT_DIR = os.path.join(ROOT, 'output')

GO_TEST_TTL = os.path.join(INPUT_DIR, 'go-nucleus.ttl')

NUCLEUS = 'GO:0005634'

def check(rs: ResultSet, min_expected=1, max_expected: int = None,
          must_contain=None, outfile=None):
    if outfile:
        yaml_dumper.dump(rs, to_file=os.path.join(OUTPUT_DIR, outfile))
    n = 0
    for result in rs.results:
        print(f'RESULT={result}')
        n += 1
    if must_contain:
        for obj in must_contain:
            assert obj in rs.results
    assert n >= min_expected
    if max_expected is not None:
        assert n <= max_expected
