



$(document).ready(function() {
    console.log('hello');
    $("#btngo").click(function() {
        console.log('hello btn');
    // add spinner to button
    $(this).after(
    '<i class="fa fa-circle-o-notch fa-spin"></i> loading...'
    );
    });
    });
