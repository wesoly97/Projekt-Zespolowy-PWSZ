let answerSpan = document.getElementById('question');
let latexSpan = document.getElementById('latex');
let questionInput = document.getElementById('input_question');

let answerMathField = MQ.MathField(answerSpan, {
handlers: {
     edit: function() {
        let enteredMath = answerMathField.latex(); // Get entered math in LaTeX format
            latexSpan.textContent = answerMathField.latex();
            
        }
    }
});

 $( "#sqrt" ).click(function() {
    
    answerMathField.write('\\sqrt{}');
    answerMathField.reflow();
});

$( "#mld" ).click(function() {
    answerMathField.write('\\cdot');
    answerMathField.reflow();
});
$( "#plus" ).click(function() {
    answerMathField.write('+');
    answerMathField.reflow();
});
$( "#minus" ).click(function() {
    answerMathField.write('-');
    answerMathField.reflow();
});
$( "#przecinek" ).click(function() {
    answerMathField.write(',');
    answerMathField.reflow();
});
$( "#pi" ).click(function() {
    answerMathField.write('\\pi');
    answerMathField.reflow();
});
$( "#dzielenie" ).click(function() {
    answerMathField.write('\\frac{ }{ }');
    answerMathField.reflow();
});
$( "#potega" ).click(function() {
    answerMathField.write('\\^{}$$');
    answerMathField.reflow();
});
$( "#cbrt" ).click(function() {
    answerMathField.write('\\sqrt[]{}');
    answerMathField.reflow();
});
