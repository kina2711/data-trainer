#!/usr/bin/env python3
from promote_l271_l300_common import run_batch
from promote_l411_l440_specs import *
LESSONS=lessons(421,425);QUERIES=queries(421,425);VERIFY=verification(421,425);TAKEAWAYS=takeaways(421,425);SOURCES=source_rows(OF,OR,OE,NG)
if __name__=="__main__":raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.84",timestamp="2026-10-02T23:59:54+07:00"))
