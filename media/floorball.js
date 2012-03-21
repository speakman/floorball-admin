function handleAttendanceClick(el,gathering,participant)
{
    var jsonRequest = new Request.JSON({
	url: '/toggle_attendance/',
	onSuccess: function(response,text) {
	    if (response.attended === true)
		el.addClass("checked");
	    else
		el.removeClass("checked");
	}
    }).post({'gathering': gathering, 'participant': participant});
}
