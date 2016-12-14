
$(function () {
    var $name = $('#register_box').find('input[name=AccountName]');
    var $psw = $('#register_box').find('input[name=Password]');
    var $psw2 = $('#register_box').find('input[name=ConfirmPassword]');
    var $code = $('#register_box').find('input[name=ValidateCode]');
    var $sendcode = $("#send_security_code");

    $name.blur(function () {
        var test = myregExp.mobile.test($(this).val());
        if (!test) {
            $(this).parent('li').attr('class', 'input_box params_error')
			.next('li').find('em').text('请输入正确的手机号注册');
        } else {
            $(this).parent('li').attr('class', 'input_box params_success')
			.next('li').find('em').text('');
        }
    });

    $psw.blur(function () {
        var test1 = myregExp.num.test($(this).val());
        var test2 = myregExp.letter.test($(this).val());
        var test3 = myregExp.password.test($(this).val());
        if (test1 || test2 || test3) {
            $(this).parent('li').attr('class', 'input_box params_success')
			.next('li').find('em').text('');
        } else {
            $(this).parent('li').attr('class', 'input_box params_error')
			.next('li').find('em').text('密码只能由6-16位英文、数字或标点符号组成');
        }
    });

    $psw2.blur(function () {
        if ($(this).val() != '' && $psw.val() == $(this).val()) {
            $(this).parent('li').attr('class', 'input_box params_success')
			.next('li').find('em').text('');
        } else {
            $(this).parent('li').attr('class', 'input_box params_error')
			.next('li').find('em').text('两次输入密码不一致');
        }
    });

    $sendcode.click(function () {
        var test = myregExp.mobile.test($name.val());
        if (!test) {
            $name.parent('li').attr('class', 'input_box params_error')
			.next('li').find('em').text('请输入正确的手机号注册');
            return false;
        }
        if (!$sendcode.hasClass("disabled")) {
            $sendcode.addClass("disabled");
            sec = 60;
            showcode();
            $.ajax({
                cache: false,
                url: '/customer/sendcode',
                data: { Phone: $name.val(), CustomerCheckType: 5, ValidateCode: $code.val() },
                type: 'post',
                success: function (rep) {
                    if (rep.error) {
                        displayPopupWarn(rep.message, function () { }, 3500);
                        sec = 0;
                    } else {
                        displayPopupOK("短信验证码已发送，请注意查收。");
                    }
                }
            });
        }
    });
});

var sec = 60;
function showcode() {
    var $sendcode = $("#send_security_code");

    if (sec >= 0) {
        var codetime = "再次发送验证码({1})";
        $sendcode.html(codetime.replace("{1}", sec));
        sec = sec - 1;
        setTimeout("showcode()", 1000);
    } else {
        var codetime = "再次发送验证码";
        $sendcode.html(codetime);
        $sendcode.removeClass("disabled")
    }
}
$(document).ready(function(){
    $('#register-button').click(function(event){
        event.preventDefault();
        var name =$('#Name').val();
        var email =$('#Email').val();
        var username=$('#AccountName').val();
        console.log(username)
        var password=$('#Password').val();
        var repassword =$('#ConfirmPassword').val();
        var address =$('#address').val();
        ssajax.ajax({
            'url':'/front/register/',
            'type':'POST',
            'data':{
                'name':name,
                'email':email,
                'username':username,
                'password':password,
                'repassword':repassword,
                'address':address

                },
                'success':function(data){
                    console.log(data)
                    if(data['code'] == '200')
                    {
                        alert('注册成功');
                        window.location.href = '/front/index';
                    }
                    if (data['error'])
                    {
                        alert('请正确填写信息')

                    }
                    
                },
                'error':function(error){
                    console.log(error);
                },
        });
    });
});