let answerSpan2 = document.getElementById('answer');
let latexSpan2 = document.getElementById('latex2');
let answerMathField2 = MQ.MathField(answerSpan2, {
handlers: {
     edit: function() {
        let enteredMath = answerMathField2.latex(); // Get entered math in LaTeX format
            latexSpan2.textContent = answerMathField2.latex();
        }
    }
});
 $( "#sqrt2" ).click(function() {
    answerMathField2.write('\\sqrt{}');
    answerMathField2.reflow();
});

$( "#mld2" ).click(function() {
    answerMathField2.write('\\cdot');
    answerMathField2.reflow();
});
$( "#plus2" ).click(function() {
    answerMathField2.write('+');
    answerMathField2.reflow();
});
$( "#minus2" ).click(function() {
    answerMathField2.write('-');
    answerMathField2.reflow();
});
$( "#przecinek2" ).click(function() {
    answerMathField2.write(',');
    answerMathField2.reflow();
});
$( "#pi2" ).click(function() {
    answerMathField2.write('\\pi');
    answerMathField2.reflow();
});
$( "#dzielenie2" ).click(function() {
    answerMathField2.write('\\frac{ }{ }');
    answerMathField2.reflow();
});
$( "#potega2" ).click(function() {
    answerMathField2.write('\\^{}');
    answerMathField2.reflow();
});
$( "#cbrt2" ).click(function() {
    answerMathField2.write('\\sqrt[]{}');
    answerMathField2.reflow();
});
