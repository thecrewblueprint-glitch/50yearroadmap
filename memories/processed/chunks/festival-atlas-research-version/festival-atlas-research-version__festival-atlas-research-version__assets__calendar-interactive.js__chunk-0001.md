---
{
  "chunk_id": "festival-atlas-research-version__festival-atlas-research-version__assets__calendar-interactive.js__chunk-0001",
  "archive_id": "festival-atlas-research-version",
  "archive_filename": "festival-atlas-research-version.zip",
  "source_path": "festival-atlas-research-version/assets/calendar-interactive.js",
  "chunk_index": 1,
  "chunk_count_for_source": 3,
  "char_start": 0,
  "char_end": 11983,
  "source_sha256": "538e908261a592e17e23d42351d08e042bf13a8416ddd490886ff74da91b0dc6",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

(function(){
  if(!document.body || document.body.dataset.page !== 'calendar') return;

  var MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];
  var DAYS=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
  var SHORT=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var state={view:'month',cursor:null};
  var MOBILE_BREAK=700;

  function $(selector){return document.querySelector(selector)}
  function esc(value){return String(value==null?'':value).replace(/[&<>'"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]})}
  function parseDate(value){if(!value)return null;var d=new Date(String(value)+'T00:00:00');return isNaN(d.getTime())?null:d}
  function dateKey(date){return date.getFullYear()+'-'+String(date.getMonth()+1).padStart(2,'0')+'-'+String(date.getDate()).padStart(2,'0')}
  function addDays(date,days){var d=new Date(date.getTime());d.setDate(d.getDate()+days);return d}
  function startOfWeek(date){var d=new Date(date.getFullYear(),date.getMonth(),date.getDate());d.setDate(d.getDate()-d.getDay());return d}
  function monthStart(date){return new Date(date.getFullYear(),date.getMonth(),1)}
  function fmt(date,year){return date?SHORT[date.getMonth()]+' '+date.getDate()+(year?', '+date.getFullYear():''):''}
  function branchName(id){var match=(window.branches||[]).find(function(b){return b.id===id});return match?match.name:id}
  function isMobile(){return window.innerWidth<MOBILE_BREAK}
  function filterValues(){return {
    q:(($('#q')||{}).value||'').trim().toLowerCase(),
    branch:(($('#branchFilter')||{}).value||''),
    region:(($('#regionFilter')||{}).value||''),
    month:(($('#monthFilter')||{}).value||''),
    state:(($('#stateFilter')||{}).value||'')
  }}
  function matchesFilter(opportunity){
    var f=filterValues();
    var hay=JSON.stringify(opportunity||{}).toLowerCase()+' '+(opportunity.departments||[]).map(branchName).join(' ').toLowerCase();
    return (!f.q||hay.indexOf(f.q)>-1)
      &&(!f.branch||(opportunity.departments||[]).indexOf(f.branch)>-1)
      &&(!f.region||opportunity.region===f.region)
      &&(!f.month||String(opportunity.month)===f.month)
      &&(!f.state||opportunity.state===f.state);
  }
  function allEvents(){
    return (window.scopedOpportunities||[]).filter(function(item){return parseDate(item.startDate)&&matchesFilter(item)}).sort(function(a,b){
      return parseDate(a.startDate)-parseDate(b.startDate) || String(a.name).localeCompare(String(b.name));
    });
  }
  function showRange(event){
    var start=parseDate(event.startDate);
    var end=parseDate(event.endDate)||start;
    if(end<start)end=start;
    return {start:start,end:end};
  }
  function workRange(event){
    var r=showRange(event);
    var big=(event.departments||[]).length>=9;
    var lead=big?9:4;
    var tail=big?3:2;
    return {start:addDays(r.start,-lead),end:addDays(r.end,tail)};
  }
  function durationDays(rangeOrEvent){
    var r=rangeOrEvent.start?rangeOrEvent:showRange(rangeOrEvent);
    return Math.max(1,Math.round((r.end-r.start)/86400000)+1);
  }
  function intersects(range,start,end){return range.end>=start&&range.start<=end}
  function clipped(range,start,end){return {start:range.start<start?start:range.start,end:range.end>end?end:range.end}}
  function eventsOnDay(events,day,rangeFn){
    rangeFn=rangeFn||showRange;
    return events.filter(function(event){var r=rangeFn(event);return r.start<=day&&r.end>=day})
  }
  function eventsInRange(events,start,end,rangeFn){
    rangeFn=rangeFn||showRange;
    return events.filter(function(event){return intersects(rangeFn(event),start,end)})
  }
  function ensureCursor(events){
    if(state.cursor)return;
    var today=new Date();
    var todayStart=new Date(today.getFullYear(),today.getMonth(),today.getDate());
    var upcoming=events.find(function(event){return showRange(event).end>=todayStart;});
    state.cursor=parseDate((upcoming||events[0]||{}).startDate)||new Date(today.getFullYear(),today.getMonth(),1);
  }
  function monthWeeks(date){
    var first=monthStart(date);
    var start=startOfWeek(first);
    var weeks=[];
    for(var w=0;w<6;w++){
      var weekStart=addDays(start,w*7);
      var days=[];
      for(var d=0;d<7;d++)days.push(addDays(weekStart,d));
      weeks.push({start:weekStart,end:addDays(weekStart,6),days:days});
    }
    return weeks;
  }
  function dayModal(day,events){
    var showItems=eventsOnDay(events,day,showRange);
    var workItems=eventsOnDay(events,day,workRange).filter(function(event){return showItems.indexOf(event)<0});
    var body='<h2>'+fmt(day,true)+'</h2><p class="sub">Muted outline shows the approximate work window. Bright inner segment shows public festival show dates. Approximate dates are estimates and subject to change.</p>';
    if(!showItems.length&&!workItems.length){body+='<p class="sub">No festival or approximate work-window records on this day in the current filters.</p>';}
    if(showItems.length){
      body+='<h3>Festival show days</h3>'+showItems.map(function(event){
        var sr=showRange(event), wr=workRange(event);
        var depts=(event.departments||[]).slice(0,4).map(branchName).join(' · ');
        return '<div class="detail cal-day-detail cal-show-detail" style="margin:10px 0;cursor:pointer" onclick="openOpportunity(\''+esc(event.id)+'\')">'+
          '<b>'+esc(event.name)+'</b><br>'+
          '<span class="sub">'+esc(event.city||'')+(event.state?', '+esc(event.state):'')+'</span><br>'+
          '<span class="sub">Festival: '+esc(fmt(sr.start,false)+' – '+fmt(sr.end,true))+' · '+durationDays(sr)+' day'+(durationDays(sr)===1?'':'s')+'</span><br>'+
          '<span class="sub">Approx. work window: '+esc(fmt(wr.start,false)+' – '+fmt(wr.end,true))+'</span>'+
          (depts?'<br><span class="sub">'+esc(depts)+'</span>':'')+
        '</div>';
      }).join('');
    }
    if(workItems.length){
      body+='<h3>Approximate work-window estimates</h3>'+workItems.map(function(event){
        var wr=workRange(event), sr=showRange(event);
        return '<div class="detail cal-day-detail cal-work-detail" style="margin:10px 0;cursor:pointer" onclick="openOpportunity(\''+esc(event.id)+'\')">'+
          '<b>'+esc(event.name)+'</b><br>'+
          '<span class="sub">Approx. work window: '+esc(fmt(wr.start,false)+' – '+fmt(wr.end,true))+'</span><br>'+
          '<span class="sub">Festival show dates: '+esc(fmt(sr.start,false)+' – '+fmt(sr.end,true))+'</span>'+
        '</div>';
      }).join('');
    }
    if(typeof window.openModal==='function')window.openModal(body);
  }
  window.openCalendarDay=function(key){var day=parseDate(key);if(day)dayModal(day,allEvents());};
  window.setCalendarView=function(view){state.view=view==='week'?'week':'month';render();};
  window.shiftCalendar=function(direction){
    var delta=Number(direction)||0;
    if(state.view==='week')state.cursor=addDays(state.cursor,delta*7);
    else state.cursor=new Date(state.cursor.getFullYear(),state.cursor.getMonth()+delta,1);
    render();
  };
  window.calendarToday=function(){state.cursor=new Date();render();};

  function combinedBar(event,weekStart,weekEnd,row){
    var wr=workRange(event), sr=showRange(event);
    var outer=clipped(wr,weekStart,weekEnd);
    var colStart=Math.floor((outer.start-weekStart)/86400000)+1;
    var colEnd=Math.floor((outer.end-weekStart)/86400000)+2;
    var cls='cal-combined-bar';
    if(wr.start<weekStart)cls+=' continues-in';
    if(wr.end>weekEnd)cls+=' continues-out';
    var showHtml='';
    if(intersects(sr,outer.start,outer.end)){
      var inner=clipped(sr,outer.start,outer.end);
      var total=Math.max(1,Math.round((outer.end-outer.start)/86400000)+1);
      var left=Math.max(0,Math.round((inner.start-outer.start)/86400000))/total*100;
      var width=Math.max(1,Math.round((inner.end-inner.start)/86400000)+1)/total*100;
      showHtml='<i class="cal-show-overlay" style="left:'+left+'%;width:'+width+'%"><span class="cal-show-name">'+esc(event.name)+'</span></i>';
    }
    return '<button class="'+cls+'" type="button" style="grid-column:'+colStart+' / '+colEnd+';grid-row:'+row+'" onclick="event.stopPropagation();openOpportunity(\''+esc(event.id)+'\')" title="'+esc(event.name)+'"><span class="cal-work-label cal-work-label-start">Approx.</span><span class="cal-work-label cal-work-label-end">Approx.</span>'+showHtml+'</button>';
  }
  function renderMonth(events){
    var month=state.cursor.getMonth();
    var todayKey=dateKey(new Date());
    return '<div class="calendar-app-frame">'+
      '<div class="cal-weekdays app-weekdays">'+DAYS.map(function(day){return '<div>'+day+'</div>'}).join('')+'</div>'+
      '<div class="cal-month-weeks">'+monthWeeks(state.cursor).map(function(week){
        var inWeek=eventsInRange(events,week.start,week.end,workRange).slice(0,8);
        var allInWeek=eventsInRange(events,week.start,week.end,workRange);
        return '<section class="cal-week-row">'+
          '<div class="cal-week-day-grid">'+week.days.map(function(day){
            var showCount=eventsOnDay(events,day,showRange).length;
            var workCount=eventsOnDay(events,day,workRange).length;
            var dots=showCount?'<div class="cal-ev-dots">'+Array(showCount+1).join('<i class="cal-ev-dot cal-ev-dot-show"></i>')+'</div>':'';
            return '<div class="cal-date-cell '+(day.getMonth()===month?'':'muted-month')+' '+(dateKey(day)===todayKey?'today':'')+'" role="button" tabindex="0" data-keyclick aria-label="'+esc(fmt(day,true))+'" onclick="openCalendarDay(\''+dateKey(day)+'\')">'+
              '<span class="cal-day-num">'+day.getDate()+'</span>'+(showCount?'<span class="cal-dot-count show">'+showCount+'</span>':(workCount?'<span class="cal-dot-count work">'+workCount+'</span>':''))+dots+'</div>';
          }).join('')+'</div>'+
          '<div class="cal-week-event-grid">'+inWeek.map(function(event,index){return combinedBar(event,week.start,week.end,index+1)}).join('')+(allInWeek.length>8?'<div class="cal-week-more" style="grid-column:1 / 8;grid-row:9">+'+(allInWeek.length-8)+' more this week</div>':'')+'</div>'+
        '</section>';
      }).join('')+'</div>'+
    '</div>';
  }
  function renderWeek(events){
    var start=startOfWeek(state.cursor);
    var days=[];
    for(var i=0;i<7;i++)days.push(addDays(start,i));
    var end=addDays(start,6);
    var rows=eventsInRange(events,start,end,workRange).slice(0,18);
    return '<div class="calendar-app-frame cal-week-app">'+
      '<div class="cal-weekdays app-weekdays">'+days.map(function(day){return '<button type="button" onclick="openCalendarDay(\''+dateKey(day)+'\')"><b>'+DAYS[day.getDay()]+'</b><span>'+fmt(day,false)+'</span></button>'}).join('')+'</div>'+
      '<div class="cal-week-track">'+(rows.length?rows.map(function(event,index){return combinedBar(event,start,end,index+1)}).join(''):'<p class="sub">No festivals or approximate work windows in this week under current filters.</p>')+'</div>'+
      '</div>';
  }
  function renderWeekMobile(events){
    var start=startOfWeek(state.cursor);
    var todayKey=dateKey(new Date());
    var days=[];
    for(var i=0;i<7;i++)days.push(addDays(start,i));
    return '<div class="cal-week-mobile">'+
      days.map(function(day){
        var showItems=eventsOnDay(events,day,showRange);
        var workItems=eventsOnDay(events,day,workRange).filter(function(e){return showItems.indexOf(e)<0;});
        var total=showItems.length+workItems.length;
        var isToday=dateKey(day)===todayKey;
        return '<div class="cal-wm-day'+(isToday?' today':'')+(total===0?' cal-wm-empty':'')+'">'+
          '<div class="cal-wm-header" role="button" tabindex="0" data-keyclick aria-label="'+esc(fmt(day,true))+'" onclick="openCalendarDay(\''+dateKey(day)+'\')">'+
            '<span class="cal-wm-dayname">'+DAYS[day.getDay()]+'</span>'+
            '<span class="cal-wm-date">'+fmt(day,false)+'</span>'+
