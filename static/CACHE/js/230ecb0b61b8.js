;$(function(){var d1=['Choluteca','Franciso Morazan'];var d2=[2,1];var d3=[[['Marcio Martinez : Choluteca',1],['Juan Martinez : Choluteca',0]],[['Marcio Martinez : Franciso Morazan',1]]];var d=[];var dx=[];d1.forEach(function(item,index){d.push({"name":item,"y":d2[index],"drilldown":item})
dx.push({"name":item,"id":item,"data":d3[index]})})
console.log(dx)
Highcharts.chart('grafico3',{chart:{type:'column'},title:{text:'Voluntarios por Departamento'},subtitle:{text:'Descripción detallada de los voluntarios por cada Departamento'},xAxis:{type:'category'},yAxis:{title:{text:'Número de Voluntarios'}},legend:{enabled:false},plotOptions:{series:{borderWidth:0,dataLabels:{enabled:true,format:'{point.y:.1f}%'}}},tooltip:{headerFormat:'<span style="font-size:11px">{series.name}</span><br>',pointFormat:'<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.0f}</b> en total<br/>'},"series":[{"name":"Departamentos","colorByPoint":true,"data":d}],"drilldown":{"series":dx}});var deptos1=['Choluteca','Franciso Morazan'];var deptos2=[240.0,120.0];var deptos=new Array();deptos1.forEach(function(item,index){deptos.push({'name':item,'y':deptos2[index]})})
Highcharts.chart('grafico1',{chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false,type:'pie'},title:{text:'Porcentaje de Voluntarios por Departamento'},tooltip:{pointFormat:'{series.name}: <b>{point.percentage:.1f}%</b>'},plotOptions:{pie:{allowPointSelect:true,cursor:'pointer',dataLabels:{enabled:true,format:'<b>{point.name}</b>: {point.percentage:.1f} %',style:{color:(Highcharts.theme&&Highcharts.theme.contrastTextColor)||'black'}}}},series:[{name:'Porcentaje',colorByPoint:true,data:deptos}]});var tipo1=['Hola2'];var tipo2=[360.0];var tipos=new Array();tipo1.forEach(function(item,index){tipos.push({'name':item,'y':tipo2[index]})})
Highcharts.chart('grafico4',{chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false,type:'pie'},title:{text:'Voluntarios por Departamento'},tooltip:{pointFormat:'{series.name}: <b>{point.percentage:.1f}%</b>'},plotOptions:{pie:{allowPointSelect:true,cursor:'pointer',dataLabels:{enabled:true,format:'<b>{point.name}</b>: {point.percentage:.1f} %',style:{color:(Highcharts.theme&&Highcharts.theme.contrastTextColor)||'black'}}}},series:[{name:'Porcentaje',colorByPoint:true,data:tipos}]});});