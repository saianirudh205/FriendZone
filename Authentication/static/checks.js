
$(document).ready(function() {

  $('#form3Example1').on('change', function() {

   alert('hereh');
    var username = $(this).val();


    $.ajax({
      url: '/check_username',
      data: {
        'username': username,
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      dataType: 'json',
      success: function(data) {


          $('#username-availability').text(data.result);

      }
    });
  });

});



$(document).ready(function() {

  $('#form3Example3').on('change', function() {

    console.log("dfgdf");


    var email = $(this).val();

    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

  if (!email.match(validRegex)) {

    $('#username-availability2').text('Not Valid');

    }




    $.ajax({
      url: '/check_email',
      data: {
        'email': email,
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      dataType: 'json',
      success: function(data) {
        $('#username-availability2').text(data.result);
      }
    });
  });

});




