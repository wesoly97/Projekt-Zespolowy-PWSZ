$(document).ready(function(){
    $(window).resize(function(){
        if($( window ).width()<1000){
            $('#splitter').removeClass("w-100");
            
        }
        else if($( window ).width()<1827){
            
            $('.col-sm').addClass("col-sm-auto");
            $('#coldel').removeClass("offset-sm-2");
            
        }
        else{
            $('#splitter').addClass("w-100");
            $('.kk').removeClass("col-sm-auto");
            $('.kk').addClass("col-sm");
            $('#coldel').addClass("offset-sm-2");
            $('#coldel').addClass("col-sm-auto");
            
           
        }
    });

    if($( window ).width()<1000){
        $('#splitter').removeClass("w-100");
    }
    else{
        $('#splitter').addClass("w-100");
    }

    $('#buttonForum').click(function(){
        ajaxCall2();
    });

    $('#buttonHistory').click(function(){
        ajaxCall1();
    });

    function ajaxCall1() {
        var s = $('#buttonHistory').attr("data-url");
        $('body').removeClass("loaded");
        return  $.ajax({
            url: s,
            success: function(result){
                $('body').html(result);
            }
        });
    }
    
    function ajaxCall2() {
        var s = $('#buttonForum').attr("data-url");
        $('body').removeClass("loaded");
        return  $.ajax({
            url: s,
            success: function(result){
                $('body').html(result);
            }
        });
    }

});
