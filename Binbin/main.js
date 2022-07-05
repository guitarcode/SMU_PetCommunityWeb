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