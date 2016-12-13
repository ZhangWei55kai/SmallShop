
$(function () {
    var $username = $('#login_form').find('input[name=AccountName]');
    var $password = $('#login_form').find('input[name=Password]');
	
	$username.blur(function () {
		var test1 = myregExp.email.test($(this).val());
		var test2 = myregExp.mobile.test($(this).val());
		if(test1 || test2){
			$('#login_form .error').hide();
		} else {
			$('#login_form .error').show().find('span').text('请输入正确的邮箱/手机号登录');
		}
	});

	$password.blur(function () {
		var test1 = myregExp.num.test($(this).val());
		var test2 = myregExp.letter.test($(this).val());
		var test3 = myregExp.password.test($(this).val());
		if(test1 || test2 || test3){
			$('#login_form .error').hide();
		} else {
			$('#login_form .error').show().find('span').text('密码只能由6-16位英文、数字或标点符号组成');
		}
	});
	//登录
	//artDialog 官方教程http://aui.github.io/artDialog/doc/index.html
	//$('#loginBtn').click(function () {
	//	var d = dialog({
	//	    title: '提示',
	//	    content: '按钮回调函数返回 false 则不许关闭',
	//	    okValue: '确定',
	//	    ok: function () {
	//	        this.title('提交中…');
	//	        return false;
	//	    },
	//	    cancelValue: '取消',
	//	    cancel: function () {}
	//	});
	//	d.show();
	//});

});