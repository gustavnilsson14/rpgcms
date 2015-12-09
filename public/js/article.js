$(document).ready(function(){

    function bindMap(){
        if ( $('div.map').length < 1 ){
            return;
        }
        $.each( $('div.instance'),function(){
            var posX = $(this).attr('posx');
            var posY = $(this).attr('posy');
            var name = $(this).attr('name');
            name = name.charAt(0).toUpperCase() + name.slice(1);
            var city = $(
                '<div class="city">' +
                    '<img src="/img/city.png" />' +
                    '<p>'+ name +'</p>' +
                '</div>'
            );
            $( city ).css( 'left', posX + 'px' );
            $( city ).css( 'top', posY + 'px' );
            $('div.map').append( city );
        } );
        $('div.map').css('zoom', 0.5).click(function(e) {
            $(this).css('zoom', 1);
            var posX = Math.round( e.pageX - $(this).offset().left ) * 2;
            var posY = Math.round( e.pageY - $(this).offset().top ) * 2;
            var model = $(this).data( 'model' );
            $( 'form[data-model="'+model+'"]' ).find( '[mapx]' ).val(posX);
            $( 'form[data-model="'+model+'"]' ).find( '[mapy]' ).val(posY);
            $( 'div.city.current' ).css( 'left', posX + 'px' );
            $( 'div.city.current' ).css( 'top', posY + 'px' );
            $( 'div.city.current' ).show();
            $(this).css('zoom', 0.5);
        });
    }

    function init(){
        bindMap();
    }


    init();


});
