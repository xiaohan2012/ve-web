(function($, window, document, undefined){
    
    String.prototype.format = String.prototype.f = function() {
	var s = this,
	i = arguments.length;
	
	while (i--) {
            s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
	}
	return s;
    };
    
    
    $.fn.justtext = function() {
	//util, just the text of the jq, not its children's
	return $(this).clone()
            .children()
            .remove()
            .end()
            .text();
    };
    
})(jQuery, window, document);
