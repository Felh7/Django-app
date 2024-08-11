
$(document).ready(function() {
    UpdateLikeButtons();
    $(document).on('htmx:afterSwap', function(event) {
                UpdateLikeButtons(); 
    });
    LikeButtonClickHandle();
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
function UpdateLikeButtons() {
    $(".post-body").each(function() {
        var $this = $(this)
        var $button = $this.find(".like-btn")
        var post_id = $button.data("post-id");

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