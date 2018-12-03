;$(function(){var e1=['Choluteca','Francisco Morazan','La Ceiba'];var e2=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];var e3=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,1,0],[1,1,3]];var ed=[];e2.forEach(function(item,index){ed.push({name:item,data:e3[index]})})
Highcharts.chart('grafico2',{chart:{type:'bar'},title:{text:'Eventos por Departamentos'},subtitle:{text:'Número de eventos por departamentos mensuales'},xAxis:{categories:e1,title:{text:null}},yAxis:{min:0,title:{text:'Número de Eventos',align:'high'},labels:{overflow:'justify'}},tooltip:{valueSuffix:' Eventos'},plotOptions:{bar:{dataLabels:{enabled:true}}},legend:{layout:'vertical',align:'right',verticalAlign:'top',x:-40,y:80,floating:true,borderWidth:1,backgroundColor:((Highcharts.theme&&Highcharts.theme.legendBackgroundColor)||'#FFFFFF'),shadow:true},credits:{enabled:false},series:ed});var d1=['Choluteca','Francisco Morazan','La Ceiba'];var d2=[2,2,1];var d3=[[['Francisco Martinez : Choluteca',1],['Juan Martinez : Choluteca',0]],[['Marcio Martinez : Francisco Morazan',1],['Walter Cruz : Francisco Morazan',1]],[['Fernando Sanchez : La Ceiba',3]]];var d=[];var dx=[];d1.forEach(function(item,index){d.push({"name":item,"y":d2[index],"drilldown":item})
dx.push({"name":item,"id":item,"data":d3[index]})})
console.log(dx)
Highcharts.chart('grafico3',{chart:{type:'column'},title:{text:'Voluntarios por Departamento'},subtitle:{text:'Descripción detallada de los voluntarios por cada Departamento, y Eventos por cada Voluntario'},xAxis:{type:'category'},yAxis:{title:{text:'Número de Voluntarios'}},legend:{enabled:false},plotOptions:{series:{borderWidth:0,dataLabels:{enabled:true,format:'{point.y:.0f}'}}},tooltip:{headerFormat:'<span style="font-size:11px">{series.name}</span><br>',pointFormat:'<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.0f}</b> en total<br/>'},"series":[{"name":"Departamentos","colorByPoint":true,"data":d}],"drilldown":{"series":dx}});var deptos1=['Choluteca (2)','Francisco Morazan (2)','La Ceiba (1)'];var deptos2=[144.0,144.0,72.0];var deptos=new Array();deptos1.forEach(function(item,index){deptos.push({'name':item,'y':deptos2[index]})})
Highcharts.chart('grafico1',{chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false,type:'pie'},title:{text:'Porcentaje de Voluntarios por Departamento'},tooltip:{pointFormat:'{series.name}: <b>{point.percentage:.1f}%</b>'},plotOptions:{pie:{allowPointSelect:true,cursor:'pointer',dataLabels:{enabled:true,format:'<b>{point.name}</b>: {point.percentage:.1f} %',style:{color:(Highcharts.theme&&Highcharts.theme.contrastTextColor)||'black'}}}},series:[{name:'Porcentaje',colorByPoint:true,data:deptos}]});var tipo1=['Junta (2)','Equipo (1)','Donaciones (2)'];var tipo2=[144.0,72.0,144.0];var tipos=new Array();tipo1.forEach(function(item,index){tipos.push({'name':item,'y':tipo2[index]})})
Highcharts.chart('grafico4',{chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:false,type:'pie'},title:{text:'Voluntarios por Tipo'},tooltip:{pointFormat:'{series.name}: <b>{point.percentage:.1f}%</b>'},plotOptions:{pie:{allowPointSelect:true,cursor:'pointer',dataLabels:{enabled:true,format:'<b>{point.name}</b>: {point.percentage:.1f} %',style:{color:(Highcharts.theme&&Highcharts.theme.contrastTextColor)||'black'}}}},series:[{name:'Porcentaje',colorByPoint:true,data:tipos}]});});