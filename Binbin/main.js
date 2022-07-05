//디자인
const inputs = document.querySelectorAll(".input");


function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

// //html 이동
// function To_SignIn(){
// 	location.href("signIn.html")
// };
// function To_Login(){
// 	location.href("login.html")
// };
// function To_Start(){
// 	location.href("start.html")
// };
// function To_Find(){
// 	location.href("find.html")
// };
// function To_FindId(){
// 	location.href("findId.html")
// };
// function To_FindPw(){
// 	location.href("findPw.html")
// };
// function To_Infofix(){
// 	location.href("info-fix.html")
// };

function Login(){
	
};

$(".Login-Content").keypress(function(e){
	if (e.keyCode === 13) {
		Login();
	}
});

//start 페이지 버튼 호버 이미지 변경. 랜덤 수는 데이터베이스에 있는 갯수만큼 해도 될거같슴드아
var img1 = document.getElementById('img-1');
var img2 = document.getElementById('img-2');
var img3 = document.getElementById('img-3');

// var btn = document.querySelector('.button');
// btn.addEventListener("mouseover",function(){
// 	var num = Math.floor(Math.random() * 3) + 1;
// 	img1.src = num+".jpg"
// 	var num = Math.floor(Math.random() * 3) + 1;
// 	img2.src = num+".jpg"
// 	var num = Math.floor(Math.random() * 3) + 1;
// 	img3.src = num+".jpg"
// });
function img_change(){
	var num = Math.floor(Math.random() * 3) + 1;
	// fade(img1)
	img1.src = num+".jpg"
	var num = Math.floor(Math.random() * 3) + 1;
	// fade(img2)
	img2.src = num+".jpg"
	var num = Math.floor(Math.random() * 3) + 1;
	// fade(img3)
	img3.src = num+".jpg"
}
// start 이미지 변경 애니메이션
// function fade(element) {
//     var op = 0.8;  // initial opacity
//     var timer = setInterval(function () {
//         if (op >= 1){
//             clearInterval(timer);
//         }
//         element.style.opacity = op;
//         element.style.filter = 'alpha(opacity=' + op * 100 + ")";
//         op += 0.05;
//     }, 50);
// }