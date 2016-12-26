/*
* @Author: zhangwei
* @Date:   2016-12-22 21:44:40
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-23 13:44:39
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
					window.location.href='backstage/createCommodity/'
				}
				else{
					alert('创建失败，请检查输入的信息')
				}

			}
		})
	})
})