$(document).ready(function() {

    $('.form-product, .form-create-count, .basket-delete').ajaxForm(function () {
        get_basket()
    });

    function get_basket() {
        $.get("/basket/get_data_basket", function (data) {
            $('#count, #hide-basket-count').text(data.number_product_in_basket);
            $('#count-price, #hide-basket-total').text(data.total_amount + ' р.');
        })}

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

    activeMenu();

    function show_new() {
        var products = $('.products');
        products.hide();
        for (var i=0; i<products.length; i++) {
            if (products.eq(i).find('#marker-new').length) {
                products.eq(i).show()
            }
        }
    }

    function show_hit() {
        var products = $('.products');
        products.hide();
        for (var i=0; i<products.length; i++) {
            if (products.eq(i).find('#marker-hit').length) {
                products.eq(i).show();
            }
        }
    }

    function switch_home() {
        var button_new = $('#new');
        var button_hit = $('#hit');

        $('.products').hide();
        show_new();

        button_new.on('click', function () {
            $('.switch').find('button').removeClass('switch-active');
            show_new();
            $('#new').addClass('switch-active')
        });
        button_hit.on('click', function () {
            $('.switch').find('button').removeClass('switch-active');
            show_hit();
            $('#hit').addClass('switch-active')
        })
    }

    if (document.location.pathname === '/') {
        $('#product-list').before('<div class="row">\n' +
            '<div class="switch">\n' +
            '<button id="new" class="btn btn-default switch-active">Новые</button>\n' +
            '<button id="hit" class="btn btn-default">Хит</button>\n' +
            '</div>\n' +
            '</div>');

        switch_home()
    }

    $('#search').on('input', function () {
        var window_result = $('#result-search');
        window_result.find('p').children().remove();
        var position = $(this).offset();
        var input = $('#search').val().toLowerCase();
        var path;
        var result;
        var n;
        window_result.css({'top': position.top + 35, 'left': position.left});
        $.ajax({
            type: 'POST',
            url: '/search/',
            data: {'input': input, 'csrfmiddlewaretoken': getCookie('csrftoken')},
            dataType: 'json',
            success: function (res) {
                if (!($.isEmptyObject(res))) {
                    for (var key in res) {
                        result = res[key][0].toLowerCase();
                        n = result.search(input);
                        result = res[key][0].slice(0,n) + '<span style="background:yellow">' + res[key][0].slice(n,n+input.length) + '</span>' + res[key][0].slice(n+input.length);
                        path = '/product/' + res[key][1] + '/';
                        window_result.find('p').append('<a href="' + path +'" class="search-item">' + result + '</a>')
                    }
                } else {
                    window_result.find('p').append('<p style="color:darkgrey" class="search-item">Ничего не найдено</p>')
                }
            }
        });
        window_result.show()
    });

    $('body').click(function (event) {
        if (!($('#search').is(event.target))) {
            $('#result-search').hide()
        }
    });
});
