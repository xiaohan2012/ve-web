(function($){
    $("a.upload-pdb").unbind("click").on("click", function(e){
	e.preventDefault();

	$(this)
	    .closest("div.select-pdb")
	    .toggleClass("hidden")
	    .siblings("div.upload-pdb")
	    .toggleClass("hidden");
    });

    $("button.next-pdb").unbind("click").on("click", function(e){
	e.preventDefault();
	
	//validate the data
	
	//the tab name should be changed
	
	var $id = $(this).closest(".tab-pane").attr("id");
	var a = $("#pdbchain-selection a[href=#" + $id +"]");
	
	a.children(".icon").removeClass("hidden");
	
	a.parent().next().children("a").tab('show');
	
    });
})(jQuery)
