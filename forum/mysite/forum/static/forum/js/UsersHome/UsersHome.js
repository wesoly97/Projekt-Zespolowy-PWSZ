$(window).resize(function(){
    if($( window ).width()<1000){
        $('#splitter').removeClass("w-100");
    }
    else{
        $('#splitter').addClass("w-100");
    }
});

$('#buttonHistory').click(function(){
    ajaxCall1();
})
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
$('#buttonForum').click(function(){
    ajaxCall2();
})
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