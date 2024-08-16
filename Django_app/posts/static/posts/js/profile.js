$(document).ready(function() {
    CheckSubscription();
    SubscribeStatusChange();
});

function CheckSubscription(){
    var author = window.location.pathname.split('/').at(-1);
    var data = {
        'author': author,
        'csrfmiddlewaretoken': csrftoken
    };

    $.ajax({
        type: 'POST',
        url: checksubscription_ajax, // URL to check subscription status
        data: data,
        success: function(data) {
            if (data.subscribed) {
                $('.subscribe-btn').text('Unsubscribe').removeClass('subscribe-btn').addClass('unsubscribe-btn');
            } else {
                $('.unsubscribe-btn').text('Subscribe').removeClass('unsubscribe-btn').addClass('subscribe-btn');
            }
        },
        error: function(xhr, status, error) {
            console.log('error');
            console.log(xhr.responseText);
        }
    });
}

function SubscribeStatusChange(){
    var author = window.location.pathname.split('/').at(-1);
    var data = {
        'author': author,
        'csrfmiddlewaretoken': csrftoken
    };
    $('.subscribe-btn, .unsubscribe-btn').click(function() {
        var button = $(this); // Get the current button element
        var url = button.hasClass('subscribe-btn') ? subscribe_ajax_url : unsubscribe_ajax_url;
        if (button.hasClass('unsubscribe-btn')) {
            data.delete = true;
        }
        $.ajax({
            type: 'POST',
            url: url,
            data: data,
            success: function(data) {
                if (data.subscribed) {
                    $('.subscribe-btn').text('Unsubscribe').removeClass('subscribe-btn').addClass('unsubscribe-btn');
                }
                else {
                    $('.unsubscribe-btn').text('Subscribe').removeClass('unsubscribe-btn').addClass('subscribe-btn');
                }
            },
            error: function(xhr, status, error) {
                console.log('error');
                console.log(xhr.responseText);
            }
        });
    });
}