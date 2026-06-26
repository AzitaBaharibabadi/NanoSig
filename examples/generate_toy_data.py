#!/usr/bin/env python3
"""
Generate a small, fully synthetic, reproducible toy FASTQ dataset for
NanoSig's examples/ folder. NOT biologically meaningful -- purely for
letting a new user/reviewer clone the repo and exercise the CLI quickly.
"""
import gzip
import random

random.seed(42)  # fixed seed -> reproducible output every time this is run

N_READS = 300
MIN_LEN, MAX_LEN = 500, 3000
BASES = "ACGT"


def random_seq(length):
    return "".join(random.choice(BASES) for _ in range(length))


def random_qual(length, mean_q=12):
    return "".join(chr(33 + max(2, min(40, int(random.gauss(mean_q, 3))))) for _ in range(length))


def main():
    with gzip.open("examples/toy_reads.fastq.gz", "wt") as f:
        for i in range(N_READS):
            length = random.randint(MIN_LEN, MAX_LEN)
            seq = random_seq(length)
            qual = random_qual(length)
            f.write(f"@toy_read_{i}\n{seq}\n+\n{qual}\n")
    print(f"Wrote {N_READS} synthetic reads to examples/toy_reads.fastq.gz")


if __name__ == "__main__":
    main()
