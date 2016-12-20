/*
* @Author: zhangwei
* @Date:   2016-12-14 21:09:09
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-17 20:03:56
*/

'use strict';
$(document).ready(function(){
	$('#loginBtn').click(function(event){
		event.preventDefault();
		var username=$('#AccountName').val();
		var password=$('#Password').val();
		var remember=$('#RememberMe');
		if (remember.is(':checked')){
			var flag=true
		}
		console.log(username)
		ssajax.ajax({
			'url':'/front/login/',
			'type':'POST',
			'data':{
				'username':username,
				'password':password,
				'remember':flag,
				},
				'success':function(data){
					console.log(data)
					if(data['message'] == '登陆成功')
					{
						window.location.href = '/front/index';
					}
					if (data['error'] ==  '用户名或密码错误')
					{
						alert('用户名或密码错误')

					}
					
				},
				'error':function(error){
					console.log(error);
				},
		});
	});
});