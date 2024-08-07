
$(document).ready(function() {
    $(".post-body").each(function() {
        var $this = $(this)
        console.log($this)
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
                $this.find(".like-btn").text('unlike').removeClass('like-btn').addClass("unlike-btn");
            } else {
                $this.find(".unlike-btn").text('like').removeClass("unlike-btn").addClass("like-btn");
            }
            console.log('succes')
          }
        });
      });

    $('.like-btn, .unlike-btn').click(function() {
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
                    button.text('unlike').removeClass('like-btn').addClass('unlike-btn');
                }
                else {
                    button.text('like').removeClass('unlike-btn').addClass('like-btn');
                }
            },
            error: function(xhr, status, error) {
                console.log('error');
                console.log(xhr.responseText);
            }
        });
    });
});