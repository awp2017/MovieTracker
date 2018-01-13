$(document).ready(function(){
    $(".glyphicon-menu-hamburger" ).click(function() {
        $(".sidebar-wrapper").show();
    });

    $(".glyphicon-remove" ).click(function() {
        $(".sidebar-wrapper").hide();
    });
});