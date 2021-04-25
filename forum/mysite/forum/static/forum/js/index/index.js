
$(document).ready(function(){
    //setTopSpange();
    let showFirstSvg = true;
    let showSecondSvg = true;
    let showThirdSvg = true;
    let showNumber = true;

   

    $(window).on('scroll', function(){
        showNumbers();
        //setTopSpange();
    });

    $(window).resize(function(){
        //setTopSpange();
        responsiveSvgs();
    });

    responsiveSvgs();
    //setTopSpange();
/*
function setTopSpange(){
    let topPos1 = parseInt($('#info').css('height'), 10);
    let topPos2 = $('#info').offset().top;
    let topPos3 = parseInt($('#spange').css('height'), 10);
    let topPosSpange = topPos1+topPos2-topPos3;
    $('#spange').css('top',topPosSpange +'px');
}
*/
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
        let tests = new countUp.CountUp('tests', 12640, options);
        let tasks = new countUp.CountUp('tasks', 2200, options);
        let users = new countUp.CountUp('users', 46352, options);

        if($(window).scrollTop()>=200 && $(window).scrollTop()<=1270){
            tests.start();
            tasks.start();
            users.start();
            showNumber = false;
        }
    }
}

function showSvgs(){
    if(showFirstSvg){
        if($(window).scrollTop()>=600 && $(window).scrollTop()<=1540){
            showFirstSvg = false;
            $('.infoImgs:nth-child(1)').css('display', 'block');
        }
    }
    if(showSecondSvg){
        if($(window).scrollTop()>=1205 && $(window).scrollTop()<=2200){
            showSecondSvg = false;
            $('.infoImgs:nth-child(2)').css('display', 'block');
        }
    }
    if(showThirdSvg){
        if($(window).scrollTop()>=900 && $(window).scrollTop()<=1800){
            showThirdSvg = false;
            $('.infoImgs:nth-child(3)').css('display', 'block');
        }
    }
}




});

const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursor");

const textArray = ["LEPIEJ", "SZYBCIEJ", "MOCNIEJ"];
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


/*
// Make the DIV element draggable:
dragElement(document.getElementById("spange"));

function dragElement(element) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    element.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = DragElementOff;
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        element.style.top = (element.offsetTop - pos2) + "px";
        element.style.left = (element.offsetLeft - pos1) + "px";
    }
    function DragElementOff() {
        document.onmouseup = null;
        document.onmousemove = null;
    }

}

*/