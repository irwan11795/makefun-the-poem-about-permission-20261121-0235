"""Short poem about agency: the power to ask and to be given.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR,
./output, or the system temp dir as fallback). Stdlib only, deterministic.
"""
import os
import sys
import tempfile

TEXT = (
    "For years the door stayed shut.\n"
    "I did not push it.\n"
    "I asked \u2014\n"
    "and behind it, a room I had never entered,\n"
    "and a chair already pulled out for me."
)


def _candidates():
    seen = []
    for cand in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        "./output",
        tempfile.gettempdir(),
    ):
        if cand and cand not in seen:
            seen.append(cand)
    return seen


def main():
    data = TEXT.encode("utf-8")
    last_err = None
    for outdir in _candidates():
        try:
            os.makedirs(outdir, exist_ok=True)
            path = os.path.join(outdir, "entry.txt")
            with open(path, "wb") as f:
                f.write(data)
            return 0
        except OSError as exc:
            last_err = exc
    print("could not write entry.txt: %s" % last_err, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
