createMathquill("Question");
createMathquill("Answer");
createMathquill("A");
createMathquill("B");
createMathquill("C");
createMathquill("D");
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


$( "#sqrt"+id).click(function() {
answerMathField2.write('\\sqrt{}');
answerMathField2.reflow();
});

$( "#mld"+id).click(function() {
answerMathField2.write('\\cdot');
answerMathField2.reflow();
});
$( "#plus"+id).click(function() {
answerMathField2.write('+');
answerMathField2.reflow();
});
$( "#minus"+id).click(function() {
answerMathField2.write('-');
answerMathField2.reflow();
});
$( "#przecinek"+id).click(function() {
answerMathField2.write(',');
answerMathField2.reflow();
});
$( "#pi"+id).click(function() {
answerMathField2.write('\\pi');
answerMathField2.reflow();
});
$( "#dzielenie"+id ).click(function() {
answerMathField2.write('\\frac{ }{ }');
answerMathField2.reflow();
});
$( "#potega"+id ).click(function() {
answerMathField2.write('\\^{}');
answerMathField2.reflow();
});
$( "#cbrt"+id).click(function() {
answerMathField2.write('\\sqrt[]{}');
answerMathField2.reflow();
});

}
