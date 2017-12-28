$(document).ready(function() {

    function banner() {

        var slider = $('.slider');
        var slideWidth = $('.element-slider').outerWidth();
        var scrollSlider = slider.position().left - slideWidth;
        var interval = 5000;
        var flag = false;
        var mouse = false;
        var auto = setInterval(clickFunc, interval);


        $('.banner').on('mouseover', function () {
            mouse = true
        });
        $('.banner').on('mouseout', function () {
            mouse = false
        });

        function clickFunc() {
            if (!(mouse)) {
                $('#button-slider-right').click()
            }
        }

        $('#button-slider-right').on('click', function () {
            if (flag) {
                return false
            }
            flag = true;
            slider.animate({'left': scrollSlider}, 500, function () {
                flag = false;
                slider
                    .find('.element-slider:first')
                    .appendTo(slider)
                    .parent()
                    .css({'left': 0});
            });
            clearInterval(auto);
            auto = setInterval(clickFunc, interval);
        });

        $('#button-slider-left').on('click', function () {
            if (flag) {
                return false
            }
            flag = true;
            slider
                .css({'left': scrollSlider})
                .find('.element-slider:last')
                .prependTo(slider)
                .parent()
                .animate({'left': 0}, 500, function () {
                    flag = false
                });
            clearInterval(auto);
            auto = setInterval(clickFunc, interval);
        });
    }

    banner();
});