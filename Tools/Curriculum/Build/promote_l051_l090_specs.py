"""Source assignments for Engineering Foundation lessons 51–90."""

TLPI = "src.book.tlpi.2010"
KERNEL = "src.docs.linux-kernel-runtime"
SYSTEMD = "src.docs.systemd-official"
BASH = "src.docs.gnu-bash-reference"
KUR = "src.book.kurose-ross-networking.8e"
TCP = "src.standard.rfc9293-tcp"
TLS = "src.standard.rfc8446-tls13"
RFC9110 = "src.web.rfc9110-http-semantics"
COD = "src.book.patterson-hennessy-cod.5e"
AMD = "src.paper.amdahl-1967"
GUS = "src.paper.gustafson-1988"
DB = "src.book.silberschatz-database-system-concepts.7e"
PET = "src.book.petrov-database-internals.1e"
PP = "src.book.hunt-thomas-pragmatic-programmer.20ae"
SOM = "src.book.sommerville-software-engineering.10e"
SRE_MON = "src.web.google-sre-monitoring"
SRE_CAP = "src.web.google-sre-capacity-load-testing"
AWS_RETRY = "src.web.aws-timeouts-retries-backoff"
TRINO_PLAN = "src.web.trino-distributed-plans"

SOURCES = {
    51: (TLPI, COD), 52: (TLPI, COD), 53: (TLPI,), 54: (TLPI,),
    55: (AMD, GUS, COD), 56: (COD, AMD, GUS), 57: (COD, DB, PET),
    58: (COD, AMD, GUS, TRINO_PLAN), 59: (PP, SRE_MON), 60: (COD, PP),
    61: (TLPI,), 62: (TLPI, KERNEL), 63: (TLPI, KERNEL), 64: (TLPI,),
    65: (TLPI,), 66: (TLPI, KERNEL), 67: (TLPI,), 68: (BASH,),
    69: (SYSTEMD,), 70: (TLPI,), 71: (TLPI, KERNEL), 72: (KERNEL, SRE_MON),
    73: (TLPI,), 74: (TLPI, KUR), 75: (TLPI, SRE_MON),
    76: (TLPI, KERNEL, SRE_MON), 77: (KUR,), 78: (KUR,),
    79: (KUR, TCP), 80: (KUR, TLS), 81: (KUR, RFC9110), 82: (KUR,),
    83: (KUR, AWS_RETRY), 84: (KUR, RFC9110, AWS_RETRY),
    85: (KUR, TLPI, TCP), 86: (KUR, SRE_MON),
    87: (KUR, SRE_CAP, AWS_RETRY), 88: (KUR, SRE_MON),
    89: (SOM,), 90: (SOM, PP),
}
