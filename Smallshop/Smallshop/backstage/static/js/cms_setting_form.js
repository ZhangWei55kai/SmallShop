/*
* @Author: zhangwei
* @Date:   2016-11-06 16:59:02
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-22 10:33:43
*/

'use strict';
$(function(){
	var domain = 'http://og7kdr0cj.bkt.clouddn.com/';
	var upload = Qiniu.uploader({
		runtimes:'html5,flash,html4',
		browse_button: 'pickfiles',
		container: 'container',
		drop_element: 'container',
		max_file_size:'500mb',
		dragdrop:true,
		chunk_size:'4mb',
		uptoken_url:'/cms/get_token',
		domain:domain,
		get_new_uptoken:false,
		auto_start:true,
		log_level:5,
		init:{
			'FilesAdded':function(up,files){
				console.log('file added');
			},
			'BeforeUpload':function(up,file){
				console.log('before upload');
			},
			'UploadProgress':function(){
				console.log('upload progress');
			},
			'FileUploaded':function(up,file,info){
				console.log('file uploaded');
				var avatar = domain + file.name;
				$('.img').attr('src',avatar)

				
			},
			'Error':function(up,err,errTip){
				console.log('error:'+err)
			},
		},
	});
	// upload.start();
	// 提交按钮执行
	$('.submit').click(function(event){
		event.preventDefault();
		var username = $('.username').val();
		var avatar = null
		// 根据upload.files.length判断文件的长度是否大于1，因为files属性是一个数组，说明图片上传了
		if(upload.files.length>0){
			avatar = $('#pickfiles').attr('src')
		}
		 zwajax.ajax({
		'url':'setimg',
		'method':'POST',
		'data':{'username':username,'avatar':avatar},
		'success':function(data){
			console.log(data);
		},
		'error':function(error){
			console.log(error)
		},

		});
		
		
	})
});
// $(function(){
// 	$('#myModal').modal(show)
// })