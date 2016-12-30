/*
* @Author: zhangwei
* @Date:   2016-12-22 21:44:40
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-31 00:48:56
*/

'use strict';
$(function(){
	$('#submit_c').click(function(event){
		event.preventDefault();
		var commodityName= $('#commodityName').val();
		var tags = [];
		$('#tag:checked').each(function(){
			tags.push($(this).val());
		})
		var category = $('#categoryId').find('option:selected').val();
		var commodityImg = $('#commodityImg').val();
		var commodityStock = $('#commodityStock').val();
		var commodityPrice = $('#commodityPrice').val();
		var points = $('#points').val();
		var commodityDes = $('#commodityDes').val();
		console.log(tags)
		zwajax.ajax({
			'url':'backstage/createCommodity/',
			'type':'POST',
			'data':{
				'commodityName':commodityName,
				'tags[]':tags,
				'categoryId':category,
				'commodityImg':commodityImg,
				'commodityStock':commodityStock,
				'commodityPrice':commodityPrice,
				'points':points,
				'commodityDes':commodityDes,
			},
			'success':function(data){
				if(data['message']=='创建成功'){
					alert('创建成功');
					window.location.reload();
				}
				else{
					alert('创建失败，请检查输入的信息')
				}

			}
		})
	})
	
	$('.editcom').click(function(event){
		event.preventDefault();
		var comid = $(this).attr("id");
		zwajax.ajax({
			'url':'../editCommodity/'+comid,
			'type':'GET',
			'success':function(data){
				if(data['message']!= null){
					$('#E_commodityName').val(data['message']['commodityName']);
					$('#E_commodityImg').val(data['message']['commodityImg']);
					$('#E_commodityStock').val(data['message']['commodityStock']);
					$('#E_commodityPrice').val(data['message']['commodityPrice']);
					$('#E_points').val(data['message']['commodityPoints']);
					$('#E_commodityDes').val(data['message']['commodityDes']);
					$('.editid').val(data['message']['commodityId']);
					if(data['message']['commondityCate']){
						var id = data['message']['commondityCate']
						$("#E_categoryId").find("option[value="+id+"]").attr("selected",true);
					};
					var cke= $('.checktag').children()
						for (var i = 0;i<cke.length; i++) {
							cke.attr("checked",false);
						}
					if(data['message']['commodityTag'].length>0){
						
						var tagid = data['message']['commodityTag']
						
						 $(tagid).each(function (i,dom){
						 	console.log(i,dom)
					        $(":checkbox[id='"+dom+"']").prop("checked",true);
					    });
					};
				}
				else{
					alert('程序出错无法编辑')
				}

			}
		})

	})
	$('#submit_e').click(function(event){
		event.preventDefault();
		var commodityName= $('#E_commodityName').val();
		var comid = $('.editid').val();
		var tags = [];
		$('.eTag:checked').each(function(){
			tags.push($(this).val());
		})
		var category = $('#E_categoryId').find('option:selected').val();
		var commodityImg = $('#E_commodityImg').val();
		var commodityStock = $('#E_commodityStock').val();
		var commodityPrice = $('#E_commodityPrice').val();
		var points = $('#E_points').val();
		var commodityDes = $('#E_commodityDes').val();
		console.log(tags,commodityName,category,commodityImg,commodityStock,commodityPrice,points,commodityDes)
		zwajax.ajax({
			'url':'../editCommodity/'+comid,
			'type':'POST',
			'data':{
				'commodityName':commodityName,
				'tags[]':tags,
				'categoryId':category,
				'commodityImg':commodityImg,
				'commodityStock':commodityStock,
				'commodityPrice':commodityPrice,
				'points':points,
				'commodityDes':commodityDes,
			},
			'success':function(data){
				if(data['message']=='修改成功'){
					alert('修改成功');
					window.location.reload();
				}
				else{
					console.log(data['error']);
					alert('创建失败，请检查输入的信息')
				}

			}
		})
	})
})