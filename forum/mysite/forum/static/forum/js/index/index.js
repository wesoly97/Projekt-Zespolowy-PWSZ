
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

const test = new Letterize({
    targets: ".animate-me"
});

const animation = anime.timeline({
    targets: test.listAll,
    delay: anime.stagger(100, {
        grid: [test.list[0].length, test.list.length],
        from: "center"
    }),
    loop: true
});

animation
.add({
    scale: 0.5
}).add({
    letterSpacing: anime.random(10,15)
}).add({
    scale: 1.5
}).add({
    letterSpacing: "6px"
});

const animation1 = anime.timeline({
    targets: 'header > div',
    delay: anime.stagger(100, {
        from: "center"
    }),
    loop: true
});

animation1.add({
    background: 'linear-gradient(45deg, #f3ec78, #af4261)'
}, 0).add({
    'background-size': '100%'
}).add({
    background: 'linear-gradient(45deg, #124215, #642673)'
}, 0).add({
    'background-size': '100%'
});