;$(function(){var deptos1=[];var deptos2=['Choluteca',180.0,'Franciso Morazan',180.0];var deptos=new Array();deptos1.forEach(function(item,index){deptos.push({'name':item,'y':deptos2[index]})})
console.log(deptos1)
console.log(deptos2)
console.log(deptos)
Highcharts.chart('grafico1',{chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false,type:'pie'},title:{text:'Número de voluntarios por departamento'},tooltip:{pointFormat:'{series.name}: <b>{point.percentage:.1f}%</b>'},plotOptions:{pie:{allowPointSelect:true,cursor:'pointer',dataLabels:{enabled:true,format:'<b>{point.name}</b>: {point.percentage:.1f} %',style:{color:(Highcharts.theme&&Highcharts.theme.contrastTextColor)||'black'}}}},series:[{name:'Brands',colorByPoint:true,data:deptos}]});});