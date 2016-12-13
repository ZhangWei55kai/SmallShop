window.onload = function() {
	var mySwiper1 = new Swiper('.menu', {
		freeMode: true,
		slidesPerView: 'auto',
	});
}
var goodsCount = 0;
$('.yimi_goods_add').bind('click', function() {
	goodsCount++;
	if(goodsCount) {
		$('.yimi_shopcart').html(goodsCount);
		$('.yimi_shopcart').css('display', 'block');

	} else {
		$('.yimi_shopcart').css('display', 'none');
	}
});
$('body').on('click', '.yimi_goods_add', function() {
	if($(this).hasClass('yimi_turn-around')) {
		$(this).removeClass('yimi_turn-around-a').removeClass('yimi_turn-around');
		$(this).addClass('yimi_turn-around-a').addClass('yimi_turn-around-s');

	} else {
		$(this).removeClass('yimi_turn-around-a').removeClass('yimi_turn-around-s');
		$(this).addClass('yimi_turn-around-a').addClass('yimi_turn-around');

	}

});
