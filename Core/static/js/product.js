$(document).ready(function() {

    $('.up').on('click', function () {
        var input = $(this).siblings('input[name="count"]');
        var last_value = input.val();
        input.val(+last_value + 1);
        input.keyup();
    });
    $('.down').on('click', function () {
        var input = $(this).siblings('input[name="count"]');
        var last_value = input.val();
        input.val(+last_value - 1);
        input.keyup();
    });
    $('input[name="count"]').on('input keyup', function () {
        var max_count = $(this).siblings('.max-count-product').val();
        if ($(this).val() < 1 || this.value.match(/[^0-9]/g)) {
            ($(this).val(1));
            return false;
        }
        if ($(this).val() > parseInt(max_count)) {
            ($(this).val(max_count));
            var position = $(this).offset();
            var window = $('#small-modal-window');
            var textDiv = window.find('p');
            window.css({'top': position.top + 30, 'left': position.left});
            textDiv.text('К сожалению, у нас осталось всего ' + max_count + ' ед. этого продукта.');
            window.show();
            setTimeout(function () {window.hide()}, 6000);
            return false
        }
    });


    $.get("/basket/get_ids_product_in_basket", function (data) {
        var buttons = $('.basket-button');
        var button;
        for (var i=0;i<buttons.length;i++) {
            button = buttons.eq(i);
            if (button.attr('id') in data) {
                change_button(button)
            }
        }
    })

});
