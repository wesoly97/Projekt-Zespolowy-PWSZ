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
    focusInput('#QueDiv'+id);
});
$( "#cbrt"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\sqrt[]{}');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#przerwa" + id).click(function () {
    clearInputs();
    answerMathField2.write("\\textcolor{black}{\\text{}}");
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
  });
  $( "#calka"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\ \\int');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#suma"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\sum');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#log"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\log_{}{}');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#newton"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\binom{ }{ }');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#Alfa"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\alpha');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#Beta"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\beta');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});

$("#le"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\le');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});

$("#ge"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\ge');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});

$("#nalezy"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\isin');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#index"+id).click(function() {
    clearInputs();
    answerMathField2.write('{}_{}^{}');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
$("#inf"+id).click(function() {
    clearInputs();
    answerMathField2.write('\\infin');
    answerMathField2.reflow();
    answerMathField2.focus();
    focusInput('#QueDiv'+id);
});
}


