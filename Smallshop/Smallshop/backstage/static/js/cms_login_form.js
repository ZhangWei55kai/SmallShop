/*
* @Author: zhangwei
* @Date:   2016-11-02 15:59:25
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-22 10:59:17
*/

'use strict';
$(document).ready(function(){
	$('.sub').click(function(event){
		event.preventDefault();
		var username=$('.username').val();
		var password=$('.password').val();
		zwajax.ajax({
			'url':'/backstage/login/',
			'method':'POST',
			'data':{
				'username':username,
				'password':password,
				},
				'success':function(data){
					console.log(data)
					window.location.href = '/backstage/index';
					if(data['message'] == '登陆成功')
					{
						window.location.href = '/backstage/index';
					}
					if (data['message'] ==  '用户名或密码错误')
					{
						var alerted = $('.tanchu');
						alerted.show();
						alerted.html(data['message']);
						var oldSrc = $('.change').attr('src');
						var newSrc = oldSrc + '?code='+Math.floor(Math.random()*100);
						$('.change').attr('src',newSrc);

					}
					else if (data['code'] == 400) {
						var alerted = $('.tanchu');
						alerted.show();
						alerted.html('用户名或密码格式不对')
						var oldSrc = $('.change').attr('src');
						var newSrc = oldSrc + '?code='+Math.floor(Math.random()*100);
						$('.change').attr('src',newSrc);

					}
					else if(data['code'] == 401){
						var alerted = $('.tanchu');
						alerted.show();
						alerted.html('验证码错误')
						var oldSrc = $('.change').attr('src');
						var newSrc = oldSrc + '?code='+Math.floor(Math.random()*100);
						$('.change').attr('src',newSrc);

					}
					
				},
				'error':function(error){
					console.log(error);
				},
		});
	});
	$('.change').click(function(){

		var oldSrc = $(this).attr('src');
		var newSrc = oldSrc + '?code='+Math.floor(Math.random()*100)
		$(this).attr('src',newSrc)
	})
});