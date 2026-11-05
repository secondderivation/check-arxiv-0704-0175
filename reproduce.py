#!/usr/bin/env python3
"""Bounded replay; never overwrite reference evidence."""
from pathlib import Path
import argparse, hashlib, json, math, subprocess, sys
ROOT=Path(__file__).resolve().parent
REFERENCE_SHA="b90d85b78ef3d4cd702f462159867b6d9d57e541d644c3183b5f606aba94da04"
def compare(actual, expected, location="root"):
    if type(actual) is not type(expected): raise ValueError(f"Type mismatch: {location}")
    if isinstance(expected, dict):
        if actual.keys()!=expected.keys(): raise ValueError(f"Keys differ: {location}")
        for k in expected:
            if location=="root" and k=="runtime": continue
            compare(actual[k],expected[k],location+"."+k)
    elif isinstance(expected,list):
        if len(actual)!=len(expected): raise ValueError(f"Length differs: {location}")
        for i,(a,e) in enumerate(zip(actual,expected)): compare(a,e,f"{location}[{i}]")
    elif isinstance(expected,float):
        if not math.isfinite(actual) or not math.isclose(actual,expected,rel_tol=1e-12,abs_tol=1e-12): raise ValueError(f"Value differs: {location}")
    elif actual!=expected: raise ValueError(f"Value differs: {location}")
def guard():
    import resource
    resource.setrlimit(resource.RLIMIT_CPU,(30,30))
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',default='run-results'); args=parser.parse_args()
    reference=ROOT/'reference/check-results.json'
    before=reference.read_bytes()
    if hashlib.sha256(before).hexdigest()!=REFERENCE_SHA: raise ValueError('Reference hash mismatch')
    expected=json.loads(before)
    out=Path(args.output).resolve(); out.mkdir(parents=True,exist_ok=False)
    if out==ROOT or reference.is_relative_to(out): raise ValueError('Output cannot contain reference')
    try:
        with (out/'stdout.txt').open('w') as stdout, (out/'stderr.txt').open('w') as stderr:
            subprocess.run([sys.executable,'-I',str(ROOT/'code/check.py'),'--output',str(out/'check-results.json')],stdout=stdout,stderr=stderr,timeout=30,check=True,preexec_fn=guard if sys.platform!='win32' else None)
        actual=json.loads((out/'check-results.json').read_text())
        if actual.get('passed') is not True or len(actual.get('checks',[]))!=21 or not all(x.get('pass') is True for x in actual['checks']): raise ValueError('Scientific checks failed')
        compare(actual,expected)
        (out/'replay.json').write_text(json.dumps({'replay':'pass','scientific_scope':'conditional equation consistency only','checks':len(actual['checks']),'reference_sha256':REFERENCE_SHA},indent=2)+'\n')
        print('PASS: 21 checks; reference comparison passed. No observational fit performed.')
    finally:
        if reference.read_bytes()!=before: raise ValueError('Reference changed during replay')
if __name__=='__main__': main()
