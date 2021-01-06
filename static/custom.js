$("#idForm").submit(function (e) {

    e.preventDefault();
    var form = $(this);
    var url = 'https://433627e3c684.ngrok.io/webhook';
    var message = $('#input_message').val()

    $.ajax({
        type: "POST",
        url: url,
        data: {message:message}, 
        success: function (data) {
            console.log(data);
        }
    });


});