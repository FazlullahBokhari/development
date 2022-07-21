function hi(){
  alert("hi");
}

var add_two = new Function("a","b","return a+b;");

function sum_two_int(){
  var result;
  result = add_two(100,300);
  document.write(result)
};
