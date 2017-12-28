$(document).ready(function() {

    $('.logist').on('click', function () {
        logistic(this)
    });

    function logistic(element) {
        $('#logist').text($(element).parent().next().next().children().text());
        price_amount_order()
    }

    function price_amount_order() {
        var prices = $('.price-amount');
        var counts = $('.count-amount');
        var amount = 0;
        for (var i=0; i<prices.length; i++) {
            amount += (parseInt(prices.eq(i).text()) * parseInt(counts.eq(i).text()));
        }
        amount += parseInt($('#logist').text());
        $('#amount-price-order').text(amount);
        $('#amount-price-order-input').val(amount)
    }


    $('#phone-order').mask('+7(999)999-99-99');

    if ('repeat' === document.location.pathname.split('/')[2]) {
        $.get("", function (data) {

            var radioLogistic = $('input[name=logistic]');
            var radioPayment = $('input[name=payment]');

            for (var i=0; i<radioLogistic.length; i++) {
                if (radioLogistic.eq(i).val() === data.logistic) {
                    radioLogistic.eq(i).attr('checked', 'true');
                    logistic(radioLogistic.eq(i));
                    break
                }
            }

            for (var q=0; q<radioPayment.length; q++ ) {
                if (radioPayment.eq(q).val() === data.payment) {
                    radioPayment.eq(q).attr('checked', 'true');
                    break
                }
            }
        })
    }
    price_amount_order();


});