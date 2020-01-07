$(document).ready(function() {

    $('.sidenav').sidenav();

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

    // add event handler to form submit
    $('#linkForm').on('submit', function(e) {
        e.preventDefault();
        var email = $('#emailID').val();
        var link = $('#musicLinkID').val();

        // make an ajax call
        $.ajax({
            url: 'submissions',
            cache: 'false',
            type: 'POST',
            data: {csrfmiddlewaretoken: CSRF_TOKEN, 'email': email, 'link': link},
            success: function(data) {

                // see if it worked
                if (data['status'] != 'success') {
                    $('#formDiv p').html(data['status']);
                    $('#formDiv p').css('color', 'red');
                } else {
                    // hide the form and say thanks for signing up
                    $('#formDiv h5').html('Thank you for the submission! I will listen and get back to you!');
                    $('#formDiv h5').css('color', 'green');
                    $('#formDiv p').hide();
                    $('#emailFormRow').hide();
                }
            },
            error: function(data) {
                $('#formDiv h5').html(data['status']);
            }
        });
    });

    // collapsible
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
        }
      });
    }
});
