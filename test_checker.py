#!/usr/bin/env python3
"""Checker controls using frozen JSON only; no science execution."""
import copy, json, math, unittest
from reproduce import ROOT, compare
class CheckerTests(unittest.TestCase):
    def setUp(self): self.ref=json.loads((ROOT/'reference/check-results.json').read_text())
    def rejected(self, edit):
        x=copy.deepcopy(self.ref); edit(x)
        with self.assertRaises(ValueError): compare(x,self.ref)
    def test_changed_coefficient(self): self.rejected(lambda x:x['exact'].__setitem__('roundtrip_delay','1024'))
    def test_changed_bound(self): self.rejected(lambda x:x['bounds'][0].__setitem__('corrected_formula_A_m2','1'))
    def test_failed_verdict(self): self.rejected(lambda x:x.__setitem__('passed',False))
    def test_missing_check(self): self.rejected(lambda x:x['checks'].pop())
    def test_nonfinite(self): self.rejected(lambda x:x['quadrature_infinite'].__setitem__('value',math.nan))
    def test_roundoff(self):
        x=copy.deepcopy(self.ref); x['quadrature_infinite']['value']+=1e-14; compare(x,self.ref)
    def test_runtime_ignored(self):
        x=copy.deepcopy(self.ref); x['runtime']={'different':'environment'}; compare(x,self.ref)
if __name__=='__main__': unittest.main()
