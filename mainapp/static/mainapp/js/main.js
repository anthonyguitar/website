$(document).ready(function() {

    // show that js has loaded
    console.log('JQuery has loaded');
    
    // add event handler to form submit
    $('#emailListForm').on('submit', function(e) {
        e.preventDefault();
        var email = $('#emailID').val();

        // make an ajax call
        $.ajax({
            url: 'createFan',
            cache: 'false',
            type: 'POST',
            data: {csrfmiddlewaretoken: CSRF_TOKEN, 'email': email},
            success: function(data) {

                // see if it worked
                if (data['status'] != 'success') {
                    $('#formDiv p').html(data['status']);
                    $('#formDiv p').css('color', 'red');
                } else {
                    // hide the form and say thanks for signing up
                    $('#formDiv h5').html('Welcome to the family '+email+'!<br><i class="material-icons">mood</i>');
                    $('#formDiv h5').css('color', 'green');
                    $('#formDiv p').html('You are fan number '+data['count']+'.');
                    $('#formDiv p').css('color', 'antiquewhite');
                    $('#emailFormRow').hide();
                }
            },
            error: function(data) {
                $('#formDiv h5').html(data['status']);
            }
        });
    });
});
