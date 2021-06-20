$(document).ready(function(){
  

   

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
