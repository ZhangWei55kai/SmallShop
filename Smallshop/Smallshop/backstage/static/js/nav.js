/*
* @Author: zhangwei
* @Date:   2016-09-14 15:32:50
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-22 19:00:53
*/

'use strict';
$(function(){
	var href = window.location.href;
	var offset = 0;
	if (href.indexOf('/index')>0){
		offset = 0;
	}
	else if(href.indexOf('/article')>0){
		offset = 1;
	}
	else if(href.indexOf('/createCommodity')>0){
		offset = 3;
	}
	else if(href.indexOf('/setting')>0){
		offset = -1
	};
	var oUl = $('.alltag');
	if(offset>=0){
	oUl.children().eq(offset).addClass('active').siblings().removeClass('active')	
	}
	else{
		oUl.children().removeClass('active')
	}

})

// $(function(){
// 	$('#C_shop').click(function(event){
// 		event.preventDefault()
// 		$('#myModal').show();
// 	})

		
	

// })

// window.onload = function(){
// 	var link = window.location.href
// 	console.log(link)
// };