$(document).ready(function() {

    if (~location.href.indexOf('?all=')) {
        $('#content h1').text('Осуществите поиск по всем элементам или ' + $('#content h1').text());
        $('.field-__str__').parent().css({'background': 'white'});
        $('.actions label').before('<label style="height:24px">' +
            '<input id="value" style="margin-right: 10px; height: 12px" type="text" placeholder="Начните вводить...">' +
            '<span hidden id="search-info" style="margin-right: 10px; font-size: 13px">Найдено ' +
            '<span style="font-weight: bold;color:#447e9b;" id="result"></span> из <span style="font-weight: bold;color:#447e9b;" id="amount"></span> объектов</span></label>')
    } else {
        var all_loc = location.href + '?all=';
        $('.actions label').before('<button id="all" style="margin-right: 10px" type="button" class="button" title="Поиск по элементам">Открыть список всех элементов для поиска</button>');
        $('#all').on('click', function () {
            window.location.href = all_loc
        })
    }

    $('#changelist-form').on('keyup keypress', function(e) {
        var keyCode = e.keyCode || e.which;
        if (keyCode === 13) {
            e.preventDefault();
            return false;
        }
    });

    $('#value').on('input', function () {
        var table_item = $('.field-__str__');
        var value = $('#value').val().toLowerCase();
        var table_item_children;
        var item;
        var count = 0;

        if (value) {
            table_item.parent().hide();
            $('.paginator').hide();
            $('.action-counter').hide();
            $('#search-info').show()
        } else {
            table_item.parent().show();
            $('.paginator').show();
            $('.action-counter').show();
            $('#search-info').hide()
        }

        for (var i=0; i<table_item.length; i++) {
            table_item_children = table_item.eq(i).children();
            for (var j=0; j<table_item_children.length; j++) {
                item = table_item_children.eq(j).text().toLowerCase();
                if (~item.indexOf(value)) {
                    table_item.eq(i).parent().show();
                    count += 1;
                    break
                }
            }
        }
        $('#result').text(count);
        $('#amount').text(table_item.length)
    })
});