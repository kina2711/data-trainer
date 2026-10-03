#!/usr/bin/env python3
from promote_l006_l050_common import load_lesson, run

LESSONS = tuple(load_lesson(number) for number in range(46, 51))

if __name__ == "__main__":
    raise SystemExit(run(46, 50, "1.0.97", "2026-10-03T01:05:00+07:00"))
