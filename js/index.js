$(document).ready(function(){
	var callback = function(json){
		console.log(json);
	}
	function get_content(){
		$.ajax({
             type: "GET",
             url: "http://localhost:8000/mNews/",
             dataType: "jsonp",
             jsonp:"callback",
             jsonpCallback:"callback",
             success:function(data){
             	$.each(data,function(id,rs){
             		var li = '<li>'+'<a href="'+rs.url+'" title="'+rs.title+'">'+rs.title+'</a></li>'
             		$(".news").append(li);
             	});
             	//console.log(data[0].title);
             },
             error: function(x,t,e){
             	console.log(x);
             	console.log(t);
             	console.log(e);
             }
	});
	}
	get_content();
});
