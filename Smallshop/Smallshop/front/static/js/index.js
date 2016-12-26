/*
* @Author: zhangwei
* @Date:   2016-12-17 21:12:57
* @Last Modified by:   zhangwei
* @Last Modified time: 2016-12-22 10:03:21
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
		if(!search){
			search=','
		};
		$.ajax({
			'url':'/front/search/'+search,
			'type':'GET',
			'success':function(data){
				window.location.href='/front/search/'+search
			},
			'error':function(error){
					console.log(error);
				},

		})
	})
	

})