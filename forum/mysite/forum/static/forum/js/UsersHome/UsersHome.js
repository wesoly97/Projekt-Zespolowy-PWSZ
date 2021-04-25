$(window).resize(function(){
    if($( window ).width()<1000){
        $('#splitter').removeClass("w-100");
        
    }
    else{
        $('#splitter').addClass("w-100");
    }
});
