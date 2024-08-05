$(document).ready(function() {
    $('#subscribe-btn').click(function() {
        var author = window.location.pathname.split('/').at(-1)
        $.ajax({
            type: 'POST',
            url: ajax_url,
            data: {
                'author': author,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(data) {
                if (data.subscribed) {
                    $(this).text('Unsubscribe');
                } else {
                    $(this).text('Subscribe');
                }
            }
        });
    });
});