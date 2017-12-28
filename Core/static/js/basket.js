$(document).ready(function() {
    function get_basket() {
        $.get("/basket/get_data_basket", function (data) {

            $('#count').text(data.number_product_in_basket);
            $('#count-price').text(data.total_amount + ' р.');
        })}

    $('input[name="count-in-basket"]').on('input keyup', function() {
        var max_count = $(this).siblings('.max-count-product').val();
        if ($(this).val() < 1 || this.value.match(/[^0-9]/g)) {
            ($(this).val(1));
            return false;
        }
        if ($(this).val() > parseInt(max_count)) {
            $(this).val(max_count);
            var position = $(this).offset();
            var window = $('#small-modal-window');
            var textDiv = window.find('p');
            window.css({'top': position.top + 30, 'left': position.left});
            textDiv.text('К сожалению, у нас осталось всего ' + max_count + ' ед. этого продукта.');
            window.show();
            setTimeout(function () {window.hide()}, 6000);
        }
        $(this).siblings('.button-create-count').click();
        get_basket();
        weight_price_basket();
        amount_basket()
    });

    $('.up').on('click', function () {
        var input = $(this).siblings('input[name="count-in-basket"]');
        var last_value = input.val();
        input.val(+last_value + 1);
        input.keyup();
    });
    $('.down').on('click', function () {
        var input = $(this).siblings('input[name="count-in-basket"]');
        var last_value = input.val();
        input.val(+last_value - 1);
        input.keyup();
    });

    $('.delete-element').on('click', function () {
        $.ajax({
            url: 'delete/',
            type: 'POST',
            data: {'csrfmiddlewaretoken': getCookie('csrftoken'), 'id': $(this).attr('id')}
        });
        $(this).parent().parent().parent().remove();
        get_basket();
        amount_basket();
        if ($('.delete-element').length < 1) {
            location.reload();
        }
    });

    function weight_price_basket() {
        var colWeight = $('.weight-basket');
        var count;
        for (var i=0; i < colWeight.length; i++) {
            count = colWeight.eq(i).siblings('.count-basket').children().find('input[name="count-in-basket"]').val();
            colWeight.eq(i).children().eq(0).text(colWeight.eq(i).children().eq(0).attr('id') * count + ' г.');
            colWeight.eq(i).next().children().eq(0).text(colWeight.eq(i).next().children().eq(0).attr('id') * count);
        }
    }

    weight_price_basket();

    function amount_basket() {
        var colWeight = $('.weight-basket');
        var colPrice = $('.price-basket');
        var colCount = $('.input-count');
        var colSale = $('.sale');
        var amount_weight = 0;
        var amount_price = 0;
        var amount_count = 0;
        var amount_sale = 0;

        for (var i=0; i<colWeight.length;i++) {
            amount_price += parseInt(colPrice.eq(i).children().eq(0).text());
            amount_weight += parseInt(colWeight.eq(i).children().eq(0).text());
            amount_count += parseInt(colCount.eq(i).val());
            if (parseInt(colSale.eq(i).children().text())) {
                amount_sale += parseInt(colPrice.eq(i).children().eq(0).text())/(100 - parseInt(colSale.eq(i).children().text()))*100 - parseInt(colPrice.eq(i).children().eq(0).text())
            }
        }
        $('#amount-weight').text(amount_weight);
        $('#amount-price').text(amount_price);
        $('#amount-count').text(amount_count);
        $('#amount-sale').text(Math.round(amount_sale));
    }

    amount_basket()

});