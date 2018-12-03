;var detector=!false;$('#imgF').prop('class','glyphicon glyphicon-menu-right')
$('.btn-expand-collapse').click(function(e){detector=!detector;validate();$('.navbar-primary').toggleClass('collapsed');});$('.navbar-primary').toggleClass('collapsed');function validate(){if(detector){$('#imgF').prop('class','glyphicon glyphicon-menu-right')}else{$('#imgF').prop('class','glyphicon glyphicon-menu-left')}}
$('#changes').on('click',function(e){var co=prompt('Ingrese la contraseña:');if(co){location.href="application/change/"+co+"/"
return true;}else{return false;}});