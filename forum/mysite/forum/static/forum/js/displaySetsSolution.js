let solutionSpan = document.getElementById('solution0');
let SolutionlatexSpan = document.getElementById('latexsolution0');
let answerSpan2 = document.getElementById('answer0');
let latexSpan2 = document.getElementById('latexanswer0');

let solutionSpan1 = document.getElementById('solution1');
let SolutionlatexSpan1 = document.getElementById('latexsolution1');
let answerSpan12 = document.getElementById('answer1');
let latexSpan12 = document.getElementById('latexanswer1');

let answerMathField = MQ.MathField(solutionSpan, {
handlers: {
     edit: function() {
        let enteredMath = answerMathField.latex(); // Get entered math in LaTeX format
        SolutionlatexSpan.textContent = answerMathField.latex();
        }
    }
});
let answerMathField2 = MQ.MathField(answerSpan2, {
    handlers: {
         edit: function() {
            let enteredMath = answerMathField2.latex(); // Get entered math in LaTeX format
                latexSpan2.textContent = answerMathField2.latex();
            }
        }
    });

   
    let answerMathField1 = MQ.MathField(solutionSpan1, {
    handlers: {
         edit: function() {
            let enteredMath = answerMathField1.latex(); // Get entered math in LaTeX format
            SolutionlatexSpan1.textContent = answerMathField1.latex();
            }
        }
    });
    let answerMathField12 = MQ.MathField(answerSpan12, {
        handlers: {
             edit: function() {
                let enteredMath = answerMathField12.latex(); // Get entered math in LaTeX format
                    latexSpan12.textContent = answerMathField12.latex();
                }
            }
        });

    $( "#sqrtsolution0" ).click(function() {
        answerMathField.write('\\sqrt{}');
        answerMathField.reflow();
    });
    
    $( "#mldsolution0" ).click(function() {
        answerMathField.write('\\cdot');
        answerMathField.reflow();
    });
    $( "#plussolution0" ).click(function() {
        answerMathField.write('+');
        answerMathField.reflow();
    });
    $( "#minussolution0" ).click(function() {
        answerMathField.write('-');
        answerMathField.reflow();
    });
    $( "#przecineksolution0" ).click(function() {
        answerMathField.write(',');
        answerMathField.reflow();
    });
    $( "#pisolution0" ).click(function() {
        answerMathField.write('\\pi');
        answerMathField.reflow();
    });
    $( "#dzieleniesolution0" ).click(function() {
        answerMathField.write('\\frac{ }{ }');
        answerMathField.reflow();
    });
    $( "#potegasolution0" ).click(function() {
        answerMathField.write('\^{}');
        answerMathField.reflow();
    });
    $( "#cbrtsolution0" ).click(function() {
        answerMathField.write('\\sqrt[]{}');
        answerMathField.reflow();
    });

 $( "#sqrtanswer0" ).click(function() {
    answerMathField2.write('\\sqrt{}');
    answerMathField2.reflow();
});

$( "#mldanswer0" ).click(function() {
    answerMathField2.write('\\cdot');
    answerMathField2.reflow();
});
$( "#plusanswer0" ).click(function() {
    answerMathField2.write('+');
    answerMathField2.reflow();
});
$( "#minusanswer0" ).click(function() {
    answerMathField2.write('-');
    answerMathField2.reflow();
});
$( "#przecinekanswer0" ).click(function() {
    answerMathField2.write(',');
    answerMathField2.reflow();
});
$( "#pianswer0" ).click(function() {
    answerMathField2.write('\\pi');
    answerMathField2.reflow();
});
$( "#dzielenieanswer0" ).click(function() {
    answerMathField2.write('\\frac{ }{ }');
    answerMathField2.reflow();
});
$( "#potegaanswer0" ).click(function() {
    answerMathField2.write('\\^{}');
    answerMathField2.reflow();
});
$( "#cbrtanswer0 ").click(function() {
    answerMathField2.write('\\sqrt[]{}');
    answerMathField2.reflow();
});

    $( "#sqrtsolution1" ).click(function() {
        answerMathField1.write('\\sqrt{}');
        answerMathField1.reflow();
    });
    
    $( "#mldsolution1" ).click(function() {
        answerMathField1.write('\\cdot');
        answerMathField1.reflow();
    });
    $( "#plussolution1" ).click(function() {
        answerMathField1.write('+');
        answerMathField1.reflow();
    });
    $( "#minussolution1" ).click(function() {
        answerMathField1.write('-');
        answerMathField1.reflow();
    });
    $( "#przecineksolution1" ).click(function() {
        answerMathField1.write(',');
        answerMathField1.reflow();
    });
    $( "#pisolution1" ).click(function() {
        answerMathField1.write('\\pi');
        answerMathField1.reflow();
    });
    $( "#dzieleniesolution1" ).click(function() {
        answerMathField1.write('\\frac{ }{ }');
        answerMathField1.reflow();
    });
    $( "#potegasolution1" ).click(function() {
        answerMathField1.write('\^{}');
        answerMathField1.reflow();
    });
    $( "#cbrtsolution1" ).click(function() {
        answerMathField1.write('\\sqrt[]{}');
        answerMathField1.reflow();
    });

 $( "#sqrtanswer1" ).click(function() {
    answerMathField12.write('\\sqrt{}');
    answerMathField12.reflow();
});

$( "#mldanswer1" ).click(function() {
    answerMathField12.write('\\cdot');
    answerMathField12.reflow();
});
$( "#plusanswer1" ).click(function() {
    answerMathField12.write('+');
    answerMathField12.reflow();
});
$( "#minusanswer1" ).click(function() {
    answerMathField12.write('-');
    answerMathField12.reflow();
});
$( "#przecinekanswer1" ).click(function() {
    answerMathField12.write(',');
    answerMathField12.reflow();
});
$( "#pianswer1" ).click(function() {
    answerMathField12.write('\\pi');
    answerMathField12.reflow();
});
$( "#dzielenieanswer1" ).click(function() {
    answerMathField12.write('\\frac{ }{ }');
    answerMathField12.reflow();
});
$( "#potegaanswer1" ).click(function() {
    answerMathField12.write('\^{}');
    answerMathField12.reflow();
});
$( "#cbrtanswer1 ").click(function() {
    answerMathField12.write('\\sqrt[]{}');
    answerMathField12.reflow();
});
