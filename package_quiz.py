"""Create a portable, single-file offline copy with all source photos included."""
import base64
import json
from pathlib import Path

root = Path(__file__).parent
html = (root/'index.html').read_text(encoding='utf-8')
css = (root/'style.css').read_text(encoding='utf-8')
data = (root/'data.js').read_text(encoding='utf-8')
app = (root/'app.js').read_text(encoding='utf-8')
sources = {p.relative_to(root).as_posix(): 'data:image/jpeg;base64,'+base64.b64encode(p.read_bytes()).decode('ascii') for p in (root/'image').glob('*.jpg')}
source_script = 'const sourceImages = '+json.dumps(sources)+'; window.QUIZ_DATA.passages.forEach(p => p.source = sourceImages[p.source]);'
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>'+css+'</style>')
html = html.replace('<script src="data.js" defer></script><script src="app.js" defer></script>', '')
html = html.replace('href="index.html"', 'href="#"')
html = html.replace('</body>', '<script>'+data+'</script><script>'+source_script+'</script><script>'+app+'</script></body>')
(root/'on-tap-trac-nghiem.html').write_text(html, encoding='utf-8')
print('Created on-tap-trac-nghiem.html (self-contained, photos embedded).')
