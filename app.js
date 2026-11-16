(() => {
  'use strict';
  const {passages, questions} = window.QUIZ_DATA;
  const $ = id => document.getElementById(id);
  const KEY = 'reading-room-v1';
  let state = {answers:{}, checked:{}, flags:{}, current:questions[0].id};
  try {
    const saved = JSON.parse(localStorage.getItem(KEY));
    if(saved && typeof saved === 'object') {
      for(const key of ['answers','checked','flags']) if(saved[key] && typeof saved[key] === 'object' && !Array.isArray(saved[key])) state[key] = saved[key];
      if(questions.some(q => q.id === saved.current)) state.current = saved.current;
      for(const q of questions) if(!Number.isInteger(state.answers[q.id]) || state.answers[q.id]<0 || state.answers[q.id]>3) delete state.answers[q.id];
    }
  } catch {}
  let visible = questions.slice();
  let collapsed = false;
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); $('saveStatus').textContent='Đã lưu tiến độ trên trình duyệt này.'; }
    catch { $('saveStatus').textContent='Trình duyệt không cho lưu. Bạn có thể tải kết quả JSON ở cuối trang.'; }
  }
  const answered = q => Number.isInteger(state.answers[q.id]);
  const wrong = q => state.checked[q.id] && state.answers[q.id] !== q.answer;
  function applyFilters() {
    const term = $('search').value.trim().toLowerCase();
    visible = questions.filter(q => ($('part').value==='all' || q.kind===$('part').value)
      && ($('filter').value==='all' || ($('filter').value==='unanswered' && !answered(q)) || ($('filter').value==='flagged' && state.flags[q.id]) || ($('filter').value==='wrong' && wrong(q)))
      && (!term || q.number.toLowerCase().includes(term) || q.q.toLowerCase().includes(term) || passages[q.passage].title.toLowerCase().includes(term)));
  }
  function renderMap() {
    applyFilters();
    $('questionMap').replaceChildren();
    $('visibleCount').textContent=visible.length;
    if(!visible.length){const p=document.createElement('p');p.className='empty';p.textContent='Không có câu phù hợp. Hãy đổi bộ lọc hoặc từ khóa.';$('questionMap').append(p);}
    for(const q of visible){
      const b=document.createElement('button');b.type='button';b.className='q-link';b.textContent=q.number;
      if(answered(q))b.classList.add('answered');
      if(state.current===q.id){b.classList.add('active');b.setAttribute('aria-current','true');}
      if(state.flags[q.id])b.classList.add('flagged');
      if(state.checked[q.id])b.classList.add(wrong(q)?'wrong':'correct');
      b.setAttribute('aria-label',`Câu ${q.number}${answered(q)?', đã chọn':''}${state.flags[q.id]?', đánh dấu':''}`);
      b.onclick=()=>go(q.id);$('questionMap').append(b);
    }
    const count=questions.filter(answered).length;
    $('progress').max=questions.length;$('progress').value=count;$('progressText').textContent=`${count} / ${questions.length}`;
    const i=visible.findIndex(q=>q.id===state.current);
    $('prev').disabled=i<=0;$('next').disabled=i<0 || i>=visible.length-1;
    $('pageCount').textContent=i>=0?`${i+1} / ${visible.length}`:'Ngoài bộ lọc hiện tại';
  }
  function go(id){state.current=id;save();render();}
  function render(){
    const q=questions.find(q=>q.id===state.current),p=passages[q.passage];
    const index=questions.indexOf(q);
    $('position').textContent=`ÔN TẬP ĐỌC HIỂU / ${String(index+1).padStart(2,'0')} TRÊN ${questions.length}`;
    $('passageTitle').textContent=p.title;$('passageText').textContent=p.text;
    $('passageText').hidden=collapsed;
    $('sourceImage').src=p.source;$('sourceLink').href=p.source;$('sourceDetails').open=false;
    $('questionNumber').textContent=`CÂU ${q.number}`;
    $('typeBadge').textContent=q.kind==='original'?'TỪ TÀI LIỆU GỐC':'LUYỆN TẬP BỔ SUNG';
    $('questionText').textContent=q.q;$('questionNote').textContent=q.note||'';$('questionNote').hidden=!q.note;
    $('flag').setAttribute('aria-pressed',!!state.flags[q.id]);$('flag').textContent=state.flags[q.id]?'⚑ Đã đánh dấu':'⚑ Đánh dấu';
    const options=$('options');options.replaceChildren();const legend=document.createElement('legend');legend.className='sr-only';legend.textContent='Chọn một đáp án';options.append(legend);
    q.options.forEach((text,i)=>{
      const label=document.createElement('label');label.className='option';
      if(state.answers[q.id]===i)label.classList.add('selected');
      if(state.checked[q.id] && i===q.answer)label.classList.add('correct-answer');
      if(state.checked[q.id] && state.answers[q.id]===i && i!==q.answer)label.classList.add('wrong-answer');
      const radio=document.createElement('input');radio.type='radio';radio.name=q.id;radio.value=i;radio.checked=state.answers[q.id]===i;
      radio.onchange=()=>{state.answers[q.id]=i;delete state.checked[q.id];$('result').hidden=true;save();render();};
      const letter=document.createElement('span');letter.className='letter';letter.textContent='ABCD'[i];
      const span=document.createElement('span');span.textContent=text;label.append(radio,letter,span);options.append(label);
    });
    $('feedback').hidden=!state.checked[q.id];
    $('feedback').classList.toggle('incorrect',!!wrong(q));
    if(state.checked[q.id]){
      const lead=document.createElement('strong');lead.textContent=state.answers[q.id]===q.answer?'Chính xác!':answered(q)?'Chưa đúng.':'Bạn chưa chọn đáp án.';
      const desc=document.createElement('div');desc.textContent=`Đáp án: ${'ABCD'[q.answer]}. ${q.options[q.answer]}`;
      const exp=document.createElement('div');exp.textContent=q.explanation;
      $('feedback').replaceChildren(lead,desc,exp);
    }
    $('check').disabled=!answered(q);
    renderMap();
  }
  $('check').onclick=()=>{state.checked[state.current]=true;save();render();};
  $('flag').onclick=()=>{state.flags[state.current]=!state.flags[state.current];save();render();};
  $('toggleReading').onclick=()=>{collapsed=!collapsed;$('passageText').hidden=collapsed;$('toggleReading').textContent=collapsed?'Mở đoạn đọc +':'Thu gọn −';$('toggleReading').setAttribute('aria-expanded',!collapsed);};
  for(const id of ['part','filter','search']) $(id).addEventListener(id==='search'?'input':'change',()=>{
    applyFilters();if(visible.length && !visible.some(q=>q.id===state.current)){state.current=visible[0].id;save();render();}else renderMap();
  });
  for(const [id,delta] of [['prev',-1],['next',1]])$(id).onclick=()=>{const i=visible.findIndex(q=>q.id===state.current);if(visible[i+delta]){go(visible[i+delta].id);$('question').scrollIntoView({behavior:'smooth',block:'start'});}};
  $('gradeAll').onclick=()=>{
    const done=questions.filter(answered);const correct=done.filter(q=>state.answers[q.id]===q.answer).length;
    if(!done.length){$('result').textContent='Hãy chọn ít nhất một đáp án trước khi chấm bài.';$('result').hidden=false;return;}
    done.forEach(q=>state.checked[q.id]=true);save();render();
    const title=document.createElement('strong');title.textContent=`Kết quả: ${correct} / ${done.length} câu đã làm đúng (${Math.round(correct/done.length*100)}%).`;
    const detail=document.createElement('div');detail.textContent=`Còn ${questions.length-done.length} câu chưa làm. Câu chưa làm chưa được chấm. Điểm tính trên toàn bộ bộ đề: ${correct}/${questions.length}.`;
    const b=document.createElement('button');b.className='quiet';b.textContent='Ôn lại câu sai';b.onclick=()=>{$('filter').value='wrong';$('part').value='all';$('search').value='';applyFilters();if(visible.length)go(visible[0].id);else renderMap();};
    $('result').replaceChildren(title,detail,b);$('result').hidden=false;$('result').scrollIntoView({behavior:'smooth',block:'center'});
  };
  $('reset').onclick=()=>$('resetDialog').showModal();$('cancelReset').onclick=()=>$('resetDialog').close();
  $('confirmReset').onclick=()=>{state={answers:{},checked:{},flags:{},current:questions[0].id};$('part').value='all';$('filter').value='all';$('search').value='';$('result').hidden=true;save();render();$('resetDialog').close();};
  $('export').onclick=()=>{
    const blob=new Blob([JSON.stringify({exportedAt:new Date().toISOString(),total:questions.length,answered:questions.filter(answered).length,results:questions.map(q=>({number:q.number,kind:q.kind,question:q.q,selected:answered(q)?'ABCD'[state.answers[q.id]]:null,checked:!!state.checked[q.id],correct:state.checked[q.id]?state.answers[q.id]===q.answer:null,flagged:!!state.flags[q.id]}))},null,2)],{type:'application/json;charset=utf-8'});
    const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='ket-qua-on-tap.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  };
  $('total').textContent=questions.length;$('extraCount').textContent=questions.filter(q=>q.kind==='extra').length;render();
})();
