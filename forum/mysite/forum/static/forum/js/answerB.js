let answerSpanB = document.getElementById('answerB');
let latexSpanB = document.getElementById('latexB');
let answerMathFieldB = MQ.MathField(answerSpanB, {
handlers: {
     edit: function() {
        let enteredMath = answerMathFieldB.latex(); // Get entered math in LaTeX format
            latexSpanB.textContent = answerMathFieldB.latex();
        }
    }
});
 $( "#sqrtB" ).click(function() {
    answerMathFieldB.write('\\sqrt{}');
    answerMathFieldB.reflow();
});

$( "#mldB" ).click(function() {
    answerMathFieldB.write('\\cdot');
    answerMathFieldB.reflow();
});
$( "#plusB" ).click(function() {
    answerMathFieldB.write('+');
    answerMathFieldB.reflow();
});
$( "#minusB" ).click(function() {
    answerMathFieldB.write('-');
    answerMathFieldB.reflow();
});
$( "#przecinekB" ).click(function() {
    answerMathFieldB.write(',');
    answerMathFieldB.reflow();
});
$( "#piB" ).click(function() {
    answerMathFieldB.write('\\pi');
    answerMathFieldB.reflow();
});
$( "#dzielenieB" ).click(function() {
    answerMathFieldB.write('\\frac{ }{ }');
    answerMathFieldB.reflow();
});
$( "#potegaB" ).click(function() {
    answerMathFieldB.write('\\^{}');
    answerMathFieldB.reflow();
});
$( "#cbrtB" ).click(function() {
    answerMathFieldB.write('\\sqrt[]{}');
    answerMathFieldB.reflow();
});
