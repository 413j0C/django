

function renderGraph(elementId,data,type){

  const grafico1 = document.getElementById(elementId).getContext('2d')
    return new Chart(grafico1, {
      type:type,
      data:data
    });
  }


   
 
  

  
  
    
  
  
  
  