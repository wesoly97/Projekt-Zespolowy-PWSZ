let answerSpanC = document.getElementById('answerC');
let latexSpanC = document.getElementById('latexC');
let answerMathFieldC = MQ.MathField(answerSpanC, {
handlers: {
     edit: function() {
        let enteredMath = answerMathFieldC.latex(); // Get entered math in LaTeX format
            latexSpanC.textContent = answerMathFieldC.latex();
        }
    }
});
 $( "#sqrtC" ).click(function() {
    answerMathFieldC.write('\\sqrt{}');
    answerMathFieldC.reflow();
});

$( "#mldC" ).click(function() {
    answerMathFieldC.write('\\cdot');
    answerMathFieldC.reflow();
});
$( "#plusC" ).click(function() {
    answerMathFieldC.write('+');
    answerMathFieldC.reflow();
});
$( "#minusC" ).click(function() {
    answerMathFieldC.write('-');
    answerMathFieldC.reflow();
});
$( "#przecinekC" ).click(function() {
    answerMathFieldC.write(',');
    answerMathFieldC.reflow();
});
$( "#piC" ).click(function() {
    answerMathFieldC.write('\\pi');
    answerMathFieldC.reflow();
});
$( "#dzielenieC" ).click(function() {
    answerMathFieldC.write('\\frac{ }{ }');
    answerMathFieldC.reflow();
});
$( "#potegaC" ).click(function() {
    answerMathFieldC.write('\\^{}');
    answerMathFieldC.reflow();
});
$( "#cbrtC" ).click(function() {
    answerMathFieldC.write('\\sqrt[]{}');
    answerMathFieldC.reflow();
});
