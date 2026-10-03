#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l381_l400_specs import *
LESSONS=lessons(396,400);QUERIES=queries(396,400);VERIFY=verification(396,400);TAKEAWAYS=takeaways(396,400);SOURCES=source_rows(OW)
if __name__=="__main__": raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.79",timestamp="2026-10-02T23:59:59+07:00"))
