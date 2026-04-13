import re
from pathlib import Path
voids = {'meta','img','link','br','hr','input','area','base','col','embed','keygen','param','source','track','wbr'}
regex = re.compile(r'</?([a-zA-Z0-9_-]+)([^>]*)>')
for file in Path('.').glob('*.html'):
    html = file.read_text(encoding='utf-8')
    stack = []
    errors = []
    for m in regex.finditer(html):
        tag = m.group(1).lower()
        tok = m.group(0)
        is_close = tok.startswith('</')
        self_close = tok.endswith('/>') or tag in voids
        if is_close:
            if not stack:
                errors.append(f'extra close </{tag}> at {m.start()}')
                continue
            top = stack[-1]
            if top == tag:
                stack.pop()
            else:
                errors.append(f'mismatch </{tag}> expected </{top}> at {m.start()}')
                if tag in stack:
                    stack = stack[:stack.index(tag)]
        elif not self_close:
            stack.append(tag)
    if errors or stack:
        print('FILE', file.name)
        for e in errors:
            print('  ERROR', e)
        if stack:
            print('  REMAINING', ' > '.join(stack))
