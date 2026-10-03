#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l381_l400_specs import *
LESSONS=lessons(386,390);QUERIES=queries(386,390);VERIFY=verification(386,390);TAKEAWAYS=takeaways(386,390);SOURCES=source_rows(KX)
if __name__=="__main__": raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.77",timestamp="2026-10-02T23:59:57+07:00"))
