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

   

    $('#buttonForum').click(function(){
        ajaxCall2();
    });

    $('#buttonHistory').click(function(){
        ajaxCall1();
    });
    $('#buttonStats').click(function(){
        ajaxCall3();
    });

    function ajaxCall1() {
        var s = $('#buttonHistory').attr("data-url");
        $('body').removeClass("loaded");
        window.location.href = s;
    }
    
    function ajaxCall2() {
        var s = $('#buttonForum').attr("data-url");
        $('body').removeClass("loaded");
        window.location.href = s;
        
    }
    function ajaxCall3() {
        var s = $('#buttonStats').attr("data-url");
        $('body').removeClass("loaded");
        window.location.href = s;
    }

});
