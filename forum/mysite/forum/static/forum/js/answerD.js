let answerSpanD = document.getElementById('answerD');
let latexSpanD = document.getElementById('latexD');
let answerMathFieldD = MQ.MathField(answerSpanD, {
handlers: {
     edit: function() {
        let enteredMath = answerMathFieldD.latex(); // Get entered math in LaTeX format
            latexSpanD.textContent = answerMathFieldD.latex();
        }
    }
});
 $( "#sqrtD" ).click(function() {
    answerMathFieldD.write('\\sqrt{}');
    answerMathFieldD.reflow();
});

$( "#mldD" ).click(function() {
    answerMathFieldD.write('\\cdot');
    answerMathFieldD.reflow();
});
$( "#plusD" ).click(function() {
    answerMathFieldD.write('+');
    answerMathFieldD.reflow();
});
$( "#minusD" ).click(function() {
    answerMathFieldD.write('-');
    answerMathFieldD.reflow();
});
$( "#przecinekD" ).click(function() {
    answerMathFieldD.write(',');
    answerMathFieldD.reflow();
});
$( "#piD" ).click(function() {
    answerMathFieldD.write('\\pi');
    answerMathFieldD.reflow();
});
$( "#dzielenieD" ).click(function() {
    answerMathFieldD.write('\\frac{ }{ }');
    answerMathFieldD.reflow();
});
$( "#potegaD" ).click(function() {
    answerMathFieldD.write('\\^{}');
    answerMathFieldD.reflow();
});
$( "#cbrtD" ).click(function() {
    answerMathFieldD.write('\\sqrt[]{}');
    answerMathFieldD.reflow();
});
