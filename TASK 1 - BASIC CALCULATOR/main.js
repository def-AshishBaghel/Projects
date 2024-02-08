let screen = document.getElementById("screen");

function return_value(value) {
  screen.value += value;
}

function Ac() {
  screen.value = " ";
}
function calculate(value) {
  let ex = "";
  ex += screen.value;
  if (ex.length == 1) {
    screen.value = "error";
  } else {
    screen.value = eval(screen.value);
  }
}

function back() {
  let ex = "";
  ex += screen.value;
  value = ex.substring(0, ex.length - 1);
  screen.value = value;
}
