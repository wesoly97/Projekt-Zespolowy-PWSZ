let mathquill;

MQ.registerEmbed('tg', function(id){
  console.log("asd")
  return {
    htmlString: '<span class="tg"></span>',
    text: function() { return 'tg'; },
    latex: function() { return '\\tg'; }
  };
});

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
  prod: "\\prod",
  log2: "\\log_{}",
  log: "\\log",
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
  ctg: "\\cot",
  lim: "\\lim",
  ent: "\\textcolor{black}{\\text{}}",
  degree: "\\degree"
};


// add special keys, but don't override previous keyaction definitions
Object.keys(specialKeys).forEach(function (key) {
  if (!$.keyboard.keyaction[key]) {
    $.keyboard.keyaction[key] = specialKeys[key];
  }
});

$(".keyboardInputDiv").click(function () {
  mathquill = MQ.MathField($(this).find(".keyboardInput")[0]);
  renderMathInElement(
    $(this).find(".keyboardInput")[0],
    {
      delimiters: [
          {left: "$$", right: "$$", display: true},
          {left: "$", right: "$", display: false}
      ]
    }
  );
  $(this).find(".keyboardInput").data("keyboardPosition", this).trigger("focus");
});

$(".keyboard")
  .on("keyboardChange", function (e, keyboard, el) {
    if (specialKeys[e.action]) {
      mathquill.keystroke(specialKeys[e.action]);
    } else {
      mathquill.write(e.action);
      mathquill.reflow();
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
      katex.render("\\log_{n}", $('.ui-keyboard-log2').children()[0], {
        throwOnError: false
      });
      katex.render("\\log", $('.ui-keyboard-log').children()[0], {
        throwOnError: false
      });
      katex.render("\\int", $('.ui-keyboard-integral').children()[0], {
        throwOnError: false
      });
      katex.render("\\int_{0}^{2}", $('.ui-keyboard-integral2').children()[0], {
        throwOnError: false
      });
      katex.render("\\prod", $('.ui-keyboard-prod').children()[0], {
        throwOnError: false
      });
      katex.render("\\sum", $('.ui-keyboard-sum').children()[0], {
        throwOnError: false
      });
    },
    // usePreview: false, causes error with typing double character
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
      prod: "∏",
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
      ent: "↵",
      degree: "°"
    },
    customLayout: {
      default: [
        "sin cos {tg} {ctg} {log2} {log}",
        "{alfa} {beta} {ge} {le} {ent}",
        "{frac} {power} {lower} {sqrt} {exsqrt}",
        "{sum} \u03c0 {integral} {integral2} {inf}",
        "{prod} {isin} {binom} {lim} {degree}"
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