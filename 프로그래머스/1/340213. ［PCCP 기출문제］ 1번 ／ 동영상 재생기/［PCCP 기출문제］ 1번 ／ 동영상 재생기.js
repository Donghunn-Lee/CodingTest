function timeToSeconds(time) {
  const [mm, ss] = time.split(":").map(Number);
  return mm * 60 + ss;
}

function calTime(cur, time) {
  let [mm, ss] = [cur[0], cur[1] + time];

  // 초가 음수일 때
  if (ss < 0) {
    while (ss < 0 && mm > 0) {  // mm > 0 조건을 추가해 mm이 0 이상일 때만 초를 조정
      ss += 60;
      mm--;
    }
    if (mm === 0 && ss < 0) {  // mm이 0이고 ss가 음수인 경우
      ss = 0;  // 절대로 음수로 넘어가지 않게 처리
    }
  } else if (ss >= 60) {
    ss -= 60;
    mm++;
  }
  
  return [mm, ss];
}

function openingSkip(s, cur, e) {
  const s_t = timeToSeconds(s);  // 초로 변환
  const cur_t = cur[0] * 60 + cur[1];  // 현재 시간을 초 단위로 계산
  const e_t = timeToSeconds(e);  // 초로 변환

  if (s_t <= cur_t && cur_t <= e_t) {
    return e.split(":").map(Number);  // 오프닝 구간 끝으로 이동
  }
  return cur;  // 현재 시간 그대로 반환
}

function checkVideoLen(cur, video_len) {
  const cur_t = cur[0] * 60 + cur[1];
  const video_t = video_len[0] * 60 + video_len[1];

  // 비디오 끝을 넘어가면 비디오의 마지막 시간을 반환
  return cur_t >= video_t ? video_len : cur;
}

function solution(video_len, pos, op_start, op_end, commands) {
  video_len = video_len.split(":").map(Number);
  pos = pos.split(":").map(Number);

  pos = openingSkip(op_start, pos, op_end);
  
  for (let cmd of commands) {
    if (cmd == "prev") {
      pos = calTime(pos, -10);
    } else if (cmd == "next") {
      pos = calTime(pos, 10);
    }
    
    pos = openingSkip(op_start, pos, op_end);
    pos = checkVideoLen(pos, video_len);
  }
  
  let result_mm = pos[0] < 10 ? '0' + pos[0] : pos[0];
  let result_ss = pos[1] < 10 ? '0' + pos[1] : pos[1];
  
  return `${result_mm}:${result_ss}`;
}
