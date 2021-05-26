let mathquill;

let specialKeys = {
  bksp: "Backspace",
  frac: "\\frac{}{}",
  sqrt: "\\sqrt{}",
  power: "{}^{}",
  lower: "{}_{}",
  exsqrt: "\\sqrt[]{}",
  integral: "\\int",
  integral2: "\\int{}^{}_{}",
  sum: "\\sum",
  log: "\\log_{}{}",
  multi: "\\cdot",
  div: "\\div",
  add: "\\add",
  sub: "\\sub",
  inf: "\\infin",
  alfa: "\\alpha",
  beta: "\\beta",
  le: "\\le",
  ge: "\\ge",
  isin: "\\isin",
  binom: "\\binom{ }{ }",
  tg: "\\tan",
  ctg: "\\ctan",
  lim: "\\lim",
  ent: "\\textcolor{black}{\\text{}}"
};

// add special keys, but don't override previous keyaction definitions
Object.keys(specialKeys).forEach(function (key) {
  if (!$.keyboard.keyaction[key]) {
    $.keyboard.keyaction[key] = specialKeys[key];
  }
});

$(".answerDiv").click(function () {
  mathquill = MQ.MathField($(this).parent().find(".answerO")[0]);
  $(this).parent().find(".answerO").data("keyboardPosition", this).trigger("focus");
});

$(".keyboard")
  .on("keyboardChange", function (e, keyboard, el) {
    if (specialKeys[e.action]) {
      mathquill.keystroke(specialKeys[e.action]);
    } else {
      if(e.action === "\\tan"){
        // katex.render(e.action, el, {
        //   displayMode: true,
        //   throwOnError: true
        // });
        mathquill.write("\\tan \\ctan");
        mathquill.reflow();
      }
      else{
        mathquill.write(e.action);
        mathquill.reflow();
      }
    }
  })
  .keyboard({
    beforeVisible : function(event, keyboard, el) {
      katex.render("\\binom n k", $('.ui-keyboard-binom').children()[0], {
        throwOnError: false
      });
      katex.render("a\\raisebox{0.3em}{$b$}", $('.ui-keyboard-power').children()[0], {
        throwOnError: false
      });
      katex.render("x_n", $('.ui-keyboard-lower').children()[0], {
        throwOnError: false
      });
      katex.render("\\lim", $('.ui-keyboard-lim').children()[0], {
        throwOnError: false
      });
      katex.render("\\log_{n}k", $('.ui-keyboard-log').children()[0], {
        throwOnError: false
      });
      katex.render("\\int", $('.ui-keyboard-integral').children()[0], {
        throwOnError: false
      });
      katex.render("\\int_{0}^{2}", $('.ui-keyboard-integral2').children()[0], {
        throwOnError: false
      });
    },
    // usePreview: false, powoduje błąd z wpisywaniem dwukrotnym znaku
    autoAccept: true,
    lockInput: false,
    restrictInput: false, // Prevent keys not in the displayed keyboard from being typed in
    preventPaste: false, // prevent ctrl-v and right click
    noFocus: false,
    reposition: true,
    appendLocally: true, // Append the keyboard locally (next to the input), so tabNavigation will work
    layout: "custom",
    display: {
      frac: "¼",
      sqrt: "√",
      exsqrt: "∛",
      sum: "Σ",
      multi: "*",
      div: "÷",
      inf: "∞",
      alfa: "α",
      beta: "β",
      ge: "⩾",
      le: "⩽",
      isin: "∈",
      tg: "tg",
      ctg: "ctg",
      ent: "↵"
    },
    customLayout: {
      default: [
        "sin cos {tg} {ctg} {log}",
        "{alfa} {beta} {ge} {le} {ent}",
        "{frac} {power} {lower} {sqrt} {exsqrt}",
        "{sum} \u03c0 {integral} {integral2} {inf}",
        "{isin} {binom} {lim}"
      ],
    },
    useCombos: false,
    css: {
      // input & preview
      input: "form-control input-sm",
      // keyboard container
      container: "center-block dropdown-menu", // jumbotron
      // default state
      buttonDefault: "btn btn-dark",
      // hovered button
      buttonHover: "btn-primary",
      // Action keys (e.g. Accept, Cancel, Tab, etc);
      // this replaces "actionClass" option
      buttonAction: "active",
      // used when disabling the decimal button {dec}
      // when a decimal exists in the input area
      buttonDisabled: "disabled",
    },
  })
  .addTyping({
    showTyping: true,
    delay: 250,
  });