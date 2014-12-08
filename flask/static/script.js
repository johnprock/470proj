
function update_chart(x, y) {
    $('#chart').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 0,
            plotShadow: false
        },
        title: {
            text: 'Similarity<br>score',
            align: 'center',
            verticalAlign: 'middle',
            y: 50
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                dataLabels: {
                    enabled: true,
                    distance: -50,
                    style: {
                        fontWeight: 'bold',
                        color: 'white',
                        textShadow: '0px 1px 2px black'
                    }
                },
                startAngle: -90,
                endAngle: 90,
                center: ['50%', '75%']
            }
        },
        series: [{
            type: 'pie',
            name: 'Similarity',
            innerSize: '50%',
            data: [
                ['Wikipedia', x],
                ['You',    y]
            ]
        }]
    });
}

function synonym_tool() {
    $.getJSON('/synonym', {
      word: $("#syn_box").val()
    }, function(data) {
       var text = "";
       for(i=0; i<data.result.length; i++)
       {
           text = text + '<option value=' + data.result[i] + '>' + data.result[i] + '</option>';
       }
       document.getElementById("selectable").innerHTML = text;
     });
    return false;
}

function load_tool(t) { 
    var t = document.getElementById("tools").value;
    $.getJSON('/tool', {
      tool: t
    }, function(data) {
      document.getElementById("toolbox").innerHTML = data.result;
    });
    return false;
    
}

function async_similarity() {
    $.getJSON('/similarity', {
      fetch: $('#fetch').text(),
      edit: $('#edit').text()
    }, function(data) {
      update_chart(data.result, 1-data.result);
    });
      return false;
}

function fetch() {
    $.getJSON('/fetch', {
      t: $('#topic').val(),
    }, function(data) {
      $("#fetch").text(data.result);
    });
      return false;
}

function find_replace(old_word, new_word) {
    var text = $("#edit").text();
    text = text.replace(old_word, new_word);
    $("#edit").text(text);
}

function replace_syn() {
   var old_word = $("#syn_box").val();
   var new_word = $("#selectable").val()[0];
   console.log(old_word);
   console.log(new_word);
   find_replace(old_word, new_word);
}

function replace_tool() {
    find_replace( $("#oldreplace_box").val(), $("#newreplace_box").val());
}

function merge_tool() {
    $.getJSON('/merge', {
      text: $('#edit').text()
    }, function(data) {
      $('#sim1').text(data.s1);
      $('#sim2').text(data.s2);
    });
    return false;
}

function search_tool() {
    $.getJSON('/search', {
      text: $('#sentence').val(),
      topic: $('#topic').val() 
    }, function(data) {
        $('#search_result').text(data.result);
    });
    return false;
}
