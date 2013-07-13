(function($){
    $(".select-pdb input[type='text']").focusout(function(){
	var $controlGroup = $(this).closest(".control-group");
	$.getJSON("/select-pdb/{0}".format($(this).val()))
	    .done(function(data){
		$controlGroup.addClass("success");
		$controlGroup.find(".help-inline").text("Good!").removeClass("hidden");
	    })
	    .fail(function(data){
		$controlGroup.addClass("error");
		$controlGroup.find(".help-inline").text("Not such Id").removeClass("hidden");
	    });
    });
})(jQuery)
