let answerSpanA = document.getElementById('answerA');
let latexSpanA = document.getElementById('latexA');
let answerMathFieldA = MQ.MathField(answerSpanA, {
handlers: {
     edit: function() {
        let enteredMath = answerMathFieldA.latex(); // Get entered math in LaTeX format
            latexSpanA.textContent = answerMathFieldA.latex();
        }
    }
});
 $( "#sqrtA" ).click(function() {
    answerMathFieldA.write('\\sqrt{}');
    answerMathFieldA.reflow();
});

$( "#mldA" ).click(function() {
    answerMathFieldA.write('\\cdot');
    answerMathFieldA.reflow();
});
$( "#plusA" ).click(function() {
    answerMathFieldA.write('+');
    answerMathFieldA.reflow();
});
$( "#minusA" ).click(function() {
    answerMathFieldA.write('-');
    answerMathFieldA.reflow();
});
$( "#przecinekA" ).click(function() {
    answerMathFieldA.write(',');
    answerMathFieldA.reflow();
});
$( "#piA" ).click(function() {
    answerMathFieldA.write('\\pi');
    answerMathFieldA.reflow();
});
$( "#dzielenieA" ).click(function() {
    answerMathFieldA.write('\\frac{ }{ }');
    answerMathFieldA.reflow();
});
$( "#potegaA" ).click(function() {
    answerMathFieldA.write('\\^{}');
    answerMathFieldA.reflow();
});
$( "#cbrtA" ).click(function() {
    answerMathFieldA.write('\\sqrt[]{}');
    answerMathFieldA.reflow();
});
