createMathquill("Question");
createMathquill("Answer");
createMathquill("A");
createMathquill("B");
createMathquill("C");
createMathquill("D");
function createMathquill(id) {
  let answerMathField2 = MQ.MathField(
    document.getElementById("mathQuill" + id),
    {
      handlers: {
        edit: function () {
          answerMathField2.latex();
          document.getElementById(
            "latex" + id
          ).textContent = answerMathField2.latex();
        },
      },
    }
  );

  $("#sqrt" + id).click(function () {
    answerMathField2.write("\\sqrt{}");
    answerMathField2.reflow();
  });

  $("#pi" + id).click(function () {
    answerMathField2.write("\\pi");
    answerMathField2.reflow();
  });
  $("#dzielenie" + id).click(function () {
    answerMathField2.write("\\frac{ }{ }");
    answerMathField2.reflow();
  });
  $("#potega" + id).click(function () {
    answerMathField2.write("\\^{}");
    answerMathField2.reflow();
  });
  $("#cbrt" + id).click(function () {
    answerMathField2.write("\\sqrt[]{}");
    answerMathField2.reflow();
  });
  $("#przerwa" + id).click(function () {
    answerMathField2.write("\\textcolor{black}{\\text{}}");
    answerMathField2.reflow();
  });
  $( "#calka"+id).click(function() {
    answerMathField2.write('\\ \\int');
    answerMathField2.reflow();
});
$("#suma"+id).click(function() {
    answerMathField2.write('\\sum');
    answerMathField2.reflow();
});
$("#log"+id).click(function() {
    answerMathField2.write('\\log_{}{}');
    answerMathField2.reflow();
});
$("#newton"+id).click(function() {
    answerMathField2.write('\\binom{ }{ }');
    answerMathField2.reflow();
});
$("#Alfa"+id).click(function() {
    answerMathField2.write('\\alpha');
    answerMathField2.reflow();
});
$("#Beta"+id).click(function() {
    answerMathField2.write('\\beta');
    answerMathField2.reflow();
});

$("#le"+id).click(function() {
    answerMathField2.write('\\le');
    answerMathField2.reflow();
});

$("#ge"+id).click(function() {
    answerMathField2.write('\\ge');
    answerMathField2.reflow();
});

$("#nalezy"+id).click(function() {
    answerMathField2.write('\\isin');
    answerMathField2.reflow();
});
$("#index"+id).click(function() {
    answerMathField2.write('{}_{}^{}');
    answerMathField2.reflow();
});
$("#inf"+id).click(function() {
    answerMathField2.write('\\infin');
    answerMathField2.reflow();
});
}
