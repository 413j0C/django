import Chart from 'chart.js/auto';

/*const usuarios = {data[],labels[],backgroundColor[]};
const activos = {data[],labels[],backgroundColor[]};
*/
function init(){

const grafico1 = document.getElementById("registros_total_activos")
  new Chart(grafico1, {
    type: 'doughnut',
    data: {
      labels: ["EEUU","India","Japon","Alemania","Brasil"],
      datasets: [{
        label: 'Cantidad Personas',
        
        data: [57000000,65000000,45000000,40000000,38000000],
        borderWidth: 1,
        borderColor: '#36A2EB',
        backgroundColor: [
          "rgb(0, 123, 177)",
          "rgb(74, 136, 162)",
          "rgb(176, 211, 228)",
          "rgb(250, 172, 130)",
          "rgb(187, 90, 44)",
          "rgb(127, 90, 44)"
        ]
      }]
    }
  });

  const grafico2 = document.getElementById("registro_total_usuarios")
  new Chart(grafico2, {
    type: 'doughnut',
    data: {
      labels: ["Python","JavaScript","Java","C#","C++"],
      datasets: [{
        label: 'Uso Lenguajes Programacion',
        
        data: [85,68,60,54,51],
        borderWidth: 1,
        borderColor: '#36A2EB',
        backgroundColor: [
          "rgb(0, 123, 177)",
          "rgb(74, 136, 162)",
          "rgb(176, 211, 228)",
          "rgb(250, 172, 130)",
          "rgb(187, 90, 44)",
          "rgb(127, 90, 44)"
        ]
      }]
    }
  });
  
  }

  init()



