;$('.form_datetime').datetimepicker({weekStart:1,todayBtn:1,autoclose:1,todayHighlight:1,startView:2,forceParse:0,showMeridian:1});$.notify('Evento modificado exitosamente!',{className:'success',globalPosition:"right bottom",clickToHide:true,autoHide:true,autoHideDelay:5000,arrowShow:true,arrowSize:5,style:'bootstrap',showAnimation:'slideDown',showDuration:400,hideAnimation:'slideUp',hideDuration:200,gap:2});var tablex=$('#tb').DataTable({lengthChange:false,buttons:['copy','excel','pdf','colvis',{extend:'pdfHtml5',download:'open',orientation:'landscape',pageSize:'LEGAL',text:'Ver',title:'Reporte de eventos'}],"scrollX":true,"language":{"lengthMenu":"Mostrar _MENU_ por páginas","zeroRecords":"No se encontró ningún registro","info":"Mostrando página _PAGE_ de _PAGES_","infoEmpty":"Registro no valido","infoFiltered":"(filtrado de _MAX_ registros totales)",'search':'Buscar:',"paginate":{"next":"Siguiente",'previous':'Anterior'},buttons:{colvis:'Columnas visibles',copy:'Copiar'}}});tablex.buttons().container().appendTo('#tb_wrapper .col-sm-6:eq(0)');