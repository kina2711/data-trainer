#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l351_l380_specs import *
LESSONS=lessons(376,380); QUERIES=queries(376,380); VERIFY=verification(376,380); TAKEAWAYS=takeaways(376,380); SOURCES=source_rows(DV,DS,TF,TM)
if __name__=="__main__": raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.75",timestamp="2026-10-02T23:59:55+07:00"))
