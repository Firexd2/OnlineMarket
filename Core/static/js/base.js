$(document).ready(function() {

    $('.form-product, .form-create-count, .basket-delete').ajaxForm(function () {
        get_basket()
    });

    function get_basket() {
        $.get("/basket/get_data_basket", function (data) {

            $('#count, #hide-basket-count').text(data.number_product_in_basket);
            $('#count-price, #hide-basket-total').text(data.total_amount + ' р.');
        })}

    $('#logo').on('mouseover', function () {
        $('.slogan').css({'color': 'green'});

    });
    $('#logo').on('mouseout', function () {
        $('.slogan').css({'color': '#ffb801'});
    });

    $('.change-color').on('mouseover', function () {
        $(this).find('.fa').css({'color': '#ffb812', 'transition': '0.3s'})

    });
    $('.change-color').on('mouseout', function () {
        if ($(this).children('a').attr('href') !== window.location.pathname ) {
            $(this).find('.fa').css({'color': 'grey'})
        }
    });

    $('.btn-add-fav').on('click', function () {
        var product_and_user = $(this).parent('.btn-information').attr('id').split('-');
        if (!(product_and_user[1] === 'AnonymousUser')) {
            $.ajax({
                url: '/personal_room/add_to_favorites/',
                type: 'POST',
                data: {'csrfmiddlewaretoken': getCookie('csrftoken'), 'id': product_and_user[0]}
            });
            modal_window_for_alert('favorite')
        } else {
            modal_window_for_alert('no-auth')
        }
    });

    $('.form-product').on('submit', function () {
        change_button($(this).find('.basket-button'));
    });

    function modal_window_for_alert(id) {
        var blackout = $('#mask');
        var modal;
        var body = $('html, body');

        if (id === 'favorite') {
            modal = $('#modal-window-for-favorite');
        } else if (id === 'no-auth') {
            modal = $('#modal-window-no-auth');
        } else {

        }
        modal.show(200);
        blackout.show();
        body.css('overflow','hidden');

        $('#close-modal, #next-buy, #mask').on('click', function () {
            modal.hide();
            blackout.hide();
            body.css('overflow','auto');
        });
    }


    $(window).scroll(function () {
        if (document.location.pathname === '/') {
            if ($(this).scrollTop() > 150) {
                $('#hide-basket').fadeIn()
            } else {
                $('#hide-basket').fadeOut()
            }
        }});

    function activeMenu() {
        var link = $('#menu').children();
        var location = window.location.pathname;
        var cur_li;

        for (var i=0; i<link.length; i++) {
            cur_li = link.eq(i);
            if (cur_li.children('a').attr('href') === location) {
                cur_li.attr('style', 'background-color:#eee');
                cur_li.find('i').attr('style', 'color:#ffb812')
            }
        }

    }

    activeMenu()

});

