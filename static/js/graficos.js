function g1(grafico) {
  data = JSON.parse(grafico);
  crear_dona("#grafico_1");
}

function g2(grafico) {
  data = JSON.parse(grafico);
  crear_dona("#grafico_2");
}

function g3(grafico) {
  data = JSON.parse(grafico);
  console.log(data[0].fechas);
  labels = data[0].fechas
  // info = [12, 19, 3, 5, 2, 3, 8];
  // ["180.00", "767.00", "994.00", "1941.00", "227.00", "370.00", "1278.98"]
  info = data[0].data
  crear_barra("grafico_3", labels, info);
}

function g4(grafico) {
  data = JSON.parse(grafico)
  labels = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
  ];
  info = [12, 19, 3, 5, 2, 3, 8, 5, 6, 0, 0, 0];
  info = data[0].totales
  crear_barra("grafico_4", labels, info);
}

function crear_dona(nombre_id) {
  var plotObj = $.plot($(nombre_id), data, {
    series: {
      pie: {
        innerRadius: 0.5,
        show: true,
      },
    },
    grid: {
      hoverable: true,
    },
    color: null,
    tooltip: true,
    tooltipOpts: {
      content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
      shifts: {
        x: 20,
        y: 0,
      },
      defaultTheme: false,
    },
  });
}

function crear_barra(myID, etiquetas, info) {
  var ctx = document.getElementById(myID).getContext("2d");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      yAxisID: "joto",
      labels: etiquetas,
      datasets: [
        {
          label: "Total Ventas",
          data: info,
          backgroundColor: [
            "rgba(119,77,155, 0.5)",
            "rgba(47,108,226, 0.5)",
            "rgba(233,64,55, 0.5)",
            "rgba(254,210,56, 0.5)",
            "rgba(62,168,42, 0.5)",
            "rgba(255,156,59, 0.5)",
            "rgba(119,77,155, 0.5)",
            "rgba(47,108,226, 0.5)",
            "rgba(233,64,55, 0.5)",
          ],
          borderColor: [
            "rgba(119,77,155, 1)",
            "rgba(47,108,226, 1)",
            "rgba(233,64,55, 1)",
            "rgba(254,210,56, 1)",
            "rgba(62,168,42, 1)",
            "rgba(255,156,59, 1)",
            "rgba(119,77,155, 1)",
            "rgba(47,108,226, 1)",
            "rgba(233,64,55, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
    },
  });
}
