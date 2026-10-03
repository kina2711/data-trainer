#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l381_l400_specs import *
LESSONS=lessons(391,395);QUERIES=queries(391,395);VERIFY=verification(391,395);TAKEAWAYS=takeaways(391,395);SOURCES=source_rows(OC)
if __name__=="__main__": raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.78",timestamp="2026-10-02T23:59:58+07:00"))
