#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l351_l380_specs import *
LESSONS=lessons(361,365); QUERIES=queries(361,365); VERIFY=verification(361,365); TAKEAWAYS=takeaways(361,365); SOURCES=source_rows(AR,AI,AV)
if __name__=="__main__": raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.72",timestamp="2026-10-02T23:59:52+07:00"))
