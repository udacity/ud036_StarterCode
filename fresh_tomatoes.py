import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <script src="https://code.jquery.com/jquery-2.1.4.min.js" type="text/javascript"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            margin-left: 2px;
            margin-right: 2px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .thumbnail:hover {
            background-color: #333;
            cursor: pointer;
        }
        .thumbnail{
            padding: 10px;
        }
        .popover-title{
            font-weight: bold;
            text-align: center;
        }
        /* centered columns styles see -> http://goo.gl/pv4oow */
        .row-centered {
            text-align:center;
        }
        .col-centered {
            display:inline-block;
            float:none;
            /* reset the text-align */
            text-align:left;
            /* inline-block space fix */
            margin-right:-15px;
        }
        .movie-btn{
            overflow: hidden;
            text-overflow: ellipsis;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-img', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          var deferred = $.Deferred();
          $(".movie-btn").hide();
          var movie_tile_length = $('.movie-tile').length
          i = 0;
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
            i++;
            if(i == movie_tile_length)
                $(".movie-btn").show('slow');
            console.log(i);
          });
              
          //is_touch_device see -> http://stackoverflow.com/a/15691248/1815624
          var is_touch_device = ("ontouchstart" in window) || window.DocumentTouch && document instanceof DocumentTouch;
          $('[data-toggle="popover"]').popover({ html : true, trigger: is_touch_device ? "focus" : "hover focus"});
          
        });
        /**
         * Vertically center Bootstrap 3 modals
         * see -> https://gist.github.com/CrandellWS/8bcd88c6eca4a8260e16
         */
        $(function() {
            function reposition() {
                var modal = $(this),
                    dialog = modal.find('.modal-dialog');
                modal.css('display', 'block');
                dialog.css("margin-top", Math.max(0, ($(window).height() - dialog.height()) / 2));
            }
            $('.modal').on('show.bs.modal', reposition);
            $(window).on('resize', function() {
                $('.modal:visible').each(reposition);
            });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal " id="trailer">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src='data:image/x-png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAQAAABKfvVzAAAACXBIWXMAAAsTAAALEwEAmpwYAAABgElEQVQ4y72TPS9DYRiGr/dg5E+0/Q8MRBgkJho1iY+FjaHMIh2QMJgQCX/AgoVExEmbaGKxSHxUWqOxWqU4vQ3nnPZoNSae6bwn9/Xc7/PkfuHfSyHFZSuvvGzFFfpNbMtRsBzZTSEN14lrUPRnue61U8e8aFmPkhoQheRca0wxreuzKn/WgmKaUEaSwq7S8ohdrEvKQJpNKgCUWCEHlMgB7LlC4/bnDkvscQxAJ3OUSJADDDP0udqIyUArAENYYJjknTMgTRtPbl+mfDkMseY72PR4s1Rd+N4dIGW6fSBPh/+3whbn3vckg8HNFE17behqeSMCcIPTsH4XuPKPr6wGgDTb3sZqKhc49DxZ5Na7+wAA52zUXA7q1lokQRYwTNOP2OUEgC5maamu1QIwD6RgnywA4/QDhil6AbhwwZTJBKMRlvOmJY3qNJCkinYU06o+JClSn6aoVFKyIahHKkvSyE95japZjTR7EeEGCynp57Q5NK+kCiooqflfxH9SX7sUOLwGLpqpAAAAAElFTkSuQmCC' alt='Close' />
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        <div class="row row-centered">
          {movie_tiles}
        </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_content = '''
<div class="col-md-3 col-sm-4 col-xs-6 col-centered movie-tile">
    <div class="thumbnail">
        <img class="img-responsive movie-img" src="{poster_image_url}" alt="{movie_title}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <button class="btn btn-sm btn-block movie-btn" data-toggle="popover" data-placement="top auto" title="{movie_title}" data-content="<p>{storyline}</p>">{movie_title}</button>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_content.format(
            movie_title=movie.title,
            storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)




