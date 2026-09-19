# Regenera o index.html a partir de prompt.md + tools/index.tpl.html
# Uso: python3 tools/gen.py  (a partir da raiz do repositorio)

import json, io

src = io.open('prompt.md', encoding='utf-8').read()

START = "- Nome:"
END = "- O que quer conseguir e até quando:"
i = src.index(START)
j = src.index(END) + len(END)
head, tail = src[:i], src[j:]

def js(s):
    return json.dumps(s, ensure_ascii=False).replace("</", "<\\/")

tpl = io.open('./tools/index.tpl.html', encoding='utf-8').read()
out = tpl.replace('"__HEAD__"', js(head)).replace('"__TAIL__"', js(tail))

io.open('index.html', 'w', encoding='utf-8').write(out)
print("head ends:", repr(head[-40:]))
print("tail starts:", repr(tail[:40]))
print("bytes:", len(out))
