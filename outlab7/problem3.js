$(document).ready(function(){
	$("#text").find("ol").css("background-color","red");
	$("#text").find("ol").css("color","blue");
	$("#text").find("ol").find("li").append(" in the list");
	$("a[name]").css("background-color","#eee");
	$("a[href='#!']").click(function(){
    	alert("You clicked some link");
	});
});