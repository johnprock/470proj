function async_similarity() {
    $.getJSON('/similarity', {
      t1: $('#fetch').text(),
      t2: $('#edit').text()
    }, function(data) {
      $("#sim_score").text(data.result);
    });
      return false;
}

function fetch() {
    var topic = $("#topic").val();
    window.location.href = "/?topic="+topic;
}
