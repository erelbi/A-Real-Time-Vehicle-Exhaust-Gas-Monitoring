     var svg = d3.select("#memory")
                .append("svg:svg")
                .attr("width", 400)
                .attr("height", 400);


        var gauge = iopctrl.arcslider()
                .radius(120)
                .events(false)
                .indicator(iopctrl.defaultGaugeIndicator);
        gauge.axis().orient("in")
                .normalize(true)
                .ticks(12)
                .tickSubdivide(3)
                .tickSize(10, 8, 10)
                .tickPadding(5)
                .scale(d3.scale.linear()
                        .domain([0, 100])
                        .range([-3*Math.PI/4, 3*Math.PI/4]));

        var segDisplay = iopctrl.segdisplay()
                .width(80)
                .digitCount(6)
                .negative(false)
                .decimals(0);

        svg.append("g")
                .attr("class", "segdisplay")
                .attr("transform", "translate(130, 200)")
                .call(segDisplay);

        svg.append("g")
                .attr("class", "gauge")
                .call(gauge);


       const Sensors = new WebSocket(
            'ws://'
            + window.location.host
            + '/notifications/'
        );
          Sensors.onmessage = function(e) {
              const datac = JSON.parse(e.data)
              console.log(datac.cpu_freq)
                 var data = [
                  {
                      domain: {x: [0, 1], y: [0, 1]},
                      value: datac.cpu,
                      title: {text: "MHz"},
                      type: "indicator",
                      mode: "gauge+number",
                      delta: {reference: 400},
                      gauge: {axis: {range: [null, 3000]}}
                  }
              ];

              var layout = {width: 600, height: 400};
              Plotly.newPlot('cpu', data, layout);
            gauge.value(datac.mem);
         segDisplay.value(datac.cpu);};