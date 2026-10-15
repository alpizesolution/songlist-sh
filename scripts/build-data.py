import csv, json, re, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8')))
def key(s):
    return re.sub(r'^[^0-9A-Za-z]+', '', s).casefold() or s.casefold()
artists = sorted({(r['ARTIST'].strip() or 'Unknown') for r in rows}, key=lambda a: (key(a), a))
ai = {a: i for i, a in enumerate(artists)}
# Song numbers may come as Excel text (="036527"); keep them as 6-digit strings.
num = lambda r: re.sub(r'[="\s]', '', r['NUMBER']).zfill(6)
songs = sorted(rows, key=lambda r: (key(r['TITLE']), r['TITLE'], num(r)))
S = [[num(r), r['TITLE'].strip(), ai[r['ARTIST'].strip() or 'Unknown']] for r in songs]
js = 'const ARTISTS=' + json.dumps(artists, ensure_ascii=False, separators=(',', ':')) + ';\nconst SONGS=' + json.dumps(S, ensure_ascii=False, separators=(',', ':')) + ';'
js = js.replace('</', '<\\/')
open(sys.argv[2], 'w', encoding='utf-8').write(js)
print(len(S), len(artists), len(js))
