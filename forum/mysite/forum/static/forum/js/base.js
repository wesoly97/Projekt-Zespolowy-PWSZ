$(document).ready(function(){
    let disable = false;
    $('.navbar-toggler').click(function(){
        if(!disable){
            disable = true;
            $('.hamburger > span:nth-child(1) ').toggleClass('hamburger-top');
            $('.hamburger > span:nth-child(2) ').toggleClass('hamburger-middle');
            $('.hamburger > span:nth-child(3) ').toggleClass('hamburger-bottom');
            setTimeout(function() { 
                console.log("Szymon");
                disable = false;
            }, 370);
        }
    });
});