;$(function(){$('#opinion').on('keypress',function(e){var tecla=e.which||e.keyCode;if(tecla==13){if($(this).val().trim()==''){return;}
$.get('/opiniones_guardar/',{'opinion':$(this).val().trim()},function(data){$('#opiniones').prepend(data.opinion);$('#opinion').val('');$('#opinion').focus();})}});});