createMathquill("Question");
createMathquill("Answer");
createMathquill("A");
createMathquill("B");
createMathquill("C");
createMathquill("D");
function clearInputs(){
    $("div[id^='QueDiv']").css("outline","0");
    $("div[id^='QueDiv']").css("-webkit-box-shadow","none");
    $("div[id^='QueDiv']").css("box-shadow","none");
    $("div[id^='QueDiv']").css("border-color","white");
}
function focusInput(name){
    $(name).css("border-color","#66afe9");
    $(name).css("outline","0");
    $(name).css("-webkit-box-shadow","0 0 0 0.2rem rgba(102,175,233,.5)");
    $(name).css("box-shadow","0 0 0 0.2rem rgba(102,175,233,.5)");
    $(name).css("border-color","#66afe9");
}
function createMathquill(id)
{

let answerMathField2 = MQ.MathField(document.getElementById('mathQuill'+id), {
handlers: {
     edit: function() {
            answerMathField2.latex();
            document.getElementById('latex'+id).textContent = answerMathField2.latex();
        }
    }
});

$('#QueDiv'+id ).click( function(e) {
    clearInputs();
    answerMathField2.focus();
    focusInput(this);
});
$( "#sqrt"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\sqrt{}');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});

$( "#mld"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\cdot');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$( "#plus"+id).click(function() {
    clearInputs();
    answerMathField2.write('+');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$( "#minus"+id).click(function() {
    clearInputs();
    answerMathField2.write('-');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$( "#przecinek"+id).click(function() {
    clearInputs();
    answerMathField2.write(',');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$( "#pi"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\pi');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$( "#dzielenie"+id ).click(function() {
    clearInputs();
    answerMathField2.write('\\frac{ }{ }');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$( "#potega"+id ).click(function() {
    clearInputs();
    answerMathField2.write('\\^{}');
    answerMathField2.reflow();
    answerMathField2.focus();
});
$( "#cbrt"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\sqrt[]{}');
    answerMathField2.reflow();
    answerMathField2.focus();
});

}
