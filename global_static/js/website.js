$(function () {
  /*===================Pagina Quienes Somos===============*/


    $(".QS1").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQS1').text('SOLIDARIDAD');
    });

    $(".QS1").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQS1').text('');
    });


    $(".QS2").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQS2').text('Valores');
    });


    $(".QS2").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQS2').text('');
    });

    $(".QS3").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQS3').text('Carrusel');
    });


    $(".QS3").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background','transparent');
      $('.etiquetaQS3').text('');
    });

    $(".QS4").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQS4').text('Rendición de Cuentas');
    });


    $(".QS4").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQS4').text('');
    });

    $(".QS5").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQS5').text('Preguntas Frecuentes');
    });


    $(".QS5").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQS5').text('');
    });
	/* =================Pagina Donde estamos===============*/
	$('#CH').on('click', ()=>{
		location.href='#Choluteca';
	});


	$('#CO').on('click', ()=>{
		location.href='#Comayagua';
	});

	$('#FM').on('click', ()=>{
		location.href='#FranciscoMorazan';
	});

	$('.PE').on('click', ()=>{
		location.href='#ProximasExtenciones';
	});

	$(".hover").mouseleave(()=>{
    	$(this).removeClass("hover");
  	});

  	$(".o1").hover(function(){
    	$(this).css( 'border','2px solid blue');
    	$(this).css( 'background','blue');
    	$('.etiqueta1').text('Mapa');
  	});


  	$(".o1").mouseleave(function(){
  		$(this).css( 'border','2px solid black');
    	$(this).css( 'background-color','transparent');
    	$('.etiqueta1').text('');
  	});


  	$(".o2").hover(function(){
    	$(this).css( 'border','2px solid blue');
    	$(this).css( 'background','blue');
    	$('.etiqueta2').text('Choluteca');
  	});


  	$(".o2").mouseleave(function(){
  		$(this).css( 'border','2px solid black');
    	$(this).css( 'background-color','transparent');
    	$('.etiqueta2').text('');
  	});

  	$(".o3").hover(function(){
    	$(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiqueta3').text('Francisco Morazán');
    });


  	$(".o3").mouseleave(function(){
  		$(this).css( 'border','2px solid black');
    	$(this).css( 'background','transparent');
    	$('.etiqueta3').text('');
  	});

  	$(".o4").hover(function(){
    	$(this).css( 'border','2px solid blue');
    	$(this).css( 'background','blue');
    	$('.etiqueta4').text('Comayagua');
  	});


  	$(".o4").mouseleave(function(){
  		$(this).css( 'border','2px solid black');
    	$(this).css( 'background-color','transparent');
    	$('.etiqueta4').text('');
  	});

  	$(".o5").hover(function(){
    	$(this).css( 'border','2px solid blue');
    	$(this).css( 'background','blue');
    	$('.etiqueta5').text('Proximas Extensiones');
  	});


  	$(".o5").mouseleave(function(){
  		$(this).css( 'border','2px solid black');
    	$(this).css( 'background-color','transparent');
    	$('.etiqueta5').text('');
  	});

/*====================Pagina Que hacemos===================*/
    $(".Q1").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQ1').text('CNS-Letrinas');
    });


    $(".Q1").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQ1').text('');
    });


    $(".Q2").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQ2').text('CNS-Becas');
    });


    $(".Q2").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQ2').text('');
    });

    $(".Q3").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQ3').text('CNS-Huertos Familiares');
    });


    $(".Q3").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background','transparent');
      $('.etiquetaQ3').text('');
    });

    $(".Q4").hover(function(){
      $(this).css( 'border','2px solid BLUE');
      $(this).css( 'background','blue');
      $('.etiquetaQ4').text('CNS-Cajas Rurales');
    });


    $(".Q4").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQ4').text('');
    });

    $(".Q5").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaQ5').text('CNS- Pisos');
    });


    $(".Q5").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaQ5').text('');
    });

    /*====================Pagina Voluntario==================*/
    $(".V1").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaV1').text('Tipos de Voluntarios');
    });


    $(".V1").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaV1').text('');
    });


    $(".V2").hover(function(){
      $(this).css( 'border','2px solid blue');
      $(this).css( 'background','blue');
      $('.etiquetaV2').text('Consultas');
    });


    $(".V2").mouseleave(function(){
      $(this).css( 'border','2px solid black');
      $(this).css( 'background-color','transparent');
      $('.etiquetaV2').text('');
    });

    $(".VL").on('click', function(){
      $("#ML").trigger("click");
    });

    $(".VG").on('click', function(){
      $("#MG").trigger("click");
    });

    $(".VA").on('click', function(){
      $("#MA").trigger("click");
    });

    /*=============================== Donde Estamos================================*/

    $(".TextD").on('click', function(){
      $(".TextD").trigger("click");
    });

});