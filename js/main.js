function send_request(request_string)
{
    var payload = {'command': request_string};
    $.ajax({
        url: "./test",
        data: payload
    }).done(function(data) {
        $("#content").append(data + "<br />");
        var content  = $('#content');
        var height = $('#content').height();
        content.scrollTop(height);
    });
}

$(function(){

	$('#plrinput').bind('change', function(e) {
		send_request($('#plrinput').val());
		$('#plrinput').val("");
	});

});
