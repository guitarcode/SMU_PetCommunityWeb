function Find(){
    let btn = document.querySelector('.Find-Btn');
    btn.addEventListener('click',function(){
        var design = document.getElementsByClassName('Find-Content');
        design.style.display = hidden;
    
        document.getElementsByClassName('Find-Txt').innerHTML = "등록하신 이메일로 아이디가 전송되었습니다.:)";
    
        document.getElementsByClassName('Find-Btn').innerHTML = "로그인 창으로 돌아가기";
    })
}
Find();