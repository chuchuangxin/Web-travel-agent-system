/**
 * Flot chart page
 */
(function($) {
  'use strict';

  var data = [],
    totalPoints = 300,
    updateInterval = 300,
    previousPoint = null,
    plot;

  // Define data points
  var browserData = [{
    label: 'IE',
    data: 15,
    color: $.constants.danger
  }, {
    label: 'Safari',
    data: 14,
    color: $.constants.info
  }, {
    label: 'Chrome',
    data: 34,
    color: $.constants.warning
  }, {
    label: 'Opera',
    data: 13,
    color: $.constants.bodyBg
  }, {
    label: 'Firefox',
    data: 24,
    color: $.constants.dark
  }];

  var getRandomArbitrary = function() {
    return Math.round(Math.random() * 100);
  };

  function showTooltip(x, y, contents) {
    $('<div id=\'tooltip\'>' + contents + '</div>').css({
      top: y - 10,
      left: x + 20
    }).appendTo('body').fadeIn(200);
  }

  var visits = [
    [0, getRandomArbitrary()],
    [1, getRandomArbitrary()],
    [2, getRandomArbitrary()],
    [3, getRandomArbitrary()],
    [4, getRandomArbitrary()],
    [5, getRandomArbitrary()],
    [6, getRandomArbitrary()],
    [7, getRandomArbitrary()],
    [8, getRandomArbitrary()]
  ];
  var visitors = [
    [0, getRandomArbitrary()],
    [1, getRandomArbitrary()],
    [2, getRandomArbitrary()],
    [3, getRandomArbitrary()],
    [4, getRandomArbitrary()],
    [5, getRandomArbitrary()],
    [6, getRandomArbitrary()],
    [7, getRandomArbitrary()],
    [8, getRandomArbitrary()]
  ];

  /******** Line chart ********/
  var plotdata = [{
    data: visits,
    color: $.constants.success
  }, {
    data: visitors,
    color: $.constants.default
  }];
  /*jshint -W030 */
  $.plot($('.line'), plotdata, {
    series: {
      lines: {
        show: true,
        lineWidth: 0
      },
      splines: {
        show: true,
        tension: 0.5,
        lineWidth: 1,
        fill: 0.2
      },
      shadowSize: 0
    },
    grid: {
      color: $.constants.border,
      borderWidth: 1,
      hoverable: true
    }
  });

  /******** Bart chart ********/
  var barData = [{
    data: [
      [1391761856000, 80],
      [1394181056000, 40],
      [1396859456000, 20],
      [1399451456000, 20],
      [1402129856000, 50]
    ],
    bars: {
      show: true,
      barWidth: 7 * 24 * 60 * 60 * 1000,
      fill: true,
      lineWidth: 0,
      order: 1,
      fillColor: $.constants.info
    }
  }, {
    data: [
      [1391761856000, 50],
      [1394181056000, 30],
      [1396859456000, 10],
      [1399451456000, 70],
      [1402129856000, 30]
    ],
    bars: {
      show: true,
      barWidth: 7 * 24 * 60 * 60 * 1000,
      fill: true,
      lineWidth: 0,
      order: 2,
      fillColor: $.constants.danger
    }
  }, {
    data: [
      [1391761856000, 30],
      [1394181056000, 60],
      [1396859456000, 40],
      [1399451456000, 40],
      [1402129856000, 40]
    ],
    bars: {
      show: true,
      barWidth: 7 * 24 * 60 * 60 * 1000,
      fill: true,
      lineWidth: 0,
      order: 3,
      fillColor: $.constants.success
    }
  }];
  $.plot($('.bar'), barData, {
    grid: {
      hoverable: false,
      clickable: false,
      labelMargin: 8,
      color: $.constants.border,
      borderWidth: 0
    },
    xaxis: {
      mode: 'time',
      timeformat: '%b',
      tickSize: [1, 'month'],
      monthNames: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      tickLength: 0,
      axisLabel: 'Month',
      axisLabelUseCanvas: true,
      axisLabelFontSizePixels: 12,
      axisLabelFontFamily: 'Roboto',
      axisLabelPadding: 5
    }
  });

  /******** Realtime chart ********/
  function getRandomData() {
    if (data.length > 0) {
      data = data.slice(1);
    }
    // Do a random walk
    while (data.length < totalPoints) {
      var prev = data.length > 0 ? data[data.length - 1] : 50,
        y = prev + Math.random() * 10 - 5;
      if (y < 0) {
        y = 0;
      } else if (y > 100) {
        y = 100;
      }
      data.push(y);
    }
    // Zip the generated y values with the x values
    var res = [];
    for (var i = 0; i < data.length; ++i) {
      res.push([i, data[i]]);
    }
    return res;
  }
  //Update realtime series
  function update() {
    plot.setData([getRandomData()]);
    plot.draw();
    setTimeout(update, updateInterval);
  }
  // Plot realtime chart
  plot = $.plot('.realtime', [getRandomData()], {
    colors: ['rgba(0,0,0,.5)'],
    lines: {
      lineWidth: 1
    },
    grid: {
      color: $.constants.border,
      borderWidth: 0,
      hoverable: true
    },
    yaxis: {
      min: 0,
      max: 100
    }
  });
  update(); // Update realtime chart

  /******** Pie chart ********/
  $.plot($('.pie'), browserData, {
    series: {
      pie: {
        show: true,
        innerRadius: 0.5,
        stroke: {
          width: 0
        },
        label: {
          show: false
        }
      }
    },
    legend: {
      show: true
    }
  });

  // Chart tooltip
  $('.chart, .chart-sm').bind('plothover', function(event, pos, item) {
    if (item) {
      if (previousPoint !== item.dataIndex) {
        previousPoint = item.dataIndex;
        $('#tooltip').remove();
        var x = item.datapoint[0],
          y = item.datapoint[1];
        showTooltip(item.pageX, item.pageY, y + ' at ' + x);
      }
    } else {
      $('#tooltip').remove();
      previousPoint = null;
    }
  });
})(jQuery);
