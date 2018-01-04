$(document).ready(function() {

    function page() {

        var objects = $('.table-item');
        objects.hide();

        var number_objects_on_page = 10;
        var max_numbers_pages = Math.ceil(objects.length / number_objects_on_page);

        objects.slice(0, number_objects_on_page).show();

        for (var i=0; i<max_numbers_pages; i++) {
            $('#pages').find('span').append('<a class="page" id="' + (i+1) + '">' + (i+1) + '</a>'  )
        }

        $('.page').eq(0).addClass('current-page');

        $('.page').on('click', function () {
            var number = $(this).attr('id');
            $('.page').removeClass('current-page');
            $(this).addClass('current-page');
            objects.hide();
            objects.slice(number_objects_on_page * (number - 1), number_objects_on_page * number).show();
        })

    }

    page();

    $('#search').on('submit', function (e) {
        e.preventDefault();
        var table_item = $('.table-item');
        var value = $(this).find('input').val();
        var table_item_children;
        if (value) {
            table_item.hide();
        } else {
            return false
        }
        for (var i=0; i<table_item.length; i++) {
            table_item_children = table_item.eq(i).children();
            for (var j=0; j<table_item_children.length; j++) {
                if (~table_item_children.eq(j).text().indexOf(value)) {
                    table_item.eq(i).show();
                    break
                }
            }
        }
    })
});