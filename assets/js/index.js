jQuery(function(){
    $('#left-tabs a').click(function (e) {
	e.preventDefault();
	$(this).tab('show');
	//badge-warning
    }).on('shown', function (e) {
	var $this = $(e.target); // activated tab
	$this.children(".badge").addClass("badge-warning");

	var $prev = $(e.relatedTarget);
	$prev.children(".badge").removeClass("badge-warning");
    });
    
    /*
    $('#epitope-selection ul.nav').click(function (e) {
	e.preventDefault();
	$(this).tab('show');
    });
    */
})
