;var detector=!false;$('#imgF').prop('class','glyphicon glyphicon-menu-right')
$('.btn-expand-collapse').click(function(e){detector=!detector;validate();$('.navbar-primary').toggleClass('collapsed');});$('.navbar-primary').toggleClass('collapsed');function validate(){if(detector){$('#imgF').prop('class','glyphicon glyphicon-menu-right')}else{$('#imgF').prop('class','glyphicon glyphicon-menu-left')}};$(function(){var Page=(function(){var $navArrows=$('#nav-arrows').hide(),$shadow=$('#shadow').hide(),slicebox=$('#sb-slider').slicebox({onReady:function(){$navArrows.show();$shadow.show();},orientation:'r',cuboidsRandom:true}),init=function(){initEvents();},initEvents=function(){$navArrows.children(':first').on('click',function(){slicebox.next();return false;});$navArrows.children(':last').on('click',function(){slicebox.previous();return false;});};return{init:init};})();Page.init();});