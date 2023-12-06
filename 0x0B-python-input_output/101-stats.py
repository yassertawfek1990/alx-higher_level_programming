#!/usr/bin/python3
"""define dd"""


def tats(si, st):
    """Print accumulated metrics."""
    print("File size: {}".format(si))
    for k in sorted(st):
        print("{}: {}".format(k, st[k]))

if __name__ == "__main__":
    import sys

    si = 0
    st = {}
    va = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                tats(si, st)
                c = 1
            else:
                c += 1
            line = line.split()
            try:
                si += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in va:
                    if st.get(line[-2], -1) == -1:
                        st[line[-2]] = 1
                    else:
                        st[line[-2]] += 1
            except IndexError:
                pass
        tats(si, st)
    except KeyboardInterrupt:
        tats(si, st)
        raise
