function execCalculator() {
// Operator Selector


// Buid query parameter
    var param = {};
    param["num"] = document.getElementById("num").value;
    param["text"] = document.getElementById("text").value;
    var query = jQuery.param(param);
    console.log(param["text"])
// Query with a new parameter 
    $.get("/" + "?" + query, function(data) {
        document.getElementById("result").textContent = data;
    });
};

var Timer;
function inputNum(){
    if(Timer){clearTimeout(Timer);}
    timer=setTimeout(inputEnd,200);
}
function inputEnd(){
    execCalculator();
    changeButtonColor(document.getElementById("exec"));
}

execCalculator();
