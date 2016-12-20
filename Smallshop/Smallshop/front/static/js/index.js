/*
* @Author: zhangwei
* @Date:   2016-12-17 21:12:57
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-19 20:36:53
*/

'use strict';
window.onload=function(){
	var oDiv = document.getElementsByClassName('user')[0]
	var oDiv1 = document.getElementsByClassName('set')[0]
	oDiv.onmousemove = function(){
		oDiv1.style.display='block';
	};
	oDiv1.onclick=function(){
		oDiv1.style.display='none';
	}
}
$(function(){
	$('.buttom_a').click(function(event){
		var search = $('.search').val()
		$.ajax({
			'url':'/front/search/'+search,
			'type':'GET',
			'success':function(data){
				console.log(data)
			},
			'error':function(error){
					console.log(error);
				},

		})
	})
	

})