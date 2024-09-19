//location.href='http://127.0.0.1:5000/result/activity'
function updateDateTime() {
    const date = new Date();
    
    // 날짜 관련 변수
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    const week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    const dayOfWeek = week[date.getDay()];
    
    // 시간 관련 변수
    const hours = date.getHours();
    const minutes = date.getMinutes();
    
    // 한 자리 숫자는 두 자리로 맞추기
    const formattedMinutes = minutes < 10 ? '0' + minutes : minutes;
    const formattedHours = hours < 10 ? '0' + hours : hours;
    
    // 첫째 줄: 년/월/일 요일
    document.getElementById("current_date").innerHTML = year + "/" + month + "/" + day + ' ' + dayOfWeek;
    
    // 둘째 줄: 시:분
    document.getElementById("current_time").innerHTML = formattedHours + " : " + formattedMinutes;
}

// 매 초마다 시간을 업데이트하도록 설정
setInterval(updateDateTime, 1000);

// 6초 후에 updateDateTime 함수 실행
setTimeout(() => {
    updateDateTime(); // 6초 후에 호출
}, 6000)



function show_page(index) {
    const skin = document.getElementById('skin');
    const activity = document.getElementById('activity');
    const diary = document.getElementById('diary');
    if ( index == 1 ) {
        skin.style.display = 'flex';
        activity.style.display = 'none';
        diary.style.display = 'none';
    } else if ( index == 2 ) {
        skin.style.display = 'none';
        activity.style.display = 'flex';
        diary.style.display = 'none';
    } else {
        skin.style.display = 'none';
        activity.style.display = 'none';
        diary.style.display = 'flex';
    }
}