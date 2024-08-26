
$(document).ready(function() {
    SetSavedTheme();
    UpdateLikeButtons();
    $(document).on('htmx:afterSwap', function(event) {
                UpdateLikeButtons(); 
    });
    LikeButtonClickHandle();
    DeletePostButtonClickHandle();
    $(document).on('click', "#theme-toggle-btn", function(){
        toggleTheme();
    })
    DropdownListHandle()
});

function LikeButtonClickHandle(){
    $(".posts-holder").on("click", ".like-btn, .unlike-btn", function() {
        var button = $(this);
            var post_id = button.data('post-id');
            var url = button.hasClass('like-btn') ? like_ajax_url : unlike_ajax_url;
            var data = {
                'csrfmiddlewaretoken': csrftoken,
                'post_id': post_id,
            }
            if (button.hasClass('unlike-btn')) {
                data.delete = true;
            }
            $.ajax({
                type: 'POST',
                url: url,
                data: data,
                success: function(data) {
                    if (data.liked) {
                        button.text('Unlike').removeClass('like-btn').addClass('unlike-btn');
                    }
                    else {
                        button.text('Like').removeClass('unlike-btn').addClass('like-btn');
                    }
                },
                error: function(xhr, status, error) {
                    console.log('error');
                    console.log(xhr.responseText);
                }
            });
    });
}

function DeletePostButtonClickHandle() {
    $('.post-body').on('click', '.delete-post-button', function() {
        var button = $(this)
        var post_id = button.data('post-id')
        var PostContent = button.closest('.post-content')
        console.log(PostContent)

        $.ajax({
            type: "POST",
            url: DeletPostUrl,
            data: {
                'post_id': post_id,
                'csrfmiddlewaretoken': csrftoken,
                'delete': true,
            },
            success: function(response){
                if (response.deleted){
                    console.log('post has been deleted')
                    PostContent.hide()
                    PostContent.closest('#deleted-post-placeholder').show()
                }
                else{
                    console.log('post has not been deleted')
                }
            }
        })
    })

}
function UpdateLikeButtons() {
    $(".post-body").each(function() {
        var $this = $(this)
        var $button = $this.find(".like-btn")
        var post_id = $button.data("post-id")

        // Make an AJAX request to the API endpoint
        $.ajax({
          type: "GET",
          url: CheckIfLiked_ajax_url,
          data: {
            'post_id': post_id,
          },
          success: function(response) {
            // Update the like button's state based on the response
            if (response.liked) {
                $this.find(".like-btn").text('Unlike').removeClass('like-btn').addClass("unlike-btn");
            } 
          }
        });
      });
}
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
// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}
// function to toggle between light and dark theme
function toggleTheme() {
   if (localStorage.getItem('theme') === 'theme-dark'){
       setTheme('theme-light');
   } else {
       setTheme('theme-dark');
   }
}
// Immediately invoked function to set the theme on initial load
function SetSavedTheme() {
   if (localStorage.getItem('theme') === 'theme-dark') {
       setTheme('theme-dark');
   } else {
       setTheme('theme-light');
   }
}

function DropdownListHandle(){
    $('.dropdown-btn').click(function(){
        var button = $(this);
        var siblings = button.siblings('.dropdown');
        if (siblings.hasClass('dropdown-hidden')) {
            siblings.removeClass('dropdown-hidden');
            siblings.toggleClass('dropdown-showen');
        }
        else{
            siblings.removeClass('dropdown-showen');
            siblings.toggleClass('dropdown-hidden');
        }
    });
}