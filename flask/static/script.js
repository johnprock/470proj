function update_chart(x, y) {
    $('#chart').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 0,
            plotShadow: false
        },
        title: {
            text: 'Browser<br>shares',
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

function async_similarity() {
    $.getJSON('/similarity', {
      t1: $('#fetch').text(),
      t2: $('#edit').text()
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
      $("#edit").text(data.result);
    });
      return false;
//    var topic = $("#topic").val();
//    window.location.href = "/?topic="+topic;
}
