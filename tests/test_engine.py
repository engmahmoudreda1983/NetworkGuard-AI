"""Internal check of the calculation engine (run before every release):  python -m pytest tests  or  python tests/test_engine.py

Load flow against the IEEE 9 and 14 bus published results, IEC 60909 short circuits against hand calculation,
IEC 60255-151 relay curves, and the demo network runs every analysis."""
import os
import sys
import warnings

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
warnings.filterwarnings('ignore')
import networkguard_core as ng  # noqa: E402


def test_published_results():
    T = ng.validation()
    bad = T[T['Result'] != 'PASS']
    assert bad.empty, bad.to_string()


def test_demo_network_runs():
    D = ng.demo()
    assert not ng.validate_links(D) and not ng.missing_required(D)
    lf = ng.load_flow(D)
    assert lf['converged']
    sc = ng.short_circuit(D, 'max', 'CJ-400')
    assert (sc['bus']['Ik3 (kA)'] > 0).all()
    pr = ng.protection(D)
    assert len(pr['distance']) and len(pr['oc_pairs'])
    assert len(ng.contingency(D)['table'])


def test_line_parameters():
    p = ng.line_parameters('Flint AAAC 740.8 kcmil', '400 kV double-circuit, quad bundle')
    assert 0.2 < p['x1'] < 0.35 and 10 < p['c1'] < 16 and p['x0'] > 2 * p['x1']


if __name__ == '__main__':
    for f in (test_published_results, test_demo_network_runs, test_line_parameters):
        f(); print('PASS', f.__name__)
