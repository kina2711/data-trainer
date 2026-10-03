#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l381_l400_specs import *
LESSONS=lessons(381,385);QUERIES=queries(381,385);VERIFY=verification(381,385);TAKEAWAYS=takeaways(381,385);SOURCES=source_rows(KS,KW)
if __name__=="__main__": raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.76",timestamp="2026-10-02T23:59:56+07:00"))
