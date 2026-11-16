"""Run interaction checks in the installed Chrome, without external dependencies."""
import subprocess
from pathlib import Path

root=Path(__file__).parent.resolve()
test_script=r'''
<script>
try {
 const el=id=>document.getElementById(id);
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const event=(id,value)=>{el(id).value=value;el(id).dispatchEvent(new Event(id==='search'?'input':'change'))};
 assert(window.QUIZ_DATA.questions.length===234,'Question count');
 assert(document.querySelectorAll('.q-link').length===234,'Initial map');
 assert(el('questionNumber').textContent==='CÂU 147','First question');
 document.querySelector('#options input[value="0"]').click();
 el('check').click();
 assert(el('feedback').textContent.includes('Chính xác!'),'Correct answer feedback');
 el('next').click();
 assert(el('questionNumber').textContent==='CÂU 148','Sequential next');
 document.querySelector('#options input[value="0"]').click();el('check').click();
 assert(el('feedback').classList.contains('incorrect'),'Wrong answer feedback');
 el('flag').click();assert(el('flag').getAttribute('aria-pressed')==='true','Flag');
 el('gradeAll').click();assert(el('result').textContent.includes('1 / 2'),'Score');
 event('filter','wrong');assert(document.querySelectorAll('.q-link').length===1,'Wrong filter');
 assert(el('questionNumber').textContent==='CÂU 148','Wrong item');
 event('filter','flagged');assert(document.querySelectorAll('.q-link').length===1,'Flag filter');
 event('filter','all');event('part','extra');assert(document.querySelectorAll('.q-link').length===180,'Supplement count');
 assert(el('questionNumber').textContent==='CÂU BS001','Supplement order');
 event('search','BS180');assert(document.querySelectorAll('.q-link').length===1,'Search');
 assert(el('questionNumber').textContent==='CÂU BS180','Search result');
 event('search','nothing_matches_xyz');assert(document.querySelectorAll('.q-link').length===0,'Empty state');
 el('reset').click();assert(el('resetDialog').open,'Reset dialog');el('cancelReset').click();
 assert(!el('resetDialog').open,'Cancel reset');
 const saved=JSON.parse(localStorage.getItem('reading-room-v1'));
 assert(saved.answers.g147===0 && saved.answers.g148===0,'Persistent answers');
 el('reset').click();el('confirmReset').click();
 assert(el('progress').value===0 && el('questionNumber').textContent==='CÂU 147','Reset');
 const doc=document.documentElement;
 assert(doc.scrollWidth<=window.innerWidth,'Responsive overflow');
 const marker=document.createElement('p');marker.id='qa-result';marker.textContent='QA_PASS_234';document.body.append(marker);
}catch(e){const marker=document.createElement('p');marker.id='qa-result';marker.textContent='QA_FAIL: '+e.message;document.body.append(marker)}
</script>
'''
temporary=root/'qa-interactions.html'
html=(root/'on-tap-trac-nghiem.html').read_text(encoding='utf-8')
temporary.write_text(html.replace('</body>',test_script+'</body>'),encoding='utf-8')
try:
    for width,height in [(1440,1100),(390,844)]:
        args=[r'C:\Program Files\Google\Chrome\Application\chrome.exe','--headless','--disable-gpu','--no-first-run','--no-default-browser-check','--user-data-dir='+str(root/'.chrome-qa'),f'--window-size={width},{height}','--dump-dom',temporary.as_uri()]
        result=subprocess.run(args,capture_output=True,timeout=45)
        dom=result.stdout.decode('utf-8',errors='replace')
        assert '<p id="qa-result">QA_PASS_234</p>' in dom, 'Browser checks failed: '+dom[dom.rfind('<p id="qa-result">'):][:200]+result.stderr.decode(errors='replace')[:300]
        print(f'PASS {width}x{height}: 234 questions, answer selection, correct/wrong feedback, score, navigation, filters, search, flags, persistence, reset, no horizontal overflow.')
finally:
    temporary.unlink(missing_ok=True)
