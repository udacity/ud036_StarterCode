'use strict';

// Pause the video when the modal is closed
$(document)
    .on('click', '.hanging-close, .modal-backdrop, .modal', function(event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $('#trailer-video-container').empty();
    })
    .on('click', '.movie-tile', function(event) {
        // Start playing the video whenever the trailer modal is opened
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id'),
            sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId
                + '?autoplay=1&html5=1';

        $('#trailer-video-container').empty().append(
            $('<iframe></iframe>', {
                id: 'trailer-video',
                type: 'text-html',
                src: sourceUrl,
                frameborder: 0
            })
        );
    })
    .ready(function() {
        // Animate in the movies when the page loads
        $('.movie-tile').hide().first().show('fast', function showNext() {
            $(this).next('div').show('fast', showNext);
        });
    });