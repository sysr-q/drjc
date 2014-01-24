Zepto(function ($) {
	var fact = $("#fact"),
		actualFact = $("#actual-fact");
	function refresh() {
		fact.toggleClass("spinning");
		$.ajax({
			url: "/drjc.json",
			success: function (data) {
				actualFact.text(data.fact);
			},
			complete: function () {
				fact.toggleClass("spinning");
			}
		});
		return false;
	}
	$("#hashtag").click(refresh);
});
