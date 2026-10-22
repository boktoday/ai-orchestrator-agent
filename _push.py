"""Publish the AI Orchestrator agent profile as a new public repo."""
import base64
import json
import pathlib
import re
import urllib.error
import urllib.request

ROOT = pathlib.Path('C:/Users/insig/figures/orchestrator-agent-repo')
REPO = 'boktoday/ai-orchestrator-agent'
token = re.search(r'https://([^:]+):([^@]+)@github\.com',
                  pathlib.Path('C:/Users/insig/.git-credentials').read_text(encoding='utf-8', errors='replace')).group(2)
H = {'Authorization': 'token ' + token, 'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json'}


def gh(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request('https://api.github.com' + path, data=data, method=method, headers=H)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b'{}')


status, _ = gh('GET', '/repos/' + REPO)
if status == 404:
    status, body = gh('POST', '/user/repos', {
        'name': 'ai-orchestrator-agent',
        'description': 'A free Hermes agent profile that teaches AI orchestration by building real artefacts with one student at a time.',
        'private': False,
        'has_issues': True,
        'has_wiki': False,
    })
    print('create repo:', status, body.get('full_name', body.get('message', '')))
else:
    print('repo exists:', status)

pushed, failed = [], []
for path in sorted(p for p in ROOT.rglob('*') if p.is_file()):
    rel = path.relative_to(ROOT).as_posix()
    payload = {'message': 'Add ' + rel,
               'content': base64.b64encode(path.read_bytes()).decode('ascii'),
               'branch': 'main'}
    st, cur = gh('GET', '/repos/%s/contents/%s' % (REPO, rel))
    if st == 200 and isinstance(cur, dict) and cur.get('sha'):
        payload['sha'] = cur['sha']
    st, resp = gh('PUT', '/repos/%s/contents/%s' % (REPO, rel), payload)
    if st in (200, 201):
        pushed.append(rel)
    else:
        failed.append((rel, st, str(resp)[:120]))

print('pushed', len(pushed), 'files')
for f in failed:
    print('FAILED', f)
