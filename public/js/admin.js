$(document).ready(function(){

    function getURIParameter(param, asArray) {
        return document.location.search.substring(1).split('&').reduce(function(p,c) {
            var parts = c.split('=', 2).map(function(param) { return decodeURIComponent(param); });
            if(parts.length == 0 || parts[0] != param) return (p instanceof Array) && !asArray ? null : p;
            return asArray ? p.concat(parts.concat(true)[1]) : parts.concat(true)[1];
        }, []);
    }

    function bindMap(){
        if ( $('div.map').length < 1 ){
            return;
        }
        $.each( $('div[model="city"]'),function(){
            var posX = $(this).find('[name="pos_x"]').attr('value');
            var posY = $(this).find('[name="pos_y"]').attr('value');
            var name = $(this).find('[name="name"]').attr('value');
            name = name.charAt(0).toUpperCase() + name.slice(1);
            var city = $(
                '<div class="city">' +
                    '<img src="img/city.png" />' +
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


    function bindSelect(){
        $('select:not([multiple])').select2();
        $.each($('select[multiple="true"]'),function(){
            var valuesElement = $(this).parent().parent().find('.link-values');
            var name = $(this).attr('name');
            $(this).select2().on("select2:select select2:unselect", function(e) {
                var valuesElement = $(this).parent().parent().find('.link-values');
                var name = $(this).attr('name');
                switch (e.type) {
                    case "select2:select":
                        for( index in $(this).val() ){
                            var id = $(this).val()[index];
                            var text = $(this).select2('data')[index].text;
                            if ( $(valuesElement).find('div.fieldbox[name="'+id+'"]').length == 0 && e.type == "select2:select" ) {
                                var valueElement = '<div class="fieldbox" name="'+id+'">' +
                                    '<label>Värde för '+text+'</label>' +
                                    '<input type="text" name="'+name+'--'+id+'--value"/>' +
                                '</div>';
                                $(valuesElement).append(valueElement);
                            }
                        }
                        break;
                    case "select2:unselect":
                        var values = $(this).val();
                        if ( !values ){
                            $(valuesElement).empty();
                        }else{
                            $.each( $(valuesElement).find('div.fieldbox'), function(){
                                console.log(values, $(this).attr('name') );
                                if (values.indexOf($(this).attr('name')) == -1){
                                    $(this).remove();
                                }
                            } );
                        }
                        break;
                }
            });
            for( index in $(this).val() ){
                var id = $(this).val()[index];
                var text = $(this).select2('data')[index].text;
                if ( $(valuesElement).find('div.fieldbox[name="'+id+'"]').length == 0 ) {
                    var valueElement = '<div class="fieldbox" name="'+id+'">' +
                        '<label>Värde för '+text+'</label>' +
                        '<input type="text" name="'+name+'--'+id+'--value"/>' +
                    '</div>';
                    $(valuesElement).append(valueElement);
                }
            }
        });
    }

    function bindAdminForms(){
        $('button[edit]').click(function(){
            var id = $(this).attr('edit');
            $( 'form[edit-instance="'+id+'"]' ).toggle();
        });
    }

    function formToTop(){
        var formId = getURIParameter('form-success', false);
        if ( !formId ){
            show();
            return;
        }
        $('body').prepend($('div#'+formId+'-container'));
        show();
        $('div#'+formId+'-container>form').find('input#name').focus();
        $('div#'+formId+'-container>form').find('input#name').focus();
        var type = getURIParameter('type', false);
        if ( !type ){
            return;
        }
        $('form[form-id="'+formId+'"] select[name="type"]').val( type ).trigger("change");;
    }

    function show(){
        $('body').show();
    }

    function init(){
        formToTop();
        setTimeout( function(){
            bindMap();
            bindAdminForms();
            bindSelect();
        }, 100 );
    }


    init();


});
