$(document).ready(function() {

    if (document.location.pathname === '/personal_room/favorites/') {
        var bodyProduct = $('.product');

        for (var i=0; i<bodyProduct.length; i++) {
            bodyProduct.eq(i).append('<div class="remove-favorites">' +
                '<img src="/media/image/remove-favorite.png" alt=""></i>' +
                '</div>')
        }

        $('.remove-favorites').on('click', function () {
            var id = $(this).parent().find('input[name="id"]').val();
            $.post('/personal_room/remove_to_favorites/', {'id': id, 'csrfmiddlewaretoken': getCookie('csrftoken')});
            $(this).parent().parent().remove();
            if ($('.remove-favorites').length < 1) {
                location.reload();
            }
        })
    }

    $('.form-personal-data').ajaxForm(function () {
    });

    $('.form-personal-data').on('submit', function () {
        if ($('#loader-succefull').css('display') === 'none') {
            $('#loader').show().delay(1500).queue(function () {
                $(this).hide();
            });
            $('#loader-succefull').delay(1500).queue(function () {
                $(this).show();
            })
        }
    });

    $('.procces, .prep, .road, .delivered, .repeat-order, .remove-order').on('mouseover', function () {

        var position = $(this).offset();
        var window = $('#small-modal-window');
        var textDiv = window.find('p');
        var thisClass = this.className;
        window.css({'top': position.top + 30, 'left': position.left});
        if (thisClass === 'procces') {
            textDiv.text('Заказ в обработке. Ожидайте звонка оператора.');
        } else if (thisClass === 'prep') {
            textDiv.text('Заказ готов к отправке. В самое ближайшее время заказ будет отправлен.')
        } else  if (thisClass === 'road') {
            textDiv.text('Заказ уже в пути. Ожидайте звонка!')
        } else if (thisClass === 'delivered') {
            textDiv.text('Заказ доставлен.')
        } else if (thisClass.split(' ')[0] === 'repeat-order') {
            textDiv.text('Нажмите на эту кнопку, если хотите повторить этот заказ')
        } else if (thisClass.split(' ')[0] === 'remove-order') {
            textDiv.html('Удалить заказ из базы данных. <b>ВНИМАНИЕ!</b> После удаления заказ не восстановить.')
        }
        window.show();
    });

    $('.procces, .prep, .road, .delivered, .repeat-order, .remove-order').on('mouseout', function () {
        $('#small-modal-window').hide()
    });

    $('.remove-order').on('click', function () {
        var id = $(this).attr('id');
        $.post('/order/remove/', {'id': id, 'csrfmiddlewaretoken': getCookie('csrftoken')});
        $(this).parent().parent().remove()
    });

});