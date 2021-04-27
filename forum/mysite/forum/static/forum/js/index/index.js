
$(document).ready(function(){
    let showFirstSvg = true;
    let showSecondSvg = true;
    let showThirdSvg = true;
    let showNumber = true;

   
    $(window).on('scroll', function(){
        showNumbers();
    });

    $(window).resize(function(){
        responsiveSvgs();
    });
    showNumbers();
    responsiveSvgs();

    function responsiveSvgs(){
        if($(window).width()>=1200){
            showSvgs();
            $(window).on('scroll', function(){
                showSvgs();
            });
            if(!showFirstSvg) $('.infoImgs:nth-child(1)').css('display', 'block');
            if(!showSecondSvg) $('.infoImgs:nth-child(2)').css('display', 'block');
            if(!showThirdSvg) $('.infoImgs:nth-child(3)').css('display', 'block');
        }
        else{
            $('.infoImgs:nth-child(1)').css('display', 'none');
            $('.infoImgs:nth-child(2)').css('display', 'none');
            $('.infoImgs:nth-child(3)').css('display', 'none');
        }
    }

    function showNumbers(){
        if(showNumber){
            const options = {
                duration: 3,
            };
            let tests = new countUp.CountUp('tests', NumberDone, options);
            let tasks = new countUp.CountUp('tasks', numberQuestion, options);
            let users = new countUp.CountUp('users', userNumber, options);

            if($(window).scrollTop()>=200 && $(window).scrollTop()<=1190){
                tests.start();
                tasks.start();
                users.start();
                showNumber = false;
            }
        }
    }

    function showSvgs(){
        if(showFirstSvg){
            if($(window).scrollTop()>=450 && $(window).scrollTop()<=1330){
                showFirstSvg = false;
                $('.infoImgs:nth-child(1)').css('display', 'block');
            }
        }
        if(showSecondSvg){
            if($(window).scrollTop()>=750 && $(window).scrollTop()<=1450){
                showSecondSvg = false;
                $('.infoImgs:nth-child(3)').css('display', 'block');
            }
        }
        if(showThirdSvg){
            if($(window).scrollTop()>=1000 && $(window).scrollTop()<=1650){
                showThirdSvg = false;
                $('.infoImgs:nth-child(2)').css('display', 'block');
            }
        }
    }

});

const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursor");

const textArray = ["WYDAJNIEJ", "SZYBCIEJ", "EFEKTYWNIEJ"];
const typingDelay = 200;
const erasingDelay = 100;
const newTextDelay = 2000; // Delay between current and next text
let textArrayIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < textArray[textArrayIndex].length) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
  	setTimeout(erase, newTextDelay);
  }
}

function erase() {
	if (charIndex > 0) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
    charIndex--;
    setTimeout(erase, erasingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
    textArrayIndex++;
    if(textArrayIndex>=textArray.length) textArrayIndex=0;
    setTimeout(type, typingDelay + 1100);
  }
}

document.addEventListener("DOMContentLoaded", function() { // On DOM Load initiate the effect
  if(textArray.length) setTimeout(type, newTextDelay + 250);
});