;var tablex=$('#tb').DataTable({lengthChange:false,buttons:['copy','excel','pdf','colvis',{extend:'pdfHtml5',download:'open',orientation:'landscape',pageSize:'LEGAL',text:'Ver',title:'Reporte de voluntarios'}],"scrollX":true,"language":{"lengthMenu":"Mostrar _MENU_ por páginas","zeroRecords":"No se encontró ningún registro","info":"Mostrando página _PAGE_ de _PAGES_","infoEmpty":"Registro no valido","infoFiltered":"(filtrado de _MAX_ registros totales)",'search':'Buscar:',"paginate":{"next":"Siguiente",'previous':'Anterior'},buttons:{colvis:'Columnas visibles',copy:'Copiar'}}});tablex.buttons().container().appendTo('#tb_wrapper .col-sm-6:eq(0)');