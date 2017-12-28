$(document).ready(function() {

    var container_small_image = $('.small-image');
    for (var i=0; i < container_small_image.length; i++) {
        container_small_image.eq(i).attr('id', i);
    }

    container_small_image.eq(0).addClass('active');

    $('.small-image').on('click', function () {
        var id = $(this).attr('id');
        var data = $('.input-hide').eq(id).val();
        $('#big-image').attr('src', '/media/' + data);
        $('.active').removeClass('active');
        container_small_image.eq(parseInt(id)).addClass('active')
    });

});