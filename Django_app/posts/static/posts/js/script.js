$(document).ready(function() {
    $('.subscribe-btn').click(function() {
        var author = window.location.pathname.split('/').at(-1);
        var button = $('.subscribe-btn');
        $.ajax({
            type: 'POST',
            url: ajax_url,
            data: {
                'author': author,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(data) {
                console.log('succes')
                if (data.subscribed) {
                    button.text('Unsubscribe');
                } else {
                    button.text('Subscribe');
                }
            },
            error: function(xhr, status, error) {
                console.log('error');
                console.log(xhr.responseText);
            }
        });
    });
});