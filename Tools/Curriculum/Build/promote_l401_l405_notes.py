#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l401_l410_specs import *
LESSONS=lessons(401,405);QUERIES=queries(401,405);VERIFY=verification(401,405);TAKEAWAYS=takeaways(401,405);SOURCES=source_rows(GA)
if __name__=="__main__":raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.80",timestamp="2026-10-02T23:59:58+07:00"))
