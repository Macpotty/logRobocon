function checkRegist() {
    with(document.all) {
        if (registOrigin.value != registVerify.value) {
            alert("两次输入密码不同")
            registOrigin.value = "";
            registVerify.value = "";
        } else document.forms[0].submit();
    }
}

function checkChange() {
    with(document.all) {
        if (changeOrigin.value != changeVerify.value) {
            alert("两次输入密码不同")
            changeOrigin.value = "";
            changeVerify.value = "";
        } else document.forms[0].submit();
    }
}

$(".delVerify").click(function(){
    if(confirm("Confirm?"))
        window.location.assign($(this).attr("url"));
});