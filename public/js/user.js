$(document).ready(function(){

    function bindInputs(){
        $('input').change(function(){
            var data = {}
            data[$(this).attr('name')] = $(this).val();
            $.ajax({
                method: "POST",
                url: "/user",
                data: data
            }).done(function() {

            });
        });
    }

    function init(){
        bindInputs();
    }
    init();
});
