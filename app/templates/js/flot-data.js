/*
Template Name: Monster Admin
Author: Themedesigner
Email: niravjoshi87@gmail.com
File: js
*/
// Real Time chart
var data = []
    , totalPoints = 300;

function getRandomData() {
    if (data.length > 0) data = data.slice(1);
    // Do a random walk
    while (data.length < totalPoints) {
        var prev = data.length > 0 ? data[data.length - 1] : 50
            , y = prev + Math.random() * 10 - 5;
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
        res.push([i, data[i]])
    }
    return res;
}

// Set up the control widget
var updateInterval = 30;
$("#updateInterval").val(updateInterval).change(function () {
    var v = $(this).val();
    if (v && !isNaN(+v)) {
        updateInterval = +v;
        if (updateInterval < 1) {
            updateInterval = 1;
        } else if (updateInterval > 3000) {
            updateInterval = 3000;
        }
        $(this).val("" + updateInterval);
    }
});
var plot = $.plot("#placeholder", [getRandomData()], {
    series: {
        shadowSize: 0 // Drawing is faster without shadows
    }
    , yaxis: {
        min: 0
        , max: 100
    }
    , xaxis: {
        show: false
    }
    , colors: ["#26c6da"]
    , grid: {
        color: "#AFAFAF"
        , hoverable: true
        , borderWidth: 0
        , backgroundColor: '#FFF'
    }
    , tooltip: true
    , tooltipOpts: {
        content: "数量: %y"
        , defaultTheme: false
    }
});

function update() {
    plot.setData([getRandomData()]);
    // Since the axes don't change, we don't need to call plot.setupGrid()
    plot.draw();
    setTimeout(update, updateInterval);
}

update();
//Flot Line Chart
$(document).ready(function () {
    console.log("document ready");
    var offset = 0;
    plot();

    function plot() {
        var sin = []
            , cos = [];
        for (var i = 0; i < 12; i += 0.2) {
            sin.push([i, Math.sin(i + offset)]);
            cos.push([i, Math.cos(i + offset)]);
        }
        var options = {
            series: {
                lines: {
                    show: true
                }
                , points: {
                    show: true
                }
            }
            , grid: {
                hoverable: true //IMPORTANT! this is needed for tooltip to work
            }
            , yaxis: {
                min: -1.2
                , max: 1.2
            }
            , colors: ["#009efb", "#26c6da"]
            , grid: {
                color: "#AFAFAF"
                , hoverable: true
                , borderWidth: 0
                , backgroundColor: '#FFF'
            }
            , tooltip: true
            , tooltipOpts: {
                content: "'%s' of %x.1 is %y.4"
                , shifts: {
                    x: -60
                    , y: 25
                }
            }
        };
        var plotObj = $.plot($("#flot-line-chart"), [{
            data: sin
            , label: "sin(x)"
            ,
        }, {
            data: cos
            , label: "cos(x)"
        }], options);
    }
});
//Flot Pie Chart
$(function () {
    var data = [{
        label: "可用磁盘容量"
        , data: 10
        , color: "#4f5467"
        ,
    }, {
        label: "数据库使用容量"
        , data: 1
        , color: "#26c6da"
        ,
    }, {
        label: "备案文件使用容量"
        , data: 3
        , color: "#009efb"
        ,
    }, {
        label: "备案系统及日志容量"
        , data: 1
        , color: "#7460ee"
        ,
    }];
    var plotObj = $.plot($("#flot-pie-chart"), data, {
        series: {
            pie: {
                innerRadius: 0.5
                , show: true
            }
        }
        , grid: {
            hoverable: true
        }
        , color: null
        , tooltip: true
        , tooltipOpts: {
            content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
            shifts: {
                x: 20
                , y: 0
            }
            , defaultTheme: false
        }
    });
});
//Flot Moving Line Chart
$(function () {
    var container = $("#flot-line-chart-moving");
    // Determine how many data points to keep based on the placeholder's initial size;
    // this gives us a nice high-res plot while avoiding more than one point per pixel.
    var maximum = container.outerWidth() / 2 || 300;
    //
    var data = [];

    function getRandomData() {
        if (data.length) {
            data = data.slice(1);
        }
        while (data.length < maximum) {
            var previous = data.length ? data[data.length - 1] : 50;
            var y = previous + Math.random() * 10 - 5;
            data.push(y < 0 ? 0 : y > 100 ? 100 : y);
        }
        // zip the generated y values with the x values
        var res = [];
        for (var i = 0; i < data.length; ++i) {
            res.push([i, data[i]])
        }
        return res;
    }

    //
    series = [{
        data: getRandomData()
        , lines: {
            fill: true
        }
    }];
    //
    var plot = $.plot(container, series, {
        colors: ["#26c6da"]
        , grid: {
            borderWidth: 0
            , minBorderMargin: 20
            , labelMargin: 10
            , backgroundColor: {
                colors: ["#fff", "#fff"]
            }
            , margin: {
                top: 8
                , bottom: 20
                , left: 20
            }
            , markings: function (axes) {
                var markings = [];
                var xaxis = axes.xaxis;
                for (var x = Math.floor(xaxis.min); x < xaxis.max; x += xaxis.tickSize * 1) {
                    markings.push({
                        xaxis: {
                            from: x
                            , to: x + xaxis.tickSize
                        }
                        , color: "#fff"
                    });
                }
                return markings;
            }
        }
        , xaxis: {
            tickFormatter: function () {
                return "";
            }
        }
        , yaxis: {
            min: 0
            , max: 110
        }
        , legend: {
            show: true
        }
    });
    // Update the random dataset at 25FPS for a smoothly-animating chart
    setInterval(function updateRandom() {
        series[0].data = getRandomData();
        plot.setData(series);
        plot.draw();
    }, 40);
});
//Flot Bar Chart
$(function () {
    function str2Timestamp(item) {
        strDate = item[0];
        var date = eval('new Date(' + strDate.replace(/\d+(?=-[^-]+$)/,
            function (a) {
                return parseInt(a, 10) - 1;
            }).match(/\d+/g) + ')');
        return [Date.parse(date), item[1]];
    }

    var barOptions = {
        series: {
            bars: {
                show: true,
                // minWidth:23200000
                barWidth: 232000000,
                align: "center"
            }
        }
        , xaxis: {
            mode: "time",
            timeformat: "%y/%m/%d",
            minTickSize: [1, "month"],
            clickable: true
        }
        , yaxis: {
            max: 20
        }
        , grid: {
            hoverable: true
        }
        , legend: {
            show: false
        }
        , grid: {
            color: "#AFAFAF"
            , hoverable: true
            , borderWidth: 0
            , backgroundColor: '#FFF'
        }
        , tooltip: true
        , tooltipOpts: {
            content: "x: %x, y: %y"
        }
    };
    let date_array = [["2019-1-1", 5], ["2019-2-1", 3], ["2019-3-1", 2], ["2019-4-1", 6], ["2019-5-1", 2], ["2019-6-1", 4], ["2019-7-1", 5], ["2019-8-1", 7], ["2019-9-1", 8]];
    let list = date_array.map(str2Timestamp);
    let barData = {
        label: "bar"
        , color: "#009efb"
        , data: list
    };

    $.plot($("#flot-bar-chart"), [barData], barOptions);
});
// sales bar chart
$(function () {
    let i;

// alert('ok');
    function str2Timestamp(item) {
        strDate = item[0];
        var date = eval('new Date(' + strDate.replace(/\d+(?=-[^-]+$)/,
            function (a) {
                return parseInt(a, 10) - 1;
            }).match(/\d+/g) + ')');
        return [Date.parse(date), item[1]];
    }

    //some data
    let d1 = [];
    for (i = 1; i <= 12; i += 1) d1.push([`2019-${i}-1`, parseInt(Math.random() * 60)]);
    let d2 = [];
    for (i = 1; i <= 12; i += 1) d2.push([`2019-${i}-1`, parseInt(Math.random() * 40)]);
    // alert(d1)
    let d3 = d1.map(str2Timestamp);
    let d4 = d2.map(str2Timestamp);
    // let d3 = [];
    // for (i = 1; i <= 12; i += 1) d3.push(["2019-{}-1".format(i), parseInt(Math.random() * 25)]);
    let ds = [];
    ds.push({
        label: "备案数量"
        , data: d3
        , bars: {
            order: 1
        }
    });
    ds.push({
        label: "比对次数"
        , data: d4
        , bars: {
            order: 2
        }
    });

    var stack = 0
        , bars = true
        , lines = true
        , steps = true;
    var options = {
        bars: {
            show: true
            , barWidth: 232000000
            , fill: 1
        }
        , grid: {
            show: true
            , aboveData: false
            , labelMargin: 5
            , axisMargin: 0
            , borderWidth: 1
            , minBorderMargin: 5
            , clickable: true
            , hoverable: true
            , autoHighlight: false
            , mouseActiveRadius: 20
            , borderColor: '#f5f5f5'
        }
        , series: {
            stack: stack
        }
        , legend: {
            position: "ne"
            , margin: [0, 0]
            , noColumns: 0
            , labelBoxBorderColor: null
            , labelFormatter: function (label, series) {
                // just add some space to labes
                return '' + label + '&nbsp;&nbsp;';
            }
            , width: 30
            , height: 5
        }
        , yaxis: {
            tickColor: '#f5f5f5'
            , font: {
                color: '#bdbdbd'
            }
        }
        , xaxis: {
            mode: "time",
            timeformat: "%y/%m/%d",
            minTickSize: [1, "month"],
            clickable: true,
            tickColor: '#f5f5f5'
            , font: {
                color: '#bdbdbd'
            }
        }
        , colors: ["#4F5467", "#009efb"]
        , tooltip: true, //activate tooltip
        tooltipOpts: {
            content: "%s : %y.0"
            , shifts: {
                x: -30
                , y: -50
            }
        }
    };
    $.plot($(".sales-bars-chart"), ds, options);
});