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
    $.getJSON('/fetch', {
      t: $('#topic').val(),
    }, function(data) {
      $("#fetch").text(data.result);
      $("#edit").text(data.result);
    });
      return false;
//    var topic = $("#topic").val();
//    window.location.href = "/?topic="+topic;
}
