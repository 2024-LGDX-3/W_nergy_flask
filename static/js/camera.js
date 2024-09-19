const video = document.getElementById('video');
const captureButton = document.getElementById('capture');
const displayImage = document.getElementById('display_image');
const uploadForm = document.getElementById('uploadForm');
const testForm = document.getElementById('testForm');
let canvas;
let imageBlob = null;

// 카메라 스트림 설정
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        video.play();
    })
    .catch(err => {
        console.error('카메라 접근 실패:', err);
    });

// "캡처" 버튼 클릭 시 이미지 캡처
captureButton.addEventListener('click', () => {
    // 캔버스 생성 및 비디오 프레임을 그리기
    canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    // 캔버스에서 이미지 데이터를 가져와서 화면에 표시
    const img = document.createElement('img');
    img.src = canvas.toDataURL('image/jpg');

    // 기존 이미지 삭제 후 새로운 이미지 표시
    displayImage.innerHTML = ''; // 기존 이미지 제거
    displayImage.appendChild(img);
    video.style.display = "none";

    // 이미지 데이터를 Blob으로 변환하여 imageBlob에 저장
    canvas.toBlob((blob) => {
        imageBlob = blob;
        console.log('이미지 Blob 생성 완료');
    }, 'image/jpeg');  // JPG 형식으로 변환
});

// "분석하기" 버튼 클릭 시 이미지 캡처 및 전송
uploadForm.addEventListener('submit', async (event) => {
    event.preventDefault();  // 폼의 기본 제출 동작 방지

    if (imageBlob) {
        console.log("uploadform act")
        const formData = new FormData();
        formData.append('file', imageBlob, 'image.jpg');  // Blob 데이터를 FormData로 추가

        // 서버로 POST 요청 전송
        const response = await fetch('http://127.0.0.1:5000/result/skin', {
            method: 'POST',
            body: formData
        });
        location.href = "http://127.0.0.1:5000/result/skin";
    } else {
        alert('사진을 먼저 캡처해주세요.');
    }
});


// "분석하기" 버튼 클릭 시 이미지 캡처 및 전송
testForm.addEventListener('submit', (event) => {
    event.preventDefault();  // 폼의 기본 제출 동작 방지

    const formData = new FormData();
    formData.append('file', imageBlob, 'image.jpg');  // Blob 데이터를 FormData로 추가

    // 서버로 POST 요청 전송
    fetch('http://127.0.0.1:5000/test', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log('서버 응답:', data);
            alert('분석 완료: ' + JSON.stringify(data));
        })
        .catch(error => {
            console.error('파일 전송 실패:', error);
        });
});


// // 서버로 POST 요청 전송
// fetch('http://127.0.0.1:5000/analyze', {
//     method: 'POST',
//     body: formData
// })
//     .then(response => response.json())
//     .then(data => {
//         console.log('서버 응답:', data);
//         alert('분석 완료: ' + JSON.stringify(data));
//     })
//     .catch(error => {
//         console.error('파일 전송 실패:', error);
//     });
// } else {
//     alert('사진을 먼저 캡처해주세요.');
// }