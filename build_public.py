#!/usr/bin/env python3
"""Build the public copy of the planner from index.html.

The local build carries the full programme text so it works offline on a phone.
The published copy keeps only a short excerpt of each official description and
sends the reader to the festival's own page for the rest, so this site is a
finding aid rather than a mirror of somebody else's copy.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
EXCERPT = 300


def trim(text):
    if not text or len(text) <= EXCERPT:
        return text
    cut = text[:EXCERPT]
    stop = max(cut.rfind('. '), cut.rfind('! '), cut.rfind('? '))
    if stop > 160:
        cut = cut[:stop + 1]
    return cut.rstrip() + ' …'


def main():
    src = open(os.path.join(ROOT, 'index.html')).read()
    m = re.search(r'^const EV=(\[.*\]);$', src, re.M)
    if not m:
        sys.exit('could not find the programme data in index.html')
    events = json.loads(m.group(1))
    for e in events:
        e['d'] = trim(e.get('d'))
        e['df'] = trim(e.get('df'))
    out = src[:m.start(1)] + json.dumps(events, ensure_ascii=False,
                                        separators=(',', ':')) + src[m.end(1):]
    os.makedirs(os.path.join(ROOT, 'docs'), exist_ok=True)
    dest = os.path.join(ROOT, 'docs', 'index.html')
    open(dest, 'w').write(out)
    print(f'{len(events)} sessions · {os.path.getsize(dest)/1024:.0f} KB → docs/index.html')


if __name__ == '__main__':
    main()
