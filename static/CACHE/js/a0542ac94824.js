;$(function(){var deptos1=['Choluteca','Franciso Morazan'];var deptos2=[180.0,180.0];var deptos=new Array();deptos1.forEach(function(item,index){deptos.push({'name':item,'y':deptos2[index]})})
Highcharts.chart('grafico1',{chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false,type:'pie'},title:{text:'Voluntarios por Departamento'},tooltip:{pointFormat:'{series.name}: <b>{point.percentage:.1f}%</b>'},plotOptions:{pie:{allowPointSelect:true,cursor:'pointer',dataLabels:{enabled:true,format:'<b>{point.name}</b>: {point.percentage:.1f} %',style:{color:(Highcharts.theme&&Highcharts.theme.contrastTextColor)||'black'}}}},series:[{name:'Brands',colorByPoint:true,data:deptos}]});var tipo1=['Hola2'];var tipo2=[360.0];var tipos=new Array();tipo1.forEach(function(item,index){tipos.push({'name':item,'y':tipos2[index]})})
Highcharts.chart('grafico4',{chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false,type:'pie'},title:{text:'Voluntarios por Departamento'},tooltip:{pointFormat:'{series.name}: <b>{point.percentage:.1f}%</b>'},plotOptions:{pie:{allowPointSelect:true,cursor:'pointer',dataLabels:{enabled:true,format:'<b>{point.name}</b>: {point.percentage:.1f} %',style:{color:(Highcharts.theme&&Highcharts.theme.contrastTextColor)||'black'}}}},series:[{name:'Brands',colorByPoint:true,data:tipos}]});});