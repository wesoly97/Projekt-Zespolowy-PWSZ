let mathquill;
let specialKeys = {
  bksp: "Backspace",
  frac: "\\frac{}{}",
  sqrt: "\\sqrt{}",
  power: "\\^{}",
  exsqrt: "\\sqrt[]{}",
  integral: "\\ \\int",
  sum: "\\sum",
  log: "\\log_{}{}",
  multi: "\\cdot",
  div: "\\div",
  add: "\\add",
  sub: "\\sub",
  inf: "\\infin",
  alfa: "α",
  beta: "β",
  le: "\\le",
  ge: "\\ge",
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
      mathquill.write(e.action);
      mathquill.reflow();
    }
  })
  .keyboard({
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
      power: "^",
      exsqrt: "∛",
      integral: "∫",
      sum: "Σ",
      log: "log",
      multi: "*",
      div: "÷",
      inf: "∞",
      alfa: "α",
      beta: "β",
      ge: "⩾",
      le: "⩽",
    },
    customLayout: {
      default: [
        //default
        "1 2 3 + -",
        "4 5 6 {multi} {div}",
        "7 8 9 0 = {b}",
        //functions
        "sin cos tan cot {log}",
        "{alfa} {beta} {ge} {le}",
        "{frac} {power} {sqrt} {exsqrt}",
        "{sum} \u03c0 {integral} {inf}",
        ". , < >",
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