;$(function(){$('#opinion').on('keypress',function(e){var tecla=e.which||e.keyCode;if(tecla==13){if($(this).val().trim()==''){return;}
$('#opiniones').prepend(`<div class="panel panel-default"><div class="panel-body"><strong>Anónimo</strong><br>${$(this).val().trim()}<br><small>${'5345;3563'}</small></div></div>`)
$(this).val('');$('#opinion').focus();}});});