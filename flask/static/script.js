function similarity() {
    var t1 = $("#topic1").val();    
    var t2 = $("#topic2").val();    
    window.location.href = "/sim_score.html?t1=" + t1 + "&t2=" + t2; 
}

function fetch() {
    var topic = $("#topic").val();
    window.location.href = "/?topic="+topic;
}
